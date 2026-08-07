---
title: Activacions i inicialització
category: conceptes
tags:
  - aprenentatge-profund
  - activacions
  - inicialitzacio
sources:
  - https://proceedings.mlr.press/v9/glorot10a.html
related_concepts:
  - "[[1. Wiki/1.2. conceptes/backpropagation]]"
  - "[[1. Wiki/1.2. conceptes/batch_normalization]]"
related_models:
  - "[[1. Wiki/1.3. models/transformer]]"
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Activacions i inicialització

## Definició

Les funcions d’activació introdueixen no-linealitat en una xarxa. La inicialització defineix els valors dels pesos abans de l’entrenament.

## Per què són importants?

Sense no-linealitat, moltes capes lineals equivaldrien a una sola. Amb una mala inicialització, les activacions o els gradients poden desaparèixer o créixer descontroladament abans que el model aprengui.

## Intuïció

La inicialització és com fixar les condicions inicials d’un procés iteratiu: si parteixes d’un punt massa extrem, la informació es degrada a cada etapa. Les activacions decideixen quina part del senyal passa a la capa següent.

## Exemple

ReLU i variants són habituals en MLPs. En Transformers moderns, la combinació d’activacions, inicialització, connexions residuals i normalització manté l’entrenament estable.

## Relacions

- [[1. Wiki/1.2. conceptes/batch_normalization]]
- [[1. Wiki/1.2. conceptes/backpropagation]]
- [[1. Wiki/1.3. models/transformer]]

## Limitacions i errors habituals

Cap funció d’activació és universalment millor. Cal observar activacions, gradients i mètriques de validació, no només confiar en una recepta.

## Fonts

- [Understanding the difficulty of training deep feedforward neural networks](https://proceedings.mlr.press/v9/glorot10a.html).
