import requests
import json
import time

keywords = [
    "cybersecurity", "phishing", "malware", "ransomware", "hacking", "forensic", "pentest",
    "ids", "ips", "siem", "zeroday", "exploit", "ddos", "threat", "mitre", "nmap", "network",
    "firewall", "vulnerability", "reverse", "osint", "incident", "log", "password", "encryption",
    "soc", "mitigation", "cybercrime", "cti", "breach", "suricata", "yara", "wireshark",
    "anomaly", "dfir", "cyberattack"
]

BASE_URL = "https://catalog.data.gov/api/3/action/package_search"
MAX_ROWS = 100
ALL_RESULTS = []

print("📦 Fetching Data.gov datasets...")

for keyword in keywords:
    print(f"🔍 Searching: {keyword}")
    params = {
        "q": keyword,
        "rows": MAX_ROWS,
        "sort": "views_recent desc"
    }
    try:
        res = requests.get(BASE_URL, params=params, timeout=20)
        res.raise_for_status()
        result = res.json()
        if result["success"]:
            for entry in result["result"]["results"]:
                entry["_keyword"] = keyword  # track matched keyword
                ALL_RESULTS.append(entry)
        time.sleep(0.5)
    except Exception as e:
        print(f"❌ Error fetching {keyword}: {e}")

print(f"✅ Total collected: {len(ALL_RESULTS)} datasets")

output = {
    "total": len(ALL_RESULTS),
    "fetched_at": time.strftime("%Y-%m-%d %H:%M:%S"),
    "source": "https://catalog.data.gov/",
    "datasets": ALL_RESULTS
}

output_file = "data/data_gov_datasets.json"
with open(output_file, "w") as f:
    json.dump(output, f, indent=2)

print(f"✅ Saved to {output_file}")
