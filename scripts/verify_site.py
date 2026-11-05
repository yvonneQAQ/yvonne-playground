"""Check generated pages before publishing to GitHub Pages (standard library only)."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import os

ROOT = Path(__file__).resolve().parents[1] / 'dist'
base = os.environ.get('SITE_BASE_PATH', '').strip('/')
PREFIX = '/' + base if base else ''


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.refs, self.ids = [], set()
        self.redirect = self.noindex = self.canonical = False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        self.refs.extend(attrs[key] for key in ('href', 'src', 'poster') if attrs.get(key))
        if tag == 'meta':
            self.redirect |= attrs.get('http-equiv', '').lower() == 'refresh'
            self.noindex |= attrs.get('name') == 'robots' and 'noindex' in attrs.get('content', '')
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical |= attrs.get('href', '').startswith('https://yvonneyuansplayground.com/')


pages = {path: Page(path.read_text()) for path in ROOT.rglob('*.html')}
assert pages, 'No HTML pages were generated'
errors = []
for path, page in pages.items():
    label = str(path.relative_to(ROOT))
    if not page.redirect and (page.noindex or not page.canonical):
        errors.append(f'{label}: missing production canonical URL or still marked noindex')
    for ref in page.refs:
        url = urlsplit(ref)
        if url.scheme or url.netloc:
            continue
        if url.path.startswith('/'):
            local = unquote(url.path)
            if PREFIX:
                if not local.startswith(PREFIX + '/'):
                    errors.append(f'{label}: link is missing project prefix: {ref}')
                    continue
                local = local[len(PREFIX):]
            target = ROOT / local.lstrip('/')
        elif url.path:
            target = path.parent / unquote(url.path)
        else:
            target = path
        if target.is_dir():
            target = target / 'index.html'
        if not target.exists():
            errors.append(f'{label}: missing local target: {ref}')
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            errors.append(f'{label}: missing anchor: {ref}')

assert (ROOT / 'robots.txt').is_file(), 'Missing robots.txt'
assert (ROOT / 'sitemap.xml').is_file(), 'Missing sitemap.xml'
if errors:
    raise SystemExit('\n'.join(errors))
print(f'Checked {len(pages)} HTML pages and their local links (base path: {PREFIX or "/"}).')
