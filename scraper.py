import requests
from bs4 import BeautifulSoup

from config import KEA_URL


def get_page_data():
    response = requests.get(
        KEA_URL,
        timeout=30
    )

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    links = []

    for a in soup.find_all("a"):
        text = a.get_text(strip=True)
        href = a.get("href")

        if text:
            links.append(
                {
                    "title": text,
                    "url": href
                }
            )

    return links