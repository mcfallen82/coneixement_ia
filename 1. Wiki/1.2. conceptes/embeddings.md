---
title: Embeddings
node_id: "concept:embeddings"
node_type: "concept"
category: conceptes
tags:
  - representacions-vectorials
  - aprenentatge-profund
  - recuperacio
sources:
  - https://karpathy.ai/zero-to-hero.html
  - https://papers.nips.cc/paper_files/paper/2025/file/19909c36f51abc4856b4560aff3d36d6-Paper-Conference.pdf
related_concepts:
  - "[[1. Wiki/1.2. conceptes/tokenitzacio_i_bpe]]"
  - "[[1. Wiki/1.2. conceptes/attention]]"
  - "[[1. Wiki/1.2. conceptes/RAG]]"
related_models:
  - "[[1. Wiki/1.3. models/transformer]]"
  - "[[1. Wiki/1.3. models/GPT]]"
  - "[[1. Wiki/1.3. models/A-MEM]]"
status: reviewed
created: 2026-08-07
updated: 2026-09-25
---

# Embeddings

## Definició

Un *embedding* és una representació numèrica d’un token, una frase, un document o un altre objecte, situada en un espai vectorial on la proximitat pot reflectir relacions apreses.

## Intuïció

És com resumir un document en moltes coordenades en lloc d’una sola etiqueta. Documents amb patrons semblants tendeixen a ocupar zones properes, tot i que cada coordenada individual no acostuma a tenir una interpretació simple.

## Funcionament simplificat

En un LLM, cada token rep un vector inicial que s’actualitza a través de les capes. En recuperació documental, un model especialitzat genera vectors per a consultes i fragments; després es busquen els vectors més semblants.

## Exemple

Un sistema [[RAG]] pot trobar fragments sobre «flux de caixa lliure» encara que la pregunta utilitzi «cash flow disponible», perquè compara representacions semàntiques i no només paraules exactes.

## Limitacions i errors habituals

La proximitat vectorial no garanteix rellevància ni exactitud. Cal combinar-la amb metadades, filtres, reordenació i cites de la font original.

## Relació amb A-MEM

[[1. Wiki/1.3. models/A-MEM]] utilitza vectors de les notes enriquides per seleccionar records candidats; després un LLM proposa els enllaços. Recuperar per semblança i validar una connexió conceptual són operacions diferents.

## Fonts

- [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html).
- [Xu i col·laboradors — A-Mem: Agentic Memory for LLM Agents](https://papers.nips.cc/paper_files/paper/2025/file/19909c36f51abc4856b4560aff3d36d6-Paper-Conference.pdf), NeurIPS 2025.
