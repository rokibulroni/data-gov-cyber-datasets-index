# Data.gov Cybersecurity Datasets Index

**🔄 Auto-updated repository of cybersecurity-related datasets from Data.gov using the CKAN API.**
Structured JSON output, refreshed every 3 days—ideal for powering web apps, research, or dashboards.

* **Maintainer:** Rokibul Islam Roni
* **Website:** [https://rokibulroni.com](https://rokibulroni.com)
* **Update Schedule:** Every 3 days via GitHub Actions

---

## 🧠 What’s Inside?

This repository aggregates public datasets focused on:

* 🛡️ Cybersecurity
* 🎣 Phishing, 🐞 Malware, 🛑 Ransomware
* 🔬 Digital Forensics, 🔁 Reverse Engineering
* 🧠 IDS, IPS, SIEM, Zero-Day Threats
* 💣 Exploits, 🧱 Firewalls, 🧵 Threat Intelligence
* 🔐 Passwords, Encryption, Network Logs
* 🕵️ SOC, Breach Reports, CTI, Anomalies
* 🐍 YARA, 🧪 Suricata, 🧰 Wireshark
* 🧯 DFIR, 🚨 Incident Logs, 🔍 MITRE Tags

---

## ⚙️ How It Works

* Runs a Python script for each keyword (36+ total)
* Queries Data.gov via CKAN API for dataset listings
* Merges, filters, and deduplicates results
* Outputs to: `data/data_gov_datasets.json`
* Auto-commits updates only if new datasets are found

---

## 📁 Folder Structure

| Path                                    | Description                              |
| --------------------------------------- | ---------------------------------------- |
| `.github/workflows/update_datasets.yml` | GitHub Actions workflow (3-day interval) |
| `scripts/update_data_gov.py`            | Main Python crawler script               |
| `data/data_gov_datasets.json`           | Cleaned JSON index of datasets           |

---

## 📦 Example Usage (Frontend)

Integrate this data in your frontend by fetching the raw JSON:

* **JSON URL:**
  [https://rokibulroni.github.io/data-gov-cyber-datasets-index/data/data\_gov\_datasets.json](https://rokibulroni.github.io/data-gov-cyber-datasets-index/data/data_gov_datasets.json)

**Ideas:**

* Display datasets in searchable/filterable tables or charts
* Filter by keyword, format, agency, or publication date
* Link directly to dataset sources

---

## 🧾 JSON Sample (Simplified)

```json
{
  "total": 1793,
  "fetched_at": "2025-07-01 23:30:05",
  "datasets": [
    {
      "title": "Cyber Threat Indicators",
      "organization": "DHS CISA",
      "notes": "Indicators of Compromise (IOC) shared with federal systems",
      "url": "https://catalog.data.gov/dataset/example-threat",
      "_keyword": "threat"
    }
    // ... more items
  ]
}
```

---

## 📜 License

* This repository collects and indexes only public dataset metadata.
* All dataset content belongs to their original providers.
* Code is [MIT Licensed](LICENSE)—free to use and modify.
