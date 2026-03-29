#!/usr/bin/env python3
"""BCT Zenodo DOI Fetcher v6 — updated API format"""
import urllib.request, urllib.parse, json, os

OUTPUT_FILE = "BCT_DOI_Registry.md"

def fetch(query):
    records = {}
    page = 1
    while True:
        params = urllib.parse.urlencode({
            "q": query,
            "size": 100,
            "page": page,
            "sort": "mostrecent",
            "access_token": ""
        })
        url = "https://zenodo.org/api/records?" + params
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json"
        })
        try:
            resp = urllib.request.urlopen(req, timeout=30)
            data = json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            print(f"  Error on '{query}': {e}")
            break
        hits = data.get("hits", {}).get("hits", [])
        total = data.get("hits", {}).get("total", {})
        if isinstance(total, dict):
            total = total.get("value", 0)
        if page == 1:
            print(f"  '{query}' -> {total} records")
        if not hits:
            break
        for h in hits:
            recid = str(h.get("id", ""))
            doi = h.get("doi", "") or h.get("metadata", {}).get("doi", "")
            title = h.get("metadata", {}).get("title", "?")
            records[recid] = {"doi": doi, "recid": recid, "title": title}
        if len(hits) < 100:
            break
        page += 1
    return records

print("BCT Zenodo DOI Fetcher v6")
print("=" * 50)

all_records = {}
queries = [
    "Cabrie BCT",
    "Cabri BCT Superfluid",
    "BCT Superfluid Lattice Model",
    "Octet-Hopfion Condensate",
]
for q in queries:
    all_records.update(fetch(q))

records = sorted(all_records.values(), key=lambda x: x["recid"])
print(f"\nTotal unique records: {len(records)}")
print("=" * 50)
for r in records:
    print(f"  {r['doi']:<45} {r['title'][:55]}")

lines = [
    "# BCT Zenodo DOI Registry",
    "",
    f"Total: {len(records)} records",
    "",
    "| # | Record ID | DOI | Title |",
    "|---|-----------|-----|-------|"
]
for i, r in enumerate(records, 1):
    if r['doi']:
        doi = f"[{r['doi']}](https://doi.org/{r['doi']})"
    else:
        doi = "pending"
    lines.append(f"| {i} | {r['recid']} | {doi} | {r['title'][:65]} |")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"\nSaved to: {os.path.abspath(OUTPUT_FILE)}")
