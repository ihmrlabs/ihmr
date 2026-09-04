# R2 bucket layout

Bucket: **`ihmr`**

The bucket mirrors this repository folder for folder, and keeps every version. A published
version may already have been cited, so a path that once resolved has to keep resolving.

```text
ihmr/
├── corpus/                          mirrors the repository
│   ├── research/
│   │   └── IHMR-RSCH-001-state-of-indias-healthcare/
│   │       ├── manifest.json        what exists, and which version is current
│   │       ├── v1/
│   │       │   ├── IHMR-RSCH-001-state-of-indias-healthcare-v1.md
│   │       │   ├── IHMR-RSCH-001-state-of-indias-healthcare-v1.pdf
│   │       │   └── visualisations/
│   │       └── v2/
│   ├── essays/
│   ├── questions/
│   ├── rfcs/
│   ├── decisions/
│   ├── experiments/
│   ├── sources/
│   ├── updates/
│   ├── architecture/
│   ├── schema/
│   └── llms.txt
│
├── revisions/                       immutable snapshots, keyed by commit
│   └── <commit-sha>/
│       ├── research/
│       └── essays/
│
├── renderings/                      pre-rendered documents, written by the site
│   └── <document-id>/<commit-sha>.json
│
├── datasets/                        from ihmr-engine
│   └── <dataset-id>/
│
└── last-sync.json                   which commit the bucket currently holds
```

## Why three copies of the same content

They answer different questions.

**`corpus/`** is the current state. The site reads this to render pages.

**`revisions/<sha>/`** is what the repository looked like at one commit. This is what makes a
citation to a revision resolve years later, and what lets a comment be shown against the text
its author actually read.

**`renderings/`** is parsed and rendered output, written by the site rather than by the sync.
Serving these means a document read never touches the database in Mumbai.

## Never delete from `corpus/`

The sync uses `copy`, not `sync`, so nothing is removed. Deleting a published path would break
citations, DOI landing pages, and every comment anchored to it.

If something genuinely must be withdrawn, it is done deliberately and recorded, not by a
pipeline.

## Secrets this needs

| Secret | What it is |
|:--|:--|
| `R2_ACCOUNT_ID` | Cloudflare account id |
| `R2_ACCESS_KEY_ID` | R2 API token key |
| `R2_SECRET_ACCESS_KEY` | R2 API token secret |
| `INGEST_WEBHOOK_URL` | Optional. Tells the site new content has landed |
| `INGEST_WEBHOOK_TOKEN` | Optional. Bearer token for the above |

The R2 token needs object read and write on the `ihmr` bucket only. Nothing else.
