---
title: FinBERT
node_id: "model:finbert"
node_type: "model"
category: models
model_family: BERT
architecture: encoder-only transformer
modalities:
  - text
training_objective: masked-language-model pretraining and task-specific fine-tuning
authors:
  - ProsusAI
sources:
  - https://arxiv.org/abs/1908.10063
  - https://github.com/ProsusAI/finBERT
related_concepts:
  - "[[1. Wiki/1.2. conceptes/LLM]]"
  - "[[1. Wiki/1.2. conceptes/entrenament_validacio_i_overfitting]]"
  - "[[1. Wiki/1.2. conceptes/raonament_numeric_documental]]"
related_models:
  - "[[1. Wiki/1.3. models/transformer]]"
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# FinBERT

## Què és?

FinBERT és un model BERT adaptat al llenguatge financer. Està pensat sobretot per extreure representacions i classificar text financer, en especial tasques de sentiment o de to.

## Quin problema resol?

El vocabulari, les convencions i el context del text financer poden fer que un model general interpreti malament expressions com «liability», «guidance» o «dilution». L’adaptació al domini redueix aquesta distància lingüística.

## Arquitectura i entrenament

És un Transformer de només codificador. El preentrenament emmascara part dels tokens i el model aprèn a reconstruir-los utilitzant el context dels dos costats. Després s’ajusta per a una tasca concreta.

## Quan és adequat?

- classificació de sentiment o to;
- etiquetatge de fragments;
- cerca o representació de text financer;
- suport per revisar grans col·leccions de comunicacions.

## Limitacions

No és un sistema complet per respondre preguntes ni el millor instrument per a càlculs. Per a raonament sobre text i taules calen recuperació, eines de càlcul i validació, com explica [[1. Wiki/1.2. conceptes/raonament_numeric_documental]].

## Fonts

- [FinBERT: Financial Sentiment Analysis with Pre-trained Language Models](https://arxiv.org/abs/1908.10063).
- [Repositori FinBERT](https://github.com/ProsusAI/finBERT).
