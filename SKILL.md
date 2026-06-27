---
name: person-timeline-web
description: Given only a person name, generate a sourced Chinese timeline webpage. Default: fast lightweight page. Use --profile deep for full deep-profile. Use when user asks for "人物时间线", "大事记", "biography timeline", etc. Optimized: pre-filled DB for known figures, parallel research, fast path.
version: 3.1.0
updated: 2026-06-26
---

# Person Timeline Web（v3.0.0 — 全功能升级版）

## ⚠️ 核心原则

1. **禁止编造** — 所有数据必须来自真实网络来源或预置数据库
2. **预置优先** — 数据库中的人物跳过网络搜索，直接生成
3. **并行研究** — 每次搜索尽量并行，不串行
4. **直接生成** — JSON模板内嵌，模型照填不白填 token
5. **头像优先百度百科** — `portrait_url` 优先从百度百科提取，其次维基百科，最后CSS首字母兜底
6. **生成即部署** — 任何人物时间线渲染成功后，**默认立即部署到 `example.com`**，不需要用户额外提示。详见下方「⚙️ 部署策略」一节。

---

## 提速流程（三档）

### 档位A：已知人物（毫秒级，直接用预置数据）

**适用**：毛泽东、邓小平、周恩来、朱德、刘少奇、任正非、钱学森、马云、杨振宁（已入库9人）。

**流程**：
```
1. 确认人物在 person_db.py 中 → 直接取出预置JSON
2. 生成HTML：python render_timeline.py <name>-timeline.json --allow-incomplete
3. 部署 → 完成
```

**预计耗时**：3-8秒（纯生成+部署），节省约 90% 时间。

### 档位B：未知人物 — WebFetch 快速路径（推荐，10-15秒）

**适用**：数据库中没有的人物。

> ⚠️ 2026-06-26 重大修复：opencli/web_search 工具失效，改用 WebFetch 直接抓取维基百科页面，比 browser 工具快3-5倍。

**流程（2步并行）**：

```
第1步（并行 WebFetch，最快路径）：
  WebFetch https://en.wikipedia.org/wiki/<Name>     → 英文维基（信息最全）
  WebFetch https://zh.wikipedia.org/wiki/<人名>      → 中文维基（补充中文表述）
  → 从返回的 markdown 中提取：生平、事件日期、头像图片URL

第2步（构建JSON + 渲染 + 部署）：
  构建 <name>-timeline.json（照填模板，含 portrait_url）
  python render_timeline.py <name>-timeline.json --output <name>-timeline.html --allow-incomplete
  npx wrangler pages deploy → 完成
```

**预计耗时**：10-15秒。

**头像获取方法**：
从英文维基返回内容中找到 `upload.wikimedia.org/wikipedia/commons/` 开头的图片 URL，填入 `portrait_url`。
若维基无图片，留空但 `portrait_url` 字段必须存在（值为空字符串）。

### 档位C：未知人物 — browser 兜底路径（20-40秒）

**适用**：WebFetch 超时或被限流时使用。

**流程**：
```
browser open https://baike.baidu.com/item/<人名>
browser open https://en.wikipedia.org/wiki/<Name>
browser snapshot compact=true
→ 提取信息后构建JSON → 渲染 → 部署
```

---

## 快速生成模式（直接照填）

对于已知人物，用以下 **JSON模板直接生成**，不需要白填 token 推理格式：

```json
{
  "generated_at": "2026-06-26",
  "subject": { /* 直接从 person_db 取出 */ },
  "summary": [ /* 直接填 */ ],
  "scope_note": "本页依据维基百科、百度百科等公开资料编制。",
  "uncertainty_notes": [],
  "events": [ /* 直接从预置取出 */ ],
  "sources": [ /* 固定2-4个 */ ],
  "life_stages": [ /* 直接从预置取出 */ ],
  "turning_points": [ /* 直接从预置取出 */ ],
  "timeline_sidebar": { /* 直接从预置取出 */ },
  "achievement_controversy_brief": { /* 直接从预置取出 */ },
  "relationship_network": { /* 直接从预置取出 */ },
  "era_map": [],
  "influence_legacy": { /* 直接从预置取出 */ },
  "growth_curves": [ /* 直接从预置取出 */ ],
  "source_notes": [ /* 固定 */ ]
}
```

