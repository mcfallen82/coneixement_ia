---
title: "LLM"
node_id: "concept:llm"
node_type: "concept"
---


---
title: Models de llenguatge de gran escala
category: conceptes
tags:
  - inteligencia-artificial
  - models-de-llenguatge
  - deep-learning
sources:
  - https://arxiv.org/abs/2005.14165
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Models de llenguatge de gran escala (LLM)

## Definició

Un **LLM** és un model neuronal entrenat amb grans col·leccions de text per predir i generar seqüències de llenguatge. La sigla prové de Large Language Model.

## Per què és important?

Permet resumir, traduir, classificar, respondre preguntes, escriure codi i transformar documents. La utilitat depèn de les dades, del model, del context i de les instruccions.

## Intuïció

Un LLM ha après patrons estadístics del llenguatge. Quan genera una resposta, calcula quins tokens poden venir després del text disponible. Aquesta fluïdesa no garanteix que cada afirmació sigui certa.

## Funcionament

1. El text es divideix en tokens.
2. Els tokens es transformen en representacions numèriques.
3. Un Transformer calcula les relacions entre tokens.
4. El model prediu una distribució de probabilitat per al token següent.
5. El procés es repeteix fins a completar la resposta.

Durant el preentrenament, el model ajusta els seus paràmetres. Després pot rebre ajustos amb instruccions, preferències humanes o dades específiques.

## Exemple

En una wiki, un LLM pot llegir una font, extreure conceptes, comparar-los amb fitxes existents i proposar una actualització. La font continua sent necessària perquè el model pot ometre dades o inventar connexions.

## Relacions

- [[prompting]]
- [[prompt_engineering]]
- [[context_engineering]]
- [[RAG]]
- [[frontmatter]]

## Aplicacions

- síntesi i classificació de documents;
- assistents de programació;
- recuperació de coneixement;
- transformació de text en Markdown;
- tutorització.

## Limitacions i errors habituals

- confondre fluïdesa amb exactitud;
- assumir que el model recorda dades actuals;
- ignorar la procedència;
- donar massa context irrellevant;
- valorar-lo amb un únic exemple.

## Fonts

- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165).
