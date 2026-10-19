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
  - https://arxiv.org/abs/2609.29144v1
related_concepts:
  - "[[1. Wiki/1.2. conceptes/memoria_agentica]]"
  - "[[1. Wiki/1.2. conceptes/zettelkasten]]"
  - "[[1. Wiki/1.2. conceptes/evergreen_notes]]"
related_models:
  - "[[1. Wiki/1.3. models/A-MEM]]"
  - "[[1. Wiki/1.3. models/llm_wiki]]"
status: reviewed
created: 2026-09-25
updated: 2026-10-19
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

## Validar una revisió i delimitar-ne l'abast

*Scope Before You Persist* (Cheng et al., setembre de 2026) estudia actualitzacions persistents de procediments en tasques de reparació de codi. Mostra que una modificació validada per a una família pot interferir en una altra si es recupera globalment. Validar el canvi i decidir on reutilitzar-lo són controls complementaris. És una **prepublicació** sobre un entorn concret, no una garantia per a wikis.

**Adaptació editorial proposada:** documenta font, família de tasques, condicions, versió i evidència d'una regla apresa. Recupera-la només quan el cas compleixi aquest abast i revisa regressions abans d'ampliar-lo. Això no limita la consulta d'un fet general ben documentat: limita la generalització d'un procediment local.

Exemple inferit: una convenció de citació validada per informes financers no s'hauria de convertir automàticament en norma per a totes les notes. La relació amb A-MEM és comparativa: aquest treball tracta procediments persistents, no l'actualització d'atributs de notes d'A-MEM.

## Font

- Xu i col·laboradors, [*A-Mem: Agentic Memory for LLM Agents*](https://papers.nips.cc/paper_files/paper/2025/file/19909c36f51abc4856b4560aff3d36d6-Paper-Conference.pdf), NeurIPS 2025, secció 3.3 i estudi d'ablació. Consultat el 2026-09-25.
- Cheng et al., [Scope Before You Persist: Preventing Cross-Family Interference in Agent Memory](https://arxiv.org/abs/2609.29144v1), 2026-09-24, prepublicació; consultada el 2026-10-19.
