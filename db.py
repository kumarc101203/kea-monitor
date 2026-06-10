import sqlite3

DB_NAME = "notifications.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS notifications(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT UNIQUE,
            url TEXT
        )
    """)

    conn.commit()
    conn.close()

def exists(title):
    conn = sqlite3.connect(DB_NAME)

    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM notifications WHERE title=?",
        (title,)
    )

    result = cur.fetchone()

    conn.close()

    return result is not None

def save(title,url):
    conn = sqlite3.connect(DB_NAME)

    conn.execute(
        "INSERT OR IGNORE INTO notifications(title,url) VALUES(?,?)",
        (title,url)
    )

    conn.commit()
    conn.close()