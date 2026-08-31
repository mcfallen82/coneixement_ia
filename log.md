## 2026-08-31 — Consolidació de la documentació d’Ar9av

- AUDITORIA: comparats els documents `resum_ar9av_obsidian_wiki_beagle_ai.md` i `resum_ar9av_obsidian_wiki_ia_knowledge.md`.
- DOCUMENTACIÓ: consolidats en una única versió canònica els conceptes generalitzables sobre Karpathy, Ar9av, Obsidian, agents, skills, ingesta, traçabilitat i deduplicació.
- NETEJA: eliminades les seccions específiques de Beagle AI, empreses, documents SEC i decisions financeres.
- ELIMINACIÓ: suprimit el document redundant `4. Templates/90.2. docs_support/resum_ar9av_obsidian_wiki_beagle_ai.md`.
- REFERÈNCIES: actualitzat `4. Templates/90.2. docs_support/README.md` i corregits els enllaços de la wiki al document canònic.
- RESULTAT: el document vigent és `4. Templates/90.2. docs_support/resum_ar9av_obsidian_wiki_ia_knowledge.md`; no hi ha referències actives a Beagle AI en la documentació revisada.

## 2026-08-13 - Ingesta Raw: graph engineering segons Eugeniu Ghelbur

- FONT RAW: incorporat `0. Raw/graph_engineering_decoded_two_definitions_2026-08-11.md`, atribuit a Eugeniu Ghelbur i publicat a The AI Operator.
- AVALUACIO: la font aporta informacio nova; diferencia graph engineering com a graf de coneixement i com a topologia d'agents.
- FITXA: creada `1. Wiki/1.2. conceptes/graph_engineering.md`.
- ENLLACOS: actualitzades les fitxes `Ghelbur, Eugeniu.md` i `grafs_i_models_de_llenguatge.md`, a mes de `index.md` i `dashboard_fonts.md`.
- VALIDACIO: `wiki_lint.py` i `graph_scan.py --check` passen amb 0 errors.

## 2026-08-13 - Integracio plana de `0. Raw`

- ESTRUCTURA: integrats els documents de `0. Raw/` a la carpeta base i retirat el criteri actiu per subcarpetes.
- FRONTMATTER: afegits o normalitzats `raw_type`, `source_type`, `processing_status`, `status`, `created`, `updated`, `previous_path` i `processed_into` quan correspon.
- GOVERNANCA: actualitzats `AGENTS.md`, `0. Raw/README.md`, `index.md` i el dashboard de fonts per descriure el nou criteri.
- VALIDACIO: `wiki_lint.py` comprova ara que els documents Raw siguin a la carpeta base i tinguin frontmatter minim.

## 2026-08-13 - Revisio visual i index frequent

- AUDITORIA VISUAL: revisats errors visibles de codificacio en fitxers Markdown, Python, JSON i YAML fora de `.git` i `.obsidian`.
- CORRECCIO: normalitzats fitxers de seguiment i README amb restes de mojibake.
- INDEX: actualitzat `index.md` amb una seccio de revisio frequent segons el flux d'`AGENTS.md`.
- VALIDACIO: `wiki_lint.py` ara detecta errors visuals de codificacio i continua passant amb 0 errors; `graph_scan.py --check` passa amb 0 errors.

## 2026-08-13 - Auditoria de governanca del projecte

- AUDITORIA: revisada la coherencia entre l'estructura real del projecte, `AGENTS.md`, `wiki_lint.py` i `graph_scan.py`.
- GOVERNANCA: actualitzat `AGENTS.md` per incloure `1. Wiki/1.4. llibres/`, `0. Raw/` i la convencio interna de `2. Skills/<skill>/README.md` + `<skill>.md`.
- VALIDACIO: `wiki_lint.py` comprova ara les fitxes de llibres i l'estructura interna de skills.
- RESULTAT: `wiki_lint.py` passa amb 0 errors i 0 advertiments; `graph_scan.py --check` passa amb 0 errors i 0 wikilinks trencats.

## 2026-08-13 - Neteja compacta de `2. Skills`

- ESTRUCTURA: cada carpeta de skill conserva un `README.md` breu i un fitxer `<skill>.md` amb el procediment complet.
- ABAST: canvi limitat a la documentacio operativa de `2. Skills/`.
- VALIDACIO: `wiki_lint.py` i `graph_scan.py --check` passen amb 0 errors.

## 2026-08-13 - Reorganitzacio de `2. Skills`

- ESTRUCTURA: cada skill de `2. Skills/` s'ha mogut a una carpeta propia amb document `README.md`.
- NAVEGACIO: actualitzat `2. Skills/README.md` per apuntar als nous README de cada skill.
- VALIDACIO: `scripts/wiki_lint.py` ara resol tambe els enllacos curts cap a `2. Skills/<skill>/README.md`.
- TRACABILITAT: actualitzats `log.md`, `hot.md` i `.manifest.json`.
## 2026-08-13 — Normalització d'advertiments i wikilinks trencats

