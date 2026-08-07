---
title: QMD
node_id: "concept:qmd"
node_type: "concept"
category: conceptes
tags:
  - recuperacio
  - cerca-semantica
  - gestio-del-coneixement
sources:
  - https://github.com/tobi/qmd
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# QMD

## Definició

QMD és una eina local de cerca semàntica per trobar notes i documents relacionats pel significat, no només per coincidència exacta de paraules.

## Per què és important?

Pot facilitar la recuperació de coneixement dins d’una wiki local quan la pregunta utilitza paraules diferents de les que apareixen en la nota.

## Intuïció

Una cerca tradicional pregunta si dues expressions comparteixen paraules. Una cerca semàntica intenta estimar si comparteixen significat.

## Funcionament

El sistema indexa documents, crea representacions vectorials i recupera resultats relacionats amb una consulta. La utilitat final depèn de la qualitat de l’índex, de la segmentació i del model d’embeddings.

## Exemple

Una consulta sobre «com donar informació rellevant a un model» pot recuperar [[context_engineering]] encara que no contingui exactament aquesta frase.

## Relacions

- [[RAG]]
- [[context_engineering]]
- [[second_brain]]
- [[frontmatter]]
- [[LLM]]

## Aplicacions

- cerca local d’Obsidian;
- recuperació per a sistemes RAG;
- exploració de wikis;
- localització de notes relacionades.

## Limitacions i errors habituals

- recuperar resultats semblants però no útils;
- no indexar fitxers nous;
- dependre d’un embedding inadequat;
- confondre semblança semàntica amb veritat;
- no mostrar la font original.

## Fonts

- [QMD — Local semantic search](https://github.com/tobi/qmd).
