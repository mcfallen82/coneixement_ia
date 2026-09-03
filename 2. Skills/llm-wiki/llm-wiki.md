# llm-wiki

## Finalitat

Definir l'arquitectura i els principis compartits per mantenir `coneixement_ia` com una wiki pública, traçable i independent de l'eina local utilitzada per editar-la.

## Arquitectura

La wiki segueix tres capes conceptuals:

1. **Fonts externes:** articles, papers, llibres, vídeos, documentació, repositoris i altres materials verificables. Es referencien mitjançant URLs o referències bibliogràfiques; les còpies locals no formen part del repositori públic.
2. **Wiki:** coneixement destil·lat a `1. Wiki/`, amb fitxes d'autors, conceptes, models i llibres quan correspongui.
3. **Governança i esquema:** `AGENTS.md`, plantilles, skills, scripts i fitxers de control que defineixen com es crea, valida i manté el coneixement.

## Principis

- Compila coneixement: actualitza fitxes abans de crear-ne de noves.
- Conserva la procedència: tota afirmació important ha de tenir una font verificable.
- Connecta les pàgines: els wikilinks i les relacions converteixen les fitxes en una xarxa.
- Mantén una sola font de veritat: no dupliquis conceptes en carpetes diferents.
- Explica primer la intuïció i després la part tècnica.
- Separa fets documentats, interpretació i preguntes obertes.
- No facis dependre el projecte d'un editor, plugin o gestor de coneixement concret.

## Categories

- `autors`: persones, investigadors i divulgadors;
- `conceptes`: idees, tècniques, processos i fonaments;
- `models`: arquitectures, models entrenats i famílies de models;
- `llibres`: obres estables que mereixen una fitxa pròpia.

Les fonts que no necessiten una fitxa pròpia es conserven com a referències al camp `sources`, a les seccions de fonts i, quan correspongui, al manifest.

## Fitxa mínima

~~~yaml
---
title: Nom
category: conceptes
tags: []
sources: []
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
~~~

Les relacions addicionals poden utilitzar `related_concepts`, `related_models`, `authors` i `related_authors`. Els noms han de coincidir amb fitxes reals.

## Fitxers de control

- `index.md`: mapa de la wiki.
- `log.md`: registre cronològic.
- `hot.md`: resum curt de l'activitat recent.
- `.manifest.json`: traçabilitat de fonts i operacions.

Qualsevol skill que escrigui fitxers ha d'actualitzar aquests elements quan el canvi sigui significatiu.

## Ordre de treball

Font externa → classificació → comprovació de duplicats → creació o actualització → enllaços → índex → registre → auditoria.
