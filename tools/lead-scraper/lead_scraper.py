#!/usr/bin/env python3
"""
Google Maps lead scraper.

Pulls businesses from Google Maps for a search (e.g. "roofers in Dallas TX")
and saves a CSV with: name, category, phone, website, email(s), address,
rating, review count, and the Google Maps link.

Emails are not on Google Maps, so the tool visits each business website
(home page + common contact/about pages) and pulls emails from there.

Usage:
    python lead_scraper.py "roofers in Dallas TX"
    python lead_scraper.py "med spa" --cities cities.txt --max 60
    python lead_scraper.py --queries queries.txt --out leads.csv
    python lead_scraper.py "dentist in Miami" --headful   # watch the browser
"""

from __future__ import annotations

import argparse
import csv
import html
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import quote_plus, urljoin, urlparse, unquote

import requests
from bs4 import BeautifulSoup
from playwright.sync_api import TimeoutError as PWTimeout
from playwright.sync_api import sync_playwright

FIELDS = [
    "query", "name", "category", "phone", "website", "website_status",
    "facebook", "instagram", "emails", "address", "rating", "review_count",
    "maps_link",
]

# A "website" on these domains means the business has no real site.
SOCIAL_HOSTS = {
    "facebook": ("facebook.com", "fb.com", "fb.me"),
    "instagram": ("instagram.com",),
}
NOT_A_REAL_SITE = SOCIAL_HOSTS["facebook"] + SOCIAL_HOSTS["instagram"] + (
    "yelp.com", "linktr.ee", "business.site", "nextdoor.com", "google.com",
)

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
)

# ----------------------------------------------------------------------------
# Google Maps
# ----------------------------------------------------------------------------

def handle_consent(page) -> None:
    """Click through Google's cookie wall (shows up in the EU/UK)."""
    if "consent.google" not in page.url:
        return
    for label in ("Accept all", "Reject all", "I agree"):
        btn = page.get_by_role("button", name=label)
        if btn.count():
            btn.first.click()
            page.wait_for_load_state("domcontentloaded")
            return


def collect_place_links(page, query: str, max_results: int) -> list[str]:
    """Search Maps and scroll the results list to collect place URLs."""
    url = f"https://www.google.com/maps/search/{quote_plus(query)}?hl=en"
    page.goto(url, wait_until="domcontentloaded")
    handle_consent(page)

    # Some searches jump straight to a single place page.
    try:
        page.wait_for_selector('div[role="feed"], h1.DUwDvf', timeout=15000)
    except PWTimeout:
        print(f"  ! No results loaded for: {query}")
        return []
    if not page.locator('div[role="feed"]').count():
        return [page.url]

    feed = page.locator('div[role="feed"]')
    links: list[str] = []
    stale_rounds = 0
    while len(links) < max_results and stale_rounds < 6:
        hrefs = page.eval_on_selector_all(
            'div[role="feed"] a[href*="/maps/place/"]',
            "els => els.map(e => e.href)",
        )
        before = len(links)
        for h in hrefs:
            if h not in links:
                links.append(h)
        stale_rounds = stale_rounds + 1 if len(links) == before else 0

        if page.get_by_text("You've reached the end of the list").count():
            break
        feed.evaluate("el => el.scrollBy(0, el.scrollHeight)")
        page.wait_for_timeout(1500)

    return links[:max_results]


def text_or_empty(page, selector: str, attr: str | None = None) -> str:
    loc = page.locator(selector)
    if not loc.count():
        return ""
    loc = loc.first
    val = loc.get_attribute(attr) if attr else loc.inner_text()
    return (val or "").strip()


def scrape_place(page, link: str) -> dict:
    """Open one place page and read its details."""
    page.goto(link, wait_until="domcontentloaded")
    try:
        page.wait_for_selector("h1.DUwDvf", timeout=15000)
    except PWTimeout:
        return {}
    page.wait_for_timeout(800)

    name = text_or_empty(page, "h1.DUwDvf")
    category = text_or_empty(page, "button.DkEaL")

    phone = ""
    phone_id = text_or_empty(page, 'button[data-item-id^="phone:tel:"]', "data-item-id")
    if phone_id:
        phone = phone_id.replace("phone:tel:", "")
    phone_label = text_or_empty(page, 'button[data-item-id^="phone:tel:"]', "aria-label")
    if phone_label:  # nicer formatting, e.g. "(214) 555-1234"
        phone = phone_label.replace("Phone:", "").strip() or phone

    website = text_or_empty(page, 'a[data-item-id="authority"]', "href")
    website = clean_google_redirect(website)

    address = text_or_empty(page, 'button[data-item-id="address"]', "aria-label")
    address = address.replace("Address:", "").strip()

    rating, reviews = "", ""
    box = page.locator("div.F7nice")
    if box.count():
        txt = box.first.inner_text()
        m = re.search(r"(\d[.,]\d)", txt)
        if m:
            rating = m.group(1).replace(",", ".")
        m = re.search(r"\(([\d,.\s]+)\)", txt)
        if m:
            reviews = re.sub(r"\D", "", m.group(1))
    if not reviews:
        label = text_or_empty(page, 'div.F7nice span[aria-label*="review"]', "aria-label")
        reviews = re.sub(r"\D", "", label)

    return {
        "name": name,
        "category": category,
        "phone": phone,
        "website": website,
        "address": address,
        "rating": rating,
        "review_count": reviews,
        "maps_link": page.url.split("?")[0] if "/maps/place/" in page.url else link,
    }


