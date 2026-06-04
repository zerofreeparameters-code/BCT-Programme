import json
from datetime import datetime

with open('zenodo_response.json') as f:
    data = json.load(f)

hits = data.get('hits', {}).get('hits', [])
total = data.get('hits', {}).get('total', 0)

lines = [
    '# BCT Programme - Zenodo DOI Registry',
    '',
    'Auto-updated: ' + datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC'),
    '',
    'Total records: ' + str(total),
    '',
    '| DOI | Title | Date |',
    '|-----|-------|------|',
]

for hit in hits:
    doi = hit.get('doi', 'N/A')
    title = hit.get('metadata', {}).get('title', 'Untitled').replace('|', '-')[:80]
    date = hit.get('metadata', {}).get('publication_date', '')
    lines.append('| [' + doi + '](https://doi.org/' + doi + ') | ' + title + ' | ' + date + ' |')

with open('ZENODO_DOIS.md', 'w') as f:
    f.write('\n'.join(lines))

print('Written ' + str(len(hits)) + ' records')
