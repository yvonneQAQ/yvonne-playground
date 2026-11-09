"""Build the portfolio pages from shared navigation and editable content."""
from pathlib import Path
from html import escape
from string import Template
import json
import os
import re

ROOT = Path(__file__).resolve().parent
SITE_URL = 'https://yvonneyuansplayground.com'
base_path = os.environ.get('SITE_BASE_PATH', '').strip('/')
BASE_PATH = '/' + base_path if base_path else ''
published_paths = []


def prepare_html(html):
    """Support the GitHub project preview as well as the production domain root."""
    if not BASE_PATH:
        return html
    html = re.sub(r'((?:href|src|poster)=[\"\'])(/(?!/))', lambda m: m[1] + BASE_PATH + m[2], html)
    return html.replace('content="0;url=/', 'content="0;url=' + BASE_PATH + '/')


data = json.loads((ROOT / 'content.json').read_text())
links = data['links']
values = {key: escape(str(value), quote=True) for key, value in data.items() if isinstance(value, str)}
values.update({key + '_url': escape(value, quote=True) for key, value in links.items()})
values['events_html'] = '\n'.join('<p>' + escape(event) + '</p>' for event in data['events'])
about = data['about']
values.update({ 'about_' + key: escape(value, quote=True) for key, value in about.items() if isinstance(value, str) })
values['about_introduction_html'] = '\n'.join('<p>' + escape(p) + '</p>' for p in about['introduction'])
values['technical_areas_html'] = '\n'.join(
    '<article class="technical-area"><h3>' + escape(area['title']) + '</h3><p>' + escape(area['text']) + '</p></article>'
    for area in about['technical_areas']
)
values['selected_projects_html'] = '\n'.join(
    '<article class="about-project"><h3>' + escape(p['title']) + '</h3><p>' + escape(p['description']) + '</p>'
    '<a href="' + escape(p['link'], quote=True) + '">' + escape(p['link_label']) + '<span aria-hidden="true"> ↗</span></a></article>'
    for p in about['selected_projects']
)
values['education_html'] = '\n'.join(
    '<div class="education-entry"><dt>' + escape(e['degree']) + '</dt><dd>' + escape(e['institution']) + '<span>' + escape(e['date']) + '</span></dd></div>'
    for e in about['education']
)

def render_page(page, template_name, output, extra=None):
    context = dict(values)
    public_path = '/' + output.removesuffix('index.html')
    context.update({
        'canonical_url': SITE_URL + public_path,
        'site_url': SITE_URL,
        'home_current': ' aria-current="page"' if page == 'home' else '',
        'about_current': ' aria-current="page"' if page == 'about' else '',
        'audio_tools_current': ' aria-current="page"' if page == 'audio-tools' else '',
        'works_current': ' aria-current="page"' if page == 'works' else '',
        'poetry_current': ' aria-current="page"' if page == 'poetry' else '',
        'events_url': '#events' if page == 'home' else '/#events',
    })
    context.update(extra or {})
    for partial in ('navigation', 'footer'):
        context[partial + '_html'] = Template((ROOT / (partial + '.template.html')).read_text()).substitute(context)
    target = ROOT / 'dist' / output
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(prepare_html(Template((ROOT / template_name).read_text()).substitute(context)))
    published_paths.append(public_path)
    print('Built', target.relative_to(ROOT))


def text_html(text):
    """Keep authored line breaks while discarding Wix's empty spacer lines."""
    return '<br>'.join(escape(line) for line in text.splitlines())


