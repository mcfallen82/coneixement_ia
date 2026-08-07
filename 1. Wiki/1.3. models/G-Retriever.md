---
title: G-Retriever
node_id: "model:g_retriever"
node_type: "model"
category: models
model_family: GraphRAG
architecture: graph_retrieval_plus_GNN_plus_LLM
modalities:
  - text
  - graphs
training_objective: graph_question_answering
authors: []
sources:
  - https://arxiv.org/abs/2402.07630
  - https://arxiv.org/html/2402.07630
related_concepts:
  - "[[grafs_i_models_de_llenguatge]]"
  - "[[RAG]]"
  - "[[xarxes_neuronals_de_graf]]"
  - "[[GraphRAG]]"
related_models: []
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# G-Retriever

## Identificació

G-Retriever és un marc de recuperació augmentada per respondre preguntes sobre grafs textuals. Combina un recuperador gràfic, una xarxa neuronal de graf i un LLM.

## Problema que resol

Els grafs textuals poden ser massa grans per introduir-los sencers en el context d’un LLM. El sistema ha de seleccionar una part del graf que sigui rellevant i que mantingui les relacions necessàries per respondre.

## Funcionament

1. Rep una pregunta i un graf textual.
2. Genera representacions del graf i del text.
3. Recupera un subgraf rellevant.
4. Formula la selecció com un problema d’optimització amb connectivitat.
5. Envia el subgraf i el context textual al LLM.
6. Genera una resposta sobre el graf.

El treball utilitza una formulació basada en el problema de l’arbre de Steiner amb premis per seleccionar una estructura connectada i rellevant.

## Punts forts

- preserva informació textual i topològica;
- permet treballar amb grafs que superen la finestra de context;
- s’adapta a tasques de GraphQA;
- està dissenyat per reduir al·lucinacions mitjançant context estructurat.

## Limitacions

- la recuperació depèn de la qualitat del graf;
- l’optimització pot ser costosa;
- el marc no és una solució universal per a qualsevol RAG;
- cal distingir els resultats del paper dels resultats obtinguts en altres dominis.

## Relacions

- [[GraphRAG]]
- [[RAG]]
- [[xarxes_neuronals_de_graf]]
- [[grafs_i_models_de_llenguatge]]
- [[avaluacio_de_models]]

## Fonts

- [G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering](https://arxiv.org/abs/2402.07630).
- [Versió HTML del paper](https://arxiv.org/html/2402.07630).
