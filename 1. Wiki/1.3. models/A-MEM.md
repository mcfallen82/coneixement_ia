---
title: A-MEM — Agentic Memory for LLM Agents
category: models
node_id: "model:a_mem"
node_type: "model"
model_family: agent_memory
architecture: dynamic_linked_memory_notes
authors:
  - Wujiang Xu
  - Zujie Liang
  - Kai Mei
  - Hang Gao
  - Juntao Tan
  - Yongfeng Zhang
tags:
  - model
  - memoria-agentica
  - zettelkasten
sources:
  - https://papers.nips.cc/paper_files/paper/2025/hash/19909c36f51abc4856b4560aff3d36d6-Abstract-Conference.html
  - https://papers.nips.cc/paper_files/paper/2025/file/19909c36f51abc4856b4560aff3d36d6-Paper-Conference.pdf
  - https://github.com/WujiangXu/A-mem
  - https://github.com/agiresearch/A-mem
related_concepts:
  - "[[1. Wiki/1.2. conceptes/memoria_agentica]]"
  - "[[1. Wiki/1.2. conceptes/evolucio_de_la_memoria]]"
  - "[[1. Wiki/1.2. conceptes/zettelkasten]]"
  - "[[1. Wiki/1.2. conceptes/embeddings]]"
  - "[[1. Wiki/1.2. conceptes/RAG]]"
related_models:
  - "[[1. Wiki/1.3. models/llm_wiki]]"
status: reviewed
created: 2026-09-25
updated: 2026-09-25
---

# A-MEM — memòria agentiva basada en notes

## Quin problema resol?

Un agent pot conservar interaccions i recuperar-ne fragments, però això no garanteix que relacioni una experiència nova amb records anteriors ni que revisi com els interpreta. **A-MEM** (Xu i col·laboradors, NeurIPS 2025) proposa una arquitectura de memòria externa que organitza notes connectades i n'actualitza la representació contextual quan arriba informació nova. És un **sistema de memòria per a agents**, no un nou model de llenguatge entrenat ni una implementació de la wiki d'aquest projecte.

## Intuïció

Pensa en una nota sobre un projecte que només adquireix tot el sentit després d'una conversa posterior. A-MEM cerca notes anteriors relacionades, proposa connexions i pot ampliar-ne les descripcions contextuals. S'inspira en [[1. Wiki/1.2. conceptes/zettelkasten|Zettelkasten]], però el model decideix automàticament com indexar i vincular records.

## Arquitectura i flux documentats

1. **Construcció de la nota:** d'una interacció es conserva el contingut i la data; un LLM genera paraules clau, etiquetes i descripció contextual. Un codificador transforma el text de la nota enriquida en un [[1. Wiki/1.2. conceptes/embeddings|vector]]. La nota també pot guardar enllaços a altres notes.
2. **Generació d'enllaços:** la semblança entre vectors selecciona notes candidates (*top-k*). El LLM examina les candidates i decideix quines connexions són pertinents; la proximitat vectorial per si sola no estableix una relació validada.
3. **Evolució:** davant la nota nova, el LLM pot revisar el context, les paraules clau i les etiquetes de notes antigues recuperades. Aquesta operació és la [[1. Wiki/1.2. conceptes/evolucio_de_la_memoria|evolució de la memòria]]; cal distingir-la de reescriure la font original.
4. **Consulta:** es representa la pregunta com un vector, es recuperen notes pertinents i s'aporta el context seleccionat a l'agent. El diagrama del treball també descriu l'accés a records relacionats mitjançant enllaços.

La idea distintiva és actuar **durant l'escriptura i la reorganització**, a més de fer recuperació durant la lectura. Vegeu [[1. Wiki/1.2. conceptes/memoria_agentica|memòria agentiva]] i [[1. Wiki/1.2. conceptes/RAG|RAG]].

## Què mostren els experiments?

Els autors avaluen preguntes sobre converses llargues amb **LoCoMo** i també presenten resultats amb **DialSim**. Comparen diverses bases, com ReadAgent, MemoryBank i MemGPT, i diferents models de llenguatge. A la taula principal de LoCoMo, amb GPT-4o-mini, l'F1 de preguntes temporals és **45,85** per a A-MEM i **25,52** per a MemGPT; en preguntes adversàries, la base LoCoMo obté **69,23** davant **50,03** d'A-MEM. L'ablació amb aquest model indica una caiguda del rendiment quan es retira l'evolució, i una caiguda més gran en retirar també la generació d'enllaços. Són **resultats reportats pels autors**, dependents del conjunt de dades, el model i la configuració; no mesuren directament la qualitat d'una wiki de fitxes científiques.

## Relació amb la wiki de coneixement

[[1. Wiki/1.3. models/llm_wiki|LLM Wiki]] descriu una base de pàgines llegibles i revisables que es consolida amb les fonts. A-MEM estudia la **memòria operativa d'un agent** formada a partir d'interaccions. Les dues idees poden complementar-se: una capa automatitzada podria *proposar* enllaços o millores a la wiki, però això és una **aplicació inferida**, no una capacitat demostrada pel paper en aquest repositori. La procedència, la revisió humana i l'historial de les fitxes continuen sent necessaris.

El projecte disposa d'una [adaptació operativa de revisió de notes](../../2.%20Skills/memory-evolution/README.md) i un [script de candidates](../../scripts/memory_candidates.py). El script només ordena fitxes per similitud lèxica; l'agent o la persona que fa la ingesta llegeix les candidates i justifica els canvis abans d'acceptar-los. Aquesta integració **no executa A-MEM** ni reprodueix els seus resultats experimentals.

## Límits i preguntes obertes

- Una connexió semànticament plausible pot ser falsa, trivial o redundant; cal comprovar-ne el significat i la font.
- Canviar metadades o context d'una nota antiga pot introduir interpretacions retroactives; convé conservar el text original i l'historial en usos documentals.
- El cost d'escriptura inclou crides al LLM per construir, connectar i fer evolucionar les notes; menys context per resposta no implica necessàriament menys cost total.
- La millora en preguntes sobre converses no prova una millora en una wiki de documents ni que A-MEM superi sempre una cerca més simple.
- El treball no substitueix una ontologia explícita ni una verificació de les relacions proposades.

## Fonts

- Xu, Wujiang, i col·laboradors. [*A-Mem: Agentic Memory for LLM Agents*](https://papers.nips.cc/paper_files/paper/2025/hash/19909c36f51abc4856b4560aff3d36d6-Abstract-Conference.html), NeurIPS 2025; [text complet](https://papers.nips.cc/paper_files/paper/2025/file/19909c36f51abc4856b4560aff3d36d6-Paper-Conference.pdf). Consultat el 2026-09-25. Font primària de l'arquitectura i els experiments.
- [Codi dels experiments](https://github.com/WujiangXu/A-mem) i [implementació del sistema](https://github.com/agiresearch/A-mem), projectes dels autors. Consultats el 2026-09-25.
