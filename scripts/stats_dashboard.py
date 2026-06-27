#!/usr/bin/env python3
"""数据库统计仪表盘 — 生成数据库覆盖率、事件分布等可视化页面。

用法：
  python3 stats_dashboard.py --output /tmp/stats.html
  python3 stats_dashboard.py --deploy
"""

import argparse
import datetime as _dt
import html
import json
import sys
from pathlib import Path
from collections import Counter

SCRIPT_DIR = Path(__file__).resolve().parent
DEPLOY_DIR = Path("/tmp/deploy-renwujianxian")


def esc(value) -> str:
    return html.escape("" if value is None else str(value), quote=True)


def load_db() -> dict:
    try:
        sys.path.insert(0, str(SCRIPT_DIR))
        from person_db import PERSON_DB
        return PERSON_DB
    except Exception:
        return {}


def compute_stats(db: dict) -> dict:
    total = len(db)
    total_events = 0
    total_sources = 0
    total_turning_points = 0
    field_counter = Counter()
    era_counter = Counter()
    persons = []

    for name, data in db.items():
        subject = data.get("subject", {})
        events = [e for e in data.get("events", []) if isinstance(e, dict)]
        sources = data.get("sources", [])
        tps = data.get("turning_points", [])

        total_events += len(events)
        total_sources += len(sources)
        total_turning_points += len(tps)

        for f in subject.get("fields", []):
            field_counter[str(f)] += 1

        date_range = str(subject.get("date_range", ""))
        import re
        year_match = re.search(r'(\d{4})', date_range)
        if year_match:
            birth_year = int(year_match.group(1))
            decade = (birth_year // 10) * 10
            era_counter[f"{decade}s"] += 1

        portrait = "有" if subject.get("portrait_url") else "无"
        persons.append({
            "name": name,
            "events": len(events),
            "sources": len(sources),
            "turning_points": len(tps),
            "date_range": date_range,
            "fields": "、".join(subject.get("fields", [])),
            "portrait": portrait,
        })

    return {
        "total_persons": total,
        "total_events": total_events,
        "total_sources": total_sources,
        "total_turning_points": total_turning_points,
        "avg_events": round(total_events / total, 1) if total else 0,
        "field_distribution": field_counter.most_common(),
        "era_distribution": dict(sorted(era_counter.items())),
        "persons": persons,
        "generated_at": _dt.date.today().isoformat(),
    }


def render_stats_html(stats: dict) -> str:
    style = """
    :root { --brand: #6f2d37; --brand-soft: #a04451; --line: #e5e7eb; --muted: #667085; }
    * { box-sizing: border-box; }
    body { margin: 0; background: #f7f7f4; color: #202124;
      font-family: ui-sans-serif, system-ui, -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif; line-height: 1.7; }
    .container { max-width: 1100px; margin: 0 auto; padding: 2rem 1rem; }
    .stats-header { text-align: center; margin-bottom: 2rem; }
    .stats-header h1 { font-size: clamp(1.5rem, 4vw, 2.2rem); color: var(--brand); margin: 0 0 0.3rem; }
    .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 1rem; margin-bottom: 2rem; }
    .stat-card { background: #fff; border: 1px solid var(--line); border-radius: 12px; padding: 1.5rem; text-align: center; }
    .stat-card .num { font-size: 2.2rem; font-weight: 800; color: var(--brand); }
    .stat-card .label { font-size: 0.82rem; color: var(--muted); margin-top: 0.3rem; }
    .section { background: #fff; border: 1px solid var(--line); border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem; }
    .section h2 { font-size: 1.15rem; color: var(--brand); margin: 0 0 1rem; padding-bottom: 0.5rem; border-bottom: 2px solid var(--brand); }
    .bar-chart { display: flex; flex-direction: column; gap: 0.5rem; }
    .bar-row { display: flex; align-items: center; gap: 0.5rem; }
    .bar-label { width: 100px; font-size: 0.85rem; color: var(--muted); text-align: right; }
    .bar-track { flex: 1; height: 24px; background: #f0f0f0; border-radius: 4px; overflow: hidden; }
    .bar-fill { height: 100%; background: linear-gradient(90deg, var(--brand), var(--brand-soft)); border-radius: 4px; display: flex; align-items: center; padding-left: 0.5rem; color: #fff; font-size: 0.75rem; font-weight: 600; }
    table { width: 100%; border-collapse: collapse; }
    th, td { padding: 0.6rem 0.5rem; text-align: left; border-bottom: 1px solid var(--line); font-size: 0.88rem; }
    th { color: var(--muted); font-weight: 600; font-size: 0.78rem; text-transform: uppercase; }
    .portrait-yes { color: #476458; font-weight: 600; }
    .portrait-no { color: #a84b24; font-weight: 600; }
    .footer { text-align: center; color: var(--muted); font-size: 0.8rem; margin-top: 2rem; }
    a { color: var(--brand); }
    """

    # Field distribution bars
    max_field = max((count for _, count in stats["field_distribution"]), default=1) or 1
    field_bars = ""
    for field, count in stats["field_distribution"][:10]:
        pct = (count / max_field) * 100
        field_bars += (
            f'<div class="bar-row">'
            f'<span class="bar-label">{esc(field)}</span>'
            f'<div class="bar-track"><div class="bar-fill" style="width:{pct:.0f}%">{count}</div></div>'
            f'</div>'
        )

    # Era distribution bars
    max_era = max(stats["era_distribution"].values(), default=1) or 1
    era_bars = ""
    for era, count in stats["era_distribution"].items():
        pct = (count / max_era) * 100
        era_bars += (
            f'<div class="bar-row">'
            f'<span class="bar-label">{esc(era)}</span>'
            f'<div class="bar-track"><div class="bar-fill" style="width:{pct:.0f}%">{count}</div></div>'
            f'</div>'
        )

    # Person table
    table_rows = ""
    for p in sorted(stats["persons"], key=lambda x: x["events"], reverse=True):
        portrait_class = "portrait-yes" if p["portrait"] == "有" else "portrait-no"
        table_rows += (
            f"<tr>"
            f'<td><a href="https://example.com/{esc(p["name"])}-timeline">{esc(p["name"])}</a></td>'
            f'<td>{esc(p["date_range"])}</td>'
            f'<td>{esc(p["fields"])}</td>'
            f'<td style="text-align:center">{p["events"]}</td>'
            f'<td style="text-align:center">{p["sources"]}</td>'
            f'<td style="text-align:center">{p["turning_points"]}</td>'
            f'<td style="text-align:center" class="{portrait_class}">{p["portrait"]}</td>'
            f"</tr>"
        )

    return (
        f"<!DOCTYPE html>\n<html lang=\"zh-CN\">\n<head>\n"
        f"<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        f"<title>人物时间线 — 数据库统计</title>\n"
        f"<style>{style}</style>\n</head>\n<body>\n"
        f'<div class="container">\n'
        f'<div class="stats-header"><h1>📊 数据库统计仪表盘</h1>'
        f'<p style="color:var(--muted)">人物时间线数据库覆盖与质量分析</p></div>\n'
        # Summary cards
        f'<div class="stats-grid">'
        f'<div class="stat-card"><div class="num">{stats["total_persons"]}</div><div class="label">收录人物</div></div>'
        f'<div class="stat-card"><div class="num">{stats["total_events"]}</div><div class="label">总事件数</div></div>'
        f'<div class="stat-card"><div class="num">{stats["total_sources"]}</div><div class="label">总来源数</div></div>'
        f'<div class="stat-card"><div class="num">{stats["total_turning_points"]}</div><div class="label">转折点</div></div>'
        f'<div class="stat-card"><div class="num">{stats["avg_events"]}</div><div class="label">人均事件</div></div>'
        f'</div>\n'
        # Field distribution
        f'<div class="section"><h2>领域分布</h2><div class="bar-chart">{field_bars}</div></div>\n'
        # Era distribution
        f'<div class="section"><h2>时代分布</h2><div class="bar-chart">{era_bars}</div></div>\n'
        # Person table
        f'<div class="section"><h2>人物明细</h2>'
        f'<table><thead><tr>'
        f'<th>人物</th><th>年代</th><th>领域</th><th>事件</th><th>来源</th><th>转折点</th><th>头像</th>'
        f'</tr></thead><tbody>{table_rows}</tbody></table></div>\n'
        f'<div class="footer">生成于 {esc(stats["generated_at"])} · <a href="https://example.com/">返回索引</a></div>\n'
        f'</div>\n</body>\n</html>\n'
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="数据库统计仪表盘")
    parser.add_argument("--output", type=Path, help="输出HTML路径")
    parser.add_argument("--deploy", action="store_true", help="生成后部署")
    args = parser.parse_args()

    db = load_db()
    if not db:
        print("数据库为空或无法读取", file=sys.stderr)
        return 1

    stats = compute_stats(db)
    html_output = render_stats_html(stats)
    output = args.output or DEPLOY_DIR / "stats.html"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(html_output, encoding="utf-8")
    print(f"Wrote {output}")
    print(f"  总人物: {stats['total_persons']}")
    print(f"  总事件: {stats['total_events']}")
    print(f"  总来源: {stats['total_sources']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