def render_block(block, page_title):
    kind = block['type']
    text = block.get('text', '')
    if kind == 'poem':
        heading = '<h2>' + escape(block['heading']) + '</h2>' if block.get('heading') else ''
        label = block.get('heading') or text.splitlines()[0]
        stanzas = ''.join('<div class="poem-stanza">' + ''.join('<span class="poem-line">' + escape(line) + '</span>' for line in stanza.splitlines()) + '</div>' for stanza in re.split(r'\n\s*\n', text))
        return '<section class="poem" id="' + escape(block['id'], quote=True) + '" aria-label="' + escape(label, quote=True) + '">' + heading + '<div class="poem-verse">' + stanzas + '</div></section>'
    if kind in ('paragraph', 'heading', 'verse'):
        if kind == 'verse':
            return '<div class="verse" lang="zh-Hans">' + escape(text) + '</div>'
        if kind == 'heading' and len(text) < 140 and '\n' not in text:
            return '<h2>' + escape(text) + '</h2>'
        return '\n'.join('<p>' + text_html(p.strip()) + '</p>' for p in re.split(r'\n\s*\n', text) if p.strip())
    if kind == 'signal-flow':
        steps = ''.join(
            f'<li><strong>{escape(step["title"])}</strong><span>{escape(step["text"])}</span></li>'
            for step in block['steps']
        )
        return f'<ol class="signal-flow">{steps}</ol>'
    src = escape(block.get('src', ''), quote=True)
    title = escape(block.get('title') or page_title, quote=True)
    if kind == 'image':
        alt = escape(block.get('alt') or page_title + ' — score or artwork', quote=True)
        width, height = block.get('width'), block.get('height')
        dimensions = f' width="{int(width)}" height="{int(height)}"' if width and height else ''
        return f'<figure class="work-image"><a href="{src}" target="_blank" rel="noopener" aria-label="Open image: {alt}"><img src="{src}" alt="{alt}" loading="lazy"{dimensions}></a></figure>'
    if kind == 'embed':
        provider = block.get('provider', '').lower()
        is_audio = provider == 'bandcamp' or 'bandcamp.com' in block.get('src', '')
        height = int(block.get('height') or (120 if is_audio else 360))
        fallback = block.get('fallback_url') or block.get('source_url', '')
        if provider == 'youtube':
            fallback = 'https://www.youtube.com/watch?v=' + block['src'].split('/embed/')[-1].split('?')[0]
        elif provider == 'vimeo':
            fallback = 'https://vimeo.com/' + block['src'].split('/video/')[-1].split('?')[0]
        if 'filesusr.com' in fallback:
            fallback = ''
        if fallback and not fallback.startswith(('https://', 'http://')):
            fallback = block.get('src', '')
        player = f'<iframe src="{src}" title="{title}" loading="lazy" height="{height}" allow="autoplay; fullscreen; picture-in-picture; encrypted-media" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe>'
        label = 'Listen on Bandcamp' if is_audio else 'Watch on Vimeo' if provider == 'vimeo' else 'Watch on YouTube' if provider == 'youtube' else 'Open recording'
        link = f'<a class="media-fallback" href="{escape(fallback, quote=True)}">{label} <span aria-hidden="true">↗</span></a>' if fallback else ''
        return '<div class="media-block ' + ('audio-embed' if is_audio else 'video-embed') + '">' + player + '</div>' + link
    if kind == 'download':
        label = escape(text or block.get('title') or 'Download')
        attribute = ' download' if block.get('src', '').startswith('/assets/') else ''
        return f'<p class="work-download"><a href="{src}"{attribute}>{label} <span aria-hidden="true">↗</span></a></p>'
    if kind == 'audio':
        artist = '<p class="audio-artist">' + escape(block['artist']) + '</p>' if block.get('artist') else ''
        return f'<div class="native-audio"><p>{title}</p>{artist}<audio controls preload="metadata" src="{src}"><a href="{src}">Listen to {title}</a></audio></div>'
    if kind == 'video':
        poster = ' poster="' + escape(block['poster'], quote=True) + '"' if block.get('poster') else ''
        return f'<video class="native-video" controls playsinline preload="metadata"{poster} src="{src}" aria-label="{title}"><a href="{src}">Watch {title}</a></video>'
    raise ValueError('Unsupported content block: ' + kind)


render_page('home', 'homepage.template.html', 'index.html')
render_page('about', 'about.template.html', 'about/index.html')
render_page('audio-tools', 'audio-tools.template.html', 'audio-tools/index.html')

