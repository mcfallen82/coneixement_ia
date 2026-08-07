## 2026-08-07 — Recerca i processament del concepte scaffold

- RECERCA: creat el dossier `0. Raw/0.2./recerca_scaffold_2026-08-07.md` amb fonts d’Anthropic, OpenAI, arXiv i Oxford University Press.
- CONCEPTE: creada la fitxa `1. Wiki/1.2. conceptes/scaffold.md`.
- DISTINCIÓ: separats els sentits d’agent scaffold/harness i scaffolding pedagògic.
- CONNEXIONS: afegits enllaços amb enginyeria del context, skills, avaluació de models i enginyeria de prompts.
- GRAF: incorporades tres relacions acceptades a `graph/relations.json`.
- PENDENT: comparar experimentalment scaffolds simples i complexos en tasques de la wiki.

## 2026-08-07 — Auditoria del frontmatter de conceptes

- AUDITORIA: revisades les 39 fitxes de `1. Wiki/1.2. conceptes/`.
- CORRECCIÓ: afegits `related_concepts: []` i `related_models: []` quan faltaven.
- CORRECCIÓ: normalitzats els wikilinks YAML perquè siguin cadenes i no llistes imbricades.
- VALIDACIÓ: `wiki_lint.py` comprova ara que aquests camps siguin llistes de cadenes.
- ABAST: no s’ha modificat el contingut pedagògic de les fitxes.

## 2026-08-07 — Activació de la capa gràfica a `1. Wiki`

- MIGRACIÓ: afegits `node_id` estable i `node_type` explícit a les 72 fitxes de `1. Wiki/`.
- TIPUS: `author`, `concept`, `model` i `source` segons la ubicació de la fitxa.
- VALIDACIÓ: `graph_scan.py --check` passa a exigir aquestes metadades i detecta incoherències.
- GOVERNANÇA: actualitzats `AGENTS.md`, `graph-layer.md` i les plantilles de fitxes.
- ABAST: Markdown continua sent la font principal; no s’introdueixen base de dades gràfica ni GraphRAG.

## 2026-08-07 — Posada en marxa de la capa gràfica lleugera

- IMPLEMENTACIÓ: creats `graph/relations.json`, `graph/relation-vocabulary.yaml` i `scripts/graph_scan.py`.
- MODEL: nodes derivats de les fitxes Markdown; relacions acceptades separades dels wikilinks candidats.
- INTEGRACIÓ: afegits `graph-layer.md`, el dashboard `3. Dashboards/graf.md` i documentació de governança.
- VALIDACIÓ: preparat el control de destinacions, vocabulari, procedència, confiança i enllaços trencats.
- ABAST: no s’introdueixen base de dades gràfica ni GraphRAG; la sortida JSON és una instantània reconstruïble per a proves.

## 2026-08-07 — Recerca sobre grafs a obsidian-second-brain

- FONT RAW: creat `0. Raw/0.2./recerca_grafs_obsidian_second_brain_2026-08-07.md`.
- ABAST: documentat l’escàner determinista de wikilinks, les relacions tipades, la visualització Canvas i la connexió entre dominis.
- CLASSIFICACIÓ: separats graf d’enllaços, graf semàntic, eina de pensament, GraphRAG i GNN.
- APLICACIÓ: identificat un patró reutilitzable per a `ia_knowledge`: Markdown → escàner → subgraf → assistència LLM.
- FITXES PERMANENTS: no se n’han creat, perquè el coneixement conceptual ja està cobert per les fitxes de grafs i la guia de creació de wikis amb grafs.
- PENDENT: valorar una implementació específica de l’escàner i de les relacions tipades adaptada a les rutes d’`ia_knowledge`.

# Registre de canvis

## 2026-08-07 — Guia per crear wikis amb grafs

- DOCUMENT DE SUPORT: creat `4. Templates/90.2. docs_support/guia_creacio_wikis_amb_grafs.md`.
- ABAST: documentats nodes, arestes tipades, direcció, procedència, confiança i nivells de maduresa del graf.
- ASSISTÈNCIA: definida una sortida revisable perquè els agents proposin relacions sense convertir inferències en fets.
- GRAPH-RAG: establerts criteris per diferenciar una wiki connectada, un graf consultable i un sistema GraphRAG.
- AUDITORIA: afegides comprovacions específiques per a nodes orfes, arestes trencades, relacions vagues, duplicats i components aïllats.

## 2026-08-07 — Recerca i processament de grafs aplicats als models de llenguatge