def clean_google_redirect(url: str) -> str:
    """Google sometimes wraps websites as /url?q=https://site.com&..."""
    if url and "google.com/url?" in url:
        m = re.search(r"[?&]q=([^&]+)", url)
        if m:
            return unquote(m.group(1))
    return url


# ----------------------------------------------------------------------------
# Email finder
# ----------------------------------------------------------------------------

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,24}")
JUNK_EMAIL_PARTS = (
    "example.", "sentry", "wixpress", "domain.com", "yourdomain", "email.com",
    "godaddy", "@2x", "@3x", "placeholder", "test@", "user@", "name@",
    "noreply", "no-reply", "squarespace", "schema.org", "cloudflare",
)
JUNK_EXT = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".css", ".js")
CONTACT_PATHS = ("/contact", "/contact-us", "/about", "/about-us")


def decode_cfemail(hex_str: str) -> str:
    """Decode Cloudflare-protected emails (data-cfemail attribute)."""
    try:
        key = int(hex_str[:2], 16)
        return "".join(
            chr(int(hex_str[i:i + 2], 16) ^ key) for i in range(2, len(hex_str), 2)
        )
    except ValueError:
        return ""


def extract_emails(page_html: str) -> set[str]:
    found: set[str] = set()
    soup = BeautifulSoup(page_html, "html.parser")

    for a in soup.select('a[href^="mailto:"]'):
        addr = unquote(a["href"][7:].split("?")[0])
        found.update(EMAIL_RE.findall(addr))
    for el in soup.select("[data-cfemail]"):
        found.update(EMAIL_RE.findall(decode_cfemail(el["data-cfemail"])))

    text = html.unescape(soup.get_text(" "))
    # Catch "name [at] site [dot] com" style.
    text = re.sub(r"\s*[\[(]\s*at\s*[\])]\s*", "@", text, flags=re.I)
    text = re.sub(r"\s*[\[(]\s*dot\s*[\])]\s*", ".", text, flags=re.I)
    found.update(EMAIL_RE.findall(text))

    clean = set()
    for e in found:
        e = e.strip(".").lower()
        if not e or e.endswith(JUNK_EXT) or any(j in e for j in JUNK_EMAIL_PARTS):
            continue
        clean.add(e)
    return clean


def host_matches(url: str, hosts: tuple[str, ...]) -> bool:
    netloc = urlparse(url).netloc.lower()
    return any(netloc == h or netloc.endswith("." + h) for h in hosts)


def extract_social(page_html: str, base_url: str) -> dict:
    """Find the business's Facebook and Instagram links on its website."""
    soup = BeautifulSoup(page_html, "html.parser")
    out = {"facebook": "", "instagram": ""}
    for a in soup.select("a[href]"):
        href = urljoin(base_url, a["href"]).split("?")[0].rstrip("/")
        for key, hosts in SOCIAL_HOSTS.items():
            if out[key] or not host_matches(href, hosts):
                continue
            path = urlparse(href).path.lower()
            # Skip share buttons and generic pages, keep profile links.
            if path in ("", "/") or any(s in path for s in ("sharer", "share", "/plugins", "/dialog", "/tr")):
                continue
            out[key] = href
    return out


def classify_website(website: str) -> str:
    if not website:
        return "none"
    if host_matches(website, SOCIAL_HOSTS["facebook"]):
        return "facebook_only"
    if host_matches(website, NOT_A_REAL_SITE):
        return "social_or_directory_only"
    return "has_site"


