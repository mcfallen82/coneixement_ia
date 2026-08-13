---
title: "Graph Engineering Decoded: Two Definitions, One Test"
raw_type: article_note
source_type: article
processing_status: processed
status: processed
created: 2026-08-13
updated: 2026-08-13
author: Eugeniu Ghelbur
publication: The AI Operator
publication_date: 2026-08-11
url: https://theaioperator.io/p/graph-engineering-decoded-two-definitions
sources:
  - https://theaioperator.io/p/graph-engineering-decoded-two-definitions
processed_into:
  - 1. Wiki/1.2. conceptes/graph_engineering.md
  - 1. Wiki/1.1. autors/Ghelbur, Eugeniu.md
---

# Graph Engineering Decoded: Two Definitions, One Test

## Atribucio

Article d'Eugeniu Ghelbur publicat a *The AI Operator* l'11 d'agost de 2026.

## Resum

L'article defensa que el terme *graph engineering* s'esta utilitzant amb dos sentits diferents: el disseny d'un graf de coneixement que representa allo que el sistema sap, i el disseny d'un graf d'agents o eines que representa com es mou el treball dins d'un sistema. La distincio practica no depen de la forma del diagrama, sino del tipus de fallada que es vol corregir.

## Idees principals

- Un graf de coneixement ajuda quan la sortida es incorrecta per informacio absent, obsoleta o mal connectada.
- Un graf d'agents ajuda quan el cami d'execucio es incorrecte, opac o poc recuperable.
- Els dos usos comparteixen nodes i arestes, pero modelen estats diferents: coneixement en repos i treball en moviment.
- El test proposat classifica fallades segons si el problema es la sortida, la repetibilitat de la fallada, el cami que no es pot dibuixar i l'efecte d'augmentar documents o passos.
- Construir el graf equivocat pot produir un sistema mes elaborat que no toca la fallada real.

## Decisio d'integracio

Aporta informacio nova al projecte. La wiki ja contenia fitxes sobre grafs, GraphRAG, Graph of Thoughts i ontologies associatives, pero no separava explicitament l'enginyeria de grafs en dues definicions operatives: graf de coneixement i graf de topologia d'agents.

Accio aplicada:

- creada la fitxa [[1. Wiki/1.2. conceptes/graph_engineering]];
- actualitzada la fitxa d'autor [[1. Wiki/1.1. autors/Ghelbur, Eugeniu]];
- connectada la nova fitxa amb [[1. Wiki/1.2. conceptes/grafs_i_models_de_llenguatge]], [[1. Wiki/1.2. conceptes/GraphRAG]], [[1. Wiki/1.2. conceptes/graph_of_thoughts]], [[1. Wiki/1.2. conceptes/ontologies_associatives]] i [[1. Wiki/1.2. conceptes/context_engineering]].

## Limitacions

La font es un article interpretatiu i pedagogic d'un autor tecnic, no un paper academic ni una especificacio formal. La conclusio s'ha integrat com a marc conceptual i criteri practic, no com a estandard consolidat.
