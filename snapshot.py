import json
import os

SNAPSHOT_FILE = "snapshot.json"


def load_snapshot():

    if not os.path.exists(SNAPSHOT_FILE):
        return []

    with open(
        SNAPSHOT_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_snapshot(data):

    with open(
        SNAPSHOT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )