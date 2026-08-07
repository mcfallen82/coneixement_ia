---
title: Avaluació de models
category: conceptes
tags:
  - llm
  - avaluacio
  - qualitat
sources:
  - https://arxiv.org/abs/2009.03300
  - https://platform.openai.com/docs/api-reference/evals
related_concepts:
  - [[1. Wiki/1.2. conceptes/alineament_dels_llm]]
  - [[1. Wiki/1.2. conceptes/raonament_numeric_documental]]
related_models:
  - [[1. Wiki/1.3. models/GPT]]
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Avaluació de models

## Què és?

L’avaluació de models és el procés sistemàtic de mesurar si un model o sistema compleix un objectiu concret amb dades de prova separades i criteris explícits.

## Per què és important?

Una resposta convincent pot ser falsa, inconsistent o inútil per al procés de treball. L’avaluació converteix la qualitat en una hipòtesi contrastable i permet comparar versions, prompts, models i configuracions.

## Intuïció

És semblant a analitzar una empresa amb un conjunt d’indicadors: una sola mètrica pot ocultar riscos. Cal observar exactitud, estabilitat, cost, latència, cobertura i comportament en casos difícils.

## Capes d’avaluació

- Capacitat general: proves com MMLU, que cobreixen molts àmbits.
- Tasques específiques: preguntes i respostes pròpies del cas d’ús.
- Avaluació del sistema: inclou recuperació, prompt, eines, format i model.
- Avaluació humana: útil per a qualitat, utilitat i criteris difícils d’automatitzar.
- Avaluació de regressió: compara una nova versió amb un conjunt fix de casos.

## Exemple per a anàlisi documental

Un conjunt de prova pot incloure fragments de memòries anuals amb una resposta esperada i la referència exacta. Les mètriques poden separar:

- identificació correcta de la dada;
- càlcul correcte;
- citació de la font;
- absència d’afirmacions no justificades;
- compliment del format.

## Errors habituals

- provar només exemples fàcils;
- utilitzar dades vistes durant l’entrenament;
- confondre una mètrica general amb l’èxit del cas d’ús;
- deixar que el mateix model sigui jutge sense controls;
- no registrar la versió del model, el prompt i les dades.

## Relacions

L’avaluació ha d’acompanyar [[1. Wiki/1.2. conceptes/ajust_fi]], [[1. Wiki/1.2. conceptes/alineament_dels_llm]] i els sistemes de [[1. Wiki/1.2. conceptes/raonament_numeric_documental]].

## Fonts

- [Measuring Massive Multitask Language Understanding](https://arxiv.org/abs/2009.03300).
- [OpenAI Evals API Reference](https://platform.openai.com/docs/api-reference/evals).