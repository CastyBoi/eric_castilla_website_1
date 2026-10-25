#!/usr/bin/env bash
# Re-renders every project card image into images/projects/.
# Usage (from repo root):  bash mockups/render.sh
# Needs: python3, Google Chrome (macOS path below), sips (built into macOS).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT="$ROOT/images/projects"
TMP="$(mktemp -d)"
mkdir -p "$OUT"

shot() { # shot <generated-html-basename> <final-jpg-name>
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --window-size=1600,740 \
    --screenshot="$TMP/$1.png" "file://$TMP/$1.html" >/dev/null 2>&1
  sips -s format jpeg -s formatOptions 85 "$TMP/$1.png" --out "$OUT/$2.jpg" >/dev/null
  echo "  $2.jpg"
}

cd "$TMP"
python3 "$ROOT/mockups/projects_gen.py"
python3 "$ROOT/mockups/tools_gen.py"

# projects_gen.py -> same name on the site
for n in rental-utilization exec-dashboard multisite-monitoring cs-doc-automation \
         ai-image-parsing line-layout-redesign equipment-chatbot; do shot "$n" "$n"; done

# tools_gen.py -> generator name  ->  site filename
shot 01_sales_projection_hub    sales-forecasting          # "Market Data" Process Overhaul card
shot 04_forecast_file_upload    equipment-forecasting      # "Forecasting" Automation card
shot 02_etl_hub                 etl-automation-hub         # ETL Automation Hub card
shot 06_productivity_monitor    plant-productivity-review  # Plant Productivity card
shot 03_delivery_report_upload  delivery-report-upload     # spare, not on a card yet
shot 05_etl_pipeline_logs       etl-pipeline-logs          # spare, not on a card yet

cd "$ROOT" && rm -rf "$TMP"
echo "Done -> $OUT"
