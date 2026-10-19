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
  - https://arxiv.org/abs/2605.12493v1
related_concepts:
  - "[[1. Wiki/1.2. conceptes/evolucio_de_la_memoria]]"
  - "[[1. Wiki/1.2. conceptes/zettelkasten]]"
  - "[[1. Wiki/1.2. conceptes/RAG]]"
  - "[[1. Wiki/1.2. conceptes/embeddings]]"
  - "[[1. Wiki/1.2. conceptes/context_engineering]]"
  - "[[1. Wiki/1.2. conceptes/avaluacio_de_models]]"
related_models:
  - "[[1. Wiki/1.3. models/A-MEM]]"
status: reviewed
created: 2026-09-25
updated: 2026-10-19
---

# Memòria agentiva

## Què és i per què importa?

És la gestió de memòria externa perquè un agent conservi i reutilitzi informació entre interaccions, amb operacions de selecció, organització o revisió segons el sistema. No designa una única arquitectura. A [[1. Wiki/1.3. models/A-MEM|A-MEM]], l'agent participa en la construcció i evolució de les notes, en lloc de limitar-se a emmagatzemar-les i recuperar-les.

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

## De les converses a l'experiència operativa

LongMemEval-V2 (Wu et al., maig de 2026) avalua experiència d'agents web: record d'estats, seguiment de canvis, coneixement de procediments, dificultats de l'entorn i detecció de premisses incorrectes. Els seus mètodes AgentRunbook-R i AgentRunbook-C contrasten recuperació indexada i consulta de fitxers amb un agent. L'estudi també assenyala el cost de latència d'aquesta segona opció.

Per tant, convé distingir memòria conversacional d'experiència operativa. Un resultat en un conjunt no prova transferència a l'altre. La font es presenta com a **treball en curs**; les prestacions depenen de la tasca, el model i el pressupost.

**Exemple inferit per a la wiki:** recordar una preferència d'estil i conservar un procediment validat per actualitzar fitxes són funcions diferents. Se'n podria comprovar la utilitat amb [[1. Wiki/1.2. conceptes/avaluacio_de_models|avaluacions]] separades; aquí no s'ha reproduït LongMemEval-V2.

## Font

- Xu i col·laboradors, [*A-Mem: Agentic Memory for LLM Agents*](https://papers.nips.cc/paper_files/paper/2025/file/19909c36f51abc4856b4560aff3d36d6-Paper-Conference.pdf), NeurIPS 2025, seccions 1–4. Font primària consultada el 2026-09-25.
- Wu et al., [LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues](https://arxiv.org/abs/2605.12493v1), 2026-05-12, prepublicació i treball en curs; consultada el 2026-10-19.
