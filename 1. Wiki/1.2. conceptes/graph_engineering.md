---
title: Graph engineering
node_id: "concept:graph_engineering"
node_type: "concept"
category: conceptes
tags:
  - grafs
  - agents
  - GraphRAG
  - sistemes-de-coneixement
  - orquestracio
sources:
  - https://theaioperator.io/p/graph-engineering-decoded-two-definitions
related_concepts:
  - "[[grafs_i_models_de_llenguatge]]"
  - "[[GraphRAG]]"
  - "[[graph_of_thoughts]]"
  - "[[ontologies_associatives]]"
  - "[[context_engineering]]"
related_models: []
status: reviewed
created: 2026-08-13
updated: 2026-08-13
---

# Graph engineering

## Definicio

*Graph engineering* es el disseny deliberat de l'estructura de graf de la qual depen un sistema amb models de llenguatge. Segons Eugeniu Ghelbur, el terme s'esta utilitzant amb dos sentits diferents: un graf de coneixement que modela allo que el sistema sap, i un graf de topologia d'agents que modela com es mou el treball.

## Fets documentats

Ghelbur descriu dues definicions operatives:

- **Graf de coneixement:** nodes com persones, documents, decisions, projectes o conceptes; arestes com relacions tipades entre aquests elements.
- **Graf d'agents o topologia:** nodes com agents, eines, avaluadors o passos d'aprovacio; arestes com rutes, transicions, comprovacions i regles de retry.

La distincio central es el tipus de fallada:

- si la resposta es incorrecta per informacio absent o mal connectada, el problema apunta al graf de coneixement;
- si el sistema segueix un cami incorrecte, variable o no auditable, el problema apunta a la topologia d'agents.

## Interpretacio pedagogica

La idea ajuda a evitar una confusio recurrent en projectes amb LLM: dibuixar nodes i arestes no diu encara quin problema s'esta resolent. Un graf pot fer el coneixement mes caminable, o pot fer el flux de treball mes controlable. S'assemblen visualment, pero tenen funcions diferents.

En aquesta wiki, el graf de coneixement es representa sobretot amb frontmatter, wikilinks i relacions tipades. La topologia d'agents seria una capa diferent: passos, eines, condicions, rutes i punts de validacio.

## Relacio amb altres conceptes

- [[grafs_i_models_de_llenguatge]] descriu el mapa general d'usos dels grafs en sistemes amb LLM.
- [[GraphRAG]] es un consumidor possible d'un graf de coneixement.
- [[graph_of_thoughts]] modela passos de raonament, i per tant queda mes a prop de la dimensio de topologia o proces.
- [[ontologies_associatives]] aporta l'esquema conceptual per convertir notes i fonts en relacions significatives.
- [[context_engineering]] es relaciona amb decidir quina informacio o estat arriba al model.

## Limitacions

La distincio no implica que un sistema madur nomes necessiti un tipus de graf. Molts sistemes poden acabar necessitant coneixement estructurat i topologia d'agents. La recomanacio practica es construir primer el costat on apareixen les fallades reals.

## Preguntes obertes

- Com s'hauria de representar una topologia d'agents dins d'una wiki Markdown sense convertir-la en un motor de workflows?
- Quins camps de frontmatter serien suficients per descriure transicions, retries i punts d'avaluacio?
- Quan una relacio de coneixement passa a ser tambe una regla operativa?

## Fonts

- [Graph Engineering Decoded: Two Definitions, One Test](https://theaioperator.io/p/graph-engineering-decoded-two-definitions), Eugeniu Ghelbur, *The AI Operator*, 2026-08-11.
