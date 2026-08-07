# Registre de canvis

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
