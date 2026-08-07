---
title: GPT-2
node_id: "model:gpt_2"
node_type: "model"
category: models
model_family: transformer
architecture: decoder-only
modalities:
  - text
training_objective: autoregressive next-token prediction
authors:
  - OpenAI
sources:
  - https://openai.com/index/better-language-models/
related_concepts:
  - "[[1. Wiki/1.2. conceptes/attention]]"
  - "[[1. Wiki/1.2. conceptes/tokenitzacio_i_bpe]]"
  - "[[1. Wiki/1.2. conceptes/LLM]]"
related_models:
  - "[[1. Wiki/1.3. models/GPT]]"
  - "[[1. Wiki/1.3. models/nanoGPT]]"
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# GPT-2

## Què és?

GPT-2 és una versió a escala més gran de la família GPT, popular com a demostració que l’entrenament autoregressiu amb molt text podia transferir-se a tasques diverses sense una supervisió específica per a cada tasca.

## Arquitectura

És un Transformer de només descodificador. Cada predicció només pot consultar els tokens anteriors, fet que permet entrenar amb el mateix objectiu que utilitza per generar text.

## Entrada i sortida

Rep tokens de text i produeix una distribució de probabilitats sobre el token següent. La generació repeteix aquest procés, escollint un token i afegint-lo al context.

## Per què és útil estudiar-lo?

La seva arquitectura és prou representativa dels GPT posteriors i prou petita per llegir-ne implementacions didàctiques com [[1. Wiki/1.3. models/nanoGPT]] o picoGPT.

## Limitacions

No és un model actual per a la majoria d’aplicacions, té un context limitat i no va ser entrenat com a assistent instructiu. El seu valor principal dins la wiki és pedagògic i històric.

## Fonts

- [Better language models and their implications](https://openai.com/index/better-language-models/).
