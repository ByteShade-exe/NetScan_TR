# logger.py – Save as JSON and SQLite

import os, json, sqlite3
from datetime import datetime

def save_results(ip, data):
    os.makedirs("scan_results", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"{ip}_{timestamp}_scan_results.json"
    with open(os.path.join("scan_results", filename), "w") as f:
        json.dump(data, f, indent=2)

    conn = sqlite3.connect("results.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS scans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT, time TEXT, port INTEGER,
        protocol TEXT, service TEXT, version TEXT, state TEXT
    )""")
    for entry in data.get("scan", []):
        cursor.execute("INSERT INTO scans VALUES (NULL,?,?,?,?,?,?,?,?)", (
            ip, timestamp, entry["port"],
            entry["protocol"], entry["service"],
            entry["version"], entry["state"]
        ))
    conn.commit()
    conn.close()
    print(f"[✔] Saved: {filename} & updated database.")