---

## JSON 字段完整对照（Deep Profile 必须字段）

### 必须字段（缺失则渲染警告）

| 字段 | 类型 | 说明 |
|------|------|------|
| `generated_at` | string | ISO日期，如 "2026-06-26" |
| `summary` | array | 1-2句话定位 |
| `scope_note` | string | 编制说明 |
| `uncertainty_notes` | array | 不确定事项 |
| `source_notes` | array | 方法论说明 |
| `life_stages` | array | 人生阶段 |
| `turning_points` | array | 命运转折点 |
| `timeline_sidebar` | object | 关键线索 |
| `achievement_controversy_brief` | object | 成就与争议 |
| `relationship_network` | object | 人物关系 |
| `era_map` | array | 时代坐标 |
| `influence_legacy` | object | 影响力评价 |
| `growth_curves` | array | 曲线 |

### subject 字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `name` | string | 中文名 |
| `native_name` | string | 英文名/外文名 |
| `identifiers` | array | 身份标签 |
| `fields` | array | 领域 |
| `date_range` | string | 如 "1893-1976" 或 "1931-" |
| `birth_date` | string | ISO日期 |
| `birth_display` | string | 中文显示 |
| `current_age` | string | 如"享年82岁"或"94岁" |
| `portrait_url` | string | **必须填写**，维基百科图片URL |

### 空值 Fallback 规范

```python
epitaph:          "资料不足，未见可靠公开墓志铭或盖棺定论"
summary:          ["资料不足，暂无可靠公开概述"]
uncertainty_notes: ["未见可靠公开资料"]
life_stages:      []
turning_points:    []
timeline_sidebar:  {"items": []}
achievement_controversy_brief: {"items": []}
relationship_network: {"center": "人名", "nodes": [], "note": "未见可靠公开资料"}
era_map:          []
influence_legacy: {"items": []}
growth_curves:    []
```

---

---

## ⚙️ 部署策略（默认行为）

> 🚨 **2026-06-26 强制规则**：**任何人物时间线页面生成完成后，必须自动部署到 `example.com`**，无需用户额外提示。
>
> 无论是档位 A（数据库人物）、档位 B（WebFetch 新人物）还是档位 C（browser 兜底），**渲染成功 → 立即部署 → 验证可访问 → 返回正式 URL 给用户**。
>
> 例外条件（仅以下情况可跳过部署，但必须显式告知用户原因）：
> - `wrangler` 部署连续失败 2 次（Token 失效 / 网络异常）
> - 用户明确说"先不部署"、"只生成本地预览"
> - 渲染出的 HTML 校验失败（如存在未替换的 `{{PLACEHOLDER}}`）

**部署后必做**：
1. `curl` 验证目标 URL 返回 HTTP 200
2. 在最终回复中给出可点击的正式链接：`https://example.com/<人名>-timeline`

---

## 渲染命令

```bash
python3 skills/person-timeline-web/scripts/render_timeline.py \
  <name>-timeline.json \
  --output <name>-timeline.html \
  --allow-incomplete
```

**注意**：已知人物和生成质量正常的页面一律加 `--allow-incomplete`，避免因少数可选字段缺失而报错卡住。

---

## 部署（默认必做）

### 标准部署流程（每次生成后执行）

```bash
# 1. 准备部署目录（务必聚合所有要保留的HTML，避免原子快照覆盖旧页面）
mkdir -p /tmp/deploy-renwujianxian
cp *-timeline.html /tmp/deploy-renwujianxian/   # 复制全部时间线HTML，不能只复制最新一个

# 2. 部署到 Cloudflare Pages
cd /tmp/deploy-renwujianxian && \
CLOUDFLARE_API_TOKEN="<CLOUDFLARE_API_TOKEN>" \
npx wrangler pages deploy . --project-name openclaw-renwushijianxian --branch main 2>&1

# 3. 验证（无 .html 后缀）
curl -s -o /dev/null -w "HTTP: %{http_code}\n" \
  "https://example.com/<人名>-timeline"
```

