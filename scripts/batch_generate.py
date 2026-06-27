#!/usr/bin/env python3
"""批量生成人物时间线 — 从名单批量生成HTML并更新索引。

用法：
  python3 batch_generate.py 毛泽东 邓小平 周恩来
  python3 batch_generate.py --all          # 生成数据库中所有人物
  python3 batch_generate.py --all --deploy  # 生成并部署到 Cloudflare Pages
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
DEPLOY_DIR = Path("/tmp/deploy-renwujianxian")


def get_all_persons() -> list[str]:
    """获取数据库中所有人物名。"""
    try:
        sys.path.insert(0, str(SCRIPT_DIR))
        from person_db import PERSON_DB
        return list(PERSON_DB.keys())
    except Exception:
        return []


def render_person(name: str, deploy: bool = False) -> bool:
    """渲染单个人物时间线。"""
    try:
        sys.path.insert(0, str(SCRIPT_DIR))
        from person_db import PERSON_DB
        if name not in PERSON_DB:
            print(f"  ✗ {name} 不在数据库中，跳过", file=sys.stderr)
            return False
        data = PERSON_DB[name]
    except Exception as e:
        print(f"  ✗ {name} 数据库读取失败: {e}", file=sys.stderr)
        return False

    json_file = DEPLOY_DIR / f"{name}-timeline.json"
    html_file = DEPLOY_DIR / f"{name}-timeline.html"
    json_file.parent.mkdir(parents=True, exist_ok=True)

    json_file.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    cmd = [
        sys.executable, str(SCRIPT_DIR / "render_timeline.py"),
        str(json_file),
        "--output", str(html_file),
        "--allow-incomplete",
        "--update-index", str(DEPLOY_DIR),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ✗ {name} 渲染失败: {result.stderr[:200]}", file=sys.stderr)
        return False

    print(f"  ✓ {name} 渲染成功")
    return True


def deploy_to_cloudflare() -> bool:
    """部署到 Cloudflare Pages。"""
    cmd = [
        "npx", "wrangler", "pages", "deploy", ".",
        "--project-name", "openclaw-renwushijianxian",
        "--branch", "main",
    ]
    env = {
        "CLOUDFLARE_API_TOKEN": "<CLOUDFLARE_API_TOKEN>",
        "PATH": "/usr/local/bin:/usr/bin:/bin:/opt/homebrew/bin",
    }
    import os
    env["HOME"] = os.path.expanduser("~")
    result = subprocess.run(cmd, cwd=str(DEPLOY_DIR), capture_output=True, text=True, env=env)
    if result.returncode != 0:
        print(f"  ✗ 部署失败: {result.stderr[:200]}", file=sys.stderr)
        return False
    print(f"  ✓ 部署成功")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="批量生成人物时间线")
    parser.add_argument("names", nargs="*", help="人物名列表")
    parser.add_argument("--all", action="store_true", help="生成数据库中所有人物")
    parser.add_argument("--deploy", action="store_true", help="生成后部署到 Cloudflare Pages")
    args = parser.parse_args()

    if args.all:
        names = get_all_persons()
        if not names:
            print("数据库为空或无法读取", file=sys.stderr)
            return 1
    elif args.names:
        names = args.names
    else:
        parser.print_help()
        return 1

    print(f"════════════════════════════════════════")
    print(f"  批量生成 {len(names)} 位人物时间线")
    print(f"════════════════════════════════════════")

    success = 0
    failed = 0
    for name in names:
        if render_person(name):
            success += 1
        else:
            failed += 1

    print(f"\n════════════════════════════════════════")
    print(f"  完成: {success} 成功, {failed} 失败")

    if args.deploy and success > 0:
        print("\n▶ 部署到 Cloudflare Pages...")
        deploy_to_cloudflare()

    print(f"  索引页: {DEPLOY_DIR}/index.html")
    print(f"════════════════════════════════════════")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
