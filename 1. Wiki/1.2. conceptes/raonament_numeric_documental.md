---
title: Raonament numèric sobre documents
node_id: "concept:raonament_numeric_documental"
node_type: "concept"
category: conceptes
tags:
  - document-qa
  - raonament-numeric
  - dades-tabulars
sources:
  - https://arxiv.org/abs/2109.00122
  - https://aclanthology.org/2021.acl-long.254/
  - https://arxiv.org/abs/2401.06915
related_concepts:
  - "[[1. Wiki/1.2. conceptes/RAG]]"
  - "[[1. Wiki/1.2. conceptes/tokenitzacio_i_bpe]]"
  - "[[1. Wiki/1.2. conceptes/LLM]]"
related_models:
  - "[[1. Wiki/1.3. models/FinBERT]]"
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Raonament numèric sobre documents

## Definició

És la capacitat d’extreure evidència d’un document, combinar text i taules, executar càlculs i justificar la resposta amb fragments verificables.

## Per què és important?

Els models de llenguatge són fluids, però els documents amb xifres exigeixen una cadena d’evidència: localitzar la taula correcta, interpretar les unitats, calcular i citar. FinQA, TAT-QA i DocFinQA són referències per estudiar aquest problema.

## Funcionament simplificat

1. segmentar i indexar el document;
2. recuperar el text i les taules pertinents;
3. identificar valors, unitats, períodes i definicions;
4. calcular o consultar una eina;
5. respondre amb el resultat i la cita.

## Exemple

Per calcular la variació interanual d’un marge, no n’hi ha prou amb recuperar dos percentatges: cal confirmar que corresponen al mateix indicador, període i base de comparació.

## Limitacions i errors habituals

Els LLM poden seleccionar la fila errònia, ignorar una unitat de milers o inventar un càlcul plausible. La verificació programàtica i les cites són requisits, no una millora opcional.

## Fonts

- [FinQA](https://arxiv.org/abs/2109.00122).
- [TAT-QA](https://aclanthology.org/2021.acl-long.254/).
- [DocFinQA](https://arxiv.org/abs/2401.06915).
