#!/usr/bin/env python3
"""Render a sourced person timeline JSON file to HTML and sources Markdown."""

from __future__ import annotations

import argparse
import datetime as _dt
import html
import json
import re
import sys
from pathlib import Path
from typing import Any


SKILL_DIR = Path(__file__).resolve().parents[1]
DEFAULT_TEMPLATE = SKILL_DIR / "assets" / "archive-template.html"

CONFIDENCE_LABELS = {
    "high": "高可信",
    "medium": "中等可信",
    "low": "低可信",
    "disputed": "存在争议",
}

TIER_LABELS = {
    "official": "官方",
    "government": "政府/公共机构",
    "primary": "一手资料",
    "scholarly": "学术",
    "reputable-media": "可靠媒体",
    "encyclopedia": "百科",
    "wikipedia": "维基百科",
    "baidu-baike": "百度百科",
    "baike": "百科",
    "reference": "参考资料",
    "secondary": "二级资料",
}


def esc(value: Any) -> str:
    return html.escape("" if value is None else str(value), quote=True)


def field_html(item: dict[str, Any], html_key: str, raw_key: str) -> str:
    """Return pre-linked HTML (set by render_cross_links) if present, else escaped raw value.

    When render_cross_links has injected cross-person hyperlinks into an item, it stores the
    resulting HTML under ``html_key``. This helper prefers that pre-rendered HTML so the links
    are not double-escaped; otherwise it falls back to escaping the raw field value.
    """
    linked = item.get(html_key)
    if linked:
        return str(linked)
    return esc(item.get(raw_key))


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def clean_slug(value: str) -> str:
    chars: list[str] = []
    last_dash = False
    for ch in value.strip().lower():
        if ch.isalnum():
            chars.append(ch)
            last_dash = False
        elif not last_dash:
            chars.append("-")
            last_dash = True
    slug = "".join(chars).strip("-")
    return slug or "person"


def event_sort_key(event: dict[str, Any]) -> tuple[int, int, int, str]:
    text = str(event.get("date") or event.get("date_display") or "")
    match = re.search(r"(-?\d{1,4})(?:-(\d{1,2}))?(?:-(\d{1,2}))?", text)
    if not match:
        return (99999, 12, 31, text)
    year = int(match.group(1))
    month = int(match.group(2) or 1)
    day = int(match.group(3) or 1)
    return (year, month, day, text)


def date_text(event: dict[str, Any]) -> str:
    if event.get("date_display"):
        return str(event["date_display"])
    start = str(event.get("date") or "日期不详")
    end = event.get("end_date")
    if end:
        return f"{start} - {end}"
    return start


def parse_partial_date(value: Any) -> tuple[int, int, int, int] | None:
    text = str(value or "")
    match = re.search(r"(-?\d{1,4})(?:-(\d{1,2}))?(?:-(\d{1,2}))?", text)
    if not match:
        return None
    year = int(match.group(1))
    month = int(match.group(2) or 1)
    day = int(match.group(3) or 1)
    precision = 3 if match.group(3) else 2 if match.group(2) else 1
    return (year, month, day, precision)


def birth_date_value(subject: dict[str, Any], events: list[dict[str, Any]]) -> Any:
    if subject.get("birth_date"):
        return subject["birth_date"]
    for event in events:
        category = str(event.get("category") or "")
        title = str(event.get("title") or "")
        if "出生" in category or "出生" in title:
            return event.get("date") or event.get("date_display")
    return None


def birth_display_value(subject: dict[str, Any], events: list[dict[str, Any]]) -> str:
    if subject.get("birth_display"):
        return str(subject["birth_display"])
    for event in events:
        category = str(event.get("category") or "")
        title = str(event.get("title") or "")
        if "出生" in category or "出生" in title:
            return date_text(event)
    birth = birth_date_value(subject, events)
    return str(birth) if birth else "未标注"


def age_label_for_date(subject: dict[str, Any], events: list[dict[str, Any]], target: Any) -> str:
    birth = parse_partial_date(birth_date_value(subject, events))
    date = parse_partial_date(target)
    if not birth or not date:
        return ""
    birth_year, birth_month, birth_day, birth_precision = birth
    year, month, day, date_precision = date
    age = year - birth_year
    if date_precision >= 2 and birth_precision >= 2 and month < birth_month:
        age -= 1
    if date_precision >= 3 and birth_precision >= 3 and (month, day) < (birth_month, birth_day):
        age -= 1
    if age < 0:
        return ""
    approximate = min(birth_precision, date_precision) < 3
    prefix = "约" if approximate else ""
    return f"{prefix}{age}岁"


def event_age_label(event: dict[str, Any], subject: dict[str, Any], events: list[dict[str, Any]]) -> str:
    if event.get("age"):
        return str(event["age"])
    return age_label_for_date(subject, events, event.get("date") or event.get("date_display"))


