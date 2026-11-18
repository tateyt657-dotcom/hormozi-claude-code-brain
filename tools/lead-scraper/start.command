#!/bin/bash
cd "$(dirname "$0")"
if ! python3 -c "import playwright, requests, bs4" 2>/dev/null; then
  echo "First run: installing what the scraper needs. This takes a minute..."
  python3 -m pip install -r requirements.txt
  python3 -m playwright install chromium
fi
python3 lead_scraper_app.py
