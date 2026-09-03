---
title: GPT
node_id: "model:gpt"
node_type: "model"
category: models
tags:
  - model
model_family: transformer
architecture: decoder-only
modalities:
  - text
training_objective: autoregressive next-token prediction
authors:
  - OpenAI
sources:
  - https://openai.com/index/language-unsupervised/
related_concepts:
  - "[[1. Wiki/1.2. conceptes/attention]]"
  - "[[1. Wiki/1.2. conceptes/embeddings]]"
  - "[[1. Wiki/1.2. conceptes/softmax_i_cross_entropy]]"
  - "[[1. Wiki/1.2. conceptes/tokenitzacio_i_bpe]]"
related_models:
  - "[[1. Wiki/1.3. models/transformer]]"
  - "[[1. Wiki/1.3. models/GPT-2]]"
  - "[[1. Wiki/1.3. models/nanoGPT]]"
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# GPT

## Què és?

GPT (*Generative Pre-trained Transformer*) és una família de models de llenguatge basada en un Transformer de només descodificador, entrenat principalment per predir el token següent.

## Quin problema resol?

Converteix una única tasca d’entrenament —completar text— en una base reutilitzable per a generació, resum, classificació, resposta a preguntes i programació, quan es combina amb instruccions, context o ajustament posterior.

## Arquitectura

Cada bloc aplica [[1. Wiki/1.2. conceptes/attention]] causal, una xarxa MLP, connexions residuals i normalització. L’atenció causal impedeix que un token consulti els tokens futurs quan s’entrena a predir el següent.

## Dades i entrenament

Es preentrena amb grans corpus de text no etiquetat. Després es pot ajustar amb exemples específics o mitjançant tècniques d’alineament amb instruccions i preferències.

## Punts forts

- una interfície general basada en text;
- generació coherent en context;
- transferència a moltes tasques sense dissenyar una arquitectura per a cada una.

## Limitacions

La predicció de tokens no garanteix veritat ni càlcul correcte. Els límits de context, les dades d’entrenament i el disseny del sistema condicionen molt el resultat.

## Fonts

- [Improving Language Understanding by Generative Pre-Training](https://openai.com/index/language-unsupervised/).
