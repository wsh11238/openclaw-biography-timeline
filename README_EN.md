# OpenClaw Biography Timeline Generator

A toolkit for transforming public biographical research into structured timelines, source notes, and archival HTML pages.

**中文介绍:** [README.md](README.md)

![Demo](docs/demo.gif)

## Understand It In 3 Seconds

**Turn scattered public research into timelines, relationship maps, long-form reviews, and source notes.**

Good fit for:
- founder profiles
- biography sites
- historical research
- course material
- long-form content archives

## Fork It In 30 Seconds

Fork it, add person JSON plus sources, then render your own source-aware biography page.

Main data to replace: person JSON files and source notes.

## Publish And Promote It

- Deployment guide: [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md)
- Launch copy kit: [docs/LAUNCH_KIT.md](docs/LAUNCH_KIT.md)
- Social preview image: [docs/social-preview.png](docs/social-preview.png)

> If this template saves you from rebuilding the same product skeleton later, consider starring the repo.

## Screenshots

The four screenshots below come from the actual rendered Chinese pages in this repository: the opening screen, the scrolled second screen, and two additional feature-focused views. They are real UI captures, not concept art or English placeholder mockups.

| Opening Screen | Scrolled Screen |
|---|---|
| ![Opening screen](docs/screenshot-2.png) | ![Scrolled screen](docs/screenshot-3.png) |
| ![Feature screenshot one](docs/screenshot-4.png) | ![Feature screenshot two](docs/screenshot-5.png) |

## What This System Does

This project turns scattered biographical material into a structured, readable, source-aware archive page. It is designed for biographies, founder profiles, historical research, educational material, and long-form content systems.

## Core Features

- **Profile opening screen** with identity, background, education, achievements, and concise biography.
- **Key-fact cards** for the most important signals in a person's life story.
- **Detailed chronological timeline** for education, career, founding, IPO, management, philanthropy, and major events.
- **Event filters** by category such as education, career, founding, achievement, management, and philanthropy.
- **Achievement and controversy overview** to keep the profile balanced.
- **Deep-review section** for turning points, relationship networks, era context, and decision analysis.
- **Source-note structure** for adding citations, review notes, and verification context.
- **Generation scripts** for rendering, batch generation, research caching, portrait fetching, and person comparison.
- **Template-based output** using JSON data and HTML archive templates.

## Good Fit For

- Founder biography pages
- Historical figure archives
- Course and research material
- Long-form profile production
- Personal knowledge-management systems

## Repository Structure

- `assets/archive-template.html`: editorial archive template.
- `scripts/`: generation and research helper scripts.
- `preview/`: generated timeline examples.
- `timelines/`: structured timeline JSON and source notes.

## Quick Start

```bash
python scripts/render_timeline.py
```

Open the generated HTML files in `preview/` or `scripts/`.

## Public-Safe Version

Private deployment URLs, production credentials, Cloudflare tokens, local environment files, logs, `.wrangler`, `node_modules`, and non-public material were removed before publication.

## Why Star This

Star this repository if you want a practical product pattern that can be studied, forked, customized, and turned into your own dashboard, content system, knowledge portal, or interactive tool.
