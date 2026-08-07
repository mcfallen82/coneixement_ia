---
title: Softmax i entropia creuada
category: conceptes
tags:
  - aprenentatge-profund
  - probabilitats
  - classificacio
sources:
  - https://cs231n.github.io/linear-classify/
related_concepts:
  - "[[1. Wiki/1.2. conceptes/backpropagation]]"
  - "[[1. Wiki/1.2. conceptes/tokenitzacio_i_bpe]]"
related_models:
  - "[[1. Wiki/1.3. models/GPT]]"
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Softmax i entropia creuada

## Definició

*Softmax* converteix puntuacions internes (*logits*) en una distribució de probabilitats. L’entropia creuada mesura fins a quin punt aquesta distribució s’allunya de la resposta correcta.

## Intuïció

Si un model ha de triar el token següent, els logits són preferències sense calibrar. Softmax les converteix en probabilitats que sumen 1. L’entropia creuada penalitza especialment donar poca probabilitat al token correcte.

## Funcionament simplificat

Per a cada classe o token:

1. el model calcula un logit;
2. softmax els normalitza en probabilitats;
3. la pèrdua compara la probabilitat assignada a la resposta correcta;
4. la [[1. Wiki/1.2. conceptes/backpropagation]] ajusta els pesos.

## Exemple

Davant «El marge brut va augmentar un», el model pot assignar probabilitats als possibles tokens següents. Si el text correcte és «3%», la pèrdua augmenta quan aquest token té probabilitat baixa.

## Limitacions i errors habituals

Una probabilitat alta no és una prova de veritat factual. La temperatura modifica el mostreig durant la generació; no converteix per si sola el model en més exacte.

## Fonts

- [Linear Classification and Softmax](https://cs231n.github.io/linear-classify/) — material docent de Stanford.
