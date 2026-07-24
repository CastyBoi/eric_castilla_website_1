# Drop your photos here

The site is already wired up to look for these files. Nothing breaks if they're
missing — each spot falls back to a dark gradient — but it'll look a lot better
with your own shots in. Recommended: wide/landscape, 2000px+ on the long edge,
compressed to keep the site fast (JPEG, ~200–400KB each is plenty).

## Background bands (referenced in `index.html`)
- `hero-bg.jpg` — the big hero shot at the very top. Something moody/wide works
  best (road, mountains, plant floor, whatever's got that "immersive" vibe).
- `divider-1.jpg` — the quote band between About and Work.
- `personal-bg.jpg` — background behind the Personal Projects section.
- `contact-bg.jpg` — background behind the Contact section at the bottom.

## Project thumbnails (`images/projects/`)
Card thumbnails — safe to leave blank, they'll show a subtle red gradient instead.
- `rental-utilization.jpg`
- `exec-dashboard.jpg`
- `multisite-monitoring.jpg`
- `cs-doc-automation.jpg`
- `equipment-forecasting.jpg`
- `dashboard-audit.jpg`
- `sales-forecasting.jpg`
- `ai-image-parsing.jpg`
- `vr-digital-twin.jpg`
- `line-layout-redesign.jpg`
- `kpi-framework.jpg`
- `equipment-chatbot.jpg`
- `honda-engine-model.jpg` — CAD render, shown in the Personal Projects gallery
- `etl-hero.jpg`, `nifi-pipeline.jpg`, `weather-dashboard.jpg` — used on the ETL case study page (`ETL_Project_1.html`)

## How to point at a different path (e.g. still hosting on S3)
Every background image is set with an inline `style="--bg-img:url('...')"` on the
element — search `index.html` / `ETL_Project_1.html` for `--bg-img` and swap the
URL for a local path or any external link (S3, Imgur, wherever).
