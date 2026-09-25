---
title: LLM Wiki
category: models
node_id: "model:llm_wiki"
node_type: "model"
model_family: knowledge_management
architecture: llm_assisted_wiki
authors:
  - "[[Karpathy, Andrej]]"
tags:
  - model
  - wiki
sources:
  - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
  - https://papers.nips.cc/paper_files/paper/2025/file/19909c36f51abc4856b4560aff3d36d6-Paper-Conference.pdf
related_concepts:
  - "[[1. Wiki/1.2. conceptes/memoria_agentica]]"
  - "[[1. Wiki/1.2. conceptes/evolucio_de_la_memoria]]"
related_models:
  - "[[1. Wiki/1.3. models/A-MEM]]"
status: active
created: 2026-04-30
updated: 2026-09-25
---
# LLM WIKI

[[LLM]] Wiki, proposa una manera de construir una base de coneixement personal en format *wiki*, normalment amb fitxers *Markdown* i eines com **Obsidian**.
## Idea central

Substituir el model típic de “pujar documents i preguntar” per una *wiki* persistent que acumula coneixement amb el temps. En un sistema [[RAG]] clàssic, el model recupera fragments cada vegada que li fas una pregunta; en canvi, en un sistema LLM_Wiki el coneixement es sintetitza, connecta i actualitza en pàgines estables.

El model exposat per **Karpathy** té un efecte *compounder*; guanya valor a mesura que s'afegeixen fonts, preguntes i connexions.

---
## Arquitectura

L’arquitectura bàsica consta de tres capes principals:

1. **FONTS BRUTES (*raw*):** articles, llibres, informes, notes, imatges o documents originals, que no s’han de modificar i actuen com a font principal.
2. **WIKI**: Col·lecció de pàgines *Markdown* amb resums, pàgines de conceptes, entitats, comparacions, síntesis i enllaços interns. 
3. **INSTRUCCIONS**: Fitxer de instruccions com [[1. Wiki/1.2. conceptes/AGENTS_MD|Agents_MD]] o `CLAUDE.md` que explica al model com ha d’organitzar, actualitzar i mantenir la *wiki*.

---
## Flux de treball

El flux de treball consta de tres operacions principals: 

**ingerir** ➡️ **consultar** ➡️ **revisar** 

La descripció d'aquests processos és el següent:

1. **INGERIR:** Afegir una nova font, llegir-la, resumir-la i connectar-la amb les pàgines ja existents.
2. **CONSULTAR:** Fer preguntes a partir de la *wiki*, no només dels documents originals; les bones respostes també es poden convertir en noves notes. 
3. **REVISAR:** Fer manteniment periòdic: detectar pàgines òrfenes, contradiccions, conceptes sense nota pròpia, afirmacions antigues o enllaços interns que falten. 

La *wiki* no és només un arxiu, és un organisme viu que es va refinant.

---
## Relació amb A-MEM

[[1. Wiki/1.3. models/A-MEM|A-MEM]] és una arquitectura publicada el 2025 per a la [[1. Wiki/1.2. conceptes/memoria_agentica|memòria d'agents]] basada en notes derivades d'interaccions. Hi ha un paral·lelisme amb les pàgines interconnectades d'aquesta wiki: en arribar una nota nova, A-MEM pot generar enllaços i fer [[1. Wiki/1.2. conceptes/evolucio_de_la_memoria|evolucionar]] els atributs contextuals de notes anteriors.

La connexió entre els dos sistemes és **comparativa**, no una derivació documentada del model de Karpathy. El paper d'A-MEM avalua preguntes sobre diàlegs llargs; no demostra que l'actualització automàtica millori la qualitat d'una wiki documental. En aquesta wiki, qualsevol enllaç o revisió proposats per un agent requereixen una font i una revisió abans d'incorporar-se com a coneixement estable.

---
## Fitxers especials & Estructura

Perquè el sistema sigui manejable, **Karpathy** recomana dos fitxers especials: `index.md` i `log.md`. L’`index.md` és el mapa de contingut: enumera les pàgines de la *wiki*, amb una breu descripció i organització per categories.

El `log.md` és el registre cronològic: apunta què s’ha incorporat, què s’ha preguntat, què s’ha modificat i quan. L’índex et dona orientació; el registre et dona memòria del procés.

---
## Filosofia

El problema d’una base de coneixement és guardar informació, mantenir-la connectada i actualitzada. Les persones sovint abandonen les *wikis* perquè el manteniment es torna feixuc: actualitzar enllaços, revisar resums, detectar contradiccions, moure notes, crear pàgines noves. 

**Karpathy** proposa que el model faci aquesta feina mecànica, mentre l’humà decideix les fonts, fa les preguntes bones i interpreta el significat. Aplicat a una *vault* manual d’**Obsidian**, el missatge pràctic seria: comença petit, conserva les fonts originals, crea notes *Markdown* interconnectades, mantén un índex i un registre, i fes revisions periòdiques per evitar que la *wiki* perdi coherència.

---
## Documents de suport

**[Plantilla canònica de wiki](../../4.%20Templates/90.2.%20docs_support/plantilla_wiki_neutra_replicable.md)** - Patró reutilitzable per estructurar una base de coneixement i les seves instruccions.

---
## Referències

Models derivats o inspirats en **Wiki LLM**.

**[[obsidian_wiki|Obsidian Wiki]]**
**[[1. Wiki/1.3. models/obsidian_second_brain_karpathy_rebuilt|Obsidian Second Brain]]**
