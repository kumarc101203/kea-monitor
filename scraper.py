import requests
from bs4 import BeautifulSoup

from config import KEA_URL


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0.0.0 Safari/537.36"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,"
        "application/xml;q=0.9,image/webp,*/*;q=0.8"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive"
}


def get_page_data():

    response = requests.get(
        KEA_URL,
        headers=HEADERS,
        timeout=60
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    links = []

    for a in soup.find_all("a"):

        text = a.get_text(strip=True)
        href = a.get("href")

        if not text:
            continue

        links.append(
            {
                "title": text,
                "url": href
            }
        )

    return links