---
title: micrograd
node_id: "concept:micrograd"
node_type: "concept"
category: conceptes
tags:
  - autodiferenciacio
  - aprenentatge-profund
  - python
sources:
  - https://github.com/karpathy/micrograd
related_concepts:
  - "[[1. Wiki/1.2. conceptes/autodiferenciacio]]"
  - "[[1. Wiki/1.2. conceptes/backpropagation]]"
  - "[[1. Wiki/1.2. conceptes/xarxes_neuronals]]"
related_models:
  - "[[1. Wiki/1.3. models/nanoGPT]]"
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# micrograd

## Què és?

micrograd és una biblioteca didàctica molt petita creada per Andrej Karpathy. Implementa l’autodiferenciació inversa sobre un graf d’operacions i permet construir xarxes neuronals senzilles.

## Per què és important?

Mostra les peces que queden amagades dins PyTorch o JAX: valors, operacions, gradients, regla de la cadena i actualització de paràmetres. És una escala pedagògica entre les fórmules i un GPT entrenable.

## Funcionament simplificat

Cada valor conserva les operacions que l’han produït. En demanar `backward()`, el sistema recorre el graf en sentit invers i acumula gradients. Amb aquests gradients es poden actualitzar els pesos d’una xarxa petita.

## Exemple

Una pràctica útil és construir una neurona amb uns quants pesos, calcular una pèrdua sobre exemples simples i observar com canvien els pesos després de cada iteració.

## Relacions

- [[1. Wiki/1.2. conceptes/autodiferenciacio]]
- [[1. Wiki/1.2. conceptes/backpropagation]]
- [[1. Wiki/1.3. models/nanoGPT]]

## Limitacions

No és un framework de producció ni una implementació de LLM. El seu valor és fer visible el mecanisme d’aprenentatge.

## Fonts

- [micrograd](https://github.com/karpathy/micrograd).
