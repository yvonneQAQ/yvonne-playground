# Yifeng Yvonne Yuan — Playground

Source code for Yifeng Yvonne Yuan's portfolio of audio research, engineering, sound art, and composition. It contains 25 content pages and 7 redirects for unused Wix template/blank routes.

The public website is **https://yvonneyuansplayground.com/**, hosted on OpenAI Sites. The custom domain was connected on November 4, 2026. The original Wix website and `yvonneyuanmusic.com` have not been redirected or removed.

This GitHub repository preserves the site's source and existing Git history. GitHub Pages deployment is not configured yet. Pushing a commit to GitHub does **not** update the current Sites-hosted website.

## Editing and version control

Git records versions of these files locally. GitHub stores a remote copy at https://github.com/yvonneQAQ/yvonne-playground. Sites currently serves the published website; GitHub Pages is a separate hosting option for a future migration.

For routine content updates, edit `content.json`, `works.json`, or `pages.json`, then run these commands from this directory:

```bash
python3 build.py
python3 -m http.server 8765 --directory dist
```

Open http://localhost:8765/ to preview the generated site. Stop the preview with Ctrl+C.

After reviewing an edit, save it to Git and upload it to GitHub:

```bash
git status
git add content.json dist/
git commit -m "Update events"
git push github main
```

The `git add` example is for an Events update. For other changes, include the content/template files actually edited and their generated `dist/` output. The GitHub remote is named `github`; the Sites workflow synchronizes its own source repository separately.

You can also edit JSON content directly on GitHub and commit it there. Until an automatic build/deployment workflow is added, this saves the source change only. Before working locally again, pull those changes with `git pull --ff-only github main`.

To publish through the current hosting setup, the updated source must also be synchronized with Sites and its matching static output deployed there. Local edits, Git commits, and GitHub pushes alone do not publish the website.

## Files

- `content.json`: homepage text, event entries, contact information, and links.
- `works.json`: the contemporary music, multimedia, and film/dance catalogue.
- `pages.json`: editable work descriptions, credits, poems, media URLs, and old-route redirects.
- `asset-manifest.json`: local static files with original source URLs and sizes.
- `homepage.template.html`, `about.template.html`, `works.template.html`, and `work.template.html`: page structures.
- `poetry.template.html`: the reading layout for the original Chinese poems.
- `navigation.template.html` and `footer.template.html`: shared navigation and footer.
- `dist/styles.css`: desktop and mobile layout.
- `dist/site.js`: mobile menu behavior.
- `dist/assets/`: locally stored photos, score images, score PDF, resume, audio recording, and compressed film reel. Third-party YouTube, Vimeo, and Bandcamp players remain on those services.
- `.openai/hosting.json`: current Sites project identity and static directory; it contains no deployment credentials.

Run `python3 build.py` after changing the content or template. The output is a standalone static site in `dist/`; it needs no database, framework, package install, or server-side code.

## Current migration boundary

The homepage, About page, Events, Contact, Works catalogue, all authored published work/poetry pages found in the Wix sitemap, and responsive navigation are implemented. Audio Tools links to the owner's GitHub. The category links jump to the corresponding section of Works.

Existing authored URL paths are retained, including older Field Poetry and Typist variants, the film reel, text scores, and the family recording. The unused `/poetry` template and its three placeholder detail pages redirect to `/mypoetry/`; `/blank-2`, `/blank-3`, and `/s-projects-basic` redirect to Works. Original public source snapshots and original-size assets are backed up outside the deployed project in `../../tmp/wix-migration-2026-11-04/`.

There are no runtime links, images, audio, video, or iframe dependencies on Wix, Wix Static, filesusr, or Parastorage. External music/video platforms and the original Google Drive patch/documentation link remain external. The 53 MB original film reel is preserved in the source backup; the website serves a 720p H.264/AAC copy (about 12 MB) with playback controls and no autoplay.

The owner confirmed two corrections during migration: The World Is My Shelter is performed by guitarist Klondike Steadman; 10000 Waves is for 28 performers. The incorrect letter-to-guitar link is replaced by `/i-wrote-you-a-letter/`, using the owner's supplied YouTube recording `APUgi03JEpY`. The owner changed that video's visibility to Public; this workflow did not alter YouTube account settings.

Works that had no detail page on the original list remain text-only entries. New material has not been invented for those works. The existing 22-event archive is unchanged by this migration.

The owner confirmed that Evil Kid’s Monologue has no video or work description available; it remains a title-only entry in Multimedia. The other five Multimedia works have independent pages. Memory includes its performance video, Bandcamp recording, local photo, and the original Google Drive Max patch/documentation link. Recording fallback links use canonical platform URLs, and Memory's patch link follows the description.

Poetry uses five separate sections matching the original page's larger breaks. Its three existing titled pieces retain their title/date lines; the two untitled pieces retain their opening lines as verse. Original words, punctuation, dates, line order, and stanza breaks are preserved. The reading layout uses local Chinese serif fonts, extra space between poems, and a hanging indent when a long authored line wraps on narrow screens. Poetry navigation points to `/mypoetry/` and marks that page as current. Text scores and the family recording remain available at their existing separate URLs.

## Source content to review later

- The Typist detail page says January 19, 2025; the homepage event says January 18. Original wording is retained pending the owner's correction.
- Memory's detail page says June 1, 2023; the homepage MAT event says June 9. These may refer to different events; neither was silently changed.
- Film/dance project years follow the original page. IMDb lists Sound of Fire as a 2025 release and A Mermaid in a Summer's Night as a 2024 release; the portfolio's existing creation/project years (2024 and 2021) are retained. Sound of Fire's title now follows IMDb. The additional festival events researched separately have not been added.

## Film links

The owner supplied IMDb profile `nm14342387`. Its three Composer credits were verified: Gu Shi `tt44933953`, Sound of Fire `tt38525789`, and A Mermaid in a Summer's Night `tt24510892`. Film titles link to their IMDb pages, with the existing Mermaid trailer retained as a secondary link. Mark and Time to Dream retain their original dance/project links. Film and Dance also links to the full IMDb profile.

The visual direction intentionally follows the current site: a white background, purple two-line title, widely spaced left navigation, a large performance photo, and the existing event archive. Content is copied from the owner's public website for this first comparison, including existing date wording and spelling.

## Future GitHub Pages migration

1. Configure a GitHub Actions workflow to run `python3 build.py` and deploy `dist/` to GitHub Pages.
2. Configure and verify the custom domain in GitHub Pages before changing Namecheap's DNS records.
3. Account for root-relative links when testing: the existing site assumes it is served at a domain root, rather than under a project-repository subpath.
4. Recheck third-party media, downloads, responsive navigation, and old URL paths on the new host.
5. Switch DNS only after the new hosting configuration is ready, then verify HTTPS and both domain variants.

The existing Sites deployment remains the live website until that migration is completed. Domain registration is separate from website hosting. The old Wix domain's permanent redirect and any Wix plan changes are separate follow-up work.