### 项目信息

- **Cloudflare Pages project**: `openclaw-renwushijianxian`
- **正式域名**: `https://example.com/<人名>-timeline`（注意：无 .html 后缀）
- **备用域名**: `https://preview.example.dev/<人名>-timeline`
- **URL naming**: `<人名>-timeline`（对应实际URL，无扩展名）
- **本地HTML**: `<人名>-timeline.html`（生成后的文件名）

> ⚠️ 2026-06-26 验证更新：`example.com` 已恢复正常（HTTP 200），`example.com/renwujianxian/` 路径已废弃（返回404），请使用 `example.com` 根路径。

### 常见错误

| 错误 | 原因 | 修复 |
|------|------|------|
| 所有页面变成同一人 | 原子快照只含最新文件 | 部署前复制全部HTML到部署目录 |
| `Invalid access token` | Token失效 | 重新验证 Token |
| `Project not found` | 项目名错误 | `wrangler pages project list` 查正确名 |
| 头像不显示 | portrait_url 为空 | 从维基百科 infobox 提取图片URL |
| 页面404 | URL带.html后缀 | 去掉.html，用 `<人名>-timeline` |

---

## 网络研究方案

### 首选：WebFetch（最快）

```
WebFetch https://en.wikipedia.org/wiki/<Name>
WebFetch https://zh.wikipedia.org/wiki/<人名>
```

从返回的 markdown 中提取：
- 生平概述（首段）
- infobox 中的图片 URL（`upload.wikimedia.org` 开头）
- 关键事件日期和标题
- 人物关系

### 备用：browser 工具（WebFetch 失败时）

```
browser open url=https://baike.baidu.com/item/<人名>
browser open url=https://en.wikipedia.org/wiki/<Name>
browser snapshot compact=true
```

### 页面快照技巧（browser snapshot）
```
browser snapshot compact=true  # 快速文本模式，不含CSS
browser snapshot refs=aria     # 结构化引用，方便定位
```

---

## 飞书推送格式

发送时间线链接时，人名必须为可点击超链接：

```
📅 今日名人：[毛泽东](https://example.com/毛泽东-timeline)
```

---

## 速度优化清单

| 优化项 | 节省时间 | 说明 |
|--------|----------|------|
| 预置数据库（档位A） | 30-40秒 | 5位已知人物跳过网络研究 |
| WebFetch 替代 browser | 15-25秒 | WebFetch 比 browser 快3-5倍 |
| 并行 WebFetch | 5-10秒 | 中英文维基同时抓取 |
| `--allow-incomplete` | 5秒 | 避免因可选字段缺失卡住 |
| 跳过不必要来源验证 | 5-10秒 | 档位B只需2个来源即可 |

---

## v3.0.0 新增功能

### 1. 百度百科头像优先 (`fetch_portrait.py`)

```bash
python3 scripts/fetch_portrait.py <人名>              # 自动优先百度百科
python3 scripts/fetch_portrait.py <人名> --source baidu  # 仅百度百科
python3 scripts/fetch_portrait.py <人名> --source wiki   # 仅维基百科
```

优先级：百度百科 infobox → 维基百科 infobox → CSS首字母头像兜底。

### 2. 批量生成 (`batch_generate.py`)

```bash
python3 scripts/batch_generate.py 毛泽东 邓小平 周恩来    # 指定人物
python3 scripts/batch_generate.py --all                   # 全部9人
python3 scripts/batch_generate.py --all --deploy         # 生成并部署
```

### 3. 人物对比 (`compare_persons.py`)

```bash
python3 scripts/compare_persons.py 毛泽东 邓小平
python3 scripts/compare_persons.py 任正非 马云 --output /tmp/compare.html
```