- VALIDACIÓ: corregida la resolució de wikilinks curts a `scripts/wiki_lint.py`.
- GRAF: corregits els 13 wikilinks trencats detectats en fitxes de models; els enllaços a plantilles s'han convertit a enllaços Markdown normals quan no havien de ser nodes del graf.
- FRONTMATTER: normalitzades fitxes de models amb camps antics `font`, `data`, `descripcio`, `estat` i `conceptes`.
- TAGS: afegit `tags` a fitxes d'autors i models que no en tenien.
- SEGUIMENT: actualitzats `hot.md`, `log.md` i `.manifest.json`.
- RESULTAT: `wiki_lint.py` passa amb 0 errors i 0 advertiments; `graph_scan.py --check` passa amb 0 errors i 0 wikilinks trencats.

## 2026-08-13 — Actualització integral de dashboards i seguiment

- DASHBOARDS: actualitzats `3. Dashboards/README.md`, `dashboard_aprenentatge.md`, `dashboard_auditoria.md`, `dashboard_fonts.md` i `graf.md`.
- COBERTURA: afegides referències explícites a `dashboard_wiki.md`, `1. Wiki/1.4. llibres/`, fonts brutes principals i fitxers de seguiment.
- SEGUIMENT: actualitzat `hot.md` per substituir la referència a consultes Dataview per dashboards Markdown estàtics.
- MANIFEST: registrada l'operació de sincronització de dashboards.
- VALIDACIÓ: executats `wiki_lint.py` i `graph_scan.py --check`; queden advertiments preexistents de normalització i wikilinks antics.

## 2026-08-13 — Dashboard d'entrada a `1. Wiki`

- DASHBOARD: creat `3. Dashboards/dashboard_wiki.md` com a entrada estàtica a autors, conceptes, models i llibres.
- NAVEGACIÓ: actualitzats `3. Dashboards/README.md`, `3. Dashboards/dashboard_aprenentatge.md` i `index.md`.
- ABAST: no s'ha introduït dependència de plugins d'Obsidian; el dashboard és Markdown estàtic.

## 2026-08-13 — Ampliació de *How Big Things Get Done*

- FONT RAW: creat `0. Raw/recerca_how_big_things_get_done_2026-08-13.md` amb fonts editorials, institucionals i acadèmiques consultades.
- LLIBRE: ampliada i estructurada la fitxa `1. Wiki/1.4. llibres/how_big_things_get_done.md`.
- AUTORS: creades les fitxes `1. Wiki/1.1. autors/Flyvbjerg, Bent.md` i `1. Wiki/1.1. autors/Gardner, Dan.md`.
- GRAF: adaptat `scripts/graph_scan.py` perquè la carpeta `1. Wiki/1.4. llibres/` es classifiqui com a font.
- TRAÇABILITAT: actualitzats `index.md`, `hot.md` i `.manifest.json`.
- VALIDACIÓ: executats `wiki_lint.py` i `graph_scan.py --check`; queden advertiments de normalització preexistents.

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

- FONT RAW: creat `0. Raw/recerca_grafs_obsidian_second_brain_2026-08-07.md`.
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

- FONT RAW: creat `0. Raw/recerca_grafs_models_llm_2026-08-07.md` amb tres rondes de recerca i 11 fonts primàries o oficials.
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
- TRAÇABILITAT: conservat el dossier a 0. Raw/ i actualitzats índex, hot i manifest.

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

- FONT: completada la transcripció de `Taula_Lectures.xlsx` a `0. Raw/Taula_Lectures.md`, amb els cinc blocs originals i el tractament assignat a cada entrada.
- CONCEPTES: creades 13 fitxes de fonaments de deep learning, tokenització, atenció i raonament numèric documental.
- MODELS: creades 6 fitxes per a Transformer, WaveNet, GPT, GPT-2, nanoGPT i FinBERT.
- CLASSIFICACIÓ: FinQA, TAT-QA, DocFinQA i els recursos d’avaluació s’han registrat com a datasets, benchmarks o casos d’aplicació.
- ENLLAÇOS: afegides relacions entre la font bruta, les fitxes creades i les fitxes existents de LLM i RAG.

## 2026-08-07 — Autors, README i adaptació de skills

- AUTORS: creades 11 fitxes d’autor i afegides relacions bidireccionals.
- README: revisats i creats els README de les carpetes principals.
- SKILLS: adaptades les operatives d’ingesta, actualització, consulta, context, deduplicació, enllaços, taxonomia, dashboards, síntesi, recerca, captura, exportació, importació, reconstrucció, validació i manteniment.
- ADAPTACIÓ: substituïdes les rutes genèriques de `concepts`, `entities` i `references` per les carpetes pròpies del projecte.
## 2026-08-13 - Dashboards sense plugins

- GOVERNANCA: actualitzat `AGENTS.md` per indicar que els dashboards han de funcionar com a Markdown estatic i no poden dependre de Dataview, Canva, Kanban ni plugins equivalents.
- DASHBOARDS: retirats els blocs Dataview de `index.md`, `3. Dashboards/dashboard_aprenentatge.md`, `3. Dashboards/dashboard_auditoria.md`, `3. Dashboards/graf.md` i `2. Skills/wiki-dashboard/README.md`.
- NETEJA: eliminats `dashboard.canvas` i `kanban.md` del projecte.
- MANIFEST: actualitzat el nom del repositori a `mcfallen82/coneixement_ia` i registrada l'operacio de neteja.
- VALIDACIO: `wiki_lint.py` i `graph_scan.py --check` passen amb 0 errors bloquejants.
