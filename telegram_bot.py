import requests

from config import (
    TELEGRAM_TOKEN,
    CHAT_ID
)


def send_message(message):

    url = (
        f"https://api.telegram.org/"
        f"bot{TELEGRAM_TOKEN}/sendMessage"
    )

    response = requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )

    return response.json()