---
title: Prompting
node_id: "concept:prompting"
node_type: "concept"
category: conceptes
tags:
  - inteligencia-artificial
  - models-de-llenguatge
sources:
  - https://platform.openai.com/docs/guides/prompt-engineering
related_concepts: []
related_models: []
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Prompting

## Definició

El prompting és la pràctica de formular instruccions i preguntes per obtenir un resultat útil d’un model d’intel·ligència artificial.

## Per què és important?

Permet treballar amb models generals sense programar una solució específica per a cada tasca. El valor apareix quan la petició és clara i el resultat es pot revisar.

## Intuïció

És una conversa orientada a un objectiu: comença amb una petició, observa el resultat i concreta la següent instrucció.

## Funcionament

Una estructura pràctica és: objectiu + informació + tasca + format + criteris. El prompting pot ser directe, amb exemples, iteratiu o basat en una plantilla.

## Exemple

1. Demanar un resum.
2. Identificar què falta.
3. Sol·licitar una comparació.
4. Demanar fonts i separar fets d’inferències.
5. Convertir el resultat en una fitxa Markdown.

## Relacions

- [[prompt]]
- [[prompt_engineering]]
- [[context_engineering]]
- [[LLM]]

## Aplicacions

- aprendre conceptes;
- analitzar documents;
- generar esborranys;
- revisar textos;
- explorar alternatives.

## Limitacions i errors habituals

- confiar en una única resposta;
- no proporcionar context;
- no establir criteris d’èxit;
- confondre exploració amb un procés reproduïble.

## Fonts

- [OpenAI — Prompt engineering guide](https://platform.openai.com/docs/guides/prompt-engineering).
