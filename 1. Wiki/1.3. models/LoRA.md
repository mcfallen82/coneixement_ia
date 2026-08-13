---
title: LoRA
node_id: "model:lora"
node_type: "model"
category: models
tags:
  - model
model_family: tècnica d’adaptació de Transformers
architecture: actualització de baix rang sobre capes lineals
modalities:
  - text
training_objective: adaptació eficient d’un model preentrenat
authors:
  - Edward J. Hu et al.
developer: Microsoft Research
release_date: 2021
sources:
  - https://arxiv.org/abs/2106.09685
related_concepts:
  - "[[1. Wiki/1.2. conceptes/ajust_fi]]"
  - "[[1. Wiki/1.2. conceptes/backpropagation]]"
related_models:
  - "[[1. Wiki/1.3. models/transformer]]"
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# LoRA

## Què és?

LoRA (Low-Rank Adaptation) és una tècnica per adaptar models grans mantenint congelats els pesos originals i afegint actualitzacions entrenables de baix rang. Per coherència amb la wiki, es registra a la carpeta de models com a tècnica/model d’adaptació, encara que no sigui una arquitectura completa.

## Quin problema resol?

L’ajustament complet exigeix actualitzar i conservar tots els paràmetres del model. LoRA redueix els paràmetres entrenables, la memòria necessària i el cost de mantenir moltes adaptacions.

## Mecanisme

En lloc de substituir directament una matriu de pesos, LoRA n’aprèn una actualització aproximada mitjançant el producte de dues matrius petites. El model base queda congelat i només s’entrenen aquestes matrius.

## Intuïció

És com modificar una empresa gran mitjançant una unitat especialitzada i petita, sense reescriure tota l’organització. La unitat pot adaptar el comportament al nou mercat, però depèn de la capacitat i de les limitacions de l’empresa de base.

## Aplicacions

- ajustament de models de llenguatge;
- adaptació a estils o dominis;
- personalització amb recursos limitats;
- combinació de diverses adaptacions.

## Punts forts

- pocs paràmetres entrenables;
- menor ús de memòria que l’ajustament complet;
- adaptacions separables del model base;
- facilita experimentar amb diversos conjunts de dades.

## Limitacions

LoRA no afegeix automàticament coneixement fiable ni elimina la necessitat de dades de qualitat. El rang, les capes escollides, la taxa d’aprenentatge i la distribució de les dades condicionen el resultat.

## Models relacionats

- [[1. Wiki/1.3. models/transformer]] — arquitectura on es va aplicar.
- [[1. Wiki/1.2. conceptes/ajust_fi]] — procés general que LoRA fa més eficient.

## Fonts

- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685).
