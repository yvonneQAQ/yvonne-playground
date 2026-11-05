"""Build the portfolio pages from shared navigation and editable content."""
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

for page, template_name, output in [
    ('home', 'homepage.template.html', 'index.html'),
    ('about', 'about.template.html', 'about/index.html'),
]:
    context = dict(values)
    context.update({
        'home_current': ' aria-current="page"' if page == 'home' else '',
        'about_current': ' aria-current="page"' if page == 'about' else '',
        'events_url': '#events' if page == 'home' else '/#events',
    })
    for partial in ('navigation', 'footer'):
        context[partial + '_html'] = Template((ROOT / (partial + '.template.html')).read_text()).substitute(context)
    target = ROOT / 'dist' / output
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(Template((ROOT / template_name).read_text()).substitute(context))
    print('Built', target.relative_to(ROOT))
