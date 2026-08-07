---
title: Skills
node_id: "concept:skills"
node_type: "concept"
category: conceptes
tags:
  - agents
  - automatitzacio
  - inteligencia-artificial
sources:
  - https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
related_concepts:
  - "[[scaffold]]"
related_models: []
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Skills

## Definició

Una skill és un procediment reutilitzable que descriu com executar una tasca concreta. En sistemes d’agents, pot incloure instruccions, criteris, plantilles i eines.

## Per què és important?

Converteix coneixement operatiu dispers en una capacitat que un agent pot activar quan la tasca ho requereix.

## Intuïció

Una skill s’assembla a una recepta: no és només informació sobre un tema, sinó una seqüència d’accions, entrades, sortides i comprovacions.

## Funcionament

Una skill ben definida especifica objectiu, quan s’ha d’utilitzar, requisits, passos, format de sortida i validació. Ha de ser prou modular per reutilitzar-la en altres tasques.

## Exemple

Una skill de wiki-ingest pot llegir una font, detectar conceptes, comparar-los amb fitxes existents, actualitzar pàgines i registrar el canvi.

## Relacions

- [[scaffold]]

- [[context_engineering]]
- [[second_brain]]
- [[LLM]]
- [[frontmatter]]

## Aplicacions

- agents de programació;
- ingestió de fonts;
- revisió de fitxes;
- automatització documental;
- fluxos de treball repetibles.

## Limitacions i errors habituals

- descriure només el tema i no el procediment;
- crear skills massa grans;
- no indicar la validació;
- duplicar instruccions de governança;
- no definir les entrades i sortides.

## Fonts

- [Anthropic — Equipping agents with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).
