---
title: Entrenament, validació i sobreajustament
node_id: "concept:entrenament_validacio_i_overfitting"
node_type: "concept"
category: conceptes
tags:
  - aprenentatge-automatic
  - validacio
  - overfitting
sources:
  - https://karpathy.ai/zero-to-hero.html
related_concepts:
  - "[[1. Wiki/1.2. conceptes/optimitzacio_i_adam]]"
  - "[[1. Wiki/1.2. conceptes/xarxes_neuronals]]"
related_models:
  - "[[1. Wiki/1.3. models/nanoGPT]]"
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Entrenament, validació i sobreajustament

## Definició

L’entrenament ajusta els paràmetres amb exemples coneguts. La validació mesura si el model generalitza amb dades que no ha vist. El sobreajustament apareix quan memoritza massa bé l’entrenament i rendeix pitjor fora de mostra.

## Intuïció

Seria com valorar una estratègia només amb el període que has fet servir per dissenyar-la: un resultat excel·lent pot ser una il·lusió si no es prova en dades noves.

## Funcionament simplificat

Les dades se separen habitualment en:

- **train**: per actualitzar pesos;
- **validation/dev**: per escollir configuracions;
- **test**: per avaluar una vegada la versió final.

Els *mini-batches* processen petites mostres en cada pas d’entrenament, fent el càlcul assumible i introduint variació útil en els gradients.

## Exemple

Si la pèrdua de train continua baixant però la de validation puja, el model està començant a sobreajustar-se.

## Limitacions i errors habituals

No s’ha d’utilitzar el conjunt de test repetidament per prendre decisions. També cal evitar fuites de dades entre períodes, documents o empreses relacionades.

## Fonts

- [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html).
