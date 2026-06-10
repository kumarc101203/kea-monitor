import requests
# pyrefly: ignore [missing-import]
from bs4 import BeautifulSoup

from config import KEA_URL


def get_page_data():

    response = requests.get(
        KEA_URL,
        timeout=60,
        headers={
            "User-Agent":
            "Mozilla/5.0"
        }
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    links = []

    card_bodies = soup.find_all(
        "div",
        class_="card-body"
    )

    for body in card_bodies:

        for a in body.find_all("a"):

            title = a.get_text(
                strip=True
            )

            href = a.get("href")

            if not title:
                continue

            if not href:
                continue

            links.append(
                {
                    "title": title,
                    "url": href
                }
            )

    return links