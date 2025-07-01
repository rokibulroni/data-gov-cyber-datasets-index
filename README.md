 

# Data.gov Cybersecurity Datasets Index

🔄 **Auto-updated repository of cybersecurity-related datasets from Data.gov** using CKAN API. The output is a structured JSON file refreshed every 3 days — perfect for powering web apps, research tools, or dashboards.

👤 Maintained by: Rokibul Islam Roni
🌐 Website: [https://rokibulroni.com](https://rokibulroni.com)
📅 Schedule: Auto-updates every 3 days via GitHub Actions

───────────────────────────────────────

🧠 What’s Inside?

This repo includes public datasets related to:

• 🛡️ Cybersecurity
• 🎣 Phishing, 🐞 Malware, 🛑 Ransomware
• 🔬 Digital Forensics, 🔁 Reverse Engineering
• 🧠 IDS, IPS, SIEM, Zero-Day
• 💣 Exploits, 🧱 Firewalls, 🧵 Threat Intel
• 🔐 Passwords, Encryption, Network Logs
• 🕵️ SOC, Breach Reports, CTI, Anomalies
• 🐍 YARA, 🧪 Suricata, 🧰 Wireshark
• 🧯 DFIR, 🚨 Incident Logs, 🔍 MITRE Tags

───────────────────────────────────────

⚙️ How It Works

• Runs a Python script for each keyword (36+ total)
• Uses CKAN API from Data.gov for dataset listings
• Merges, filters, and deduplicates the results
• Saves to: `data/data_gov_datasets.json`
• Auto-commits updated file only if new results exist

───────────────────────────────────────

📁 Folder Structure

| Folder / File                          | Description                        |
| -------------------------------------- | ---------------------------------- |
| .github/workflows/update\_datasets.yml | GitHub Actions (runs every 3 days) |
| scripts/update\_data\_gov.py           | Python crawler script              |
| data/data\_gov\_datasets.json          | Cleaned JSON index of datasets     |

───────────────────────────────────────

📦 Example Usage (Frontend)

Want to integrate with your frontend? Just fetch the raw JSON:

URL:
[Check the API](https://rokibulroni.github.io/data-gov-cyber-datasets-index/data/data_gov_datasets.json)

Frontend usage idea:
• Load datasets in tables, charts, or search components
• Filter by keyword, format, agency, or date
• Show links to download datasets directly

───────────────────────────────────────

🧾 JSON Sample (Simplified)

{
"total": 1793,
"fetched\_at": "2025-07-01 23:30:05",
"datasets": \[
{
"title": "Cyber Threat Indicators",
"organization": "DHS CISA",
"notes": "Indicators of Compromise (IOC) shared with federal systems",
"url": "[https://catalog.data.gov/dataset/example-threat](https://catalog.data.gov/dataset/example-threat)",
"\_keyword": "threat"
},
...
]
}

 

───────────────────────────────────────

📜 License

• This repo collects only public dataset metadata
• All data belongs to original dataset providers
• Code is MIT Licensed — free to use and modify
 
