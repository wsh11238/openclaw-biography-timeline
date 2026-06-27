#!/usr/bin/env bash
# generate.sh — 人物时间线一键生成流水线
# 用法: ./generate.sh <人名> [--deep]
# 流程: 检查数据库 → (可选网络研究) → 渲染HTML → 更新索引 → 部署 → 验证
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_DIR="$(dirname "$SCRIPT_DIR")"
PERSON_NAME="${1:?Usage: generate.sh <人名> [--deep]}"
PROFILE="fast"
[[ "${2:-}" == "--deep" ]] && PROFILE="deep"

# Cloudflare Pages 配置
CF_PROJECT="openclaw-renwushijianxian"
CF_TOKEN="<CLOUDFLARE_API_TOKEN>"
DEPLOY_DIR="/tmp/deploy-renwujianxian"
BASE_URL="https://example.com"

echo "════════════════════════════════════════"
echo "  人物时间线生成: $PERSON_NAME"
echo "  模式: $PROFILE"
echo "════════════════════════════════════════"

# Step 1: 检查数据库
echo "▶ [1/5] 检查预置数据库..."
python3 -c "
import sys; sys.path.insert(0, '$SCRIPT_DIR')
from person_db import get_person
p = get_person('$PERSON_NAME')
if p:
    print('FOUND_IN_DB')
    import json
    with open('/tmp/${PERSON_NAME}-timeline.json', 'w', encoding='utf-8') as f:
        json.dump(p, f, ensure_ascii=False, indent=2)
else:
    print('NOT_IN_DB')
" 2>/dev/null && DB_RESULT="FOUND" || DB_RESULT="NOT_FOUND"

if [[ "$DB_RESULT" == "NOT_FOUND" ]]; then
    echo "  ⚠ 不在数据库中，需要网络研究（请用 TRAE 的 WebFetch/browser 工具）"
    echo "  请先生成 JSON 文件: /tmp/${PERSON_NAME}-timeline.json"
    echo "  然后重新运行此脚本"
    exit 1
fi

JSON_FILE="/tmp/${PERSON_NAME}-timeline.json"
OUTPUT_HTML="/tmp/${PERSON_NAME}-timeline.html"

# Step 2: 渲染 HTML
echo "▶ [2/5] 渲染 HTML..."
python3 "$SCRIPT_DIR/render_timeline.py" "$JSON_FILE" \
    --output "$OUTPUT_HTML" \
    --allow-incomplete \
    --update-index "$DEPLOY_DIR" \
    2>&1

# Step 3: 准备部署
echo "▶ [3/5] 准备部署文件..."
mkdir -p "$DEPLOY_DIR"
cp "$OUTPUT_HTML" "$DEPLOY_DIR/${PERSON_NAME}-timeline.html"

# Step 4: 部署到 Cloudflare Pages
echo "▶ [4/5] 部署到 Cloudflare Pages..."
cd "$DEPLOY_DIR"
CLOUDFLARE_API_TOKEN="$CF_TOKEN" npx wrangler pages deploy . \
    --project-name "$CF_PROJECT" --branch main 2>&1

# Step 5: 验证
echo "▶ [5/5] 验证页面可访问..."
sleep 3
URL="${BASE_URL}/${PERSON_NAME}-timeline"
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$URL" 2>/dev/null || echo "000")

if [[ "$HTTP_CODE" == "200" ]]; then
    echo ""
    echo "════════════════════════════════════════"
    echo "  ✅ 生成成功！"
    echo "  📄 页面地址: $URL"
    echo "  📊 索引页: $BASE_URL/"
    echo "════════════════════════════════════════"
else
    echo ""
    echo "  ⚠ 部署可能未完成 (HTTP $HTTP_CODE)"
    echo "  预览地址: https://preview.example.dev/${PERSON_NAME}-timeline"
fi
