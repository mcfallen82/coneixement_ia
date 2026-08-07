---
title: Ontologies associatives
category: conceptes
tags:
  - gestio-del-coneixement
  - ontologies
  - representacio-del-coneixement
sources:
  - https://www.w3.org/standards/semanticweb/ontology
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Ontologies associatives

## Definició

Una ontologia associativa és una representació del coneixement que descriu conceptes, entitats i relacions entre ells. En aquest projecte, el terme s’utilitza per descriure una xarxa de coneixement que emergeix de les connexions entre notes.

## Per què és important?

Permet passar d’una col·lecció de documents a una estructura on les relacions també contenen informació.

## Intuïció

Una llista diu quins conceptes existeixen. Una ontologia també diu com es relacionen: un LLM és un tipus de model, el RAG recupera fonts per donar context i el frontmatter descriu una nota.

## Funcionament

Cal identificar entitats, tipus de relació i regles mínimes. Les relacions poden ser jeràrquiques, causals, temporals, de dependència o d’exemple.

## Exemple

[[RAG]] depèn d’un [[LLM]], pot utilitzar [[QMD]] per recuperar informació i necessita [[frontmatter]] per filtrar notes.

## Relacions

- [[wiki]]
- [[zettelkasten]]
- [[second_brain]]
- [[frontmatter]]
- [[RAG]]

## Aplicacions

- mapes de coneixement;
- wikis assistides;
- recuperació semàntica;
- documentació de projectes;
- sistemes d’agents.

## Limitacions i errors habituals

- confondre qualsevol enllaç amb una relació semàntica;
- crear taxonomies massa rígides;
- afegir relacions sense utilitat;
- no distingir entre relació documentada i interpretació.

## Fonts

- [W3C — Ontology and the Semantic Web](https://www.w3.org/standards/semanticweb/ontology).
