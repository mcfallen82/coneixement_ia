---
title: Retropropagació
node_id: "concept:backpropagation"
node_type: "concept"
category: conceptes
tags:
  - aprenentatge-profund
  - gradients
  - entrenament
sources:
  - https://karpathy.ai/zero-to-hero.html
related_concepts:
  - "[[1. Wiki/1.2. conceptes/autodiferenciacio]]"
  - "[[1. Wiki/1.2. conceptes/softmax_i_cross_entropy]]"
  - "[[1. Wiki/1.2. conceptes/optimitzacio_i_adam]]"
related_models:
  - "[[1. Wiki/1.3. models/GPT]]"
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Retropropagació (*backpropagation*)

## Definició

La retropropagació calcula el gradient de la pèrdua respecte de cada paràmetre d’una xarxa neuronal, propagant l’error des de la sortida cap a les capes anteriors.

## Per què és important?

Fa viable entrenar xarxes profundes. Sense aquest mecanisme, ajustar milions o milers de milions de paràmetres seria inviable.

## Intuïció

Si una previsió és errònia, la retropropagació reparteix la responsabilitat entre totes les decisions internes que hi han contribuït. No assigna una culpa arbitrària: aplica la regla de la cadena per mesurar-ne la contribució local.

## Funcionament simplificat

1. Es calcula una predicció.
2. Una funció de pèrdua en mesura l’error.
3. El gradient recorre el graf d’operacions en sentit invers.
4. Un optimitzador modifica els pesos.

## Exemple

En un model que prediu el següent token, l’error de predir «benefici» quan el text correcte diu «ingrés» es distribueix cap als embeddings, capes d’atenció i capes MLP que han produït aquella probabilitat.

## Limitacions i errors habituals

No s’ha de confondre amb l’actualització de pesos: la retropropagació calcula gradients; [[1. Wiki/1.2. conceptes/optimitzacio_i_adam]] decideix com usar-los. També pot patir gradients que desapareixen o exploten.

## Fonts

- [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html).