def enrich_from_website(row: dict, timeout: int = 10, want_emails: bool = True) -> dict:
    """Fill website_status, facebook, instagram, and emails for one lead."""
    website = row.get("website", "")
    result = {"website_status": classify_website(website), "facebook": "", "instagram": "", "emails": ""}
    for key, hosts in SOCIAL_HOSTS.items():
        if website and host_matches(website, hosts):
            result[key] = website
    if result["website_status"] != "has_site":
        return result  # Facebook/Instagram pages need a login to read, so stop here.

    session = requests.Session()
    session.headers["User-Agent"] = UA
    base = f"{urlparse(website).scheme}://{urlparse(website).netloc}"
    emails: set[str] = set()
    pages = [website] + ([urljoin(base, p) for p in CONTACT_PATHS] if want_emails else [])
    for url in pages:
        try:
            r = session.get(url, timeout=timeout, allow_redirects=True)
        except requests.RequestException:
            continue
        if not (r.ok and "text/html" in r.headers.get("content-type", "")):
            continue
        if want_emails:
            emails |= extract_emails(r.text)
        for key, link in extract_social(r.text, r.url).items():
            result[key] = result[key] or link
        if emails and url != website:
            break  # home page + first contact page with a hit is enough
    # Put emails on the business's own domain first.
    domain = urlparse(website).netloc.replace("www.", "")
    ranked = sorted(emails, key=lambda e: (domain not in e, e))
    result["emails"] = "; ".join(ranked[:5])
    return result


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------

def build_queries(args) -> list[str]:
    queries: list[str] = []
    if args.query:
        queries.append(args.query)
    if args.queries:
        queries += [l.strip() for l in Path(args.queries).read_text().splitlines() if l.strip()]
    if args.cities:
        cities = [l.strip() for l in Path(args.cities).read_text().splitlines() if l.strip()]
        base = queries or []
        queries = [f"{q} in {c}" for q in base for c in cities]
    return queries


def main() -> None:
    ap = argparse.ArgumentParser(description="Scrape business leads from Google Maps.")
    ap.add_argument("query", nargs="?", help='Search, e.g. "roofers in Dallas TX"')
    ap.add_argument("--queries", help="Text file with one search per line")
    ap.add_argument("--cities", help="Text file of cities. Runs each search in each city.")
    ap.add_argument("--max", type=int, default=120, help="Max results per search (Maps caps near 120)")
    ap.add_argument("--out", default="leads.csv", help="Output CSV file")
    ap.add_argument("--no-emails", action="store_true", help="Skip email lookup (still checks for Facebook)")
    ap.add_argument("--no-website-only", action="store_true",
                    help="Only save businesses with no real website (none, or just Facebook/Instagram)")
    ap.add_argument("--headful", action="store_true", help="Show the browser window")
    ap.add_argument("--chrome-path", help="Path to a Chrome/Chromium binary (optional)")
    args = ap.parse_args()

    queries = build_queries(args)
    if not queries:
        ap.error("Give a search, or --queries FILE")

    out_path = Path(args.out)
    seen: set[str] = set()
    if out_path.exists():  # resume: skip places already saved
        with out_path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames and reader.fieldnames != FIELDS:
                sys.exit(f"{out_path} has different columns (older version). Use a new --out file.")
            seen = {row["maps_link"] for row in reader}
    new_file = not out_path.exists()

    with sync_playwright() as p, out_path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if new_file:
            writer.writeheader()

        launch = {"headless": not args.headful}
        if args.chrome_path:
            launch["executable_path"] = args.chrome_path
        browser = p.chromium.launch(**launch)
        ctx = browser.new_context(locale="en-US", user_agent=UA, viewport={"width": 1280, "height": 900})
        ctx.route("**/*.{png,jpg,jpeg,gif,webp,woff,woff2}", lambda r: r.abort())
        page = ctx.new_page()
        pool = ThreadPoolExecutor(max_workers=8)
        total = 0

        for qi, query in enumerate(queries, 1):
            print(f"\n[{qi}/{len(queries)}] {query}")
            links = collect_place_links(page, query, args.max)
            print(f"  found {len(links)} listings")
            rows = []
            for i, link in enumerate(links, 1):
                try:
                    row = scrape_place(page, link)
                except Exception as e:  # keep going on any one bad listing
                    print(f"  ! error on listing {i}: {e}")
                    continue
                if not row or row["maps_link"] in seen:
                    continue
                seen.add(row["maps_link"])
                row["query"] = query
                rows.append(row)
                print(f"  {i:>3}. {row['name'][:45]:<45} {row['rating'] or '-':>4} ({row['review_count'] or 0})")

            print("  checking websites for emails and Facebook...")
            enrich = lambda r: enrich_from_website(r, want_emails=not args.no_emails)
            for row, extra in zip(rows, pool.map(enrich, rows)):
                row.update(extra)
            if args.no_website_only:
                rows = [r for r in rows if r["website_status"] != "has_site"]
                print(f"  {len(rows)} have no real website")
            for row in rows:
                writer.writerow({k: row.get(k, "") for k in FIELDS})
            f.flush()
            total += len(rows)
            time.sleep(2)

        browser.close()
        pool.shutdown()

    print(f"\nDone. Saved {total} new leads to {out_path.resolve()}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nStopped. Leads saved so far are in the CSV.")