def source_map(data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    mapping: dict[str, dict[str, Any]] = {}
    for source in as_list(data.get("sources")):
        if isinstance(source, dict) and source.get("id"):
            mapping[str(source["id"])] = source
    return mapping


def render_source_refs(ids: list[Any], sources: dict[str, dict[str, Any]]) -> str:
    refs = []
    for raw_id in ids:
        sid = str(raw_id)
        match = re.fullmatch(r"S(\d+)", sid)
        label = esc(match.group(1) if match else sid)
        if sid in sources:
            refs.append(f'<a class="source-ref" href="#source-{esc(sid)}" title="来源 {esc(sid)}">{label}</a>')
        else:
            refs.append(f'<span class="source-ref">{label}</span>')
    if not refs:
        return ""
    joined = '<span class="source-separator">,</span>'.join(refs)
    return f'<span class="source-refs" aria-label="来源">[{joined}]</span>'


def source_title(ids: list[Any]) -> str:
    clean = [str(item) for item in ids if str(item).strip()]
    if not clean:
        return ""
    return "来源：" + "、".join(clean)


def render_paragraphs(text: Any) -> str:
    parts = [str(item).strip() for item in as_list(text) if str(item).strip()]
    if not parts:
        return "<p>暂无简介。</p>"
    return "".join(f"<p>{esc(part)}</p>" for part in parts)


def render_hero_summary(text: Any) -> str:
    parts = [str(item).strip() for item in as_list(text) if str(item).strip()]
    if not parts:
        return ""
    body = "".join(f"<p>{esc(part)}</p>" for part in parts[:3])
    return f'<div class="hero-summary">{body}</div>'


def css_token(value: Any, fallback: str = "item") -> str:
    token = re.sub(r"[^a-z0-9_-]+", "-", str(value or "").strip().lower()).strip("-")
    return token or fallback


def render_stats(subject: dict[str, Any], events: list[dict[str, Any]], sources: list[Any]) -> str:
    fields = "、".join(str(x) for x in as_list(subject.get("fields")) if str(x).strip()) or "未标注"
    date_range = subject.get("date_range") or "未标注"
    rows = [
        ("领域", fields),
        ("年代", date_range),
        ("事件数", str(len(events))),
        ("来源数", str(len(sources))),
    ]
    items = "".join(f"<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>" for k, v in rows)
    return f'<dl class="stat-list">{items}</dl>'


def render_identifiers(subject: dict[str, Any]) -> str:
    identifiers = [str(x) for x in as_list(subject.get("identifiers")) if str(x).strip()]
    native_name = subject.get("native_name")
    if native_name:
        identifiers.insert(0, str(native_name))
    if not identifiers:
        return ""
    chips = "".join(f'<span class="chip">{esc(item)}</span>' for item in identifiers)
    return f'<div class="chips">{chips}</div>'


def render_age_overview(
    data: dict[str, Any],
    subject: dict[str, Any],
    events: list[dict[str, Any]],
    sources: dict[str, dict[str, Any]],
) -> str:
    sidebar = data.get("timeline_sidebar")
    if isinstance(sidebar, dict):
        clue_items = [item for item in as_list(sidebar.get("items")) if isinstance(item, dict)]
    else:
        clue_items = []
    if clue_items:
        items = []
        for item in clue_items[:6]:
            refs_title = source_title(as_list(item.get("source_ids")))
            title_attr = f' title="{esc(refs_title)}"' if refs_title else ""
            label = item.get("label") or item.get("period") or item.get("date") or "线索"
            value = item.get("value") or item.get("title") or "未命名线索"
            detail = item.get("description") or item.get("text") or ""
            items.append(
                f'<div class="age-fact key-fact"{title_attr}>'
                f"<span>{esc(label)}</span>"
                f"<strong>{esc(value)}</strong>"
                f"<p>{esc(detail)}</p>"
                "</div>"
            )
        return f'<div id="key-facts" class="age-overview key-overview" aria-label="关键线索">{"".join(items)}</div>'

    generated_at = data.get("generated_at") or _dt.date.today().isoformat()
    current_age = subject.get("current_age") or age_label_for_date(subject, events, generated_at) or "未标注"
    birth_display = birth_display_value(subject, events)
    stages_count = len(as_list(data.get("life_stages")))
    source_count = len(sources)
    facts = [
        ("当前年龄", current_age),
        ("出生时间", birth_display),
        ("人生阶段", f"{stages_count}段" if stages_count else "未分段"),
        ("来源数量", f"{source_count}条"),
    ]
    items = "".join(
        f'<div class="age-fact"><span>{esc(label)}</span><strong>{esc(value)}</strong></div>'
        for label, value in facts
    )
    return f'<div id="key-facts" class="age-overview" aria-label="年龄与时间概览">{items}</div>'


def render_hero_aside_title(data: dict[str, Any]) -> str:
    sidebar = data.get("timeline_sidebar")
    clue_items = sidebar.get("items") if isinstance(sidebar, dict) else []
    return "关键线索" if as_list(clue_items) else "时间概览"


def render_major_events(events: list[dict[str, Any]], sources: dict[str, dict[str, Any]], major_ids: list[Any]) -> str:
    explicit = {str(x) for x in major_ids}
    major_events = []
    for index, event in enumerate(events):
        event_id = str(event.get("id") or index)
        importance = str(event.get("importance") or "").lower()
        if (explicit and event_id in explicit) or (not explicit and importance == "major"):
            major_events.append(event)
    if not major_events:
        major_events = events[:6]
    if not major_events:
        return '<p class="notice">暂无可展示的大事记。</p>'
    items = []
    for event in major_events:
        refs = render_source_refs(as_list(event.get("source_ids")), sources)
        items.append(
            "<li>"
            f"<time>{esc(date_text(event))}</time>"
            f"<strong>{field_html(event, '_html_title', 'title') or '未命名事件'}{refs}</strong>"
            f"<p>{field_html(event, '_html_description', 'description')}</p>"
            "</li>"
        )
    return f'<ol class="major-list">{"".join(items)}</ol>'


def render_epitaph(data: dict[str, Any], sources: dict[str, dict[str, Any]]) -> str:
    value = data.get("epitaph")
    if isinstance(value, dict):
        text = str(value.get("text") or "").strip()
        refs = render_source_refs(as_list(value.get("source_ids")), sources)
    else:
        text = str(value or "").strip()
        refs = ""
    if not text:
        return ""
    return (
        '<section class="content-section pt-0" aria-labelledby="epitaph-heading">'
        '<h2 id="epitaph-heading" class="section-title">一句话定位</h2>'
        '<div class="epitaph-card">'
        '<span>人物历史坐标</span>'
        f"<p>{esc(text)}{refs}</p>"
        "</div>"
        "</section>"
    )


def render_achievement_controversy(data: dict[str, Any], sources: dict[str, dict[str, Any]]) -> str:
    block = data.get("achievement_controversy_brief")
    items = block.get("items") if isinstance(block, dict) else block
    rows = []
    for item in as_list(items):
        if not isinstance(item, dict):
            continue
        kind = css_token(item.get("type") or item.get("kind"), "achievement")
        label = item.get("label") or ("成就" if kind == "achievement" else "争议/限制")
        title = item.get("title") or "未命名条目"
        desc = item.get("description") or item.get("text") or ""
        refs_title = source_title(as_list(item.get("source_ids")))
        title_attr = f' title="{esc(refs_title)}"' if refs_title else ""
        rows.append(
            f'<article class="brief-row {esc(kind)}"{title_attr}>'
            f'<span class="brief-label">{esc(label)}</span>'
            '<div class="brief-body">'
            f"<h3>{esc(title)}</h3>"
            f"<p>{esc(desc)}</p>"
            "</div>"
            "</article>"
        )
    if not rows:
        return ""
    return (
        '<section class="sidebar-block" aria-labelledby="brief-heading">'
        '<h2 id="brief-heading" class="section-title">成就与争议速览</h2>'
        f'<div class="brief-list">{"".join(rows)}</div>'
        "</section>"
    )


def render_life_stages(data: dict[str, Any], subject: dict[str, Any], events: list[dict[str, Any]], sources: dict[str, dict[str, Any]]) -> str:
    stages = [stage for stage in as_list(data.get("life_stages")) if isinstance(stage, dict)]
    if not stages:
        return render_major_events(events, sources, as_list(data.get("major_event_ids")))
    items = []
    for stage in stages:
        period = stage.get("period") or stage.get("date") or "时间未标注"
        age = stage.get("age_range") or stage.get("age") or ""
        meta = f"{period} · {age}" if age else str(period)
        refs = render_source_refs(as_list(stage.get("source_ids")), sources)
        items.append(
            '<li class="stage-card">'
            f'<span class="stage-meta">{esc(meta)}</span>'
            f"<h3>{esc(stage.get('title') or '未命名阶段')}{refs}</h3>"
            f"<p>{esc(stage.get('description') or '')}</p>"
            "</li>"
        )
    return f'<ol class="stage-timeline">{"".join(items)}</ol>'


def render_timeline_sidebar_title(data: dict[str, Any]) -> str:
    sidebar = data.get("timeline_sidebar")
    if isinstance(sidebar, dict) and str(sidebar.get("title") or "").strip():
        return esc(sidebar["title"])
    return "关键线索"


def render_timeline_sidebar(data: dict[str, Any], events: list[dict[str, Any]], sources: dict[str, dict[str, Any]]) -> str:
    sidebar = data.get("timeline_sidebar")
    if isinstance(sidebar, dict):
        raw_items = as_list(sidebar.get("items"))
        note = str(sidebar.get("note") or "").strip()
    else:
        raw_items = []
        note = ""

    cards = []
    for item in raw_items:
        if not isinstance(item, dict):
            continue
        refs = render_source_refs(as_list(item.get("source_ids")), sources)
        label = item.get("label") or item.get("period") or item.get("date") or "线索"
        value = item.get("value") or item.get("title") or "未命名线索"
        detail = item.get("description") or item.get("text") or ""
        cards.append(
            '<li class="context-card">'
            f'<span class="context-label">{esc(label)}</span>'
            '<div class="context-body">'
            f'<strong class="context-value">{esc(value)}{refs}</strong>'
            f"<p>{esc(detail)}</p>"
            "</div>"
            "</li>"
        )

    if not cards:
        major_ids = {str(x) for x in as_list(data.get("major_event_ids"))}
        major_events = [
            event
            for index, event in enumerate(events)
            if (major_ids and str(event.get("id") or index) in major_ids)
            or (not major_ids and str(event.get("importance") or "").lower() == "major")
        ][:5]
        for event in major_events:
            refs = render_source_refs(as_list(event.get("source_ids")), sources)
            cards.append(
                '<li class="context-card">'
                f'<span class="context-label">{esc(date_text(event))}</span>'
                '<div class="context-body">'
                f'<strong class="context-value">{field_html(event, "_html_title", "title") or "未命名事件"}{refs}</strong>'
                f"<p>{field_html(event, '_html_description', 'description')}</p>"
                "</div>"
                "</li>"
            )

    if not cards:
        return '<p class="notice">暂无关键线索。</p>'
    note_html = f'<p class="context-note">{esc(note)}</p>' if note else ""
    return f'{note_html}<ol class="context-list">{"".join(cards)}</ol>'


def render_timeline(
    events: list[dict[str, Any]],
    sources: dict[str, dict[str, Any]],
    subject: dict[str, Any],
    highlight_ids: list[Any],
) -> str:
    if not events:
        return '<p class="notice">暂无时间线事件。</p>'
    explicit_highlights = {str(x) for x in highlight_ids}
    items = []
    for index, event in enumerate(events):
        event_id = str(event.get("id") or index)
        category = event.get("category") or "其他"
        confidence = str(event.get("confidence") or "medium").lower()
        confidence_label = CONFIDENCE_LABELS.get(confidence, esc(confidence))
        importance = str(event.get("importance") or "").lower()
        is_highlight = event_id in explicit_highlights if explicit_highlights else importance == "major"
        event_class = "event event-major" if is_highlight else "event"
        tags = [f'<span class="tag">{esc(category)}</span>']
        if confidence != "high":
            tags.append(f'<span class="tag confidence-{esc(confidence)}">{esc(confidence_label)}</span>')
        if is_highlight:
            tags.append('<span class="tag major">转折点</span>')
        age = event_age_label(event, subject, events)
        age_html = (
            f'<div class="event-age-tab"><span>年龄</span><strong>{esc(age)}</strong></div>'
            if age
            else '<div class="event-age-tab"><span>年龄</span><strong>-</strong></div>'
        )
        refs = render_source_refs(as_list(event.get("source_ids")), sources)
        notes = event.get("notes")
        note_html = f"<p><em>{esc(notes)}</em></p>" if notes else ""
        items.append(
            f'<li class="{event_class}">'
            '<details class="event-detail">'
            '<summary class="event-summary">'
            f"{age_html}"
            '<div class="event-body">'
            '<div class="event-meta-line">'
            f"<time>{esc(date_text(event))}</time>"
            f'<div class="event-tools">{"".join(tags)}</div>'
            "</div>"
            f"<h3>{field_html(event, '_html_title', 'title') or '未命名事件'}{refs}</h3>"
            "</div>"
            "</summary>"
            '<div class="event-extra">'
            f"<p>{field_html(event, '_html_description', 'description')}</p>"
            f"{note_html}"
            "</div>"
            "</details>"
            "</li>"
        )
    return f'<ol class="timeline">{"".join(items)}</ol>'


def render_turning_points(data: dict[str, Any], sources: dict[str, dict[str, Any]]) -> str:
    points = [item for item in as_list(data.get("turning_points")) if isinstance(item, dict)]
    cards = []
    for item in points:
        refs = render_source_refs(as_list(item.get("source_ids")), sources)
        facts = []
        for label, key in [("选择", "choice"), ("结果", "consequence"), ("低谷/代价", "dark_side_or_failure")]:
            value = str(item.get(key) or "").strip()
            if value:
                facts.append(f"<div><dt>{label}</dt><dd>{esc(value)}</dd></div>")
        period = item.get("period") or item.get("date") or ""
        cards.append(
            '<article class="turn-card">'
            f'<span class="card-kicker">{esc(period)}</span>'
            f"<h3>{esc(item.get('title') or '未命名转折')}</h3>"
            f'<dl class="turn-list">{"".join(facts)}</dl>'
            f'<div class="event-tools mt-3">{refs}</div>'
            "</article>"
        )
    if not cards:
        return ""
    return (
        '<section class="content-section" aria-labelledby="turning-heading">'
        '<h2 id="turning-heading" class="section-title">命运转折点、低谷与选择</h2>'
        f'<div class="turn-grid">{"".join(cards)}</div>'
        "</section>"
    )


def render_relationship_network(data: dict[str, Any], sources: dict[str, dict[str, Any]], subject: dict[str, Any]) -> str:
    network = data.get("relationship_network")
    if not isinstance(network, dict):
        return ""
    nodes = [item for item in as_list(network.get("nodes")) if isinstance(item, dict)]
    if not nodes:
        return ""
    center = network.get("center") or subject.get("name") or "人物"
    center_note = network.get("center_note") or "关系网络"
    note = str(network.get("note") or "").strip()
    node_html = []
    for node in nodes:
        kind = css_token(node.get("type") or node.get("category"), "node")
        relation = node.get("relation") or node.get("type") or ""
        refs = render_source_refs(as_list(node.get("source_ids")), sources)
        node_html.append(
            f'<article class="network-node {esc(kind)}">'
            f"<h3>{esc(node.get('name') or '未命名节点')}</h3>"
            f"<p><strong>{esc(relation)}</strong>{'：' if relation else ''}{field_html(node, '_html_description', 'description')}</p>"
            f'<div class="event-tools mt-2">{refs}</div>'
            "</article>"
        )
    note_html = f'<p class="section-note">{esc(note)}</p>' if note else ""
    return (
        '<section class="content-section" aria-labelledby="network-heading">'
        '<h2 id="network-heading" class="section-title">人物关系网络</h2>'
        f"{note_html}"
        '<div class="relationship-map">'
        f'<div class="network-center"><strong>{esc(center)}</strong><span>{esc(center_note)}</span></div>'
        f'<div class="network-nodes">{"".join(node_html)}</div>'
        "</div>"
        "</section>"
    )


def render_era_map(data: dict[str, Any], sources: dict[str, dict[str, Any]]) -> str:
    cards = []
    for item in as_list(data.get("era_map")):
        if not isinstance(item, dict):
            continue
        refs = render_source_refs(as_list(item.get("source_ids")), sources)
        rows = []
        for label, key in [("时代背景", "context"), ("约束条件", "constraint"), ("破局方式", "breakthrough")]:
            value = str(item.get(key) or "").strip()
            if value:
                rows.append(f"<p><strong>{label}：</strong>{esc(value)}</p>")
        period = item.get("period") or item.get("date") or ""
        cards.append(
            '<article class="era-card">'
            f'<span class="card-kicker">{esc(period)}</span>'
            f"<h3>{esc(item.get('title') or '时代阶段')}</h3>"
            f"{''.join(rows)}"
            f'<div class="event-tools mt-3">{refs}</div>'
            "</article>"
        )
    if not cards:
        return ""
    return (
        '<section class="content-section" aria-labelledby="era-heading">'
        '<h2 id="era-heading" class="section-title">时代坐标与破局</h2>'
        f'<div class="era-grid">{"".join(cards)}</div>'
        "</section>"
    )


def render_influence_legacy(data: dict[str, Any], sources: dict[str, dict[str, Any]]) -> str:
    block = data.get("influence_legacy")
    items = block.get("items") if isinstance(block, dict) else block
    cards = []
    for item in as_list(items):
        if not isinstance(item, dict):
            continue
        refs = render_source_refs(as_list(item.get("source_ids")), sources)
        cards.append(
            '<article class="legacy-card">'
            f'<span class="card-kicker">{esc(item.get("dimension") or item.get("label") or "评价")}</span>'
            f"<h3>{esc(item.get('title') or '影响力')}</h3>"
            f"<p>{esc(item.get('description') or item.get('text') or '')}</p>"
            f'<div class="event-tools mt-3">{refs}</div>'
            "</article>"
        )
    if not cards:
        return ""
    return (
        '<section class="content-section" aria-labelledby="legacy-heading">'
        '<h2 id="legacy-heading" class="section-title">影响力与后世评价</h2>'
        f'<div class="legacy-grid">{"".join(cards)}</div>'
        "</section>"
    )


def render_growth_curves(data: dict[str, Any], sources: dict[str, dict[str, Any]]) -> str:
    curves = [item for item in as_list(data.get("growth_curves")) if isinstance(item, dict)]
    cards = []
    for curve in curves:
        points = []
        for point in as_list(curve.get("points")):
            if not isinstance(point, dict):
                continue
            try:
                value = max(0, min(100, int(float(point.get("value", 0)))))
            except (TypeError, ValueError):
                value = 0
            refs = render_source_refs(as_list(point.get("source_ids")), sources)
            note = str(point.get("note") or "").strip()
            points.append(
                '<div class="curve-point">'
                f'<header><span>{esc(point.get("label") or point.get("period") or "")}</span><span>{value}</span></header>'
                f'<div class="curve-track" aria-label="{esc(point.get("label") or "")} {value}"><span class="curve-fill" style="width: {value}%"></span></div>'
                f'<div class="curve-note">{esc(note)}</div>'
                f'<div class="event-tools">{refs}</div>'
                "</div>"
            )
        if not points:
            continue
        cards.append(
            '<article class="curve-card">'
            f"<h3>{esc(curve.get('title') or '增长曲线')}</h3>"
            f"<p>{esc(curve.get('description') or '')}</p>"
            f'<div class="curve-points">{"".join(points)}</div>'
            "</article>"
        )
    if not cards:
        return ""
    return (
        '<section class="content-section" aria-labelledby="curves-heading">'
        '<h2 id="curves-heading" class="section-title">思想、权力与财富增长曲线</h2>'
        '<p class="section-note">曲线为基于公开资料的相对可见度示意，不代表净资产、私人财富或精确量化排名。</p>'
        f'<div class="curve-grid">{"".join(cards)}</div>'
        "</section>"
    )


def render_deep_review(data: dict[str, Any], sources: dict[str, Any], subject: dict[str, Any], include_curves: bool = True) -> str:
    turning_points = [item for item in as_list(data.get("turning_points")) if isinstance(item, dict)]
    relationship = data.get("relationship_network")
    era_items = [item for item in as_list(data.get("era_map")) if isinstance(item, dict)]
    legacy_block = data.get("influence_legacy")
    legacy_items = legacy_block.get("items") if isinstance(legacy_block, dict) else legacy_block
    legacy_items = [item for item in as_list(legacy_items) if isinstance(item, dict)]
    curves = [item for item in as_list(data.get("growth_curves")) if isinstance(item, dict)]

    if not any([turning_points, relationship, era_items, legacy_items, curves]):
        return ""

    decision_rows = []
    for item in turning_points:
        refs = render_source_refs(as_list(item.get("source_ids")), sources)
        facts = []
        for label, key in [("选择", "choice"), ("结果", "consequence"), ("代价/边界", "dark_side_or_failure")]:
            value = str(item.get(key) or "").strip()
            if value:
                facts.append(f"<div><dt>{label}</dt><dd>{esc(value)}</dd></div>")
        period = item.get("period") or item.get("date") or ""
        decision_rows.append(
            '<article class="decision-row">'
            f'<div class="decision-marker"><span>{esc(period)}</span></div>'
            '<div class="decision-body">'
            f"<h4>{esc(item.get('title') or '未命名转折')}{refs}</h4>"
            f'<dl class="decision-facts">{"".join(facts)}</dl>'
            "</div>"
            "</article>"
        )
    decision_html = (
        '<div class="review-block review-main">'
        '<div class="review-heading"><span>01</span><h3>决定性转折</h3></div>'
        '<p class="review-copy">把命运节点按时间推进，重点看他当时做了什么选择、带来什么结果，以及哪些地方不能脱离来源夸大。</p>'
        f'<div class="decision-rail">{"".join(decision_rows)}</div>'
        "</div>"
        if decision_rows
        else ""
    )

    network_html = ""
    if isinstance(relationship, dict):
        nodes = [item for item in as_list(relationship.get("nodes")) if isinstance(item, dict)]
        node_html = []
        for node in nodes:
            kind = css_token(node.get("type") or node.get("category"), "node")
            relation = node.get("relation") or node.get("type") or ""
            refs = render_source_refs(as_list(node.get("source_ids")), sources)
            node_html.append(
                f'<article class="relation-pill {esc(kind)}">'
                f"<strong>{esc(node.get('name') or '未命名节点')}{refs}</strong>"
                f"<span>{esc(relation)}</span>"
                f"<p>{field_html(node, '_html_description', 'description')}</p>"
                "</article>"
            )
        if node_html:
            note = str(relationship.get("note") or "").strip()
            note_html = f'<p class="review-copy">{esc(note)}</p>' if note else ""
            network_html = (
                '<div class="review-panel">'
                '<div class="review-heading"><span>02</span><h3>关系网络</h3></div>'
                f"{note_html}"
                f'<div class="relation-cloud">{"".join(node_html)}</div>'
                "</div>"
            )

    era_html = ""
    era_rows = []
    for item in era_items:
        refs = render_source_refs(as_list(item.get("source_ids")), sources)
        era_rows.append(
            '<li>'
            f'<span>{esc(item.get("period") or item.get("date") or "")}</span>'
            f"<strong>{esc(item.get('title') or '时代阶段')}{refs}</strong>"
            f"<p>{esc(item.get('breakthrough') or item.get('context') or '')}</p>"
            "</li>"
        )
    if era_rows:
        era_html = (
            '<div class="review-panel">'
            '<div class="review-heading"><span>03</span><h3>时代坐标</h3></div>'
            '<p class="review-copy">只保留时代背景中真正解释人物选择的部分。</p>'
            f'<ol class="era-list-compact">{"".join(era_rows)}</ol>'
            "</div>"
        )

    legacy_rows = []
    for item in legacy_items:
        refs = render_source_refs(as_list(item.get("source_ids")), sources)
        legacy_rows.append(
            '<li>'
            f'<span>{esc(item.get("dimension") or item.get("label") or "评价")}</span>'
            f"<strong>{esc(item.get('title') or '影响力')}{refs}</strong>"
            f"<p>{esc(item.get('description') or item.get('text') or '')}</p>"
            "</li>"
        )
    legacy_html = f'<ol class="impact-list">{"".join(legacy_rows)}</ol>' if legacy_rows else ""

    curve_rows = []
    for curve in curves:
        points = []
        for point in as_list(curve.get("points")):
            if not isinstance(point, dict):
                continue
            try:
                value = max(0, min(100, int(float(point.get("value", 0)))))
            except (TypeError, ValueError):
                value = 0
            points.append(
                '<div class="mini-curve-point">'
                f'<header><span>{esc(point.get("label") or point.get("period") or "")}</span><b>{value}</b></header>'
                f'<div class="curve-track"><span class="curve-fill" style="width: {value}%"></span></div>'
                "</div>"
            )
        if points:
            curve_rows.append(
                '<article class="trajectory-row">'
                f"<h4>{esc(curve.get('title') or '传播轨迹')}</h4>"
                f"<p>{esc(curve.get('description') or '')}</p>"
                f'<div class="mini-curve-list">{"".join(points)}</div>'
                "</article>"
            )
    trajectory_html = f'<div class="trajectory-list">{"".join(curve_rows)}</div>' if curve_rows else ""

    influence_html = ""
    if include_curves and (legacy_html or trajectory_html):
        influence_html = (
            '<div class="review-block">'
            '<div class="review-heading"><span>04</span><h3>作品、奖项与传播轨迹</h3></div>'
            '<p class="review-copy">这里保留“影响力”和“可见度”的数据表达，但不再使用私人财富或权力增长这种容易误读的标题。</p>'
            '<div class="influence-layout">'
            f'<div>{legacy_html}</div>'
            f'<div>{trajectory_html}</div>'
            "</div>"
            "</div>"
        )

    context_html = ""
    if network_html or era_html:
        context_html = f'<div class="review-grid">{network_html}{era_html}</div>'

    return (
        '<section class="content-section" aria-labelledby="review-heading">'
        '<h2 id="review-heading" class="section-title">深描复盘</h2>'
        '<p class="section-note">读完时间轴后，再从“选择、关系、时代、传播”四个角度复盘人物。这个区域合并了原先分散的后半段模块。</p>'
        f"{decision_html}{context_html}{influence_html}"
        "</section>"
    )


def render_uncertainty(data: dict[str, Any]) -> str:
    notes = [str(x).strip() for x in as_list(data.get("uncertainty_notes")) if str(x).strip()]
    source_notes = [str(x).strip() for x in as_list(data.get("source_notes")) if str(x).strip()]
    all_notes = notes + source_notes
    if not all_notes:
        return '<div class="notice"><p>未记录明显资料冲突；仍建议读者以来源目录为准复核关键事实。</p></div>'
    items = "".join(f"<li>{esc(note)}</li>" for note in all_notes)
    return f'<div class="notice"><ul class="notes-list">{items}</ul></div>'


def render_bibliography(source_items: list[Any]) -> str:
    if not source_items:
        return '<p class="notice">暂无来源。</p>'
    items = []
    for source in source_items:
        if not isinstance(source, dict):
            continue
        sid = str(source.get("id") or "S?")
        title = source.get("title") or "未命名来源"
        publisher = source.get("publisher") or source.get("author") or ""
        tier = TIER_LABELS.get(str(source.get("tier") or ""), source.get("tier") or "未分级")
        accessed = source.get("accessed") or ""
        url = source.get("url") or ""
        title_html = f'<a href="{esc(url)}">{esc(title)}</a>' if url else esc(title)
        meta_parts = [part for part in [publisher, tier, f"访问日期：{accessed}" if accessed else ""] if part]
        meta = " · ".join(str(part) for part in meta_parts)
        items.append(
            f'<li id="source-{esc(sid)}">'
            f'<span class="source-id">[{esc(sid)}]</span> {title_html}'
            f'<p class="source-meta">{esc(meta)}</p>'
            "</li>"
        )
    return f'<ol class="bibliography">{"".join(items)}</ol>'


def render_sources_markdown(data: dict[str, Any]) -> str:
    subject = data.get("subject") or {}
    name = subject.get("name") or "人物"
    lines = [f"# {name} 来源清单", ""]
    if data.get("scope_note"):
        lines.extend(["## 编制范围", "", str(data["scope_note"]), ""])
    if data.get("uncertainty_notes"):
        lines.extend(["## 不确定性说明", ""])
        for note in as_list(data.get("uncertainty_notes")):
            lines.append(f"- {note}")
        lines.append("")
    lines.extend(["## Sources", ""])
    for source in as_list(data.get("sources")):
        if not isinstance(source, dict):
            continue
        sid = source.get("id") or "S?"
        title = source.get("title") or "未命名来源"
        publisher = source.get("publisher") or source.get("author") or ""
        url = source.get("url") or ""
        tier = source.get("tier") or "未分级"
        accessed = source.get("accessed") or ""
        line = f"- [{sid}] {title}"
        if publisher:
            line += f" | {publisher}"
        line += f" | tier: {tier}"
        if accessed:
            line += f" | accessed: {accessed}"
        if url:
            line += f" | {url}"
        lines.append(line)
    lines.append("")
    return "\n".join(lines)


def replace_all(template: str, replacements: dict[str, str]) -> str:
    html_text = template
    for key, value in replacements.items():
        html_text = html_text.replace("{{" + key + "}}", value)
    return html_text


def _linkify_text(text: Any, known_persons: list[str]) -> str:
    """Escape text, then wrap any known person names with cross-person hyperlinks.

    Longer names are replaced first so that overlapping short names do not get
    double-wrapped. Each link points to ``<name>-timeline`` per the cross-link
    convention used across the skill.
    """
    value = str(text or "")
    escaped = esc(value)
    if not known_persons or not value:
        return escaped
    for name in sorted(known_persons, key=len, reverse=True):
        if not name:
            continue
        needle = esc(name)
        if needle and needle in escaped:
            link = f'<a href="{esc(name)}-timeline">{esc(name)}</a>'
            escaped = escaped.replace(needle, link)
    return escaped


def _load_default_known_persons() -> list[str]:
    """Load the default known-persons list from the bundled person_db module.

    Falls back to an empty list if person_db is unavailable (e.g. when this
    script is invoked from a different working directory).
    """
    try:
        import person_db  # type: ignore[import-not-found]
        db = getattr(person_db, "PERSON_DB", None)
        if isinstance(db, dict):
            return [str(name) for name in db.keys() if str(name).strip()]
    except Exception:
        pass
    return []


def render_cross_links(data: dict[str, Any], known_persons: list[str]) -> None:
    """Inject cross-person hyperlinks into relationship_network nodes and events.

    - For each ``relationship_network.nodes`` entry whose ``name`` is itself a known
      person, replace known person names appearing in its ``description`` with links.
    - For every event, replace known person names appearing in ``title`` and
      ``description`` with links.

    The resulting HTML is stored under ``_html_description`` / ``_html_title`` keys
    so the rendering helpers (``field_html``) emit it without double-escaping.
    """
    if not known_persons:
        return
    network = data.get("relationship_network")
    if isinstance(network, dict):
        for node in as_list(network.get("nodes")):
            if not isinstance(node, dict):
                continue
            if node.get("name") in known_persons:
                node["_html_description"] = _linkify_text(node.get("description"), known_persons)
    for event in as_list(data.get("events")):
        if not isinstance(event, dict):
            continue
        event["_html_title"] = _linkify_text(event.get("title"), known_persons)
        event["_html_description"] = _linkify_text(event.get("description"), known_persons)


def render_json_ld(data: dict[str, Any]) -> str:
    """Generate Schema.org Person JSON-LD structured data for SEO."""
    subject = data.get("subject") or {}
    events = [e for e in as_list(data.get("events")) if isinstance(e, dict)]
    name = subject.get("name") or ""
    native_name = subject.get("native_name") or ""
    birth_date = subject.get("birth_date") or ""
    fields = [str(f) for f in as_list(subject.get("fields")) if str(f).strip()]

    key_events = []
    for event in events[:10]:
        if str(event.get("importance", "")).lower() == "major" or event.get("category") == "出生":
            key_events.append({
                "@type": "Event",
                "name": str(event.get("title") or ""),
                "startDate": str(event.get("date") or ""),
            })

    ld = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": name,
    }
    if native_name:
        ld["alternateName"] = native_name
    if birth_date:
        ld["birthDate"] = birth_date
    if fields:
        ld["knowsAbout"] = fields
    if key_events:
        ld["subjectOf"] = {
            "@type": "TimelineEvent",
            "name": f"{name}生平时间线",
            "event": key_events
        }
    import json as _json
    return _json.dumps(ld, ensure_ascii=False)


