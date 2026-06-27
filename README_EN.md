# OpenClaw Biography Timeline Generator

A toolkit for transforming public biographical research into structured timelines, source notes, and archival HTML pages.

**中文介绍:** [README.md](README.md)

![Project preview](docs/screenshot.png)

## Screenshots

Both screenshots are captured from real rendered pages in this repository. The first one shows the opening screen, and the second one shows the scrolled product experience.

| Opening Screen | Scrolled Screen |
|---|---|
| ![Opening screen](docs/screenshot-2.png) | ![Scrolled screen](docs/screenshot-3.png) |

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