works = json.loads((ROOT / 'works.json').read_text())
sections = []
category_by_path = {}
for category in works['categories']:
    items = []
    for item in category['items']:
        title = escape(item['title'])
        if item.get('path'):
            if item.get('link_label'):
                title += ' <span class="work-link-label">' + escape(item['link_label']) + '<span aria-hidden="true"> ↗</span></span>'
            title = '<a href="' + escape(item['path'], quote=True) + '">' + title + '</a>'
            category_by_path[item['path']] = category
        description = escape(item.get('description', ''))
        details = ' '.join(s for s in (description, '(' + escape(item['year']) + ')') if s)
        additional_links = '<div class="work-additional-links">' + ''.join('<a href="' + escape(link['url'], quote=True) + '">' + escape(link['label']) + '<span aria-hidden="true"> ↗</span></a>' for link in item['additional_links']) + '</div>' if item.get('additional_links') else ''
        items.append('<li><span class="work-list-title">' + title + '</span><span class="work-list-details">' + details + '</span>' + additional_links + '</li>')
    intro_link = '<p class="category-link"><a href="' + escape(category['intro_link']['url'], quote=True) + '">' + escape(category['intro_link']['label']) + '<span aria-hidden="true"> ↗</span></a></p>' if category.get('intro_link') else ''
    sections.append('<section class="work-category" id="' + category['id'] + '"><h2>' + escape(category['title']) + '</h2>' + intro_link + '<ul class="work-list">' + '\n'.join(items) + '</ul></section>')
render_page('works', 'works.template.html', 'listofworks/index.html', {'works_sections_html': '\n'.join(sections)})

pages_file = ROOT / 'pages.json'
if pages_file.exists():
    pages = json.loads(pages_file.read_text())
    for page in pages['pages']:
        is_poetry = page['slug'] == 'mypoetry'
        is_audio_tool = page.get('category') == 'audio-tools'
        category = category_by_path.get('/' + page['slug'] + '/')
        back_url = '/listofworks/#' + category['id'] if category else ('/' if is_poetry else '/mypoetry/' if page.get('category') == 'poetry' else '/listofworks/')
        back_label = category['title'] if category else ('Home' if is_poetry else 'Poetry' if page.get('category') == 'poetry' else 'Works')
        if is_audio_tool:
            back_url, back_label = '/audio-tools/', 'Audio Tools'
        blocks = page['blocks']
        heading = page.get('heading') or page['title']
        render_page('poetry' if is_poetry else 'work', 'poetry.template.html' if is_poetry else 'work.template.html', page['slug'] + '/index.html', {
            'page_title': escape(page['title'], quote=True),
            'page_heading': escape(heading),
            'page_description': escape(page.get('description') or page['title'] + ' — a work by Yifeng Yvonne Yuan.', quote=True),
            'page_class': 'audio-tool-page' if is_audio_tool else '',
            'back_url': back_url,
            'back_label': escape(back_label),
            'page_blocks_html': '\n'.join(render_block(b, page['title']) for b in blocks),
        })
    for old_path, destination in pages.get('redirects', {}).items():
        target = ROOT / 'dist' / old_path.strip('/') / 'index.html'
        target.parent.mkdir(parents=True, exist_ok=True)
        href = escape(destination, quote=True)
        target.write_text(prepare_html('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0;url=' + href + '"><title>Yifeng Yvonne Yuan</title><link rel="canonical" href="' + href + '"></head><body><p><a href="' + href + '">Continue to Yifeng Yvonne Yuan’s website</a></p></body></html>'))

(ROOT / 'dist' / '.nojekyll').touch()
(ROOT / 'dist' / 'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: ' + SITE_URL + '/sitemap.xml\n')
(ROOT / 'dist' / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + '\n'.join('  <url><loc>' + escape(SITE_URL + path) + '</loc></url>' for path in published_paths) + '\n</urlset>\n')