def render_visual_timeline(data: dict[str, Any]) -> str:
    """Generate a horizontal visual timeline bar with key events as dots."""
    subject = data.get("subject") or {}
    events = [e for e in as_list(data.get("events")) if isinstance(e, dict)]
    events = sorted(events, key=event_sort_key)

    if not events:
        return ""

    date_range = str(subject.get("date_range") or "")
    range_match = re.search(r'(\d{4})\s*[-–]\s*(\d{4})?', date_range)
    if range_match:
        start_year = int(range_match.group(1))
        end_year = int(range_match.group(2)) if range_match.group(2) else _dt.date.today().year
    else:
        years = []
        for event in events:
            match = re.search(r'(-?\d{4})', str(event.get("date") or ""))
            if match:
                years.append(int(match.group(1)))
        if not years:
            return ""
        start_year = min(years)
        end_year = max(years)

    if end_year <= start_year:
        end_year = start_year + 1

    span = end_year - start_year

    # Select major events (max 15)
    major_events = [e for e in events if str(e.get("importance", "")).lower() == "major"]
    if not major_events:
        major_events = events
    major_events = major_events[:15]

    dots = []
    for event in major_events:
        event_date = str(event.get("date") or "")
        year_match = re.search(r'(-?\d{4})', event_date)
        if not year_match:
            continue
        event_year = int(year_match.group(1))
        if event_year < start_year:
            event_year = start_year
        if event_year > end_year:
            event_year = end_year
        pos = ((event_year - start_year) / span) * 100
        pos = max(2, min(98, pos))

        title = str(event.get("title") or "")
        # Truncate title for tooltip
        short_title = title[:20] + "…" if len(title) > 20 else title
        is_major = str(event.get("importance", "")).lower() == "major"
        css_class = "major" if is_major else ""

        dots.append(
            f'<div class="visual-timeline-dot {css_class}" '
            f'style="left:{pos:.1f}%" '
            f'data-date="{esc(event_date)}" '
            f'data-label="{esc(short_title)}"></div>'
        )

    if not dots:
        return ""

    dots_html = "\n".join(dots)
    return (
        '<div class="visual-timeline">'
        '<h2 class="section-title" style="font-size:1.1rem;margin-bottom:0.5rem;">生平轨迹</h2>'
        '<div class="visual-timeline-track">'
        '<div class="visual-timeline-line"></div>'
        f'{dots_html}'
        '</div>'
        '<div class="visual-timeline-labels">'
        f'<span>{esc(str(start_year))}</span>'
        f'<span>{esc(str(end_year))}</span>'
        '</div>'
        '</div>'
    )


