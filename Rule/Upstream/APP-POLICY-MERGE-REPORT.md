# App policy-group consolidation report

One App maps to one rule folder and one Surge policy group. Country/region selection remains in the Surge policy group. Distinct rule formats are preserved.

## Summary table

| App | Alias folders removed | Rule files removed | New rules added to canonical files | Final formats |
|---|---:|---:|---:|---|
| Abema | 1 | 1 | 0 | standard |
| Gemini | 1 | 1 | 0 | standard |
| PChome | 1 | 1 | 0 | standard |
| GlobalScholar | 1 | 1 | 0 | standard |
| BiliBili | 1 | 1 | 2 | resolve, standard |
| iQIYI | 1 | 2 | 22 | resolve, standard |
| Hulu | 2 | 2 | 0 | standard |
| Telegram | 3 | 6 | 0 | resolve, standard |
| Amazon | 1 | 1 | 34 | resolve, standard |
| HBO | 3 | 3 | 5 | standard |
| Cloudflare | 1 | 1 | 0 | resolve, standard |
| Steam | 1 | 1 | 10 | resolve, standard |
| Assassin's Creed Odyssey | 1 | 2 | 0 | resolve, standard |
| Assassin's Creed Origins | 1 | 2 | 0 | resolve, standard |

## Per-App details

### Abema
- Canonical folder: `Abema`
- Alias folders removed: 1; .list files removed: 1
- Alias rule occurrences checked: 29
- New rules added: 0
- Source README/license files archived: 1

### Gemini
- Canonical folder: `Gemini`
- Alias folders removed: 1; .list files removed: 1
- Alias rule occurrences checked: 14
- New rules added: 0
- Source README/license files archived: 1

### PChome
- Canonical folder: `PChome`
- Alias folders removed: 1; .list files removed: 1
- Alias rule occurrences checked: 5
- New rules added: 0
- Source README/license files archived: 1

### GlobalScholar
- Canonical folder: `GlobalScholar`
- Alias folders removed: 1; .list files removed: 1
- Alias rule occurrences checked: 231
- New rules added: 0
- Source README/license files archived: 1

### BiliBili
- Canonical folder: `BiliBili`
- Alias folders removed: 1; .list files removed: 1
- Alias rule occurrences checked: 6
- New rules added: 1 to standard and 1 to Resolve
- Source README/license files archived: 1

### iQIYI
- Canonical folder: `iQIYI`
- Alias folders removed: 1; .list files removed: 2
- Alias rule occurrences checked: 42
- New rules added: 11 to standard and 11 to Resolve
- Source README/license files archived: 1

### Hulu
- Canonical folder: `Hulu`
- Alias folders removed: 2; .list files removed: 2
- Alias rule occurrences checked: 58
- New rules added: 0
- Source README/license files archived: 2

### Telegram
- Canonical folder: `Telegram`
- Alias folders removed: 3; .list files removed: 6
- Alias rule occurrences checked: 20
- New rules added: 0
- Source README/license files archived: 3

### Amazon
- Canonical folder: `Amazon`
- Alias folders removed: 1; .list files removed: 1
- Alias rule occurrences checked: 47
- New rules added: 17 to standard and 17 to Resolve
- Source README/license files archived: 1

### HBO
- Canonical folder: `HBO`
- Alias folders removed: 3; .list files removed: 3
- Alias rule occurrences checked: 56
- New rules added: 5 to standard
- Source README/license files archived: 3

### Cloudflare
- Canonical folder: `Cloudflare`
- Alias folders removed: 1; .list files removed: 1
- Alias rule occurrences checked: 14
- New rules added: 0
- Source README/license files archived: 1

### Steam
- Canonical folder: `Steam`
- Alias folders removed: 1; .list files removed: 1
- Alias rule occurrences checked: 17
- New rules added: 5 to standard and 5 to Resolve
- Source README/license files archived: 1

### Assassin's Creed Odyssey
- Canonical folder: `Assassin'sCreed/Assassin'sCreed-Odyssey`
- Alias folders removed: 1; .list files removed: 2
- Alias rule occurrences checked: 30
- New rules added: 0
- Source README/license files archived: 1

### Assassin's Creed Origins
- Canonical folder: `Assassin'sCreed/Assassin'sCreed-Origins`
- Alias folders removed: 1; .list files removed: 2
- Alias rule occurrences checked: 32
- New rules added: 0
- Source README/license files archived: 1

## Totals

- App groups processed: 14
- Alias folders removed: 19
- Alias .list files removed: 25
- New rule lines added across files/formats: 73
- Unique new App-level rules added (counting Standard/Resolve mirrors once): 39

## Preserved boundaries

- Personal rules were not read or modified.
- This consolidation did not delete any bank/payment or other finance folders. The 14 dedicated bank/payment folders are currently present, and the exact deletion manifest is empty. No category-based keep/delete policy applies; matching domains in other Apps were not deleted.
- Standard and Resolve remain separate files; regional variants are folded into the same App folder.
- Source README/license material from removed alias folders is archived under `SourceMetadata/RegionalVariants`.
- No new author rule sets were fetched.
