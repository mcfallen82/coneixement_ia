---
title: GraphQA
node_id: "concept:graphqa"
node_type: "concept"
category: conceptes
tags:
  - grafs
  - question-answering
  - knowledge-graphs
  - GNN
  - LLM
sources:
  - https://arxiv.org/abs/2402.07630
  - https://arxiv.org/abs/2011.07743
  - https://arxiv.org/abs/2107.02865
related_concepts:
  - "[[grafs_i_models_de_llenguatge]]"
  - "[[xarxes_neuronals_de_graf]]"
  - "[[GraphRAG]]"
  - "[[RAG]]"
related_models:
  - "[[G-Retriever]]"
status: reviewed
created: 2026-09-18
updated: 2026-09-18
---

# GraphQA

## Definició

**GraphQA (Graph Question Answering)** és la tasca de respondre preguntes utilitzant informació representada com un graf. La resposta pot dependre dels atributs dels nodes, de les arestes i, sobretot, de seguir diverses relacions entre entitats.

El terme és ampli. Pot incloure **question answering sobre knowledge graphs (KGQA)**, on una pregunta en llenguatge natural es transforma o s'alinea amb una consulta sobre un graf de coneixement, i també enfocaments recents sobre **grafs textuals**, on nodes i arestes contenen text i el sistema combina recuperació, GNN i LLM.

## Per què és important?

Moltes preguntes reals no es resolen recuperant un únic fragment. Requereixen connectar informació dispersa.

Exemple:

`empresa → adquireix → filial → ven → producte → exposat_a → regulació`

Una pregunta com «Quina regulació pot afectar indirectament aquesta empresa a través de la seva filial?» exigeix seguir un camí de diverses arestes. GraphQA converteix aquesta estructura relacional en part explícita del problema.

## Intuïció

Una cerca vectorial troba fragments semblants a la pregunta. GraphQA intenta trobar **quins nodes, relacions o camins contenen la resposta**.

La diferència és semblant a consultar un arxiu per paraules clau o reconstruir una cadena de participacions empresarials: en el segon cas, l'estructura de les relacions és part de la resposta.

## Funcionament simplificat

Un sistema GraphQA pot seguir aquest flux:

1. interpreta la pregunta;
2. identifica entitats i relacions rellevants;
3. vincula la pregunta amb nodes del graf;
4. recupera un subgraf o construeix una consulta estructurada;
5. fa raonament sobre un o diversos salts;
6. genera o selecciona la resposta;
7. conserva els nodes, arestes i fonts utilitzats com a evidència.

No tots els sistemes fan servir les mateixes peces. Alguns utilitzen llenguatges de consulta i *entity linking*; altres utilitzen embeddings, GNN, recuperació de subgrafs i LLM.

## GraphQA, KGQA i GraphRAG

| Concepte | Pregunta principal | Mecanisme habitual |
|---|---|---|
| KGQA | Com responc una pregunta sobre un graf de coneixement? | entity linking + consulta o raonament sobre el KG |
| GraphQA | Com responc preguntes sobre dades estructurades com a graf? | recuperació/raonament sobre nodes, arestes i subgrafs |
| GraphRAG | Com recupero context gràfic útil perquè un LLM respongui? | indexació + recuperació de graf + generació |

GraphQA descriu sobretot **la tasca**. GraphRAG descriu sobretot **una arquitectura de recuperació i generació** que pot utilitzar-se per resoldre tasques de GraphQA.

## Relació amb les GNN

Una GNN pot codificar un graf propagant informació entre nodes connectats. En GraphQA això permet construir representacions que incorporen tant el contingut dels nodes com la topologia.

Però **GraphQA no implica obligatòriament una GNN**. Un sistema també pot resoldre la pregunta mitjançant consultes simbòliques, recorreguts del graf, recuperació de subgrafs o un LLM amb context estructurat.

## Exemple aplicat a anàlisi d'empreses

Suposem un graf amb:

- empreses;
- directius;
- productes;
- clients;
- adquisicions;
- riscos;
- documents i períodes.

Pregunta:

> «Quins riscos comparteixen dues empreses de la cartera a través d'un mateix proveïdor?»

El sistema hauria de:

`empresa A → compra_a → proveïdor ← compra_a ← empresa B`

i després:

`proveïdor → exposat_a → risc`

Aquesta consulta és naturalment multi-salt i es beneficia d'un graf explícit.

## Avaluació

GraphQA s'ha d'avaluar separant diverses capacitats:

- exactitud de la resposta;
- recuperació correcta de nodes i arestes;
- raonament multi-salt;
- generalització a entitats o composicions noves;
- traçabilitat de l'evidència;
- robustesa davant subgrafs grans o incomplets.

GrailQA és un exemple de benchmark que posa èmfasi en la generalització composicional i zero-shot en question answering sobre bases de coneixement. El treball de G-Retriever introdueix un benchmark GraphQA orientat a grafs textuals de diferents dominis.

## Relacions

- [[grafs_i_models_de_llenguatge]]
- [[xarxes_neuronals_de_graf]]
- [[GraphRAG]]
- [[RAG]]
- [[G-Retriever]]
- [[embeddings]]
- [[avaluacio_de_models]]

## Limitacions i errors habituals

- confondre GraphQA amb una única arquitectura;
- assumir que tota pregunta sobre un graf necessita una GNN;
- recuperar nodes rellevants però perdre les arestes que expliquen la relació;
- ignorar l'*entity linking* i vincular malament una entitat;
- donar una resposta correcta sense conservar el camí o l'evidència;
- avaluar només exactitud final i no la qualitat del subgraf recuperat;
- extrapolar resultats de benchmarks sintètics a grafs empresarials reals.

## Fonts

- [G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering](https://arxiv.org/abs/2402.07630).
- [Beyond I.I.D.: Three Levels of Generalization for Question Answering on Knowledge Bases — GrailQA](https://arxiv.org/abs/2011.07743).
- [Question Answering over Knowledge Graphs with Neural Machine Translation and Entity Linking](https://arxiv.org/abs/2107.02865).
