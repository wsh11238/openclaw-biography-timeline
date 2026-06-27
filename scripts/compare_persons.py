#!/usr/bin/env python3
"""人物对比 — 生成两位人物的对比页面。

用法：
  python3 compare_persons.py 毛泽东 邓小平
  python3 compare_persons.py 毛泽东 邓小平 --output /tmp/compare.html
"""

import argparse
import datetime as _dt
import html
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent


def esc(value) -> str:
    return html.escape("" if value is None else str(value), quote=True)


def load_person(name: str) -> dict:
    try:
        sys.path.insert(0, str(SCRIPT_DIR))
        from person_db import PERSON_DB
        return PERSON_DB.get(name, {})
    except Exception:
        return {}


def render_comparison(name1: str, data1: dict, name2: str, data2: dict) -> str:
    s1 = data1.get("subject", {})
    s2 = data2.get("subject", {})
    e1 = [e for e in data1.get("events", []) if isinstance(e, dict)]
    e2 = [e for e in data2.get("events", []) if isinstance(e, dict)]
    src1 = data1.get("sources", [])
    src2 = data2.get("sources", [])
    tp1 = data1.get("turning_points", [])
    tp2 = data2.get("turning_points", [])

    def portrait_html(subject, name):
        url = subject.get("portrait_url", "")
        if url:
            return f'<img src="{esc(url)}" class="compare-portrait" alt="{esc(name)}" loading="lazy" onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'flex\'"><div class="compare-portrait-fallback" style="display:none">{esc(name[0] if name else "?")}</div>'
        return f'<div class="compare-portrait-fallback" style="display:flex">{esc(name[0] if name else "?")}</div>'

    def events_html(events):
        if not events:
            return "<p>暂无事件</p>"
        items = []
        for e in events[:15]:
            items.append(f'<div class="compare-event"><time>{esc(e.get("date",""))}</time><strong>{esc(e.get("title",""))}</strong></div>')
        return "".join(items)

    def turning_html(tps):
        if not tps:
            return "<p>暂无转折点</p>"
        items = []
        for tp in tps[:5]:
            if isinstance(tp, dict):
                items.append(f'<div class="compare-tp"><strong>{esc(tp.get("title",""))}</strong><p>{esc(tp.get("description",""))}</p></div>')
        return "".join(items)

    generated = _dt.date.today().isoformat()
    style = """
    :root { --brand: #6f2d37; --brand-soft: #a04451; --line: #e5e7eb; --muted: #667085; }
    * { box-sizing: border-box; }
    body { margin: 0; background: #f7f7f4; color: #202124;
      font-family: ui-sans-serif, system-ui, -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif; line-height: 1.7; }
    .container { max-width: 1200px; margin: 0 auto; padding: 2rem 1rem; }
    .compare-header { text-align: center; margin-bottom: 2rem; }
    .compare-header h1 { font-size: clamp(1.5rem, 4vw, 2.5rem); color: var(--brand); margin: 0 0 0.5rem; }
    .compare-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; }
    @media (max-width: 768px) { .compare-grid { grid-template-columns: 1fr; } }
    .compare-col { background: #fff; border: 1px solid var(--line); border-radius: 12px; padding: 1.5rem; }
    .compare-portrait { width: 120px; height: 120px; border-radius: 50%; object-fit: cover; border: 3px solid var(--line); margin: 0 auto 0.75rem; display: block; }
    .compare-portrait-fallback { width: 120px; height: 120px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 3rem; font-weight: 700; color: #fff; background: linear-gradient(135deg, var(--brand), var(--brand-soft)); margin: 0 auto 0.75rem; }
    .compare-name { text-align: center; font-size: 1.4rem; font-weight: 700; margin: 0 0 0.3rem; color: var(--brand); }
    .compare-meta { text-align: center; color: var(--muted); font-size: 0.85rem; margin-bottom: 1rem; }
    .compare-section { margin-top: 1.2rem; }
    .compare-section h3 { font-size: 1rem; color: var(--brand); margin: 0 0 0.5rem; padding-bottom: 0.3rem; border-bottom: 2px solid var(--brand); }
    .compare-event { padding: 0.4rem 0; border-bottom: 1px solid var(--line); }
    .compare-event time { color: var(--muted); font-size: 0.8rem; margin-right: 0.5rem; }
    .compare-tp { padding: 0.4rem 0; border-bottom: 1px solid var(--line); }
    .compare-tp strong { font-size: 0.9rem; }
    .compare-tp p { font-size: 0.82rem; color: var(--muted); margin: 0.2rem 0 0; }
    .compare-stats { display: flex; gap: 1rem; justify-content: center; margin-bottom: 1rem; }
    .stat-box { text-align: center; }
    .stat-box .num { font-size: 1.8rem; font-weight: 700; color: var(--brand); }
    .stat-box .label { font-size: 0.72rem; color: var(--muted); }
    .compare-footer { text-align: center; color: var(--muted); font-size: 0.8rem; margin-top: 2rem; }
    a { color: var(--brand); }
    """

    return (
        f"<!DOCTYPE html>\n<html lang=\"zh-CN\">\n<head>\n"
        f"<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        f"<title>{esc(name1)} vs {esc(name2)} — 人物对比</title>\n"
        f"<style>{style}</style>\n</head>\n<body>\n"
        f'<div class="container">\n'
        f'<div class="compare-header"><h1>{esc(name1)} <span style="color:var(--muted);font-weight:300">vs</span> {esc(name2)}</h1>'
        f'<p style="color:var(--muted)">人物时间线对比分析</p></div>\n'
        f'<div class="compare-grid">\n'
        f'<div class="compare-col">\n'
        f'{portrait_html(s1, name1)}\n'
        f'<h2 class="compare-name">{esc(name1)}</h2>\n'
        f'<p class="compare-meta">{esc(s1.get("date_range",""))} · {esc("、".join(s1.get("fields",[])))}</p>\n'
        f'<div class="compare-stats">'
        f'<div class="stat-box"><div class="num">{len(e1)}</div><div class="label">事件</div></div>'
        f'<div class="stat-box"><div class="num">{len(src1)}</div><div class="label">来源</div></div>'
        f'<div class="stat-box"><div class="num">{len(tp1)}</div><div class="label">转折点</div></div>'
        f'</div>\n'
        f'<div class="compare-section"><h3>关键事件</h3>{events_html(e1)}</div>\n'
        f'<div class="compare-section"><h3>命运转折</h3>{turning_html(tp1)}</div>\n'
        f'</div>\n'
        f'<div class="compare-col">\n'
        f'{portrait_html(s2, name2)}\n'
        f'<h2 class="compare-name">{esc(name2)}</h2>\n'
        f'<p class="compare-meta">{esc(s2.get("date_range",""))} · {esc("、".join(s2.get("fields",[])))}</p>\n'
        f'<div class="compare-stats">'
        f'<div class="stat-box"><div class="num">{len(e2)}</div><div class="label">事件</div></div>'
        f'<div class="stat-box"><div class="num">{len(src2)}</div><div class="label">来源</div></div>'
        f'<div class="stat-box"><div class="num">{len(tp2)}</div><div class="label">转折点</div></div>'
        f'</div>\n'
        f'<div class="compare-section"><h3>关键事件</h3>{events_html(e2)}</div>\n'
        f'<div class="compare-section"><h3>命运转折</h3>{turning_html(tp2)}</div>\n'
        f'</div>\n'
        f'</div>\n'
        f'<div class="compare-footer">'
        f'<p>生成于 {esc(generated)} · '
        f'<a href="https://example.com/{esc(name1)}-timeline">{esc(name1)}完整时间线</a> · '
        f'<a href="https://example.com/{esc(name2)}-timeline">{esc(name2)}完整时间线</a>'
        f'</p></div>\n'
        f'</div>\n</body>\n</html>\n'
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="人物对比页面生成")
    parser.add_argument("name1", help="第一位人物名")
    parser.add_argument("name2", help="第二位人物名")
    parser.add_argument("--output", type=Path, help="输出HTML路径")
    args = parser.parse_args()

    data1 = load_person(args.name1)
    data2 = load_person(args.name2)

    if not data1:
        print(f"错误: {args.name1} 不在数据库中", file=sys.stderr)
        return 1
    if not data2:
        print(f"错误: {args.name2} 不在数据库中", file=sys.stderr)
        return 1

    html_output = render_comparison(args.name1, data1, args.name2, data2)
    output = args.output or Path(f"/tmp/{args.name1}-vs-{args.name2}.html")
    output.write_text(html_output, encoding="utf-8")
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
