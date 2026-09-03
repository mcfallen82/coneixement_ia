---
title: Obsidian Second Brain Karpathy Rebuilt
category: models
node_id: "model:obsidian_second_brain_karpathy_rebuilt"
node_type: "model"
model_family: knowledge_management
architecture: ai_first_obsidian_vault
authors:
  - "[[Ghelbur, Eugeniu]]"
tags:
  - model
  - wiki
sources:
  - https://theaioperator.io/p/i-rebuilt-karpathys-llm-wiki-heres
related_concepts:
  - "[[PKM]]"
status: active
created: 2026-07-09
updated: 2026-08-13
---
# 🤔 I rebuilt Karpathy's LLM Wiki gist: what's missing

## 1. Ingesta, no afegir

Diferenciar entre una *wiki* que creix d'una *wiki* que apren. Reescriure força a que cada pàgina mostri la millor resposta.

Solució: Una wiki que aprèn.
## 2. Les contradiccions s'han de resoldre, no senyalar

**Karpathy** indica que has de resoldre les contradiccions manualment. Quan acumules centenars de pàgines, els errors s'acumulen ràpidament.

**Solució:** Un procés que escaneja el *vault*. Identifica contraccions a través de les pàgines. Les resol a través de:
	- Data de la font
	- Autoritat de la font
	- Nivells de confiança explícits
Passa per davant la millor nota (claim) de totes. Els claims descartats, passen a l'arxiu. 
## 3. Els patrons han de sorgir sense demanar-ho

És una oportunitat perduda no identificar els patrons. El cervell t'hauria de dir: "has comentat això cinc vegades"

**Solució:** Un segon cervell fa les sintesis. Escaneja el vault i busca temes recorrents, contradiccions amagades entre persones i les seves decisions actuals. Connexions entre projectes que semblen independnets. 
## 4. El manteniment programat, no puntual

El manteniment de **Karpathy** funciona quan li dius. És a dir, mai. 

Solució: Un procés intermitent que funciona cada nit a la recerca d'errors. Un procés setmanal que fa un checking sanitari. No has de posar en marxa cap ordre manualment.
## 5. Notes escrites per la IA, no pels humans

El major punt en contra. Totes les [[PKM]] ([[zettelkasten]], [[second_brain]], [[evergreen_notes]]) optimitzen fitxer per lectura humana. La Wiki de Karpathy està pensada pels humans.

Alternativa: Principi AI-First Vault

## AI-First Vault

Totes les notes han de tenir:
- a `## For future ChatGPT` 
- machine-readable frontmatter
- mandatory wikilinks
- recency markers per external claim
- source URLs preserved verbatim
- confidence levels where applicable
- self-contained context so the note can be retrieved standalone

The inversion is uncomfortable for anyone who has invested in a beautiful Obsidian vault.

## 📒Documents derivats i referències

**[[1. Wiki/1.3. models/obsidian_second_brain_karpathy_rebuilt|Obsidian Second Brain]]** - Projecte principal de [[Ghelbur, Eugeniu]]
**[[llm_wiki|LLM Wiki]]** - Model de jardí digital on les idees creixen i es connecten mitjançant models [[LLM]].
**[[wiki|Wiki]]** - Com a sistema viu de coneixement
