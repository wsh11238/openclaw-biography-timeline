# 部署指南 / Deployment Guide

这个文档用于把仓库快速变成一个可分享的在线 Demo。建议使用新的中性项目名，避免暴露任何个人域名、历史域名或内部部署信息。

## 本地预览

```bash
# 静态项目
python -m http.server 8788

# Vite 项目
npm install
npm run dev
```

## Cloudflare Pages

本项目是静态站点，直接部署仓库根目录即可。

推荐设置：

- Project name：使用中性名称，例如 `openclaw-biography-timeline-demo`
- Production branch：`main`
- 构建命令：留空；输出目录：`/`。
- Environment variables：不要填写真实密钥；公开 Demo 应只使用公开示例数据

部署完成后，把 Demo 链接加到 README 顶部：

```md
在线演示 Demo: https://your-neutral-demo.pages.dev
```

## GitHub Pages

如果你不想使用 Cloudflare Pages，可以使用 GitHub Pages 或任意静态托管服务。静态项目可直接发布根目录；Vite 项目需要先构建再发布输出目录。

## 发布前安全检查

- 不提交 `.env`、`.dev.vars`、`.wrangler`、`node_modules`
- 不提交 Cloudflare、GitHub、OpenAI、Google、Stripe 等 token/key
- 不在 README 中写真实私有域名
- 只保留公开示例数据和真实渲染截图
