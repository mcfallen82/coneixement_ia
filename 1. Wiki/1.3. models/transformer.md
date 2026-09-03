---
title: Transformer
node_id: "model:transformer"
node_type: "model"
category: models
tags:
  - model
model_family: transformer
architecture: encoder-decoder
modalities:
  - text
training_objective: seq2seq or autoregressive, according to the variant
authors:
  - Ashish Vaswani et al.
sources:
  - https://arxiv.org/abs/1706.03762
related_concepts:
  - "[[1. Wiki/1.2. conceptes/attention]]"
  - "[[1. Wiki/1.2. conceptes/embeddings]]"
  - "[[1. Wiki/1.2. conceptes/tokenitzacio_i_bpe]]"
related_models:
  - "[[1. Wiki/1.3. models/GPT]]"
  - "[[1. Wiki/1.3. models/GPT-2]]"
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Transformer

## Què és?

El Transformer és una arquitectura neuronal basada en mecanismes d’[[1. Wiki/1.2. conceptes/attention]]. Va substituir la recurrència com a component central en moltes tasques de llenguatge perquè pot relacionar tokens llunyans en paral·lel.

## Quin problema resol?

Les xarxes recurrents processen les seqüències pas a pas i tenen dificultats per escalar i preservar dependències llargues. El Transformer processa una seqüència sencera com a conjunt de relacions.

## Arquitectura

L’article original proposa un codificador i un descodificador. D’altres variants adopten només el codificador (BERT) o només el descodificador ([[1. Wiki/1.3. models/GPT]]). Els seus blocs combinen:

- embeddings de token i de posició;
- atenció multi-cap;
- MLP per token;
- connexions residuals i normalització.

## Entrada i sortida

Pot rebre una seqüència de tokens i produir una representació contextual, una seqüència nova o probabilitats sobre el token següent, segons la variant.

## Punts forts

- paral·lelització eficient en entrenament;
- bona modelització de dependències llargues;
- arquitectura base de molts LLMs moderns.

## Limitacions

L’atenció estàndard és costosa amb contextos molt llargs. També és una arquitectura, no una garantia de qualitat factual ni de bon ús de dades.

## Fonts

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762).
