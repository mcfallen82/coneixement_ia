---
title: Tokenització i BPE
category: conceptes
tags:
  - models-de-llenguatge
  - tokenitzacio
  - bpe
sources:
  - https://arxiv.org/abs/1508.07909
  - https://huggingface.co/learn/llm-course/en/chapter6/5
related_concepts:
  - "[[1. Wiki/1.2. conceptes/embeddings]]"
  - "[[1. Wiki/1.2. conceptes/LLM]]"
related_models:
  - "[[1. Wiki/1.3. models/GPT]]"
  - "[[1. Wiki/1.3. models/GPT-2]]"
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Tokenització i BPE

## Definició

La tokenització converteix el text en unitats discretes que el model pot processar. BPE (*Byte-Pair Encoding*) és una família de mètodes que construeix tokens freqüents combinant progressivament fragments més petits.

## Intuïció

Un LLM no llegeix paraules ni caràcters de la mateixa manera que una persona. Llegeix una seqüència d’identificadors. La manera de partir el text determina longitud, cost, cobertura de vocabulari i alguns errors possibles.

## Funcionament simplificat

1. El text es divideix en tokens.
2. Cada token es converteix en un [[1. Wiki/1.2. conceptes/embeddings]].
3. El model processa els vectors.
4. La sortida torna a ser una distribució sobre el vocabulari de tokens.

## Exemple

Un 10-K pot contenir xifres, sigles, taules i noms de societats. El recompte de tokens, no el nombre de paraules, determina si el document cap en el context del model.

## Limitacions i errors habituals

No equival a «comprendre el text». Diferents tokenitzadors fragmenten la mateixa expressió de maneres diferents, i els textos financers poden ser costosos per la presència de xifres, codis i taules.

## Fonts

- [Neural Machine Translation of Rare Words with Subword Units](https://arxiv.org/abs/1508.07909).
- [Hugging Face: Byte-Pair Encoding tokenization](https://huggingface.co/learn/llm-course/en/chapter6/5).
