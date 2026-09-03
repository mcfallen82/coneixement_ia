---
title: Normalització per lots
node_id: "concept:batch_normalization"
node_type: "concept"
category: conceptes
tags:
  - aprenentatge-profund
  - normalitzacio
  - batchnorm
sources:
  - https://arxiv.org/abs/1502.03167
related_concepts:
  - "[[1. Wiki/1.2. conceptes/activacions_i_inicialitzacio]]"
  - "[[1. Wiki/1.2. conceptes/entrenament_validacio_i_overfitting]]"
related_models:
  - "[[1. Wiki/1.3. models/WaveNet]]"
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Normalització per lots (*BatchNorm*)

## Definició

BatchNorm normalitza les activacions intermèdies d’un lot durant l’entrenament i després n’aprèn una escala i un desplaçament.

## Intuïció

Si cada capa rep valors en escales molt diferents a cada pas, l’entrenament és inestable. La normalització dona a la capa següent un punt de partida més regular, sense impedir-li aprendre l’escala que necessita.

## Funcionament simplificat

Per a cada característica d’un mini-lot:

1. calcula mitjana i variància;
2. normalitza els valors;
3. aplica paràmetres entrenables d’escala i desplaçament;
4. durant inferència utilitza estadístiques acumulades.

## Exemple

En xarxes profundes clàssiques, pot fer més estable l’entrenament i permetre taxes d’aprenentatge més grans. Els Transformers sovint utilitzen altres esquemes, especialment LayerNorm.

## Limitacions i errors habituals

BatchNorm depèn de la mida i composició dels lots; no és la norma adequada per a tots els models seqüencials. No s’ha de confondre amb qualsevol tipus de normalització.

## Fonts

- [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/abs/1502.03167).
