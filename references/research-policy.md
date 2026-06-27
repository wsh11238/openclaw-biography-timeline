# Research Policy

Use this policy when researching people for a timeline webpage.

## Default Source Priority

When the user does not specify sources, gather sources in this order:

1. Government websites, public institution pages, official association pages, university profiles, museum/archive pages, official personal sites, publisher/award databases, and other direct institutional introductions.
2. Wikipedia and Baidu Baike pages for the subject, including their infoboxes, chronology, works lists, reference sections, and external links.
3. Other high-quality encyclopedia or reference databases, such as Encyclopaedia Britannica, library authority records, ORCID, WorldCat, IMDb, Discogs, MusicBrainz, Wikidata, and specialist databases.
4. Reputable media reports, interviews, book reviews, festival/award announcements, and trade publications.
5. Secondary blogs, forums, fan pages, and reposts only as leads or for non-critical context after verification.

Use Wikipedia and Baidu Baike as preferred overview and discovery sources, especially for Chinese-language output, name disambiguation, major chronology, works lists, and source leads. For sensitive claims, disputed events, awards, offices, legal matters, medical/private details, or exact dates, verify against government/institutional, official, primary, scholarly, or reputable-media sources before presenting the claim as settled.

## Source Tiers

- `official`: official personal site, institutional biography, company/organization profile, government record, court filing, archive catalog, publisher or award database.
- `government`: government website, official public agency profile, public archive, public cultural institution, or official gazette record.
- `primary`: interview transcript, speech, memoir, verified social post, publication, patent, filings, original dataset, scanned archival document.
- `scholarly`: peer-reviewed paper, academic press book, university archive, library authority record, thesis repository with stable metadata.
- `reputable-media`: established newspaper, magazine, wire service, public broadcaster, specialist trade publication with editorial standards.
- `encyclopedia`: Wikipedia, Baidu Baike, Encyclopaedia Britannica, and comparable edited encyclopedia pages.
- `reference`: library authority pages, IMDb/Discogs/MusicBrainz/ORCID/WorldCat/Wikidata-style databases, high-quality chronology pages.
- `secondary`: blogs, fan sites, podcasts, newsletters, forums, social reposts, unsourced listicles. Use only for leads or low-stakes color after verification elsewhere.

Prefer the highest available tier for each claim. Treat government, official, primary, and scholarly sources as strongest for factual verification. Treat Wikipedia and Baidu Baike as high-priority overview/reference sources, not as sole proof for sensitive or disputed claims.

## Verification Rules

- Cross-check major events with at least two independent sources when practical.
- For each subject, try to include at least one Wikipedia or Baidu Baike source when available, plus at least one government/official/institutional source when available.
- For birth/death dates, offices, legal proceedings, awards, education, and publication/release dates, prefer official or archival records.
- Preserve exact dates when supported. If sources disagree, use the most authoritative date and add an uncertainty note.
- Distinguish event date from publication date. News coverage after an event is not automatically the event date.
- Do not cite search result snippets as sources.
- Do not use AI-generated pages as sources.
- If Wikipedia and Baidu Baike disagree, record the disagreement in `uncertainty_notes` and resolve with a stronger source tier before using the fact in a major event.

## Confidence Labels

- `high`: direct official/primary support, or multiple independent reliable sources agree.
- `medium`: reliable secondary/reference support, but no direct primary source found.
- `low`: plausible but thinly sourced; include only if relevant and label clearly.
- `disputed`: credible sources conflict, or the subject/record challenges the claim.

## Living People and Sensitive Claims

- Avoid private addresses, personal contact details, family details, health claims, and relationship claims unless they are central, public, and reliably sourced.
- For allegations, scandals, criminal/civil cases, political disputes, or employment controversies, use neutral wording and cite primary legal/official records or reputable media.
- Include outcome/status when available, such as dismissed, settled, acquitted, convicted, resigned, denied, under investigation, or unresolved.
- Do not present allegations as established facts.
- Treat user requests for "黑历史", "宿敌", "权力", or "财富" as sensitive by default. Use neutral labels such as "低谷、争议与失败记录", "争鸣对象", "制度位置", and "商业可见度" unless reliable sources clearly justify stronger wording.
- Do not estimate a living person's net worth, private income, or wealth trajectory without reliable financial disclosures or reputable reporting. Use sourced proxies such as publications, adaptations, awards, offices, and public commercial visibility.
- Relationship graphs may include rivals or opponents only when credible sources document sustained rivalry or public opposition; otherwise use collaborators, critics, institutions, mentors, family collaborators, or public discourse objects.

## Citation Requirements

- Every event needs at least one `source_ids` entry.
- Every major event should have the best available source and preferably two sources.
- For biographies with both encyclopedic and official sources, cite both on identity/birth/role overview events when practical.
- Use stable URLs when possible. Include access dates for web sources.
- When a source is paywalled but metadata is visible, say so in source notes rather than inventing unavailable details.
- Keep direct quotes short and only when they materially clarify wording.

## Page Quality Checklist

- The person is unambiguously identified.
- The timeline is chronological and covers early life, formation, major work/roles, turning points, controversies if relevant, and late/current status.
- The "大事记" section contains only the most consequential events.
- Uncertain or conflicting dates are visible in notes.
- The bibliography is complete enough for a reader to audit the page.
- The final HTML and sources markdown are generated in the current workspace.
