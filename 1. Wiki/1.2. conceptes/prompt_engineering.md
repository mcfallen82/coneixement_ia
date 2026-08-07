---
title: "prompt engineering"
node_id: "concept:prompt_engineering"
node_type: "concept"
---


---
title: Enginyeria de prompts
category: conceptes
tags:
  - inteligencia-artificial
  - models-de-llenguatge
  - evaluacio
sources:
  - https://platform.openai.com/docs/guides/prompt-engineering
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Enginyeria de prompts

## Definició

És el procés sistemàtic de dissenyar, provar, avaluar i millorar instruccions perquè produeixin resultats útils i consistents.

## Per què és important?

Una petició que funciona una vegada pot fallar en altres casos. L’enginyeria introdueix criteris, proves i control de versions.

## Intuïció

S’assembla a millorar un model d’anàlisi: cal definir el resultat esperat, provar-lo amb diversos casos i corregir els errors observats.

## Funcionament

1. Defineix l’objectiu.
2. Escriu una primera versió.
3. Prepara casos de prova.
4. Estableix una rúbrica.
5. Compara els resultats.
6. Modifica una variable cada vegada.
7. Conserva la versió útil.

## Exemple

Una rúbrica d’extracció pot valorar exactitud, fidelitat a la font, separació entre fets i inferències, format i consistència.

## Relacions

- [[prompt]]
- [[prompting]]
- [[context_engineering]]
- [[LLM]]

## Aplicacions

- plantilles d’extracció;
- assistents de codi;
- síntesi de fonts;
- classificació;
- automatització.

## Limitacions i errors habituals

- provar amb un únic cas;
- canviar moltes coses alhora;
- no mesurar omissions;
- afegir instruccions redundants;
- confondre una resposta brillant amb un sistema fiable.

## Fonts

- [OpenAI — Prompt engineering guide](https://platform.openai.com/docs/guides/prompt-engineering).
