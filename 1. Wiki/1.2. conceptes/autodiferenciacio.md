---
title: Autodiferenciació
category: conceptes
tags:
  - aprenentatge-profund
  - gradients
  - autograd
sources:
  - https://github.com/karpathy/micrograd
related_concepts:
  - "[[1. Wiki/1.2. conceptes/backpropagation]]"
  - "[[1. Wiki/1.2. conceptes/optimitzacio_i_adam]]"
related_models: []
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Autodiferenciació

## Definició

L’autodiferenciació és el mecanisme que calcula automàticament com varia l’error d’un model quan es modifica cadascun dels seus paràmetres.

## Intuïció

És com disposar, per a cada coeficient d’un model, d’una sensibilitat exacta: quant millora o empitjora el resultat si el movem una mica. Això evita derivar manualment una funció amb milions de pesos.

## Funcionament simplificat

Durant el *forward pass*, el sistema registra les operacions que produeixen la predicció. Durant el *backward pass*, aplica la regla de la cadena sobre aquest graf de càlcul i obté els gradients.

## Exemple

[[micrograd]] és una implementació didàctica mínima: mostra que l’autodiferenciació no és màgia de PyTorch, sinó una successió de derivades locals.

## Relacions

- [[1. Wiki/1.2. conceptes/backpropagation]]
- [[1. Wiki/1.2. conceptes/optimitzacio_i_adam]]
- [[1. Wiki/1.2. conceptes/xarxes_neuronals]]

## Limitacions i errors habituals

No és un mètode d’optimització: només calcula gradients. Si el model està mal plantejat, les dades són pobres o els gradients són inestables, l’autodiferenciació ho executarà correctament però no resoldrà el problema.

## Fonts

- [micrograd](https://github.com/karpathy/micrograd) — motor d’autodiferenciació didàctic d’Andrej Karpathy.
