---
title: Xarxes neuronals
node_id: "concept:xarxes_neuronals"
node_type: "concept"
category: conceptes
tags:
  - aprenentatge-profund
  - xarxes-neuronals
  - fonaments
sources:
  - https://karpathy.ai/zero-to-hero.html
  - https://www.deeplearningbook.org/
related_concepts:
  - "[[1. Wiki/1.2. conceptes/autodiferenciacio]]"
  - "[[1. Wiki/1.2. conceptes/backpropagation]]"
  - "[[1. Wiki/1.2. conceptes/optimitzacio_i_adam]]"
related_models:
  - "[[1. Wiki/1.3. models/transformer]]"
  - "[[1. Wiki/1.3. models/GPT]]"
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Xarxes neuronals

## Definició

Una xarxa neuronal és una funció amb paràmetres ajustables que transforma unes entrades en una predicció. Les capes internes apliquen combinacions lineals i funcions d’activació per aprendre relacions massa complexes per a una regla fixa.

## Intuïció

Com en un model econòmic amb molts coeficients, els pesos indiquen quant ha d’influir cada dada sobre el resultat. La diferència és que la xarxa aprèn aquests coeficients a partir dels errors de moltes observacions.

## Funcionament simplificat

1. Rep un vector d’entrada.
2. El transforma capa a capa.
3. Calcula una predicció i la compara amb la resposta correcta.
4. Ajusta els pesos amb [[1. Wiki/1.2. conceptes/backpropagation]] i [[1. Wiki/1.2. conceptes/optimitzacio_i_adam]].

## Exemple

En un model de llenguatge, l’entrada són tokens i la sortida és una probabilitat per al token següent. En un model de classificació, la sortida pot ser la probabilitat que un fragment parli d’un risc regulatori.

## Relacions

- [[1. Wiki/1.2. conceptes/embeddings]]
- [[1. Wiki/1.2. conceptes/activacions_i_inicialitzacio]]
- [[1. Wiki/1.2. conceptes/softmax_i_cross_entropy]]
- [[1. Wiki/1.3. models/transformer]]

## Limitacions i errors habituals

Una xarxa neuronal no «entén» automàticament les causes del fenomen. Pot aprendre correlacions espúries, requereix dades representatives i necessita una validació separada de l’entrenament.

## Fonts

- [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) — curs pràctic per construir les peces des de zero.
- [Deep Learning](https://www.deeplearningbook.org/) — referència tècnica general.
