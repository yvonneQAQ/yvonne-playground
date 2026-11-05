"""Build the appearance-preserving homepage without third-party dependencies."""
from pathlib import Path
from html import escape
from string import Template
import json

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / 'content.json').read_text())
links = data['links']
values = {key: escape(str(value), quote=True) for key, value in data.items() if isinstance(value, str)}
values.update({key + '_url': escape(value, quote=True) for key, value in links.items()})
values['events_html'] = '\n'.join('<p>' + escape(event) + '</p>' for event in data['events'])
template = Template((ROOT / 'homepage.template.html').read_text())
(ROOT / 'dist/index.html').write_text(template.substitute(values))
print('Built dist/index.html')
