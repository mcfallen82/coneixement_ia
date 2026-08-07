---
title: Ajustament fi
node_id: "concept:ajust_fi"
node_type: "concept"
category: conceptes
tags:
  - llm
  - entrenament
  - adaptacio
sources:
  - https://arxiv.org/abs/2106.09685
  - https://arxiv.org/abs/2203.02155
related_concepts:
  - [[1. Wiki/1.2. conceptes/backpropagation]]
  - [[1. Wiki/1.2. conceptes/alineament_dels_llm]]
related_models:
  - [[1. Wiki/1.3. models/transformer]]
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Ajustament fi

## Què és?

L’ajustament fi és continuar l’entrenament d’un model preentrenat amb dades seleccionades per adaptar-lo a una tasca, estil, domini o comportament concret.

## Per què és important?

Permet aprofitar el coneixement i les capacitats generals d’un model sense entrenar-lo des de zero. En una eina d’anàlisi documental, per exemple, pot adaptar el model a un format de sortida o a una terminologia específica.

## Intuïció

És semblant a incorporar una empresa ja operativa a un nou mercat: la base productiva existeix, però cal adaptar processos, llenguatge i prioritats. Les dades d’ajustament no creen necessàriament coneixement general nou; modifiquen la manera com el model respon.

## Tipus principals

- SFT: ajustament supervisat amb exemples d’entrada i resposta desitjada.
- Ajustament de domini: adapta vocabulari i patrons d’un àmbit.
- Ajustament d’instruccions: ensenya a seguir ordres.
- Alineament amb preferències: optimitza respostes que els avaluadors prefereixen.

## Exemple pràctic

Per entrenar un assistent de lectura de 10-K, un conjunt d’exemples podria relacionar fragments amb una sortida estructurada: risc, evidència, període, font i interpretació. El model aprendria el format i alguns patrons, però les dades d’actualitat continuarien requerint recuperació externa.

## Limitacions i errors habituals

- confondre ajustament amb actualització fiable de coneixement;
- utilitzar dades massa petites, repetitives o esbiaixades;
- provocar sobreajustament o pèrdua de capacitats generals;
- avaluar només exemples d’entrenament;
- ignorar que el model pot memoritzar dades sensibles.

## Relacions

L’ajustament fi utilitza [[1. Wiki/1.2. conceptes/backpropagation]] i pot complementar [[1. Wiki/1.2. conceptes/attention]]. En models grans es pot fer amb tècniques eficients com [[1. Wiki/1.3. models/LoRA]] i combinar-se amb [[1. Wiki/1.2. conceptes/raonament_numeric_documental]].

## Fonts

- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685).
- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155).