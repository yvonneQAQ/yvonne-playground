# Yifeng Yvonne Yuan — Playground

Source code for Yifeng Yvonne Yuan's portfolio of audio research, engineering, sound art, and composition. It contains 25 content pages and 7 redirects for unused Wix template/blank routes.

The public website is **https://yvonneyuansplayground.com/**, hosted on **GitHub Pages**. Namecheap manages the domain's DNS. DNS cutover, both HTTPS certificates, and GitHub's Enforce HTTPS setting were verified on November 5, 2026. The original Wix website and `yvonneyuanmusic.com` have not been redirected or removed.

This GitHub repository preserves the site's source and existing Git history. The **Publish website** workflow builds and checks the site, then deploys it to GitHub Pages whenever a commit is pushed to `main`. It can also be run manually from the Actions tab.

## Editing and version control

Git records versions of these files locally. GitHub stores the source at https://github.com/yvonneQAQ/yvonne-playground, and GitHub Pages serves the generated website. The previous Sites deployment is retained as an older copy; current updates are published from this GitHub repository.

For a quick update without Codex or Terminal, open a content JSON file on GitHub, click the pencil, edit it, and choose **Commit changes** on `main`. Check the **Publish website** run at https://github.com/yvonneQAQ/yvonne-playground/actions. A successful deployment publishes the rebuilt website; a failed check leaves the last successful publication in place.

For routine content updates, edit `content.json`, `works.json`, or `pages.json`, then run these commands from this directory:

```bash
python3 build.py
python3 scripts/verify_site.py
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

The `git add` example is for an Events update. For other changes, include the content/template files actually edited and their generated `dist/` output. The GitHub remote is named `github`. A push to `main` starts the GitHub Pages publishing workflow.

You can also edit JSON content directly on GitHub and commit it there; the workflow rebuilds HTML from that source automatically. Before working locally again, pull those changes with `git pull --ff-only github main`.

The deployment workflow uses GitHub's built-in token and requires no personal tokens or hosting credentials in the repository. The build supports both the `/yvonne-playground` GitHub project URL and the custom domain root; `actions/configure-pages` supplies the appropriate base path.

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
- `.github/workflows/deploy-pages.yml`: automatic build, link checks, and GitHub Pages deployment.
- `scripts/verify_site.py`: checks generated pages, local files, internal anchors, and production metadata before deployment.
- `.openai/hosting.json`: retained identity for the previous Sites host; GitHub Pages does not use it and it contains no deployment credentials.

Run `python3 build.py` after changing the content or template. The output is a standalone static site in `dist/`; it needs no database, framework, package install, or server-side code. Edit templates and JSON rather than the generated HTML. Styles, JavaScript, and media remain tracked in `dist/`. The build also generates `robots.txt`, `sitemap.xml`, and production canonical URLs.

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

## Hosting configuration and cutover

GitHub repository Settings → Pages must use **GitHub Actions** as the publishing source. Configure `yvonneyuansplayground.com` as the custom domain there before changing DNS. At Namecheap, the apex uses GitHub Pages' four A records and `www` is a CNAME to `yvonneqaq.github.io` (without the repository name). Use the current addresses in GitHub's custom-domain documentation, then verify HTTPS and enable **Enforce HTTPS** once GitHub's certificate is ready.

The previous Sites deployment remains available as an older copy. Domain registration is separate from website hosting. The old Wix domain's permanent redirect and any Wix plan changes are separate follow-up work.
