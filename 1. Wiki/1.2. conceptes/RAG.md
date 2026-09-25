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
  - https://papers.nips.cc/paper_files/paper/2025/file/19909c36f51abc4856b4560aff3d36d6-Paper-Conference.pdf
  - https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/retrieval-augmented-generation
related_concepts:
  - "[[LLM]]"
  - "[[context_engineering]]"
  - "[[QMD]]"
  - "[[second_brain]]"
  - "[[frontmatter]]"
  - "[[grafs_i_models_de_llenguatge]]"
  - "[[GraphRAG]]"
  - "[[memoria_agentica]]"
related_models:
  - "[[1. Wiki/1.3. models/A-MEM]]"
status: reviewed
created: 2026-08-07
updated: 2026-09-25
---

# RAG — Generació augmentada amb recuperació

## Definició

El RAG combina un model de llenguatge amb una fase prèvia de recuperació de documents o fragments rellevants.

## Per què és important?

Permet utilitzar informació externa i actualitzable sense tornar a entrenar el model. És útil amb wikis, manuals i bases documentals.

## Intuïció

El model no respon només amb el que ha après. Primer consulta una biblioteca, selecciona els fragments més útils i els incorpora al context.

## Funcionament

1. Les fonts es preparen i indexen; segons el corpus, es poden dividir en fragments.
2. Una consulta recupera documents o fragments amb cerca lèxica, vectorial o híbrida. La cerca vectorial fa servir embeddings, però no són un requisit de tot sistema RAG.
3. El sistema filtra o reordena els resultats i els aporta al context del model.
4. El LLM genera una resposta amb la pregunta i el context recuperat.

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

## Relació amb la memòria agentiva

[[1. Wiki/1.3. models/A-MEM]] també recupera notes mitjançant semblança vectorial, però el seu tret distintiu és que proposa connexions i fa evolucionar atributs de notes antigues quan s'incorpora informació. Vegeu [[1. Wiki/1.2. conceptes/memoria_agentica|memòria agentiva]]. Es poden combinar recuperació i wiki persistent, però els resultats de memòria conversacional d'A-MEM no s'han mesurat en aquesta wiki.

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
- [Xu i col·laboradors — A-Mem: Agentic Memory for LLM Agents](https://papers.nips.cc/paper_files/paper/2025/file/19909c36f51abc4856b4560aff3d36d6-Paper-Conference.pdf), NeurIPS 2025.
- [Microsoft Learn — Retrieval augmented generation](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/retrieval-augmented-generation).
