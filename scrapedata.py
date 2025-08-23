import requests
from bs4 import BeautifulSoup
import csv
import time
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
import os

BASE_URL        = "https://libgen.li/series.php?id={}"
OUTPUT_CSV      = "libgen_series_basic.csv"
START_ID        = 1
END_ID          = 596257
MAX_WORKERS     = 20      # Number of concurrent threads
REQUEST_TIMEOUT = 10


def parse_series_page(html):
    """Extract series_name, series_type, language, publisher from HTML."""
    soup = BeautifulSoup(html, "html.parser")
    if soup.find(string="Record ID not found"):
        return None

    data = {}
    # h3 series name
    h3_tag = soup.find("h3")
    data["series_name"] = h3_tag.get_text(strip=True) if h3_tag else ""

    # .col-xl-9 p:nth-of-type(3), (6), (9)
    content_div = soup.select_one(".col-xl-9")
    if content_div:
        paragraphs = content_div.find_all("p")
        data["series_type"] = paragraphs[2].get_text(strip=True) if len(paragraphs) >= 3 else ""
        data["language"] = paragraphs[5].get_text(strip=True) if len(paragraphs) >= 6 else ""
        data["publisher"] = paragraphs[8].get_text(strip=True) if len(paragraphs) >= 9 else ""
    else:
        data["series_type"] = ""
        data["language"] = ""
        data["publisher"] = ""

    return data


def fetch_record(series_id, session):
    """Fetch and parse one record."""
    try:
        resp = session.get(BASE_URL.format(series_id), timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
    except requests.RequestException:
        return None
    return parse_series_page(resp.text)


def scrape_series(start_id, end_id, output_csv):
    """Scrape and continuously save results to CSV."""
    fieldnames = ["series_id", "series_name", "series_type", "language", "publisher"]

    # Write header if file doesn't exist
    if not os.path.exists(output_csv):
        with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    session = requests.Session()

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {
            executor.submit(fetch_record, sid, session): sid
            for sid in range(start_id, end_id + 1)
        }

        for future in tqdm(as_completed(futures), total=end_id - start_id + 1, desc="Fetching"):
            sid = futures[future]
            record = future.result()
            if record:
                record["series_id"] = sid
                # Append to CSV immediately
                with open(output_csv, "a", newline="", encoding="utf-8") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow(record)


if __name__ == "__main__":
    start = time.time()
    scrape_series(START_ID, END_ID, OUTPUT_CSV)
    print(f"Scraping complete in {time.time() - start:.0f}s; data saved to {OUTPUT_CSV}")
