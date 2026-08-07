# llm-wiki

## Arquitectura

La wiki segueix tres capes:

1. **Raw:** fonts originals i materials de treball a 0. Raw/.
2. **Wiki:** coneixement destil·lat a 1. Wiki/, amb fitxes d’autors, conceptes i models.
3. **Esquema:** AGENTS.md, plantilles i skills que defineixen com es crea i es manté el coneixement.

## Principis

- Compila coneixement: actualitza fitxes abans de crear-ne de noves.
- Conserva la procedència: tota afirmació important ha de tenir una font.
- Connecta les pàgines: els wikilinks converteixen les fitxes en una xarxa.
- Mantén una sola font de veritat: no dupliquis conceptes en carpetes diferents.
- Explica primer la intuïció i després la part tècnica.
- Separa fets documentats, interpretació i preguntes obertes.

## Categories

- autors: persones, investigadors i divulgadors;
- conceptes: idees, tècniques, processos i fonaments;
- models: arquitectures, models entrenats i famílies de models.

Les fonts, lectures i dades auxiliars es mantenen a 0. Raw/, no es converteixen automàticament en fitxes.

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

Les relacions addicionals poden utilitzar related_concepts, related_models, authors i related_authors. Els noms han de coincidir amb fitxes reals.

## Fitxers de control

- index.md: mapa de la wiki.
- log.md: registre cronològic.
- hot.md: resum curt de l’activitat recent.
- .manifest.json: traçabilitat de fonts i operacions.

Qualsevol skill que escrigui fitxers ha d’actualitzar aquests elements quan el canvi sigui significatiu.

## Ordre de treball

Font → classificació → comprovació de duplicats → creació o actualització → enllaços → índex → registre → auditoria. 
