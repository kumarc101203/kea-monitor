from telegram_bot import send_message
send_message("GitHub Action Started")
from scraper import get_page_data
from snapshot import (
    load_snapshot,
    save_snapshot
)
from telegram_bot import send_message


current_data = get_page_data()

ugcet_items = []

for item in current_data:

    title = item["title"]
    url = item["url"]

    if not url:
        continue

    if (
        "ugcet" in url.lower()
        or ".pdf" in url.lower()
    ):
        ugcet_items.append(item)


old_snapshot = load_snapshot()


if not old_snapshot:

    save_snapshot(ugcet_items)

    print(
        f"First snapshot created with "
        f"{len(ugcet_items)} items."
    )

else:

    old_items = {
        f"{item['title']}|{item['url']}"
        for item in old_snapshot
    }

    current_items = {
        f"{item['title']}|{item['url']}"
        for item in ugcet_items
    }

    new_items = current_items - old_items

    if not new_items:

        print("No new updates found.")

    else:

        print(
            f"\nNEW UPDATES FOUND: "
            f"{len(new_items)}\n"
        )

        for item in ugcet_items:

            item_key = (
                f"{item['title']}|{item['url']}"
            )

            if item_key in new_items:

                title = item["title"]
                url = item["url"]

                print("=" * 80)
                print(title)
                print(url)

                response = send_message(
                    f"🚨 KEA UPDATE\n\n"
                    f"{title}\n\n"
                    f"{url}"
                )

                print(response)

    save_snapshot(ugcet_items)