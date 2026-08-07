# AGENTS.md — Governança de la wiki d’aprenentatge d’IA

## 1. Objectiu i abast

Aquest repositori és una wiki d’aprenentatge acumulatiu sobre intel·ligència artificial. Serveix per estudiar, ordenar, relacionar i revisar coneixement sobre:

- intel·ligència artificial, aprenentatge automàtic i aprenentatge profund;
- models de llenguatge, models generatius i sistemes multimodals;
- enginyeria de prompts i del context;
- sistemes de coneixement, Obsidian, PKM i automatització;
- programació, dades i eines necessàries per construir aplicacions amb IA.

No és un sistema d’aprenentatge de documents financers, ni una wiki de finances o economia. Les finances només es poden utilitzar com a exemple pràctic quan ajudin a entendre un concepte d’IA.

## 2. Governança

Aquest és l’únic document principal de governança. S’ha de llegir abans d’actuar. No es crearan fitxers alternatius com CLAUDE.md o GEMINI.md, llevat que Joan ho demani explícitament.

## 3. Estructura obligatòria

~~~text
.obsidian/
0. Raw/
├── 0.1. llibres/
└── 0.2./
1. Wiki/
├── 1.1. autors/
├── 1.2. conceptes/
└── 1.3. models/
2. Skills/
3. Dashboards/
4. Templates/
├── 90.1. templates_fitxes/
└── 90.2. docs_support/
index.md
log.md
hot.md
.manifest.json
~~~

- 0. Raw/ conserva fonts originals o còpies de treball.
- 1. Wiki/ conté fitxes permanents d’autors, conceptes i models.
- 2. Skills/ conté procediments reutilitzables.
- 3. Dashboards/ conté consultes i vistes d’Obsidian.
- 4. Templates/ conté plantilles i documents de suport.

## 4. Fitxes permanents

Les fitxes de 1. Wiki/ utilitzen frontmatter YAML:

~~~yaml
---
title: Nom de la fitxa
category: conceptes
tags:
  - inteligencia-artificial
sources: []
related_concepts: []
related_models: []
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
~~~

La categoria ha de correspondre a la carpeta. Les fonts han de ser verificables. Cada fitxa ha de començar per una definició i, segons la complexitat, incloure intuïció, funcionament, exemple, aplicacions, limitacions, relacions i fonts. Cal separar dades documentades, interpretació i qüestions obertes quan hi hagi risc de confusió.

## 5. Flux d’ingesta

Cada font nova segueix aquest procés:

~~~text
font a 0. Raw/
    ↓
lectura i classificació
    ↓
extracció de conceptes, autors i models
    ↓
comprovació de duplicats i sinònims
    ↓
actualització o creació de fitxes
    ↓
wikilinks i fonts
    ↓
actualització de l’índex
    ↓
registre a log.md
    ↓
actualització de .manifest.json
~~~

Abans de crear una fitxa cal comprovar si ja existeix el mateix concepte, un sinònim, una fitxa d’entitat relacionada o una pàgina que només necessita actualització. La wiki compila coneixement persistent; no és només un repositori per recuperar fragments en el moment de respondre.

## 6. Skills operatives

Les skills de 2. Skills/ descriuen procediments, no governança:

- wiki-ingest.md: processar fonts d’aprenentatge;
- wiki-update.md: actualitzar fitxes i resoldre duplicats;
- wiki-lint.md: auditar estructura, YAML, fonts i enllaços.

Quan una skill contradigui aquest document, preval AGENTS.md.

## 7. Enllaços i Obsidian

Els wikilinks han d’apuntar a fitxes reals i conservar el nom de carpeta quan sigui necessari:

~~~markdown
[[1. Wiki/1.2. conceptes/embeddings]]
[[1. Wiki/1.3. models/transformer]]
~~~

Les consultes Dataview han d’utilitzar les rutes actuals i camps coherents, especialment title, status, sources i updated. No s’han de modificar automàticament .obsidian/ ni configuracions de GitHub sense necessitat.

## 8. Estil i fonts

La redacció principal és en català. Primer s’explica la intuïció i després el detall tècnic. Els termes anglesos es mantenen només quan són l’estàndard, i s’expliquen en català.

Les fonts es conserven al frontmatter i en una secció final. Les afirmacions documentades, les interpretacions pedagògiques i les hipòtesis no s’han de barrejar.

## 9. Registre i manifest

Cada canvi estructural o ingesta significativa s’ha d’afegir a log.md amb data, operació, fitxers afectats, resultat i incidències. Quan es processa una font, .manifest.json ha d’indicar-ne la ruta, tipus, estat i fitxes creades o actualitzades.

## 10. Validació

Abans de publicar cal comprovar:

- carpetes obligatòries i fitxers esperats;
- absència de rutes antigues en enllaços i consultes;
- YAML vàlid en fitxes modificades;
- fonts i wikilinks plausibles;
- índex, log i manifest actualitzats;
- preservació dels fitxers d’Obsidian i GitHub.
