---
authors:
  - "[[Karpathy, Andrej]]"
font: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
data: 2026-04-30
tags:
  - model
  - wiki
descripcio: Construir una base de coneixement personal en format 'wiki' amb LLM
estat: ok
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
3. **INSTRUCCIONS**: Fitxer de instruccions com [[conceptes/Agents_MD|Agents_MD]] o `CLAUDE.md` que explica al model com ha d’organitzar, actualitzar i mantenir la *wiki*.

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
## Fitxers especials & Estructura

Perquè el sistema sigui manejable, **Karpathy** recomana dos fitxers especials: `index.md` i `log.md`. L’`index.md` és el mapa de contingut: enumera les pàgines de la *wiki*, amb una breu descripció i organització per categories.

El `log.md` és el registre cronològic: apunta què s’ha incorporat, què s’ha preguntat, què s’ha modificat i quan. L’índex et dona orientació; el registre et dona memòria del procés.

---
## Filosofia

El problema d’una base de coneixement és guardar informació, mantenir-la connectada i actualitzada. Les persones sovint abandonen les *wikis* perquè el manteniment es torna feixuc: actualitzar enllaços, revisar resums, detectar contradiccions, moure notes, crear pàgines noves. 

**Karpathy** proposa que el model faci aquesta feina mecànica, mentre l’humà decideix les fonts, fa les preguntes bones i interpreta el significat. Aplicat a una *vault* manual d’**Obsidian**, el missatge pràctic seria: comença petit, conserva les fonts originals, crea notes *Markdown* interconnectades, mantén un índex i un registre, i fes revisions periòdiques per evitar que la *wiki* perdi coherència.

---
## Documents de suport

**[[plantilla_creacio_wikis_locals_codex_obsidian|Plantilla Creació Wikis]]** - Plantilla per a la creació d'un fitxer inicial `AGENTS.md` mitjançant **ChatGPT**.

---
## Referències

Models derivats o inspirats en **Wiki LLM**.

**[[obsidian_wiki|Obsidian Wiki]]**
**[[obsidian_second_brain|Obsidian Second Brain]]**
