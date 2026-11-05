# Yvonne Yuan website migration preview

This is a code-maintained reconstruction of the Wix homepage with a new technical profile on the About page. It is a migration preview, not a completed site migration. No domain, DNS, Wix plan, or live Wix content has been changed.

## Files

- `content.json`: homepage text, event entries, contact information, and links.
- `homepage.template.html` and `about.template.html`: page structures.
- `navigation.template.html` and `footer.template.html`: shared navigation and footer.
- `dist/styles.css`: desktop and mobile layout.
- `dist/site.js`: mobile menu behavior.
- `dist/assets/`: locally stored copies of the performance photo and portrait already used on the owner's Wix website.
- `.openai/hosting.json`: private preview Site identity and static directory.

Run `python3 build.py` after changing the content or template. The output is a standalone static site in `dist/`; it needs no database, framework, package install, or server-side code.

## Current migration boundary

The homepage, About page, Events section, Contact section, and responsive navigation are implemented here. Audio Tools is the first Works sub-item and links directly to the owner's GitHub profile. About includes a technical biography, the existing portrait, research areas, selected projects, education, artistic practice, and the owner's downloadable resume.

Works, individual work pages, and Poetry currently link to the existing public Wix site. These pages and their media must be migrated before changing the domain's DNS; otherwise those links would point back to the new host without corresponding pages.

The visual direction intentionally follows the current site: a white background, purple two-line title, widely spaced left navigation, a large performance photo, and the existing event archive. Content is copied from the owner's public website for this first comparison, including existing date wording and spelling.

## Before domain cutover

1. Migrate Works, Poetry, and every work-detail URL.
2. Copy original media locally and check each audio/video embed and credit.
3. Preserve existing URL paths or create explicit redirects.
4. Compare desktop and mobile pages and validate the downloadable resume.
5. Select public hosting that supports the existing custom domain.
6. Point the domain to the new host, verify it, and then decide whether to discontinue the Wix website plan. Domain registration is separate from website hosting.
