#!/usr/bin/env python3
"""飞书推送 — 部署成功后发送人物卡片到飞书群。
用法:
    python notify_feishu.py <人名> <页面URL> [--webhook URL] [--portrait URL]

环境变量:
    FEISHU_WEBHOOK_URL — 飞书机器人 Webhook URL
"""
import argparse
import json
import os
import sys
import urllib.request
import urllib.error

def send_feishu_card(name: str, page_url: str, portrait_url: str = "", summary: str = "", webhook_url: str = "") -> bool:
    """发送飞书互动卡片"""
    webhook_url = webhook_url or os.environ.get("FEISHU_WEBHOOK_URL", "")
    if not webhook_url:
        print("Warning: FEISHU_WEBHOOK_URL not set, skipping notification", file=sys.stderr)
        return False

    # 构建飞书卡片消息
    header_title = f"📅 今日人物：{name}"
    
    elements = []
    
    # 头像图片（如果有）
    if portrait_url:
        elements.append({
            "tag": "img",
            "img_key": "",
            "alt": {"tag": "plain_text", "content": name},
            "mode": "crop_center",
        })
    
    # 摘要
    if summary:
        elements.append({
            "tag": "div",
            "text": {"tag": "lark_md", "content": summary},
        })
    
    # 链接按钮
    elements.append({
        "tag": "action",
        "actions": [{
            "tag": "button",
            "text": {"tag": "plain_text", "content": "📋 查看完整时间线"},
            "url": page_url,
            "type": "primary",
        }],
    })
    
    # 分割线
    elements.append({"tag": "hr"})
    
    # 底部信息
    elements.append({
        "tag": "note",
        "elements": [{
            "tag": "plain_text",
            "content": "由 person-timeline-web 技能自动生成",
        }],
    })
    
    payload = {
        "msg_type": "interactive",
        "card": {
            "header": {
                "title": {"tag": "plain_text", "content": header_title},
                "template": "red",
            },
            "elements": elements,
        },
    }
    
    try:
        req = urllib.request.Request(
            webhook_url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("code") == 0 or result.get("StatusCode") == 0:
                print(f"Feishu notification sent for: {name}")
                return True
            else:
                print(f"Feishu API error: {result}", file=sys.stderr)
                return False
    except urllib.error.URLError as e:
        print(f"Feishu notification failed: {e}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Feishu notification error: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description="Send Feishu notification for a new person timeline")
    parser.add_argument("name", help="Person name")
    parser.add_argument("page_url", help="Timeline page URL")
    parser.add_argument("--webhook", default="", help="Feishu webhook URL (overrides env var)")
    parser.add_argument("--portrait", default="", help="Portrait image URL")
    parser.add_argument("--summary", default="", help="Person summary text")
    args = parser.parse_args()

    success = send_feishu_card(
        name=args.name,
        page_url=args.page_url,
        portrait_url=args.portrait,
        summary=args.summary,
        webhook_url=args.webhook,
    )
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
