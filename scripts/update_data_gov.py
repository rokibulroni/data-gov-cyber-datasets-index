# scripts/update_data_gov.py

import requests
import json
import os
import sys  # Import the sys module
from time import sleep

# (Your KEYWORDS_QUERY, BASE_URL, etc. remain the same)
KEYWORDS_QUERY = " OR ".join([
    "cybersecurity", "phishing", "malware", "ransomware", "hacking", "forensic",
    "pentest", "ids", "ips", "siem", "zeroday", "exploit", "ddos", "threat", "mitre",
    "nmap", "network", "firewall", "vulnerability", "reverse", "osint", "incident",
    "log", "password", "encryption", "soc", "mitigation", "cybercrime", "cti",
    "breach", "suricata", "yara", "wireshark", "anomaly", "dfir", "cyberattack"
])
BASE_URL = "https://catalog.data.gov/api/3/action/package_search"
ROWS_PER_PAGE = 100
MAX_PAGES = 10

print("📦 Fetching Data.gov datasets...")
results = []
# ... (The while loop for fetching data remains exactly the same) ...
seen_ids = set()
current_start = 0
page = 1

while page <= MAX_PAGES:
    try:
        print(f"📄 Fetching page {page}...")
        params = {"q": KEYWORDS_QUERY, "rows": ROWS_PER_PAGE, "start": current_start}
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()

        data = response.json().get("result", {})
        page_results = data.get("results", [])
        total_results = data.get("count", 0)

        if not page_results:
            print("No more results found. Ending search.")
            break

        for item in page_results:
            if item["id"] not in seen_ids:
                seen_ids.add(item["id"])
                results.append({
                    "title": item.get("title"),
                    "name": item.get("name"),
                    "notes": item.get("notes"),
                    "url": f'https://catalog.data.gov/dataset/{item.get("name")}',
                    "tags": [tag["name"] for tag in item.get("tags", [])],
                    "organization": item.get("organization", {}).get("title", "N/A"),
                    "updated": item.get("metadata_modified", "")
                })

        current_start += len(page_results)
        if current_start >= total_results:
            print("All results have been fetched.")
            break

        page += 1
        sleep(1)

    except Exception as e:
        print(f"❌ An error occurred: {e}")
        break

# 🔽🔽🔽 --- THIS IS THE NEW, CRITICAL CHECK --- 🔽🔽🔽
if not results:
    print("❌ No datasets were found. Exiting with an error to prevent committing an empty file.")
    sys.exit(1) # Exit with a non-zero status code to indicate failure

# --- The rest of the script remains the same ---
os.makedirs("data", exist_ok=True)
with open("data/data_gov_datasets.json", "w") as f:
    json.dump(results, f, indent=2)

print(f"✅ Saved {len(results)} datasets to data/data_gov_datasets.json")
