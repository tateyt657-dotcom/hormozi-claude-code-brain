# Lead Scraper (Google Maps)

Type a search like `roofers in Dallas TX`. You get a CSV with each business's:

- name and category
- phone number
- website
- email(s), found on the business's website
- address
- Google rating and review count
- Google Maps link

## Why Google Maps and not Google search pages

Maps shows phone, website, rating, and reviews on every listing. Google search
pages don't, and Google shows a CAPTCHA (a "prove you're human" check) after a
few pages. Maps gives up to about 120 businesses per search. To get more, use
`--cities` to run the same search in many cities.

## Setup (one time)

You need Python 3.9 or newer.

```bash
cd tools/lead-scraper
```

```bash
pip install -r requirements.txt
```

```bash
python -m playwright install chromium
```

## Run it

One search:

```bash
python lead_scraper.py "roofers in Dallas TX"
```

Same search across many cities (one city per line in the file):

```bash
python lead_scraper.py "med spa" --cities cities.example.txt --max 60
```

Many different searches (one per line in the file):

```bash
python lead_scraper.py --queries my_searches.txt --out leads.csv
```

## Options

| Option | What it does |
|---|---|
| `--max 50` | Stop at 50 businesses per search. Default is 120. |
| `--out file.csv` | Save to a different file. Default is `leads.csv`. |
| `--cities file.txt` | Runs your search as "search in city" for each city. |
| `--queries file.txt` | Runs every search in the file. |
| `--no-emails` | Skips website visits. Much faster, but no emails. |
| `--headful` | Opens a visible browser so you can watch it work. |

## Good to know

- **It resumes.** Re-run the same command with the same `--out` file and it
  skips businesses it already saved. Press Ctrl+C anytime. Saved rows stay.
- **Emails won't be 100%.** Many local businesses only use a contact form or
  Facebook. Expect emails for roughly 30 to 60% of businesses with a website.
- **Speed.** Plan on about 2 to 4 seconds per business, plus email lookup.
  120 leads takes around 5 to 10 minutes.
- **Go slow.** Running thousands of searches back to back can get your IP
  rate-limited by Google for a while. Spread big jobs out.
- **If it breaks,** Google probably changed their page layout. The page
  selectors sit at the top of `scrape_place()` in `lead_scraper.py`.
- **Rules.** Scraping Google Maps is against Google's terms of service. If you
  email or text these leads, follow CAN-SPAM and TCPA rules. Don't text cell
  numbers without consent.
