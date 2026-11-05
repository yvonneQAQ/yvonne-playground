# Yvonne Yuan website migration preview

This is a code-maintained reconstruction of the owner's Wix portfolio, with the revised technical About profile and Events archive. It contains 25 content pages and 7 redirects for unused Wix template/blank routes. It is deployed as an owner-private preview. The original domain, DNS, Wix plan, and public Wix content have not been changed.

## Files

- `content.json`: homepage text, event entries, contact information, and links.
- `works.json`: the contemporary music, multimedia, and film/dance catalogue.
- `pages.json`: editable work descriptions, credits, poems, media URLs, and old-route redirects.
- `asset-manifest.json`: local static files with original source URLs and sizes.
- `homepage.template.html`, `about.template.html`, `works.template.html`, and `work.template.html`: page structures.
- `navigation.template.html` and `footer.template.html`: shared navigation and footer.
- `dist/styles.css`: desktop and mobile layout.
- `dist/site.js`: mobile menu behavior.
- `dist/assets/`: locally stored photos, score images, score PDF, resume, audio recording, and compressed film reel. Third-party YouTube, Vimeo, and Bandcamp players remain on those services.
- `.openai/hosting.json`: private preview Site identity and static directory.

Run `python3 build.py` after changing the content or template. The output is a standalone static site in `dist/`; it needs no database, framework, package install, or server-side code.

## Current migration boundary

The homepage, About page, Events, Contact, Works catalogue, all authored published work/poetry pages found in the Wix sitemap, and responsive navigation are implemented. Audio Tools links to the owner's GitHub. The category links jump to the corresponding section of Works.

Existing authored URL paths are retained, including older Field Poetry and Typist variants, the film reel, text scores, and the family recording. The unused `/poetry` template and its three placeholder detail pages redirect to `/mypoetry/`; `/blank-2`, `/blank-3`, and `/s-projects-basic` redirect to Works. Original public source snapshots and original-size assets are backed up outside the deployed project in `../../tmp/wix-migration-2026-11-04/`.

There are no runtime links, images, audio, video, or iframe dependencies on Wix, Wix Static, filesusr, or Parastorage. External music/video platforms and the original Google Drive patch/documentation link remain external. The 53 MB original film reel is preserved in the source backup; the website serves a 720p H.264/AAC copy (about 12 MB) with playback controls and no autoplay.

The owner confirmed two corrections during migration: The World Is My Shelter is performed by guitarist Klondike Steadman; 10000 Waves is for 28 performers. The incorrect letter-to-guitar link is replaced by `/i-wrote-you-a-letter/`, using the owner's supplied YouTube recording `APUgi03JEpY`. The owner changed that video's visibility to Public; this workflow did not alter YouTube account settings.

Works that had no detail page on the original list remain text-only entries. New material has not been invented for those works. The existing 22-event archive is unchanged by this migration.

The owner confirmed that Evil Kid’s Monologue has no video or work description available; it remains a title-only entry in Multimedia. The other five Multimedia works have independent pages. Memory includes its performance video, Bandcamp recording, local photo, and the original Google Drive Max patch/documentation link. Recording fallback links use canonical platform URLs, and Memory's patch link follows the description.

## Source content to review later

- The Typist detail page says January 19, 2025; the homepage event says January 18. Original wording is retained pending the owner's correction.
- Memory's detail page says June 1, 2023; the homepage MAT event says June 9. These may refer to different events; neither was silently changed.
- Film/dance project years follow the original page. IMDb lists Sound of Fire as a 2025 release and A Mermaid in a Summer's Night as a 2024 release; the portfolio's existing creation/project years (2024 and 2021) are retained. Sound of Fire's title now follows IMDb. The additional festival events researched separately have not been added.

## Film links

The owner supplied IMDb profile `nm14342387`. Its three Composer credits were verified: Gu Shi `tt44933953`, Sound of Fire `tt38525789`, and A Mermaid in a Summer's Night `tt24510892`. Film titles link to their IMDb pages, with the existing Mermaid trailer retained as a secondary link. Mark and Time to Dream retain their original dance/project links. Film and Dance also links to the full IMDb profile.

The visual direction intentionally follows the current site: a white background, purple two-line title, widely spaced left navigation, a large performance photo, and the existing event archive. Content is copied from the owner's public website for this first comparison, including existing date wording and spelling.

## Before domain cutover

1. Review the migrated portfolio and resolve any source-content date conflicts.
2. Select public hosting that supports the existing custom domain and remove preview-only noindex metadata when appropriate.
3. Recheck third-party media, downloads, and old URL paths on that host.
4. Point the domain to the new host and verify it before changing the Wix website plan. Domain registration is separate from website hosting.