def render_html(data: dict[str, Any], template_path: Path, known_persons: list[str] | None = None) -> str:
    if known_persons:
        render_cross_links(data, known_persons)
    subject = data.get("subject") or {}
    events = [event for event in as_list(data.get("events")) if isinstance(event, dict)]
    events = sorted(events, key=event_sort_key)
    sources_list = as_list(data.get("sources"))
    sources = source_map(data)
    name = subject.get("name") or "人物时间线"
    native = subject.get("native_name")
    fields = "、".join(str(x) for x in as_list(subject.get("fields")) if str(x).strip())
    desc_lines = as_list(subject.get("description"))
    desc_html = "".join(
        f'<p class="subject-desc">{esc(str(line))}</p>' for line in desc_lines if str(line).strip()
    )
    meta_parts = [part for part in [native, subject.get("date_range"), fields] if part]
    generated_at = data.get("generated_at") or _dt.date.today().isoformat()
    template = template_path.read_text(encoding="utf-8")
    summary = data.get("summary") or subject.get("short_bio")
    scope_note = data.get("scope_note") or "本页依据公开可查资料编制，重点呈现可核验的时间线和大事记。"
    portrait_url = subject.get("portrait_url", "")
    if portrait_url:
        portrait_html = f'<img class="hero-portrait" src="{esc(portrait_url)}" alt="{esc(name)}" loading="lazy" onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'flex\'"><div class="hero-portrait-fallback" style="display:none">{esc(name[0] if name else "?")}</div>'
    else:
        portrait_html = f'<div class="hero-portrait-fallback" style="display:flex">{esc(name[0] if name else "?")}</div>'
    replacements = {
        "PAGE_TITLE": esc(f"{name}｜人物时间线与大事记"),
        "SUBJECT_NAME": esc(name),
        "PORTRAIT": portrait_html,
        "COVER_IMAGE": portrait_html,
        "PORTRAIT_URL": esc(portrait_url),
        "CANONICAL_URL": esc(f"https://example.com/{clean_slug(name)}-timeline"),
        "JSON_LD": render_json_ld(data),
        "VISUAL_TIMELINE": render_visual_timeline(data),
        "SUBJECT_META": esc(" · ".join(str(x) for x in meta_parts) or "人物时间线档案"),
        "SUBJECT_DESC": desc_html,
        "HERO_SUMMARY": render_hero_summary(summary),
        "HERO_ASIDE_TITLE": esc(render_hero_aside_title(data)),
        "AGE_OVERVIEW": render_age_overview(data, subject, events, sources),
        "EPITAPH": render_epitaph(data, sources),
        "ACHIEVEMENT_CONTROVERSY": render_achievement_controversy(data, sources),
        "SUMMARY": render_paragraphs(summary),
        "STATS": render_stats(subject, events, sources_list),
        "IDENTIFIERS": render_identifiers(subject),
        "SCOPE_NOTE": render_paragraphs(scope_note),
        "MAJOR_EVENTS": render_major_events(events, sources, as_list(data.get("major_event_ids"))),
        "LIFE_STAGES": render_life_stages(data, subject, events, sources),
        "TIMELINE_SIDEBAR_TITLE": render_timeline_sidebar_title(data),
        "TIMELINE_SIDEBAR": render_timeline_sidebar(data, events, sources),
        "TIMELINE_EVENTS": render_timeline(events, sources, subject, as_list(data.get("major_event_ids"))),
        "TURNING_POINTS": render_turning_points(data, sources),
        "RELATIONSHIP_NETWORK": render_relationship_network(data, sources, subject),
        "ERA_MAP": render_era_map(data, sources),
        "INFLUENCE_LEGACY": render_influence_legacy(data, sources),
        "GROWTH_CURVES": render_growth_curves(data, sources),
        "DEEP_REVIEW": render_deep_review(data, sources, subject, include_curves=False),
        "UNCERTAINTY_NOTES": render_uncertainty(data),
        "BIBLIOGRAPHY": render_bibliography(sources_list),
        "GENERATED_AT": esc(generated_at),
    }
    html_output = replace_all(template, replacements)
    # Insert JSON-LD before </head>
    json_ld = render_json_ld(data)
    json_ld_script = f'<script type="application/ld+json">{json_ld}</script>'
    html_output = html_output.replace("</head>", f"{json_ld_script}\n</head>", 1)
    return html_output


