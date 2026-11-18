@echo off
cd /d "%~dp0"
python -c "import playwright, requests, bs4" 2>nul || (
  echo First run: installing what the scraper needs. This takes a minute...
  python -m pip install -r requirements.txt
  python -m playwright install chromium
)
start "" pythonw lead_scraper_app.py
