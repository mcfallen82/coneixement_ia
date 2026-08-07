---
title: Alineament dels LLM
node_id: "concept:alineament_dels_llm"
node_type: "concept"
category: conceptes
tags:
  - llm
  - instruccions
  - preferencies
sources:
  - https://arxiv.org/abs/2203.02155
  - https://arxiv.org/abs/2212.10560
related_concepts:
  - [[1. Wiki/1.2. conceptes/ajust_fi]]
  - [[1. Wiki/1.2. conceptes/avaluacio_de_models]]
related_models:
  - [[1. Wiki/1.3. models/GPT]]
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Alineament dels LLM

## Què és?

L’alineament és el conjunt de tècniques que intenten fer que el comportament d’un model sigui més útil, segur, honest i coherent amb les instruccions i preferències humanes.

## Per què és important?

El preentrenament ensenya un model a predir text. Aquesta capacitat no especifica per si sola com ha de respondre a una persona, com ha de prioritzar instruccions o com ha de gestionar peticions amb risc.

## Intuïció

El preentrenament és comparable a donar a una persona una gran biblioteca; l’alineament és ensenyar-li criteris de resposta, prioritats i límits. La biblioteca pot contenir informació útil i perjudicial, però no determina per si sola la conducta en una conversa.

## Funcionament simplificat

El procés d’InstructGPT descriu una seqüència amb:

1. exemples humans de respostes desitjades;
2. ajustament supervisat;
3. comparacions entre respostes;
4. un model de recompensa;
5. optimització posterior segons les preferències.

Self-Instruct explora una via que genera i filtra dades d’instruccions amb ajuda del mateix model, reduint part de l’anotació manual però introduint dependència de la qualitat del model generador.

## Aplicacions

- assistents conversacionals;
- generació estructurada;
- classificació i extracció guiades;
- agents que han de respectar regles;
- eines de suport a la lectura documental.

## Limitacions

L’alineament no garanteix veritat factual ni raonament correcte. Pot afavorir respostes que sonen convincents, reflectir els biaixos dels avaluadors i reduir el rendiment en tasques que no apareixen en les dades de preferències.

## Relacions

Es basa en [[1. Wiki/1.2. conceptes/ajust_fi]] i s’ha d’avaluar amb [[1. Wiki/1.2. conceptes/avaluacio_de_models]]. En un sistema real, l’alineament és només una capa juntament amb el prompt, la recuperació i la validació.

## Fonts

- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155).
- [Self-Instruct: Aligning Language Models with Self-Generated Instructions](https://arxiv.org/abs/2212.10560).