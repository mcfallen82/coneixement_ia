---
title: Mecanisme d'atenció
category: conceptes
tags:
  - transformer
  - attention
  - models-de-llenguatge
sources:
  - https://arxiv.org/abs/1706.03762
related_concepts:
  - "[[1. Wiki/1.2. conceptes/embeddings]]"
  - "[[1. Wiki/1.2. conceptes/tokenitzacio_i_bpe]]"
related_models:
  - "[[1. Wiki/1.3. models/transformer]]"
  - "[[1. Wiki/1.3. models/GPT]]"
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Mecanisme d’atenció (*attention*)

## Definició

L’atenció permet que cada token ponderi quins altres tokens de la seqüència són més rellevants per actualitzar la seva representació.

## Intuïció

Quan llegeixes una frase, una paraula ambigua es resol mirant altres paraules concretes, encara que siguin llunyanes. L’atenció construeix aquesta consulta de rellevància de manera aprenent.

## Funcionament simplificat

Cada token produeix vectors de consulta (*query*), clau (*key*) i valor (*value*). Les similituds entre consultes i claus generen pesos; la capa combina els valors segons aquests pesos. La multiatenció fa aquest procés en diversos espais alhora.

## Exemple

En «la companyia va tancar la planta perquè era deficitària», l’atenció pot connectar «era» amb «planta» i amb «deficitària» per construir una representació contextual.

## Limitacions i errors habituals

Els pesos d’atenció no són una explicació completa del raonament del model. A més, el cost de l’atenció estàndard creix ràpidament amb la longitud de la seqüència.

## Fonts

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762).