生成双栏对比页面，展示头像、统计、关键事件、命运转折。

### 4. 数据库统计仪表盘 (`stats_dashboard.py`)

```bash
python3 scripts/stats_dashboard.py --output /tmp/stats.html
python3 scripts/stats_dashboard.py --deploy
```

可视化展示数据库覆盖率、领域分布、时代分布、人物明细。

### 5. 页面增强功能（自动嵌入）

| 功能 | 说明 |
|------|------|
| SEO + 社交分享 | JSON-LD 结构化数据、Open Graph、Twitter Card |
| 视觉时间线条 | 页面顶部横向时间线，关键事件标注 |
| 深色模式 | 🌙/☀️ 一键切换 + localStorage 持久化 |
| 键盘快捷键 | j/k 导航事件、/ 搜索、Esc 关闭 |
| 打印优化 | @media print 规则，干净 PDF 导出 |
| 阅读进度条 | 顶部进度条显示阅读位置 |
| 浮动返回顶部 | 滚动超过400px显示，点击平滑回顶 |
| 快捷导航胶囊 | Hero 底部锚点快速跳转（定位/关键线索/时间轴/复盘/来源） |
| 事件筛选条 | 顶部按类别筛选事件（动态生成 chips） |

---

## v3.1.0 前端模板重做（2026-06-26）

**档案编辑风（Editorial Archive）** 整体重做，关键变化：

1. **字体**：显示标题用 Noto Serif SC（衬线），正文用 Noto Sans SC（无衬线）。Google Fonts CDN 直引。
2. **配色**：深湖青（`#0f6e66`）+ 暖琥珀（`#b45309`）双色，浅米白背景 `#f6f4ef`，告别 Bootstrap 默认观感。
3. **去 Bootstrap 依赖**：内置轻量 grid（`.row` / `.col-lg-8` / `.col-lg-4` / `.g-4`），不再加载 bootstrap.min.css，渲染更快、视觉更统一。
4. **Hero 区**：圆形头像 + 渐变描边 + 双柱式布局（左：人物主体，右：关键事实卡）+ 顶部彩色装饰条 + `Biographical Timeline Archive` 英文 kicker。
5. **Epitaph 卡片**：深湖青径向渐变背景 + 衬线大字，凸显历史定位的视觉重量。
6. **事件卡**：左侧年龄色块（普通=青、重大=金）+ 详情折叠箭头按钮，hover 微上浮 + 描边柔化。
7. **重大事件**：左侧 4px 金色立柱 + `event-major` 浅金渐变背景，一眼区分。
8. **关系网络**：中心圆形大徽章 + 外围带左侧色条的小卡（家人=绿、机构=蓝、对手=玫红）。
9. **视觉时间线**：青→金渐变主轴，hover 圆点放大 + 双气泡（上日期、下事件名）。
10. **深色模式**：完整覆盖所有组件，深湖青切至薄荷绿 `#2dd4bf`，背景 `#131316`，全部对比度 ≥ 7:1。
11. **打印优化**：移除装饰元素，事件避免跨页截断。
12. **快捷导航 + 事件筛选条**：Hero 底部胶囊式锚点跳转；时间轴上方按事件标签筛选。

**模板路径**：`assets/archive-template.html`（render_timeline.py 默认引用，无需改命令）。

**回归验证**：王兴、黄峥 已重渲染通过，17/15 个事件全部正常出现，所有功能脚本（深色切换、进度条、键盘导航、返回顶部、筛选条）均保留可用。

---

## 禁止事项

- ❌ 直接从AI训练数据生成人物信息
- ❌ 捏造日期、数字、事件
- ❌ 字符串中混用 ASCII `"` 双引号（用「」代替）
- ❌ 生成后不验证 JSON 格式就渲染
- ❌ portrait_url 留空（优先用 `fetch_portrait.py` 从百度百科提取）
- ❌ 生成后不部署（必须上传到 Cloudflare Pages 并验证）
- ❌ 一句话定位(epitaph)使用鸡汤语录（必须是历史定位，非励志金句）