def completeness_warnings(data: dict[str, Any], profile_mode: str = "fast") -> list[str]:
    events = [event for event in as_list(data.get("events")) if isinstance(event, dict)]
    sources = [source for source in as_list(data.get("sources")) if isinstance(source, dict)]
    subject = data.get("subject") or {}
    warnings: list[str] = []

    if profile_mode == "deep":
        required_deep_fields = [
            "epitaph",
            "timeline_sidebar",
            "achievement_controversy_brief",
            "life_stages",
            "turning_points",
            "relationship_network",
            "era_map",
            "influence_legacy",
            "growth_curves",
        ]
        missing = [field for field in required_deep_fields if not data.get(field)]
        if missing:
            warnings.append("missing deep-profile fields: " + ", ".join(missing))
        if not data.get("source_notes"):
            warnings.append("source_notes is empty")
        if not data.get("uncertainty_notes"):
            warnings.append("uncertainty_notes is empty")

    if len(sources) < 4:
        warnings.append(f"only {len(sources)} sources; consider adding more")
    if len(events) < 6:
        warnings.append(f"only {len(events)} events; consider adding more")

    if not events:
        warnings.append("FATAL: no events found — cannot generate timeline")
    if not sources:
        warnings.append("FATAL: no sources found — cannot generate credible page")

    # portrait_url should be populated for a proper hero section
    if not subject.get("portrait_url"):
        warnings.append("portrait_url is empty — consider extracting from Wikipedia infobox")

    # every event should reference at least one source
    events_without_sources = [e for e in events if not e.get("source_ids")]
    if events_without_sources:
        warnings.append(f"{len(events_without_sources)} events have no source_ids")

    # birth_date should be consistent with the first birth event
    birth_events = [e for e in events if "出生" in str(e.get("category", "")) or "出生" in str(e.get("title", ""))]
    if birth_events and subject.get("birth_date"):
        event_date = str(birth_events[0].get("date", ""))
        if event_date and subject["birth_date"] not in event_date and event_date not in subject["birth_date"]:
            warnings.append(f"birth_date mismatch: subject says {subject['birth_date']}, first birth event says {event_date}")

    # event dates should fall inside the declared date_range
    if subject.get("date_range"):
        for event in events:
            event_date = str(event.get("date", ""))
            if event_date:
                match = re.search(r'(\d{4})', event_date)
                if match:
                    year = int(match.group(1))
                    range_parts = subject["date_range"].split("-")
                    if len(range_parts) >= 2:
                        try:
                            start_year = int(re.search(r'\d{4}', range_parts[0]).group())
                            end_part = range_parts[1].strip()
                            end_year = int(re.search(r'\d{4}', end_part).group()) if re.search(r'\d{4}', end_part) else 9999
                            if year < start_year or year > end_year:
                                warnings.append(f"event date {event_date} is outside date_range {subject['date_range']}")
                                break
                        except (AttributeError, ValueError):
                            pass

    return warnings