- FONT RAW: creat `0. Raw/0.2./recerca_grafs_models_llm_2026-08-07.md` amb tres rondes de recerca i 11 fonts primàries o oficials.
- CONCEPTES: creades les fitxes sobre grafs i LLM, GraphRAG, Graph of Thoughts i xarxes neuronals de graf.
- MODEL/MARC: creada la fitxa de G-Retriever, classificat com a marc de GraphQA que combina recuperació, GNN i LLM.
- RELACIONS: ampliades les fitxes RAG i ontologies associatives.
- TRAÇABILITAT: actualitzats l’índex, hot i manifest.
- PENDENTS: tipus de relació, procedència i confiança de les arestes; exportació del vault a un graf formal; comparació amb RAG vectorial.

## 2026-08-07 — Activació de la recerca i ampliació de coneixement

- SKILL: reforçada wiki-research amb tres rondes, jerarquia de fonts, confiança i criteris d’aturada.
- CONFIGURACIÓ: afegit research-config.md amb temes prioritaris i criteris de qualitat.
- RECERCA: completades tres rondes sobre ajustament fi, alineament, LoRA i avaluació.
- FITXES: creades 3 fitxes de conceptes i 1 fitxa de tècnica/model.
- TRAÇABILITAT: conservat el dossier a 0. Raw/0.2./ i actualitzats índex, hot i manifest.

## 2026-08-07 — Ajust final del validador

- FALSOS POSITIUS: limitat el control de camps i rutes antigues a fitxes i plantilles auditables; la documentació de governança no es compta com a contingut obsolet.
- MODE NORMAL: manté els errors estructurals bloquejants i informa la resta com a advertiments.
- MODE ESTRICTE: continua disponible per convertir el deute de normalització en errors.

## 2026-08-07 — Robustesa operativa i auditoria executable

- GOVERNANÇA: reforçat AGENTS.md amb contractes d’entrada, sortida, validació i criteris de seguretat.
- ACTIVACIÓ: establert l’ordre obligatori de les skills per a operacions de lectura, escriptura i manteniment.
- VALIDACIÓ: creat `scripts/wiki_lint.py`, que comprova estructura, frontmatter YAML, categories, models, wikilinks, camps obsolets, duplicats i manifest.
- AUTOMATITZACIÓ: creat `.github/workflows/wiki-lint.yml` per executar la validació en canvis de `main` i `agent/reorganitza-wiki-llm`.
- DASHBOARD: corregida la consulta d’auditoria per utilitzar els camps normalitzats i documentar que les fonts Raw tenen el manifest com a estat canònic.
- SKILLS: actualitzat `2. Skills/README.md` i reforçat `wiki-lint.md` amb modes normal i estricte.
- AUDITORIA INICIAL: el workflow va detectar 296 incidències, principalment fitxes antigues sense frontmatter complet i enllaços de l’estructura anterior.
- CORRECCIÓ DE PROCÉS: el validador ara separa errors estructurals bloquejants del deute de normalització; `--strict` permet exigir la migració completa.
- WORKFLOW: execució final completada correctament (run 22), amb 0 errors bloquejants i 245 advertiments de normalització.
- PENDENT: normalitzar progressivament les fitxes antigues i executar `python scripts/wiki_lint.py --strict` fins obtenir zero advertències.

## 2026-08-07 — Processament de la taula de lectures

- FONT: completada la transcripció de `Taula_Lectures.xlsx` a `0. Raw/0.1. llibres/Taula_Lectures.md`, amb els cinc blocs originals i el tractament assignat a cada entrada.
- CONCEPTES: creades 13 fitxes de fonaments de deep learning, tokenització, atenció i raonament numèric documental.
- MODELS: creades 6 fitxes per a Transformer, WaveNet, GPT, GPT-2, nanoGPT i FinBERT.
- CLASSIFICACIÓ: FinQA, TAT-QA, DocFinQA i els recursos d’avaluació s’han registrat com a datasets, benchmarks o casos d’aplicació.
- ENLLAÇOS: afegides relacions entre la font bruta, les fitxes creades i les fitxes existents de LLM i RAG.

## 2026-08-07 — Autors, README i adaptació de skills

- AUTORS: creades 11 fitxes d’autor i afegides relacions bidireccionals.
- README: revisats i creats els README de les carpetes principals.
- SKILLS: adaptades les operatives d’ingesta, actualització, consulta, context, deduplicació, enllaços, taxonomia, dashboards, síntesi, recerca, captura, exportació, importació, reconstrucció, validació i manteniment.
- ADAPTACIÓ: substituïdes les rutes genèriques de `concepts`, `entities` i `references` per les carpetes pròpies del projecte.
