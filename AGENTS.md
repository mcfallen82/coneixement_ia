# AGENTS.md — Governança de la wiki d’aprenentatge d’IA

## 1. Objectiu i abast

Aquest repositori és una wiki d’aprenentatge acumulatiu sobre intel·ligència artificial, aprenentatge automàtic, aprenentatge profund, models generatius, enginyeria de prompts i del context, sistemes de coneixement i automatització. Les finances i l’economia només s’hi utilitzen com a exemples d’aplicació.

No és una wiki financera ni un sistema d’anàlisi d’empreses.

## 2. Governança

Aquest és l’únic document principal de governança. S’ha de llegir abans d’actuar. Quan una skill contradigui aquest document, preval AGENTS.md.

La branca de treball actual és `agent/reorganitza-wiki-llm`. Les modificacions d’aquesta tasca no han d’afectar `main`.

## 3. Estructura obligatòria

```text
0. Raw/
├── 0.1. llibres/
└── 0.2./
1. Wiki/
├── 1.1. autors/
├── 1.2. conceptes/
└── 1.3. models/
2. Skills/
3. Dashboards/
4. Templates/
├── 90.1. templates_fitxes/
└── 90.2. docs_support/
index.md
log.md
hot.md
.manifest.json
scripts/wiki_lint.py
.github/workflows/wiki-lint.yml
```

- `0. Raw/` conserva fonts originals o còpies de treball.
- `1. Wiki/` conté fitxes permanents d’autors, conceptes i models.
- `2. Skills/` conté procediments reutilitzables.
- `3. Dashboards/` conté consultes i vistes.
- `4. Templates/` conté plantilles i documents de suport.
- `scripts/wiki_lint.py` és la validació executable; no substitueix la revisió humana.

## 4. Contracte de les fitxes

Tota fitxa permanent Markdown, excepte els README, ha de tenir frontmatter YAML amb:

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

`category` ha de coincidir amb la carpeta: `autors`, `conceptes` o `models`. Els models han d’incloure, com a mínim, `model_family` i `architecture`. Les fonts han de ser verificables o s’ha de marcar explícitament que són pendents.

Les fitxes han de començar per una definició o identificació clara i separar fets documentats, interpretació pedagògica, limitacions i preguntes obertes.

## 5. Flux operatiu únic

```text
font → Raw → classificació → cerca de duplicats
     → creació/actualització → relacions → índex
     → log + hot + manifest → wiki_lint → revisió humana
```

Una operació d’escriptura només es considera completa quan:

1. s’ha conservat la font;
2. s’han creat o actualitzat les fitxes necessàries;
3. s’han actualitzat les fonts i els wikilinks;
4. s’han actualitzat `index.md`, `log.md`, `hot.md` i `.manifest.json` quan el canvi és significatiu;
5. `scripts/wiki_lint.py` retorna `PASS`;
6. s’han revisat manualment les advertències.

## 6. Regles de seguretat

- No eliminis ni fusionis fitxes sense còpia i aprovació explícita.
- No sobreescriguis fitxes existents sense comparar-les.
- No inventis autors, models, dates, arquitectures ni fonts.
- No converteixis una font en una fitxa només perquè existeixi al directori Raw.
- No utilitzis `estat`, `autor`, `concepts/`, `entities/` o `references/` en nous continguts.
- Les operacions massives han de començar amb una validació en mode només lectura.

## 7. Enllaços i Obsidian

Els wikilinks han d’apuntar a fitxers reals o a una destinació externa explícita. Les consultes Dataview han d’utilitzar les rutes actuals i els camps `title`, `category`, `sources`, `status` i `updated`. No es modifica `.obsidian/` automàticament.

## 8. Registre i manifest

Cada canvi estructural o ingesta significativa s’ha d’afegir a `log.md` amb data, operació, fitxers afectats, resultat i incidències. `.manifest.json` ha d’indicar la font, tipus, estat i fitxes creades o actualitzades. Una font només és `processed` si les seves fitxes resultants estan indicades.

## 9. Validació obligatòria

Abans de donar una tasca per acabada:

- executa `python scripts/wiki_lint.py`;
- comprova estructura, README, YAML, categories, camps antics, wikilinks, manifest i duplicats;
- tracta els errors com a bloquejants;
- documenta les advertències i les decisions pendents a l’informe final.

La validació automàtica es reexecuta mitjançant `.github/workflows/wiki-lint.yml`.
