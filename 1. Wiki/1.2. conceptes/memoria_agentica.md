---
title: Memòria agentiva
category: conceptes
node_id: "concept:memoria_agentica"
node_type: "concept"
tags:
  - agents
  - memoria
  - gestio-del-coneixement
sources:
  - https://papers.nips.cc/paper_files/paper/2025/file/19909c36f51abc4856b4560aff3d36d6-Paper-Conference.pdf
related_concepts:
  - "[[1. Wiki/1.2. conceptes/evolucio_de_la_memoria]]"
  - "[[1. Wiki/1.2. conceptes/zettelkasten]]"
  - "[[1. Wiki/1.2. conceptes/RAG]]"
  - "[[1. Wiki/1.2. conceptes/embeddings]]"
  - "[[1. Wiki/1.2. conceptes/context_engineering]]"
related_models:
  - "[[1. Wiki/1.3. models/A-MEM]]"
status: reviewed
created: 2026-09-25
updated: 2026-09-25
---

# Memòria agentiva

## Què és i per què importa?

És una manera de gestionar la memòria externa d'un agent amb LLM perquè **organitzi, vinculi i revisi** records a partir de noves interaccions. A [[1. Wiki/1.3. models/A-MEM|A-MEM]], l'agent participa en la construcció i evolució de les notes, en lloc de limitar-se a emmagatzemar-les i recuperar-les.

## Intuïció i funcionament

Un arxiu de converses permet trobar una frase antiga. Una memòria agentiva intenta també entendre com la frase es relaciona amb experiències posteriors. A-MEM segueix el cicle **interacció → nota estructurada → candidates per semblança → enllaços proposats pel LLM → evolució de notes relacionades → recuperació**. La selecció de candidates es recolza en [[1. Wiki/1.2. conceptes/embeddings|embeddings]]; les notes connectades s'inspiren en [[1. Wiki/1.2. conceptes/zettelkasten|Zettelkasten]].

## Exemple aplicat

Un agent que ajuda a estudiar IA registra primer una pregunta sobre [[1. Wiki/1.2. conceptes/RAG|RAG]] i després una altra sobre grafs. Podria suggerir una connexió entre els dos records i afegir context a la nota antiga. **És una extrapolació didàctica**: l'estudi d'A-MEM avalua sobretot memòria sobre converses, no la precisió de relacions científiques en aquesta wiki.

## Relació amb altres conceptes

- [[1. Wiki/1.2. conceptes/RAG|RAG]] explica com es recupera context; en A-MEM també s'organitza i s'actualitza la memòria quan s'hi escriu.
- [[1. Wiki/1.2. conceptes/evolucio_de_la_memoria|Evolució de la memòria]] és l'operació concreta que revisa metadades i representacions de notes anteriors.
- [[1. Wiki/1.2. conceptes/context_engineering|Enginyeria del context]] decideix què s'incorpora al context d'una resposta; una memòria recuperable n'és una font possible.
- [[1. Wiki/1.3. models/llm_wiki|LLM Wiki]] conserva coneixement en pàgines; A-MEM és un sistema de memòria d'interaccions per a agents.

## Límits

L'automatització pot crear enllaços poc justificats, perdre la procedència o reforçar errors anteriors. Una base documental necessita que les afirmacions importants continuïn vinculades a fonts i siguin revisables per una persona. «Agentiva» descriu l'autonomia en aquestes operacions; no garanteix exactitud ni significa que s'hagin modificat els pesos del LLM.

## Font

- Xu i col·laboradors, [*A-Mem: Agentic Memory for LLM Agents*](https://papers.nips.cc/paper_files/paper/2025/file/19909c36f51abc4856b4560aff3d36d6-Paper-Conference.pdf), NeurIPS 2025, seccions 1–4. Font primària consultada el 2026-09-25.
