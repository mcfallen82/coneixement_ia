---
title: QMD
node_id: "concept:qmd"
node_type: "concept"
category: conceptes
tags:
  - recuperacio
  - cerca-semantica
  - gestio-del-coneixement
sources:
  - https://github.com/tobi/qmd
  - https://github.com/tobi/qmd/blob/86d2365d17fc682e491c2c53d1e4a884aee8682a/README.md
related_concepts:
  - "[[RAG]]"
  - "[[context_engineering]]"
  - "[[second_brain]]"
  - "[[frontmatter]]"
  - "[[LLM]]"
  - "[[1. Wiki/1.2. conceptes/avaluacio_de_models]]"
related_models: []
status: reviewed
created: 2026-08-07
updated: 2026-10-19
---

# QMD — cerca local híbrida

## Definició

QMD és un cercador local de documents que combina cerca lèxica BM25, vectors i reordenació. La descripció es basa en el README oficial al commit `86d2365d17fc682e491c2c53d1e4a884aee8682a`, consultat el 2026-10-19.

## Modes i cost

| Ordre | Mecanisme | Criteri d'ús |
|---|---|---|
| `qmd search` | BM25 | coincidències lèxiques; cost baix |
| `qmd vsearch` | vectors | similitud semàntica; necessita embeddings |
| `qmd query` | expansió, fusió lèxica/vectorial i reordenació | més treball local; qualitat a comprovar |

La fusió utilitza RRF (*Reciprocal Rank Fusion*). No pressuposis que el mode més complex sempre millora el resultat.

## Exemple didàctic

Amb una col·lecció `wiki` ja indexada:

```bash
qmd search "GraphRAG" -c wiki
qmd vsearch "com conservar experiència entre sessions" -c wiki
qmd query "com validar revisions de memòria" -c wiki --json
```

Compara els documents recuperats i comprova les fonts abans d'utilitzar-los en [[RAG]].

## Integració i manteniment

Disposa de servidor MCP per consultar i recuperar documents. Cal actualitzar l'índex després dels canvis i regenerar els vectors quan correspongui. Els filtres tipats requereixen metadades sota `qmd.metadata`; el [[frontmatter]] ordinari d'aquesta wiki no s'hi converteix automàticament.

## Límits i aplicació proposada

Recuperació no equival a veritat. Mesura rellevància, omissions i latència amb preguntes pròpies, incloent català i sinònims. Consulta [[1. Wiki/1.2. conceptes/avaluacio_de_models|avaluació de models]]. QMD és opcional: aquesta actualització no l'instal·la ni acredita el seu rendiment aquí.

## Relacions

- [[RAG]]
- [[context_engineering]]
- [[second_brain]]
- [[frontmatter]]
- [[LLM]]
- [[1. Wiki/1.2. conceptes/avaluacio_de_models]]

## Fonts

- [QMD — repositori oficial](https://github.com/tobi/qmd).
- [README de QMD, versió consultada](https://github.com/tobi/qmd/blob/86d2365d17fc682e491c2c53d1e4a884aee8682a/README.md). Documentació tècnica del projecte, commit del 2026-10-15; consulta del 2026-10-19.
