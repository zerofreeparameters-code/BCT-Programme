#!/usr/bin/env python3
"""BCT Zenodo DOI Fetcher v5 — no ORCID, no accents, just works"""
import urllib.request, urllib.parse, json, os

OUTPUT_FILE = "BCT_DOI_Registry.md"

def fetch(query):
    records = {}
    page = 1
    while True:
        params = urllib.parse.urlencode({"q": query, "size": 100, "page": page, "sort": "mostrecent"})
        url = "https://zenodo.org/api/records?" + params
        req = urllib.request.Request(url, headers={"User-Agent": "BCT/5.0"})
        try:
            data = json.loads(urllib.request.urlopen(req, timeout=30).read().decode("utf-8"))
        except Exception as e:
            print(f"  Error: {e}"); break
        hits = data.get("hits", {}).get("hits", [])
        if page == 1: print(f"  '{query}' → {data.get('hits',{}).get('total',0)} records")
        if not hits: break
        for h in hits:
            recid = str(h.get("id",""))
            records[recid] = {"doi": h.get("doi",""), "recid": recid, "title": h.get("metadata",{}).get("title","?")}
        if len(hits) < 100: break
        page += 1
    return records

print("BCT Zenodo DOI Fetcher v5\n" + "="*50)
all_records = {}
for q in ["BCT Superfluid Lattice", "BCT Letter Cabrie", "Octet-Hopfion", "ZeroFreeParameters"]:
    all_records.update(fetch(q))

records = sorted(all_records.values(), key=lambda x: x["recid"])
print(f"\nTotal unique records: {len(records)}\n" + "="*50)
for r in records:
    print(f"  {r['doi']:<45} {r['title'][:55]}")

lines = ["# BCT Zenodo DOI Registry", "", f"Total: {len(records)} records", "",
         "| # | Record ID | DOI | Title |", "|---|-----------|-----|-------|"]
for i,r in enumerate(records,1):
    doi = f"[{r['doi']}](https://doi.org/{r['doi']})" if r['doi'] else "pending"
    lines.append(f"| {i} | {r['recid']} | {doi} | {r['title'][:65]} |")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"\nSaved to: {os.path.abspath(OUTPUT_FILE)}")
