---
title: Graph of Thoughts
node_id: "concept:graph_of_thoughts"
node_type: "concept"
category: conceptes
tags:
  - grafs
  - raonament
  - prompting
  - models-de-llenguatge
sources:
  - https://arxiv.org/abs/2308.09687
  - https://github.com/spcl/graph-of-thoughts
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Graph of Thoughts

## Definició

Graph of Thoughts (GoT) és un marc d’orquestració que representa les unitats intermèdies de raonament d’un LLM com un graf. Els nodes són pensaments o resultats parcials, i les arestes expressen dependències entre ells.

## Per què és important?

La cadena de pensament és lineal i l’arbre de pensaments ramifica alternatives separades. GoT permet combinar resultats, crear bucles de revisió i reutilitzar informació entre branques.

## Intuïció

Quan analitzem una empresa, no sempre seguim una única seqüència. Podem estudiar el model de negoci, comparar-lo amb competidors, revisar riscos i tornar a modificar la hipòtesi inicial quan apareix una dada nova.

GoT intenta representar aquesta forma de treball amb operacions sobre nodes de pensament:

- generar;
- transformar;
- combinar;
- puntuar;
- verificar;
- seleccionar.

## Funcionament simplificat

1. Es defineix un graf d’operacions.
2. Cada operació genera una instrucció per al LLM.
3. Els resultats parcials s’emmagatzemen com a nodes.
4. Les operacions següents consumeixen els nodes requerits.
5. Un avaluador compara o filtra els resultats.
6. El graf produeix una resposta final.

## Diferències

| Estratègia | Estructura |
|---|---|
| Chain of Thought | cadena lineal |
| Tree of Thoughts | arbre de branques |
| Graph of Thoughts | graf amb combinacions, dependències i bucles |

GoT és una estratègia de prompting i d’orquestració. No és una arquitectura neuronal ni un nou model de llenguatge.

## Exemple

Per analitzar un informe:

1. generar una síntesi;
2. extreure riscos i oportunitats en branques separades;
3. combinar els resultats;
4. comparar-los amb les fonts;
5. revisar contradiccions;
6. redactar una conclusió.

## Relacions

- [[grafs_i_models_de_llenguatge]]
- [[RAG]]
- [[GraphRAG]]
- [[enginyeria_de_prompts]]
- [[LLM]]
- [[avaluacio_de_models]]

## Limitacions i errors habituals

- més operacions poden augmentar cost i latència;
- un graf d’operacions mal definit pot amplificar errors;
- les verificacions del LLM no són una prova independent;
- els resultats depenen de les instruccions i de l’avaluador;
- no s’ha de confondre una seqüència d’instruccions amb raonament intern observable del model.

## Fonts

- [Graph of Thoughts: Solving Elaborate Problems with Large Language Models](https://arxiv.org/abs/2308.09687).
- [Implementació oficial](https://github.com/spcl/graph-of-thoughts).