def _extract_index_entries(directory: Path) -> list[dict[str, str]]:
    """Scan directory for *-timeline.html files and pull out name/desc/portrait."""
    entries: list[dict[str, str]] = []
    for path in sorted(directory.glob("*-timeline.html")):
        if path.name == "index.html":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        title_match = re.search(r"<title>(.*?)</title>", text, re.S)
        title = title_match.group(1).strip() if title_match else path.stem
        name = re.sub(r"｜人物时间线与大事记\s*$", "", title).strip() or path.stem
        desc = ""
        desc_match = re.search(r'<p class="subject-desc">(.*?)</p>', text, re.S)
        if desc_match:
            desc = re.sub(r"<[^>]+>", "", desc_match.group(1)).strip()
        if not desc:
            summary_match = re.search(r'<div class="hero-summary">.*?<p>(.*?)</p>', text, re.S)
            if summary_match:
                desc = re.sub(r"<[^>]+>", "", summary_match.group(1)).strip()
        portrait = ""
        img_match = re.search(r'<img class="hero-portrait" src="([^"]+)"', text)
        if img_match:
            portrait = img_match.group(1).strip()
        entries.append({"name": name, "desc": desc, "portrait": portrait, "file": path.name})
    return entries


def _render_index_html(entries: list[dict[str, str]]) -> str:
    cards: list[str] = []
    for entry in entries:
        name = entry["name"]
        desc = entry["desc"] or "暂无简介"
        href = entry["file"]
        portrait = entry["portrait"]
        if portrait:
            avatar = f'<img src="{esc(portrait)}" class="card-avatar" alt="{esc(name)}" loading="lazy">'
        else:
            initial = esc(name[0] if name else "?")
            avatar = f'<div class="card-avatar card-avatar-fallback">{initial}</div>'
        cards.append(
            f'<a class="person-card" href="{esc(href)}" data-name="{esc(name)}">'
            f'{avatar}'
            f'<h3 class="person-name">{esc(name)}</h3>'
            f'<p class="person-desc">{esc(desc)}</p>'
            f"</a>"
        )
    cards_html = "\n".join(cards)
    count = len(entries)
    generated = _dt.date.today().isoformat()
    style = """
    :root { --brand: #6f2d37; --brand-soft: #a04451; }
    * { box-sizing: border-box; }
    body { margin: 0; background: #f6f1ee; color: #2b2326;
      font-family: -apple-system, "PingFang SC", "Microsoft YaHei", "Segoe UI", sans-serif; }
    .index-header { background: var(--brand); color: #fff; padding: 3rem 1rem 2.5rem; text-align: center; }
    .index-header h1 { margin: 0 0 .5rem; font-size: clamp(1.8rem, 4vw, 2.6rem); letter-spacing: .04em; }
    .index-header p { margin: 0; opacity: .85; }
    .search-wrap { max-width: 880px; margin: -1.75rem auto 0; padding: 0 1rem; position: relative; z-index: 2; }
    .search-wrap input { border-radius: 999px; border: 1px solid #e3d6d8;
      box-shadow: 0 6px 24px rgba(111,45,55,.18); padding: .9rem 1.4rem; }
    .person-grid { max-width: 1180px; margin: 2.25rem auto 1rem; padding: 0 1rem;
      display: grid; gap: 1.25rem; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); }
    .person-card { display: flex; flex-direction: column; align-items: center; text-align: center;
      text-decoration: none; color: inherit; background: #fff; border-radius: 16px;
      padding: 1.6rem 1.1rem 1.4rem; border: 1px solid #ece2e4;
      transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease; }
    .person-card:hover { transform: translateY(-6px); box-shadow: 0 14px 34px rgba(111,45,55,.16);
      border-color: var(--brand-soft); }
    .card-avatar { width: 96px; height: 96px; border-radius: 50%; object-fit: cover;
      border: 3px solid var(--archive-line, #e3d6d8); box-shadow: 0 4px 16px rgba(0,0,0,.12);
      margin-bottom: .9rem; flex-shrink: 0; }
    .card-avatar-fallback { display: flex; align-items: center; justify-content: center;
      font-size: 2.4rem; font-weight: 700; color: #fff; line-height: 1; user-select: none;
      background: linear-gradient(135deg, var(--brand), var(--brand-soft)); }
    .person-name { font-size: 1.18rem; margin: 0 0 .45rem; color: var(--brand); }
    .person-desc { font-size: .9rem; line-height: 1.55; color: #6b5f63; margin: 0;
      display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }
    .empty-hint { text-align: center; color: #8a7e82; padding: 2.5rem 1rem; }
    .index-footer { text-align: center; color: #8a7e82; font-size: .85rem; padding: 2rem 1rem 3rem; }
    @media (max-width: 540px) { .person-grid { grid-template-columns: 1fr; } }
    """
    return (
        "<!DOCTYPE html>\n"
        '<html lang="zh-CN">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        "<title>人物时间线索引</title>\n"
        '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">\n'
        f"<style>{style}</style>\n"
        "</head>\n<body>\n"
        '<header class="index-header">\n'
        "<h1>人物时间线索引</h1>\n"
        f'<p>共收录 {count} 位人物，点击卡片查看完整时间线</p>\n'
        "</header>\n"
        '<div class="search-wrap">\n'
        '<input type="search" id="person-search" class="form-control form-control-lg"'
        ' placeholder="输入人名实时搜索…" autocomplete="off">\n'
        "</div>\n"
        '<main>\n'
        f'<div class="person-grid" id="person-grid">\n{cards_html}\n</div>\n'
        '<p class="empty-hint" id="empty-hint" style="display:none">没有匹配的人物。</p>\n'
        "</main>\n"
        '<footer class="index-footer">\n'
        f"共 {count} 位人物 · 自动生成于 {esc(generated)}\n"
        "</footer>\n"
        "<script>\n"
        "(function () {\n"
        '  var input = document.getElementById("person-search");\n'
        '  var grid = document.getElementById("person-grid");\n'
        '  var hint = document.getElementById("empty-hint");\n'
        "  var cards = grid.querySelectorAll('.person-card');\n"
        "  input.addEventListener('input', function () {\n"
        "    var q = this.value.trim().toLowerCase();\n"
        "    var visible = 0;\n"
        "    cards.forEach(function (card) {\n"
        "      var name = (card.getAttribute('data-name') || '').toLowerCase();\n"
        "      var show = !q || name.indexOf(q) !== -1;\n"
        "      card.style.display = show ? '' : 'none';\n"
        "      if (show) visible++;\n"
        "    });\n"
        "    hint.style.display = visible ? 'none' : '';\n"
        "    grid.style.display = visible ? '' : 'none';\n"
        "  });\n"
        "})();\n"
        "</script>\n"
        "</body>\n</html>\n"
    )


