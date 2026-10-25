# Eric Castilla — Portfolio Website

Static site (plain HTML/CSS/JS, no build step), deployed with GitHub Pages:
https://castyboi.github.io/eric_castilla_website_1/index.html

To work on it locally, run `python3 -m http.server 8000` in the repo root and open
http://localhost:8000. Opening files with `file://` can drop styling, so use the server.

## Structure

| Path | What it is |
|---|---|
| `index.html` | Main page: About, Professional Work (project cards), Side Projects, Skills, Contact |
| `hobbies.html` | Photography and cars galleries |
| `ETL_Project_1.html` | Case study linked from the Side Projects section |
| `Project_2.html`, `Programming_Projects.html`, `Two_Apps_Display.html`, `error.html` | Other pages |
| `style.css` | All styling (theme colors are variables in `:root`, accent is `--accent`) |
| `script.js` | Nav toggle, scroll reveal, project filter buttons, footer year |
| `images/` | All images and videos (see `images/README.md` for photo and thumbnail rules) |
| `images/projects/` | The mock image shown on each project card (1600x740 JPGs) |
| `images/hobby_pics/` | Photos for `hobbies.html` (full size plus `-thumb` copies) |
| `mockups/` | Python + HTML generators that produce the project card images |

## Project cards (Professional Work section)

Each card is one `<article class="card reveal" data-tags="...">` inside
`<div class="project-grid">` in `index.html`. The banner is a link, so clicking it opens
the full image in a new tab.

### Edit a card
Change the text in the `<article>`: `card-status` (small red label), `<h3>` title,
`card-summary` (always visible), the paragraph inside `<details>` (the "Read more" text),
and the `pill` spans in `card-tools`. The corner label on the image is
`<span class="card-tag">` (e.g. "Flagship Build", "In Progress"); delete it for no label.

### Add a card
1. Copy an existing `<article class="card reveal" ...>` block and paste it in the grid.
2. Set `data-tags` to one or more filter names, comma separated and no spaces:
   `ai`, `bi`, `data`, `automation`, `cad`. These match the `data-filter` values on the
   filter buttons at the top of the section. A new filter needs a new `<button class="filter-btn" data-filter="...">` too.
3. Point the banner at a new image (next section). Update both the `href` and the
   `--bg-img:url('...')` in the same `<a class="card-media">`.
4. Cards display in file order; move the block to reorder.

### Current cards and their images
| Card | Image in `images/projects/` |
|---|---|
| Equipment Utilization Tracker | `rental-utilization.jpg` |
| Executive Dashboards Suite | `exec-dashboard.jpg` |
| Multi-Site Production Monitoring | `multisite-monitoring.jpg` |
| Plant Productivity & Review Dashboard | `plant-productivity-review.jpg` |
| Document Automation | `cs-doc-automation.jpg` |
| "Forecasting" Automation | `equipment-forecasting.jpg` |
| "Market Data" Process Overhaul | `sales-forecasting.jpg` |
| ETL Automation Hub | `etl-automation-hub.jpg` |
| AI Document-Parsing GPT | `ai-image-parsing.jpg` |
| Production Line Layout Redesign | `line-layout-redesign.jpg` |
| Internal Support Chatbot | `equipment-chatbot.jpg` |

Spare images (rendered, not on a card yet): `delivery-report-upload.jpg`, `etl-pipeline-logs.jpg`.
Some file names are older than the card titles (e.g. `sales-forecasting.jpg` is the
Market Data card); keep names stable so links don't break, or rename in both places.

## Project card images (`mockups/`)

The card images are **mock screenshots built from invented data** so nothing from an
employer's real tools is published. They are not real screenshots. Each tool is drawn
as HTML, screenshotted with headless Chrome, and saved as a JPG.

- `mockups/projects_gen.py` builds 7 mocks: utilization, exec dashboard, multi-site
  monitor, doc automation, document-parsing GPT, line layout, chatbot.
- `mockups/tools_gen.py` builds 6 mocks: Projection Builder (Market Data card), ETL
  hub, delivery upload, forecast loader (Forecasting card), log viewer, productivity
  dashboard. Each is a function call `w("name", css, body)` with plain HTML in strings.
- `mockups/render.sh` runs both generators, screenshots every page at 1600x740, and
  writes the JPGs into `images/projects/`. Run it from the repo root:

```bash
bash mockups/render.sh
```

It needs python3, Google Chrome, and macOS `sips` (all standard on this Mac).

### Change an image
Edit its `w("name", css, body)` block in the matching generator, run `render.sh`,
and reload the site. Keep the page at 1600x740 (the size every card uses).

### Add an image for a new card
1. Add a new `w("my-tool", css, body)` call at the end of `tools_gen.py`.
2. Add a line in `render.sh`: `shot my-tool my-tool` (generator name, then the JPG name).
3. Run `render.sh`, then point the card at `images/projects/my-tool.jpg`.

### Rules for the mocks
- Fake data only. No real company, vendor or plant names, SAP report codes, usernames,
  file paths, or employee data. The site says tool and company names are genericized.
- Make each mock look like a *kind* of tool, not a copy of a specific internal one.
- When numbers appear in more than one place, make them sum (e.g. department hours add
  up to the KPI totals). `tools_gen.py` has `assert` checks for the productivity mock.
- Keep real screenshots out of the repo. Reference screenshots live outside it.

## Hobbies page
Add photos per `images/README.md`: drop the full-size file in `images/hobby_pics/`,
make a thumbnail with `sips -Z 900 -s formatOptions 70 in.jpg --out in-thumb.jpg`,
then copy an existing `<a>` block. Captions use
`Location - Description &middot; Camera, Lens, F#, ISO`; read EXIF with `exiftool`
(not every photo has EXIF; leave the settings off if missing rather than guessing).

## Publishing
Push to `main` and GitHub Pages redeploys. Any image a page links to must be committed,
including full-size files that thumbnails link to (a past bug: only thumbnails were
committed, so the full-size links 404'd after deploy). Check `git status` for untracked
files in `images/` before committing.
