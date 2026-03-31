import json
from datetime import datetime

with open('zenodo_response.json') as f:
    data = json.load(f)

hits = data.get('hits', {}).get('hits', [])
total = data.get('hits', {}).get('total', 0)

with open('ZENODO_DOIS.md', 'w') as out:
    out.write("# BCT Programme Zenodo DOI Registry\n\n")
    out.write("**Last synced:** " + datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC') + "\n\n")
    out.write("**Total records:** " + str(total) + "\n\n")
    out.write("| # | Title | DOI | Date | Type |\n")
    out.write("|---|-------|-----|------|------|\n")

    for i, hit in enumerate(hits, 1):
        meta = hit.get('metadata', {})
        title = meta.get('title', 'Untitled').replace('|', '-')
        doi = meta.get('doi', 'N/A')
        date = meta.get('publication_date', 'N/A')
        rtype = meta.get('resource_type', {}).get('title', 'N/A')
        if doi != 'N/A':
            doi_link = "[" + doi + "](https://doi.org/" + doi + ")"
        else:
            doi_link = "N/A"
        if len(title) > 80:
            title = title[:77] + "..."
        out.write("| " + str(i) + " | " + title + " | " + doi_link + " | " + date + " | " + rtype + " |\n")

    out.write("\n---\n\n")
    out.write("*Auto-generated from Zenodo API. ORCID: 0009-0007-9561-9859*\n")

print("Generated ZENODO_DOIS.md with " + str(len(hits)) + " records (total: " + str(total) + ")")
