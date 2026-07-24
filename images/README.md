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
- `etl-hero.jpg`, `nifi-pipeline.jpg`, `weather-dashboard.jpg` — used on the ETL case study page (`ETL_Project_1.html`)

## CAD renders (`images/cad_images/`)
Click-to-enlarge gallery in the Personal Projects → CAD Work block on `index.html`.
To add a new render or GIF: drop the file here, then copy one of the `<a>` blocks
in the `.thumb-gallery` markup and update its `href`/`src`/`alt`/caption.

## Hobby photos (`images/hobby_pics/`)
Used on `hobbies.html` (cars, photography). Same pattern — drop a file in this
folder, copy an existing `.thumb-gallery` `<a>` block, and point it at the new file.

## How to point at a different path (e.g. still hosting on S3)
Every background image is set with an inline `style="--bg-img:url('...')"` on the
element — search `index.html` / `ETL_Project_1.html` for `--bg-img` and swap the
URL for a local path or any external link (S3, Imgur, wherever).