def generate_index(directory: Path) -> None:
    """Scan DIR for *-timeline.html files and regenerate index.html.

    For each timeline it extracts the person name (from <title>), a short
    description (from the first subject-desc / hero-summary paragraph) and the
    portrait URL (from the hero-portrait <img>), then writes a Bootstrap 5
    gallery page with a live search box.
    """
    entries = _extract_index_entries(directory)
    index_path = directory / "index.html"
    index_path.write_text(_render_index_html(entries), encoding="utf-8")
    print(f"Wrote {index_path} ({len(entries)} entries)")


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a person timeline JSON file to an archive-style HTML page.")
    parser.add_argument("data_json", type=Path, help="Path to timeline data JSON.")
    parser.add_argument("--output", type=Path, help="Output HTML path. Defaults to <person-slug>-timeline.html.")
    parser.add_argument("--sources-output", type=Path, help="Output Markdown sources path. Defaults to <person-slug>-sources.md.")
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE, help="HTML template path.")
    parser.add_argument("--allow-incomplete", action="store_true", help="Allow rendering a thin draft even when deep-profile completeness checks fail.")
    parser.add_argument("--strict-completeness", action="store_true", help="Deprecated: completeness checks are strict by default unless --allow-incomplete is passed.")
    parser.add_argument("--profile", choices=["fast","deep"], default="fast", help="Profile mode: fast=skip deep-profile field checks; deep=full completeness check. Default: fast.")
    parser.add_argument("--update-index", type=Path, metavar="DIR", help="After rendering, scan DIR for *-timeline.html files and regenerate index.html")
    parser.add_argument("--cross-link-names", default=None, help="Comma-separated list of known person names to cross-link. Defaults to all names in person_db.")
    args = parser.parse_args()

    data = json.loads(args.data_json.read_text(encoding="utf-8-sig"))
    subject = data.get("subject") or {}
    slug = clean_slug(str(subject.get("name") or args.data_json.stem))
    output = args.output or args.data_json.with_name(f"{slug}-timeline.html")
    sources_output = args.sources_output or args.data_json.with_name(f"{slug}-sources.md")

    if args.cross_link_names is not None:
        known_persons = [name.strip() for name in args.cross_link_names.split(",") if name.strip()]
    else:
        known_persons = _load_default_known_persons()

    output.write_text(render_html(data, args.template, known_persons=known_persons), encoding="utf-8")
    sources_output.write_text(render_sources_markdown(data), encoding="utf-8")
    warnings = completeness_warnings(data, profile_mode=args.profile)
    if warnings:
        print("Completeness warnings:", file=sys.stderr)
        for warning in warnings:
            print(f"- {warning}", file=sys.stderr)
        # In fast mode, only block on truly missing data (0 events / 0 sources)
        has_events = len([e for e in as_list(data.get("events")) if isinstance(e, dict)]) > 0
        has_sources = len([s for s in as_list(data.get("sources")) if isinstance(s, dict)]) > 0
        critical_missing = not has_events or not has_sources
        if (args.profile == "deep" and not args.allow_incomplete) or (critical_missing and not args.allow_incomplete):
            return 2
    print(f"Wrote {output}")
    print(f"Wrote {sources_output}")
    if args.update_index:
        generate_index(args.update_index)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
