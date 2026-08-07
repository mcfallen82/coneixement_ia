---
title: nanoGPT
node_id: "model:nanogpt"
node_type: "model"
category: models
model_family: transformer implementation
architecture: decoder-only
modalities:
  - text
training_objective: autoregressive next-token prediction
authors:
  - Andrej Karpathy
sources:
  - https://github.com/karpathy/nanoGPT
related_concepts:
  - "[[1. Wiki/1.2. conceptes/backpropagation]]"
  - "[[1. Wiki/1.2. conceptes/optimitzacio_i_adam]]"
  - "[[1. Wiki/1.2. conceptes/tokenitzacio_i_bpe]]"
related_models:
  - "[[1. Wiki/1.3. models/GPT]]"
  - "[[1. Wiki/1.3. models/GPT-2]]"
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# nanoGPT

## Què és?

nanoGPT és una implementació compacta i entrenable d’un GPT, creada com a material pràctic. No defineix una família arquitectònica nova: fa visible el codi essencial d’un Transformer de només descodificador.

## Què permet aprendre?

Connecta la teoria amb una implementació real: càrrega de dades, tokenització, batches, *forward pass*, pèrdua, [[1. Wiki/1.2. conceptes/backpropagation]], Adam, validació i generació.

## Arquitectura

Implementa blocs Transformer amb embeddings, atenció causal, MLP, residuals i normalització. S’acosta especialment a GPT-2 per disseny.

## Cas d’ús

És una bona següent etapa després de [[1. Wiki/1.2. conceptes/micrograd]] i del curs Zero to Hero: permet entendre PyTorch sense començar per un sistema de producció complex.

## Limitacions

No és una biblioteca completa per desplegar LLMs ni un model final. Entrenar-lo amb pocs recursos produeix resultats limitats; el seu valor és didàctic i experimental.

## Fonts

- [nanoGPT](https://github.com/karpathy/nanoGPT).
