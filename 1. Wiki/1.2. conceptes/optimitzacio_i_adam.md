---
title: Optimització, descens del gradient i Adam
node_id: "concept:optimitzacio_i_adam"
node_type: "concept"
category: conceptes
tags:
  - aprenentatge-profund
  - optimitzacio
  - adam
sources:
  - https://arxiv.org/abs/1412.6980
related_concepts:
  - "[[1. Wiki/1.2. conceptes/backpropagation]]"
  - "[[1. Wiki/1.2. conceptes/entrenament_validacio_i_overfitting]]"
related_models:
  - "[[1. Wiki/1.3. models/nanoGPT]]"
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Optimització, descens del gradient i Adam

## Definició

L’optimització és el procés d’ajustar els paràmetres per reduir l’error. El descens del gradient n’és la regla bàsica: desplaça cada pes en la direcció que, localment, redueix més la pèrdua.

## Intuïció

És com ajustar una cartera a partir de sensibilitats marginals: no busques d’entrada el punt perfecte, sinó que fas passos controlats segons la informació disponible. Una taxa d’aprenentatge massa gran pot passar-se del mínim; una de massa petita avança molt lentament.

## Adam

Adam combina una mitjana dels gradients recents (*momentum*) amb una mesura de la seva variabilitat. Això permet passos adaptatius per a cada paràmetre.

## Exemple

En entrenar un GPT petit, Adam acostuma a convergir amb més estabilitat que un descens del gradient bàsic, però encara cal vigilar la taxa d’aprenentatge i la validació.

## Relacions

- [[1. Wiki/1.2. conceptes/backpropagation]]
- [[1. Wiki/1.2. conceptes/entrenament_validacio_i_overfitting]]
- [[1. Wiki/1.2. conceptes/activacions_i_inicialitzacio]]

## Limitacions i errors habituals

Adam no substitueix una bona preparació de dades ni evita el sobreajustament. Una pèrdua d’entrenament que baixa no prova que el model generalitzi.

## Fonts

- [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980).
