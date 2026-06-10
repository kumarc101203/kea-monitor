# KEA UGCET 2026 Monitor 🚨

An automated monitoring system that tracks updates on the Karnataka Examinations Authority (KEA) UGCET 2026 portal and sends instant Telegram notifications whenever new links, PDFs, notifications, schedules, seat matrices, or candidate activity links are published.

## Features

- Monitors KEA UGCET 2026 webpage
- Detects newly added:
  - Notifications
  - Information PDFs
  - Candidate Activity Links
  - Schedules
  - Seat Matrix Updates
  - PH Lists
- Sends real-time Telegram alerts
- Snapshot-based change detection
- Lightweight and easy to deploy
- Supports local execution, Windows Task Scheduler, or cloud deployment

---

## Project Structure

```text
kea-monitor/
│
├── app.py
├── scraper.py
├── snapshot.py
├── telegram_bot.py
├── config.py
├── snapshot.json
├── requirements.txt
└── README.md
```

---

## How It Works

```text
KEA Website
      ↓
Scraper
      ↓
Extract UGCET Links
      ↓
Compare With Snapshot
      ↓
Detect Changes
      ↓
Telegram Alert
```

The system stores previously discovered links in `snapshot.json`.

When new content appears on the KEA portal:

- New PDFs
- New notifications
- New schedules
- New candidate activity links

the system sends an instant Telegram notification.

---

## Requirements

- Python 3.11+
- Telegram Bot Token
- Telegram Chat ID

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Telegram Setup

### Create a Telegram Bot

1. Open Telegram
2. Search for **@BotFather**
3. Create a bot using:

```text
/newbot
```

4. Copy the generated Bot Token

Example:

```text
1234567890:AAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

### Get Chat ID

Send a message to your bot.

Open:

```text
https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates
```

Copy the value of:

```json
"chat": {
    "id": 123456789
}
```

---

## Configuration

Edit `config.py`

```python
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

KEA_URL = "https://cetonline.karnataka.gov.in/kea/ugcet2026"
```

Set environment variables:

### Windows PowerShell

```powershell
$env:TELEGRAM_TOKEN="YOUR_TOKEN"
$env:CHAT_ID="YOUR_CHAT_ID"
```

### Linux

```bash
export TELEGRAM_TOKEN="YOUR_TOKEN"
export CHAT_ID="YOUR_CHAT_ID"
```

---

## Running Locally

First run:

```bash
python app.py
```

Output:

```text
First snapshot created with XX items.
```

Subsequent runs:

```text
No new updates found.
```

or

```text
NEW UPDATES FOUND: X
```

---

## Telegram Notification Example

```text
🚨 KEA UPDATE

UGCET - 2026 Mock Seat Allotment Result

https://example-link.com
```

---

## Deployment Options

### Local Machine

Use:

```text
Windows Task Scheduler
```

to run:

```bash
python app.py
```

every 5 minutes.

---

### AWS EC2 (Recommended)

Deploy to a small Ubuntu EC2 instance.

Example cron job:

```bash
*/5 * * * * cd /home/ubuntu/kea-monitor && /usr/bin/python3 app.py
```

---

## Future Improvements

- WhatsApp notifications
- Email alerts
- Multiple website monitoring
- User dashboard
- Batch notifications
- Database support
- Monitoring history logs
- Student alert platform

---

## Monitored Website

KEA UGCET 2026

https://cetonline.karnataka.gov.in/kea/ugcet2026

---

## Disclaimer

This project is an independent monitoring tool and is not affiliated with Karnataka Examinations Authority (KEA).

Users should always verify information directly from the official KEA website.