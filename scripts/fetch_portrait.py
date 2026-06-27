#!/usr/bin/env python3
"""头像抓取工具 — 优先从百度百科获取人物头像。

优先级顺序：
1. 百度百科 infobox 图片（bkimg.cdn.bcebos.com）
2. 维基百科 infobox 图片（upload.wikimedia.org）
3. 返回空字符串（触发CSS首字母头像兜底）

用法：
  python3 fetch_portrait.py <人名>
  python3 fetch_portrait.py <人名> --source baidu
  python3 fetch_portrait.py <人名> --source wiki

输出：头像URL（打印到stdout），或空字符串
"""

import argparse
import re
import sys
import urllib.parse
import urllib.request


def fetch_baidu_portrait(name: str) -> str:
    """从百度百科页面提取头像URL。"""
    url = f"https://baike.baidu.com/item/{urllib.parse.quote(name)}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "zh-CN,zh;q=0.9",
    })
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="replace")
    except Exception:
        return ""

    # Pattern 1: bkimg.cdn.bcebos.com images
    patterns = [
        r'(https?://bkimg\.cdn\.bcebos\.com/pic/[^"\'\s<>]+)',
        r'(https?://imgsrc\.baidu\.com/baike/pic/[^"\'\s<>]+)',
        r'data-src="(https?://[^"]*bcebos[^"]*)"',
        r'src="(https?://bkimg\.cdn\.bcebos\.com/[^"]+)"',
    ]
    for pattern in patterns:
        match = re.search(pattern, html)
        if match:
            img_url = match.group(1)
            # Clean URL - remove query params that might break image
            img_url = img_url.split("?")[0] if "?" in img_url else img_url
            # Verify it looks like a person photo (not a logo)
            if "item" not in img_url and "logo" not in img_url.lower():
                return img_url

    return ""


def fetch_wiki_portrait(name: str) -> str:
    """从维基百科提取头像URL。"""
    # Try English Wikipedia first
    for wiki_url in [
        f"https://en.wikipedia.org/wiki/{urllib.parse.quote(name)}",
        f"https://zh.wikipedia.org/wiki/{urllib.parse.quote(name)}",
    ]:
        req = urllib.request.Request(wiki_url, headers={
            "User-Agent": "PersonTimelineBot/1.0 (research tool)",
            "Accept": "text/html",
        })
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                html = resp.read().decode("utf-8", errors="replace")
        except Exception:
            continue

        patterns = [
            r'(https?://upload\.wikimedia\.org/wikipedia/commons/[^"\'\s<>]+\.(?:jpg|jpeg|png|JPG|JPEG|PNG))',
            r'(https?://upload\.wikimedia\.org/wikipedia/en/[^"\'\s<>]+\.(?:jpg|jpeg|png|JPG|JPEG|PNG))',
        ]
        for pattern in patterns:
            match = re.search(pattern, html)
            if match:
                return match.group(1)

    return ""


def fetch_portrait(name: str, source: str = "auto") -> str:
    """获取人物头像URL。

    Args:
        name: 人物名（中文）
        source: "auto"（默认，百度优先）、"baidu"、"wiki"

    Returns:
        头像URL字符串，找不到则返回空字符串
    """
    if source == "baidu":
        return fetch_baidu_portrait(name)
    elif source == "wiki":
        return fetch_wiki_portrait(name)
    else:  # auto
        # 百度百科优先
        url = fetch_baidu_portrait(name)
        if url:
            print(f"[baidu] Found portrait: {url[:60]}...", file=sys.stderr)
            return url
        print("[baidu] No portrait found, trying Wikipedia...", file=sys.stderr)
        url = fetch_wiki_portrait(name)
        if url:
            print(f"[wiki] Found portrait: {url[:60]}...", file=sys.stderr)
            return url
        print("[portrait] No portrait found from any source", file=sys.stderr)
        return ""


def main() -> int:
    parser = argparse.ArgumentParser(description="获取人物头像URL（百度百科优先）")
    parser.add_argument("name", help="人物名（中文）")
    parser.add_argument("--source", choices=["auto", "baidu", "wiki"], default="auto",
                        help="头像来源：auto（默认，百度优先）、baidu、wiki")
    args = parser.parse_args()

    url = fetch_portrait(args.name, args.source)
    if url:
        print(url)
        return 0
    else:
        print("", end="")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
