# Lead Scraper (Google Maps)

Type a search like `roofers in Dallas TX`. You get a CSV with each business's:

- name and category
- phone number
- website
- website status: `none`, `facebook_only`, `social_or_directory_only`, or `has_site`
- Facebook and Instagram links (from Maps, or found on their website)
- email(s), found on the business's website
- address
- Google rating and review count
- Google Maps link

## Why Google Maps and not Google search pages

Maps shows phone, website, rating, and reviews on every listing. Google search
pages don't, and Google shows a CAPTCHA (a "prove you're human" check) after a
few pages. Maps gives up to about 120 businesses per search. To get more, run the same
search across many cities or ZIP codes. ZIP codes in big cities find the most.

## Easiest way: the app

You need Python 3.9 or newer. On Windows, tick "Add Python to PATH" when you install it.

1. Open the `tools/lead-scraper` folder.
2. Double-click **`start.bat`** (Windows) or **`start.command`** (Mac).
   The first time, it installs what it needs. That takes a minute or two.
3. A window opens. Type your business types, one per line (like `roofers`).
4. Paste your locations, one per line. Cities (`Dallas TX`) or ZIP codes
   (`75201`) both work. Or click **Load file...** to load a list.
5. Click **Start**. Watch progress in the box at the bottom.
6. Click **Open CSV** when it's done.

Every business type runs in every location. So 3 business types and 50 ZIP
codes is 150 searches.

On Mac, if it says the file can't be opened, right-click `start.command` and
choose Open. If that fails, run `chmod +x start.command` in Terminal first.

## Command line (optional)

Setup, once:

```bash
pip install -r requirements.txt
```

```bash
python -m playwright install chromium
```

One search:

```bash
python lead_scraper.py "roofers in Dallas TX"
```

Bulk: several business types across a file of locations:

```bash
python lead_scraper.py "roofers, plumbers" --locations locations.example.txt
```

Locations can also go inline, but don't put commas inside a location:

```bash
python lead_scraper.py "med spa" --locations "Austin TX, Houston TX, 78701"
```

Only businesses with no real website (best for a web design offer):

```bash
python lead_scraper.py "roofers" --locations locations.example.txt --no-website-only --out no_site_leads.csv
```

| Option | What it does |
|---|---|
| `--locations file.txt` | Cities or ZIP codes, one per line (or a comma list). Runs every search in every location. |
| `--max 50` | Stop at 50 businesses per search. Default is 120. |
| `--out file.csv` | Save to a different file. Default is `leads.csv`. |
| `--delay 5` | Seconds to wait between searches. Default 3. Raise it for big runs. |
| `--restart` | Redo searches that already finished in an earlier run. |
| `--no-emails` | Skips email lookup. Faster. Still finds Facebook links. |
| `--no-website-only` | Saves only businesses with no website, or only Facebook/Instagram/Yelp. |
| `--headful` | Opens a visible browser so you can watch it work. |

## Good to know

- **Big runs resume.** Each finished search is listed in a file next to your
  CSV (`leads.done.txt`). Stop anytime, then start again with the same CSV.
  It skips finished searches and businesses it already saved. Failed searches
  get retried.
- **No duplicates.** Nearby cities and ZIP codes return many of the same
  businesses. The tool skips repeats before opening them, so they cost almost
  no time.
- **Emails won't be 100%.** Many local businesses only use a contact form or
  Facebook. Expect emails for roughly 30 to 60% of businesses with a website.
- **No emails for Facebook-only businesses.** Facebook needs a login to read
  pages, so the tool saves the Facebook link and phone but can't pull an email.
  Call them, or message them on Facebook.
- **Speed.** Plan on about 2 to 4 seconds per business, plus email lookup.
  120 leads takes around 5 to 10 minutes.
- **Go slow.** Running thousands of searches back to back can get your IP
  rate-limited by Google for a while. Spread big jobs out.
- **If it breaks,** Google probably changed their page layout. The page
  selectors sit at the top of `scrape_place()` in `lead_scraper.py`.
- **Rules.** Scraping Google Maps is against Google's terms of service. If you
  email or text these leads, follow CAN-SPAM and TCPA rules. Don't text cell
  numbers without consent.
