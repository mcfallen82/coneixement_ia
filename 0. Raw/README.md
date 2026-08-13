# 0. Raw

Fonts originals i materials de treball de la wiki d'aprenentatge d'IA.

## Criteri

`0. Raw/` es manté com una carpeta plana: els documents viuen directament en aquesta carpeta i es diferencien pel frontmatter, no per subcarpetes.

Cada document Raw, excepte aquest README, ha d'incloure com a mínim:

```yaml
---
title: Nom de la font
raw_type: research_dossier
source_type: recerca_web
processing_status: raw_ingested
status: raw_ingested
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

## Camps principals

- `raw_type`: naturalesa documental interna (`reading_plan`, `tutorial`, `research_dossier`, `notes`, `source_copy`).
- `source_type`: tipus de font o origen (`book`, `paper`, `tutorial`, `recerca_web`, `repository_review`, etc.).
- `processing_status`: estat del flux (`raw_ingested`, `reviewed`, `processed`, `archived`).
- `previous_path`: ruta anterior quan el document s'ha mogut dins el projecte.
- `processed_into`: fitxes o carpetes permanents que han rebut coneixement d'aquesta font.

## Flux

1. Incorpora la font a `0. Raw/`.
2. Completa el frontmatter abans de processar-la.
3. Processa-la amb [[2. Skills/wiki-ingest/README|wiki-ingest]] o [[2. Skills/wiki-research/README|wiki-research]].
4. Crea o actualitza fitxes a `1. Wiki/`.
5. Registra la procedència a `.manifest.json` i `log.md`.
6. Executa `python scripts/wiki_lint.py`.

La font original no s'ha de substituir per una síntesi. Les interpretacions s'han de distingir dels fets documentats.
