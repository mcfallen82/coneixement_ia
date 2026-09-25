---
title: Evolució de la memòria
category: conceptes
node_id: "concept:evolucio_de_la_memoria"
node_type: "concept"
tags:
  - agents
  - memoria
  - actualitzacio
sources:
  - https://papers.nips.cc/paper_files/paper/2025/file/19909c36f51abc4856b4560aff3d36d6-Paper-Conference.pdf
related_concepts:
  - "[[1. Wiki/1.2. conceptes/memoria_agentica]]"
  - "[[1. Wiki/1.2. conceptes/zettelkasten]]"
  - "[[1. Wiki/1.2. conceptes/evergreen_notes]]"
related_models:
  - "[[1. Wiki/1.3. models/A-MEM]]"
  - "[[1. Wiki/1.3. models/llm_wiki]]"
status: reviewed
created: 2026-09-25
updated: 2026-09-25
---

# Evolució de la memòria

## Definició i intuïció

En el sentit concret d'[[1. Wiki/1.3. models/A-MEM|A-MEM]], és la revisió de la **descripció contextual, les paraules clau i les etiquetes** de records antics quan s'incorpora una nota nova relacionada. És com ampliar la fitxa de lectura d'una idea després de descobrir una connexió, sense necessàriament canviar l'esdeveniment que s'havia registrat.

## Com funciona en A-MEM?

Després de recuperar notes properes per semblança i proposar enllaços, el sistema presenta al LLM la nota nova i les candidates antigues. El LLM decideix si cal actualitzar-ne els atributs contextuals. Així, el record passat es pot fer més fàcil d'interpretar i recuperar en el nou context. L'estudi d'ablació dels autors mostra que retirar aquesta fase perjudica el rendiment en les seves tasques de memòria conversacional; no demostra que tota revisió automàtica sigui correcta.

## Exemple i distinció important

Una nota anterior diu «un agent recupera fragments amb RAG»; una font posterior presenta memòria que vincula notes. Es podria afegir a la **descripció de la nota anterior** una connexió amb [[1. Wiki/1.2. conceptes/memoria_agentica|memòria agentiva]]. Aquest és un **exemple didàctic**: una wiki amb fonts verificables hauria de conservar intacte el document original i registrar quina font justifica la nova interpretació.

Les [[1. Wiki/1.2. conceptes/evergreen_notes|notes permanents]] també es revisen, però descriuen una pràctica de pensament i escriptura; l'evolució d'A-MEM és un mecanisme automatitzat concret d'un sistema de memòria. No implica reentrenar el LLM.

## Limitacions

Si una connexió suggerida és incorrecta, actualitzar una nota antiga pot propagar l'error. Fan falta versions, procedència i un criteri per acceptar o rebutjar canvis quan s'aplica a coneixement públic.

## Font

- Xu i col·laboradors, [*A-Mem: Agentic Memory for LLM Agents*](https://papers.nips.cc/paper_files/paper/2025/file/19909c36f51abc4856b4560aff3d36d6-Paper-Conference.pdf), NeurIPS 2025, secció 3.3 i estudi d'ablació. Consultat el 2026-09-25.
