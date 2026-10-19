---
title: AGENTS.md
node_id: "concept:agents_md"
node_type: "concept"
category: conceptes
tags:
  - agents
  - governança
  - programació
sources:
  - https://agents.md/
  - https://arxiv.org/abs/2602.11988v3
related_concepts:
  - "[[1. Wiki/1.2. conceptes/avaluacio_de_models]]"
  - "[[1. Wiki/1.2. conceptes/context_engineering]]"
related_models:
  - "[[1. Wiki/1.3. models/model_agents_md]]"
status: reviewed
created: 2026-08-07
updated: 2026-10-19
---

# AGENTS.md

## Definició

Un AGENTS.md és un document de context i governança per a agents de programació. Explica com han de treballar dins d’un repositori.

## Per què és important?

Concentra objectius, convencions, ordres, proves, límits i criteris de validació en un lloc que un agent pot llegir abans d’actuar.

## Intuïció

És semblant a un manual d’incorporació per a una persona nova en un projecte: indica què ha de saber abans de modificar res.

## Funcionament

Pot descriure:

- l’objectiu del projecte;
- l’estructura de carpetes;
- les convencions de noms;
- les ordres de proves;
- les zones que no s’han de tocar;
- el procés de revisió i lliurament.

En aquest repositori, AGENTS.md és la font única de governança. Les fitxes de coneixement expliquen conceptes; AGENTS.md estableix les regles de treball.

## Exemple

Abans d’actualitzar una fitxa, l’agent ha de llegir AGENTS.md, comprovar si el concepte ja existeix, conservar les fonts i validar els enllaços.

## Relacions

- [[LLM]]
- [[context_engineering]]
- [[skills]]
- [[frontmatter]]

## Aplicacions

- projectes de codi;
- wikis assistides;
- fluxos amb Codex;
- documentació operativa;
- col·laboració entre persones i agents.

## Limitacions i errors habituals

- duplicar instruccions en diversos fitxers;
- donar ordres contradictòries;
- no actualitzar el document quan canvia el projecte;
- confondre governança amb una fitxa de contingut;
- descriure intencions sense criteris verificables.

## Evidència i ús proporcionat

Gloaguen i col·laboradors, a *Evaluating AGENTS.md* (versió 3, 2026-09-29), estudien agents de programació en tasques de repositoris. No troben una millora general de l'èxit amb aquests fitxers i observen més d'un 20% de cost d'inferència addicional de mitjana. Els agents segueixen les instruccions, però els resums generals del repositori no aporten necessàriament valor. La revisió més recent destaca la utilitat d'explicitar pràctiques no estàndard i d'avaluar qualsevol pretensió de millora.

**Límit:** el resultat depèn dels agents, repositoris i tasques estudiats; no demostra que aquest document sobri ni que eliminar normes millori aquesta wiki.

## Criteri pràctic per a una wiki

Com a adaptació proposada, concentra aquí les convencions difícils d'inferir, les ordres fiables i els límits imprescindibles. Trasllada les explicacions temàtiques a les fitxes. Abans d'afegir instruccions redundants, compara versions en tasques representatives amb èxit, errors i cost. La fitxa de [[1. Wiki/1.3. models/model_agents_md|generació d'AGENTS.md]] explica una eina; [[1. Wiki/1.2. conceptes/avaluacio_de_models|l'avaluació]] comprova si el document ajuda.

## Fonts

- [AGENTS.md](https://agents.md/).
- Gloaguen et al., [Evaluating AGENTS.md](https://arxiv.org/abs/2602.11988v3), prepublicació, v3 del 2026-09-29; consultada el 2026-10-19. Evidència empírica, no validació d’aquesta wiki.
