
---
title: Enginyeria del context
category: conceptes
tags:
  - inteligencia-artificial
  - models-de-llenguatge
  - agents
sources:
  - https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Enginyeria del context

## Definició

És el disseny i la gestió de tota la informació que un model rep, conserva o recupera durant una tasca.

## Per què és important?

La qualitat depèn de la informació que el model veu en el moment adequat. Afegir informació també pot introduir soroll, redundància o dades antigues.

## Intuïció

El prompting decideix què demanem. L’enginyeria del context dissenya l’entorn informatiu complet que permet respondre.

## Funcionament

Els processos principals són:

- **Escriure:** guardar conclusions, instruccions o estat.
- **Seleccionar:** recuperar informació rellevant.
- **Comprimir:** resumir sense perdre evidència.
- **Aïllar:** separar el context segons la tasca o l’agent.

En una wiki, això implica conservar fonts, consultar l’índex, recuperar fitxes relacionades i evitar duplicats.

## Exemple

Per analitzar un concepte nou, un agent pot rebre la font original, la fitxa existent, les instruccions d’AGENTS.md i una plantilla. No necessita rebre tota la wiki.

## Relacions

- [[prompting]]
- [[prompt_engineering]]
- [[RAG]]
- [[LLM]]
- [[frontmatter]]

## Aplicacions

- wikis actualitzables;
- agents amb memòria;
- sistemes documentals;
- recerca;
- processos amb rols separats.

## Limitacions i errors habituals

- omplir el context amb tota la informació;
- recuperar fragments poc relacionats;
- comprimir fins a perdre la font;
- compartir dades entre agents sense necessitat;
- no controlar l’estat ni la vigència.

## Fonts

- [Anthropic — Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
