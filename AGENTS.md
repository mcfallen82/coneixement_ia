# AGENTS.md - Governanca de la wiki d'aprenentatge d'IA

## 1. Objectiu i abast

Aquest repositori es una wiki d'aprenentatge acumulatiu sobre intel.ligencia artificial, aprenentatge automatic, aprenentatge profund, models generatius, enginyeria de prompts i del context, sistemes de coneixement i automatitzacio. Les finances i l'economia nomes s'hi utilitzen com a exemples d'aplicacio.

No es una wiki financera ni un sistema d'analisi d'empreses.

## 2. Governanca

Aquest es l'unic document principal de governanca. S'ha de llegir abans d'actuar. Quan una skill contradigui aquest document, preval AGENTS.md.

El repositori principal es `main`. Les modificacions es fan en branques `agent/...` i s'integren mitjancant pull request.

## 3. Estructura obligatoria

```text
0. Raw/
1. Wiki/
|-- 1.1. autors/
|-- 1.2. conceptes/
|-- 1.3. models/
`-- 1.4. llibres/
2. Skills/
|-- README.md
`-- <skill>/
    |-- README.md
    `-- <skill>.md
3. Dashboards/
4. Templates/
|-- 90.1. templates_fitxes/
`-- 90.2. docs_support/
index.md
log.md
hot.md
.manifest.json
scripts/wiki_lint.py
graph/
|-- README.md
|-- relation-vocabulary.yaml
`-- relations.json
scripts/graph_scan.py
.github/workflows/wiki-lint.yml
```

- `0. Raw/` conserva fonts originals o copies de treball en una carpeta plana. Els documents Raw es diferencien pel frontmatter, no per subcarpetes.
- `1. Wiki/` conte fitxes permanents d'autors, conceptes, models i llibres o fonts bibliografiques processades.
- `2. Skills/` conte procediments reutilitzables. Cada skill ha de tenir carpeta propia; el `README.md` descriu breument la naturalesa de la skill i `<skill>.md` conserva el procediment complet.
- `3. Dashboards/` conte consultes i vistes.
- `4. Templates/` conte plantilles i documents de suport.
- `scripts/wiki_lint.py` es la validacio executable; no substitueix la revisio humana.

## 4. Contracte de les fitxes

Tota fitxa permanent Markdown dins de `1. Wiki/`, excepte els README, ha de tenir frontmatter YAML amb:

```yaml
---
title: Nom de la fitxa
category: conceptes
tags: []
sources: []
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

`category` ha de coincidir amb la carpeta: `autors`, `conceptes`, `models` o `llibres`. Els models han d'incloure, com a minim, `model_family` i `architecture`. Les fitxes de llibres han d'indicar `node_type: source` i, quan sigui possible, `source_type`, autors, data de publicacio i editor. Les fonts han de ser verificables o s'ha de marcar explicitament que son pendents.

Les fitxes han de comencar per una definicio o identificacio clara i separar fets documentats, interpretacio pedagogica, limitacions i preguntes obertes.

## 4.1. Contracte de les fonts Raw

Tot document Markdown dins de `0. Raw/`, excepte `README.md`, ha de tenir frontmatter YAML amb:

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

`raw_type` descriu la naturalesa documental interna, com ara `reading_plan`, `tutorial`, `research_dossier`, `notes` o `source_copy`. `source_type` descriu el tipus d'origen, com ara `book`, `paper`, `tutorial`, `recerca_web` o `repository_review`. `processing_status` indica el punt del flux: `raw_ingested`, `reviewed`, `processed` o `archived`.

Quan un document Raw es mogui, s'ha d'afegir `previous_path`. Quan una font ja hagi alimentat fitxes permanents, s'ha d'indicar `processed_into`.

## 5. Flux operatiu unic

```text
font -> Raw -> classificacio -> cerca de duplicats
     -> creacio/actualitzacio -> relacions -> index
     -> log + hot + manifest -> wiki_lint -> revisio humana
```

Una operacio d'escriptura nomes es considera completa quan:

1. s'ha conservat la font;
2. s'han creat o actualitzat les fitxes necessaries;
3. s'han actualitzat les fonts i els wikilinks;
4. s'han actualitzat `index.md`, `log.md`, `hot.md` i `.manifest.json` quan el canvi es significatiu;
5. `scripts/wiki_lint.py` retorna `PASS`;
6. s'han revisat manualment les advertencies.

## 6. Regles de seguretat

- No eliminis ni fusionis fitxes sense copia i aprovacio explicita.
- No sobreescriguis fitxes existents sense comparar-les.
- No inventis autors, models, dates, arquitectures ni fonts.
- No converteixis una font en una fitxa nomes perque existeixi al directori Raw.
- No utilitzis `estat`, `autor`, `concepts/`, `entities/` o `references/` en nous continguts.
- Les operacions massives han de comencar amb una validacio en mode nomes lectura.

## 7. Enllacos i Obsidian

Els wikilinks han d'apuntar a fitxers reals o a una destinacio externa explicita. Els dashboards han de funcionar com a Markdown estatic i/o com a guies per executar `scripts/wiki_lint.py` i `scripts/graph_scan.py`; no han de dependre de plugins d'Obsidian com Dataview, Canva, Kanban o equivalents. No es modifica `.obsidian/` automaticament.

## 8. Registre i manifest

Cada canvi estructural o ingesta significativa s'ha d'afegir a `log.md` amb data, operacio, fitxers afectats, resultat i incidencies. `.manifest.json` ha d'indicar la font, tipus, estat i fitxes creades o actualitzades. Una font nomes es `processed` si les seves fitxes resultants estan indicades.

## 9. Validacio obligatoria

Abans de donar una tasca per acabada:

- executa `python scripts/wiki_lint.py`;
- comprova estructura, README, YAML, categories, camps antics, wikilinks, manifest, duplicats i estructura interna de skills;
- tracta els errors com a bloquejants;
- documenta les advertencies i les decisions pendents a l'informe final.

La validacio automatica es reexecuta mitjancant `.github/workflows/wiki-lint.yml`.

## 10. Capa grafica lleugera

La wiki mante Markdown com a font principal i utilitza la carpeta `graph/` com a representacio derivada. Les fitxes permanents de `1. Wiki/` han d'incloure `node_id` estable i `node_type` coherent amb la seva carpeta. Les relacions acceptades es registren a `graph/relations.json`; els wikilinks no tipats nomes son candidats. Abans d'incorporar una relacio cal comprovar-ne la destinacio, el tipus, la procedencia i la confianca.

La validacio inicial s'executa amb:

    python scripts/graph_scan.py --check

No s'introdueix una base de dades grafica ni GraphRAG en aquesta fase. La capa serveix per fer proves reproduibles de nodes, arestes, hubs, components i exportacio JSON.
