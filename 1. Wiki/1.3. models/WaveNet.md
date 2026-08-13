---
title: WaveNet
node_id: "model:wavenet"
node_type: "model"
category: models
tags:
  - model
model_family: convolutional autoregressive model
architecture: dilated causal convolutions
modalities:
  - audio
  - text
training_objective: autoregressive next-step prediction
authors:
  - DeepMind
sources:
  - https://arxiv.org/abs/1609.03499
related_concepts:
  - "[[1. Wiki/1.2. conceptes/xarxes_neuronals]]"
  - "[[1. Wiki/1.2. conceptes/softmax_i_cross_entropy]]"
related_models:
  - "[[1. Wiki/1.3. models/transformer]]"
  - "[[1. Wiki/1.3. models/GPT]]"
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# WaveNet

## Què és?

WaveNet és una arquitectura autoregressiva que utilitza convolucions causals dilatades per modelitzar seqüències. Es va presentar inicialment per generar àudio, però és útil per entendre com es podia ampliar el context abans dels Transformers.

## Quin problema resol?

Una convolució normal veu un context local. Les dilatacions amplien el camp receptiu de forma jeràrquica sense haver d’augmentar proporcionalment el nombre de capes.

## Arquitectura

Les convolucions són **causals**: una predicció no pot consultar el futur. Les dilatacions salten posicions a escales creixents, de manera que una capa pot combinar context proper i llunyà.

## Relació amb LLMs

És un punt intermedi pedagògic entre un model bigrama i un Transformer: segueix fent predicció autoregressiva, però construeix context amb una arquitectura diferent.

## Punts forts

- context jeràrquic;
- generació autoregressiva de gran qualitat en la seva aplicació original;
- bona intuïció sobre causalitat i camp receptiu.

## Limitacions

No és la base dels LLMs actuals. Les convolucions no ofereixen la mateixa flexibilitat que l’atenció per relacionar qualsevol parell de tokens.

## Fonts

- [WaveNet: A Generative Model for Raw Audio](https://arxiv.org/abs/1609.03499).
