#!/usr/bin/env python3
"""
BCT Zenodo Bulk Downloader v4
Fixes URL encoding for filenames with spaces and brackets
Run: python3 download_zenodo_BCT_v4.py
"""

import urllib.request
import urllib.parse
import json
import os
import time

OUTPUT_DIR = "BCT_Zenodo_Downloads"

# Failed IDs from v3 run
KNOWN_RECORD_IDS = [
    "18975018",  # Appendix JH
    "18974754",  # Letter 36
    "19139402",  # Letter 86 Cabibbo
    "19139592",  # Appendix AD1
    "19139846",  # Appendix AD2
    "19139680",  # Letter 87 CP Violation
    "19139789",  # Open Challenge
    "19142917",  # Letters Vol 4
]

def fetch_json(url):
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "BCT-Downloader/4.0", "Accept": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())

def download_file(url, filepath):
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "BCT-Downloader/4.0"}
    )
    with urllib.request.urlopen(req, timeout=120) as r, open(filepath, "wb") as f:
        total = 0
        while True:
            chunk = r.read(16384)
            if not chunk:
                break
            f.write(chunk)
            total += len(chunk)
    return total

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("BCT Zenodo Bulk Downloader v4 — fixing failed downloads")
    print(f"Output folder: {os.path.abspath(OUTPUT_DIR)}/")
    print(f"Records to retry: {len(KNOWN_RECORD_IDS)}")
    print("-" * 55)

    downloaded = 0
    skipped = 0
    failed = 0

    for i, record_id in enumerate(KNOWN_RECORD_IDS):
        print(f"\n[{i+1}/{len(KNOWN_RECORD_IDS)}] Fetching record {record_id}...")

        try:
            url = f"https://zenodo.org/api/records/{record_id}"
            record = fetch_json(url)
            title = record.get("metadata", {}).get("title", "Untitled")[:55]
            print(f"  Title: {title}")

            files = record.get("files", [])
            if not files:
                print(f"  ⚠️  No files found")
                skipped += 1
                continue

            for file_info in files:
                filename = file_info.get("key", f"{record_id}.pdf")
                
                # URL-encode the filename to handle spaces and brackets
                encoded_filename = urllib.parse.quote(filename, safe="")
                file_url = f"https://zenodo.org/api/records/{record_id}/files/{encoded_filename}/content"

                # Save with a clean local filename (replace spaces and brackets)
                clean_name = filename.replace(" ", "_").replace("(", "").replace(")", "")
                safe_name = f"{record_id}_{clean_name}"
                filepath = os.path.join(OUTPUT_DIR, safe_name)

                if os.path.exists(filepath):
                    size_kb = os.path.getsize(filepath) / 1024
                    print(f"  ✅ Already have: {safe_name} ({size_kb:.0f} KB)")
                    skipped += 1
                    continue

                print(f"  ⬇️  Downloading: {filename}")
                try:
                    size = download_file(file_url, filepath)
                    print(f"  ✅ Saved: {safe_name} ({size/1024:.0f} KB)")
                    downloaded += 1
                    time.sleep(0.5)
                except Exception as e:
                    print(f"  ❌ Download failed: {e}")
                    failed += 1

        except Exception as e:
            print(f"  ❌ Could not fetch record {record_id}: {e}")
            failed += 1

        time.sleep(0.3)

    print("\n" + "=" * 55)
    print("COMPLETE!")
    print(f"  ✅ Downloaded: {downloaded} files")
    print(f"  ⏭️  Skipped:    {skipped}")
    print(f"  ❌ Failed:     {failed}")
    print(f"\n  📁 Location: {os.path.abspath(OUTPUT_DIR)}/")
    print("=" * 55)
    print("\n✨ Now drag BCT_Zenodo_Downloads/ into GitHub!")

if __name__ == "__main__":
    main()
