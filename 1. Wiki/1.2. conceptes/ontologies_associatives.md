---
title: Ontologies associatives
node_id: "concept:ontologies_associatives"
node_type: "concept"
category: conceptes
tags:
  - gestio-del-coneixement
  - ontologies
  - representacio-del-coneixement
sources:
  - https://www.w3.org/standards/semanticweb/ontology
  - https://www.w3.org/TR/skos-reference/
related_concepts:
  - "[[wiki]]"
  - "[[zettelkasten]]"
  - "[[second_brain]]"
  - "[[frontmatter]]"
  - "[[RAG]]"
  - "[[grafs_i_models_de_llenguatge]]"
  - "[[GraphRAG]]"
related_models: []
status: reviewed
created: 2026-08-07
updated: 2026-09-25
---

# Ontologies associatives

## Definició

En aquesta wiki, «ontologia associativa» és un terme de treball per a una xarxa de conceptes i relacions documentades. No implica que la wiki implementi una ontologia formal amb axiomes, inferència o llenguatges com OWL; les relacions tipades es registren en una capa gràfica lleugera.

## Per què és important?

Permet passar d’una col·lecció de documents a una estructura on les relacions també contenen informació.

## Intuïció

Una llista diu quins conceptes existeixen. Una ontologia també diu com es relacionen: un LLM és un tipus de model, el RAG recupera fonts per donar context i el frontmatter descriu una nota.

## Funcionament

Cal identificar entitats, tipus de relació i regles mínimes. Les relacions poden ser jeràrquiques, causals, temporals, de dependència o d’exemple.

## Exemple

[[RAG]] combina recuperació i generació amb un [[LLM]]; una implementació pot utilitzar [[QMD]] per recuperar informació i camps de [[frontmatter]] per filtrar notes.

## Relacions

- [[wiki]]
- [[zettelkasten]]
- [[second_brain]]
- [[frontmatter]]
- [[RAG]]
- [[grafs_i_models_de_llenguatge]]
- [[GraphRAG]]

## Relació amb els grafs aplicats als LLM

Una ontologia pot servir com a esquema per construir un graf de coneixement. GraphRAG pot utilitzar aquesta estructura per recuperar entitats, relacions i comunitats. En aquesta wiki, els wikilinks assenyalen connexions candidates; `graph/relations.json` recull una selecció de relacions tipades, orientades i revisades manualment amb evidència i fonts. Aquesta capa no és una ontologia formal completa.

## Aplicacions

- mapes de coneixement;
- wikis assistides;
- recuperació semàntica;
- documentació de projectes;
- sistemes d’agents.

## Limitacions i errors habituals

- confondre qualsevol enllaç amb una relació semàntica;
- crear taxonomies massa rígides;
- afegir relacions sense utilitat;
- no distingir entre relació documentada i interpretació.

## Fonts

- [W3C — Ontology and the Semantic Web](https://www.w3.org/standards/semanticweb/ontology).
- [W3C — SKOS Simple Knowledge Organization System Reference](https://www.w3.org/TR/skos-reference/).
