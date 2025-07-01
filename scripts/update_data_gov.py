# scripts/update_data_gov.py

import requests
import json
import os
from time import sleep

# Join all keywords for a single, powerful search query
KEYWORDS_QUERY = " OR ".join([
    "cybersecurity", "phishing", "malware", "ransomware", "hacking", "forensic",
    "pentest", "ids", "ips", "siem", "zeroday", "exploit", "ddos", "threat", "mitre",
    "nmap", "network", "firewall", "vulnerability", "reverse", "osint", "incident",
    "log", "password", "encryption", "soc", "mitigation", "cybercrime", "cti",
    "breach", "suricata", "yara", "wireshark", "anomaly", "dfir", "cyberattack"
])

BASE_URL = "https://catalog.data.gov/api/3/action/package_search"
ROWS_PER_PAGE = 100  # The number of results to fetch per API call
MAX_PAGES = 10       # Safety limit to prevent excessive API calls (10 * 100 = 1000 records)

print("📦 Fetching Data.gov datasets...")

results = []
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
            break # Exit loop if there are no more results

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

        # Prepare for the next page
        current_start += len(page_results)
        if current_start >= total_results:
            print("All results have been fetched.")
            break # Exit loop if we've processed all available results

        page += 1
        sleep(1) # Be polite to the API before the next request

    except Exception as e:
        print(f"❌ An error occurred: {e}")
        break # Stop the script if an error occurs

# Save to file
os.makedirs("data", exist_ok=True)
with open("data/data_gov_datasets.json", "w") as f:
    json.dump(results, f, indent=2)

print(f"✅ Saved {len(results)} datasets to data/data_gov_datasets.json")