---
title: Generació augmentada amb recuperació
node_id: "concept:rag"
node_type: "concept"
category: conceptes
tags:
  - inteligencia-artificial
  - models-de-llenguatge
  - recuperacio
sources:
  - https://arxiv.org/abs/2005.11401
related_concepts: []
related_models: []
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# RAG — Generació augmentada amb recuperació

## Definició

El RAG combina un model de llenguatge amb una fase prèvia de recuperació de documents o fragments rellevants.

## Per què és important?

Permet utilitzar informació externa i actualitzable sense tornar a entrenar el model. És útil amb wikis, manuals i bases documentals.

## Intuïció

El model no respon només amb el que ha après. Primer consulta una biblioteca, selecciona els fragments més útils i els incorpora al context.

## Funcionament

1. Les fonts es divideixen en fragments.
2. Cada fragment es transforma en un embedding.
3. La pregunta també es transforma en un embedding.
4. El sistema recupera els fragments més rellevants.
5. El LLM genera una resposta amb la pregunta i el context recuperat.

Un sistema complet necessita metadades, filtratge, reordenació i una política per citar fonts.

## Exemple

Davant la pregunta «Què és el context engineering?», el sistema pot recuperar la fitxa corresponent, la fitxa de [[LLM]] i una font externa.

## Relacions

- [[LLM]]
- [[context_engineering]]
- [[QMD]]
- [[second_brain]]
- [[frontmatter]]
- [[grafs_i_models_de_llenguatge]]
- [[GraphRAG]]

## Relació amb GraphRAG

GraphRAG amplia la RAG amb una representació gràfica de les entitats, les relacions i les comunitats del corpus. La RAG vectorial continua sent útil quan la pregunta depèn sobretot de fragments locals i no requereix seguir relacions explícites.

## Aplicacions

- wikis assistides per LLM;
- preguntes sobre manuals;
- recerca en articles;
- assistents amb documentació actualitzable.

## Limitacions i errors habituals

- recuperar fragments semblants però no pertinents;
- utilitzar fragments massa petits o massa grans;
- confiar en la recuperació sense comprovar fonts;
- assumir que RAG elimina totes les al·lucinacions;
- no actualitzar la base de coneixement.

## Fonts

- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401).
