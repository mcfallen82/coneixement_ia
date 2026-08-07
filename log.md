# Registre de canvis

## 2026-08-07 — Robustesa operativa i auditoria executable

- GOVERNANÇA: reforçat AGENTS.md amb contractes d’entrada, sortida, validació i criteris de seguretat.
- ACTIVACIÓ: establert l’ordre obligatori de les skills per a operacions de lectura, escriptura i manteniment.
- VALIDACIÓ: creat `scripts/wiki_lint.py`, que comprova estructura, frontmatter YAML, categories, models, wikilinks, camps obsolets, duplicats i manifest.
- AUTOMATITZACIÓ: creat `.github/workflows/wiki-lint.yml` per executar la validació en canvis de `main` i `agent/reorganitza-wiki-llm`.
- DASHBOARD: corregida la consulta d’auditoria per utilitzar els camps normalitzats i documentar que les fonts Raw tenen el manifest com a estat canònic.
- SKILLS: actualitzat `2. Skills/README.md` i reforçat `wiki-lint.md` amb entrades, sortides, errors bloquejants i advertències.
- RESULTAT: pendent d’executar el primer workflow de GitHub Actions sobre la branca.

## 2026-08-07 — Processament de la taula de lectures

- FONT: completada la transcripció de `Taula_Lectures.xlsx` a `0. Raw/0.1. llibres/Taula_Lectures.md`, amb els cinc blocs originals i el tractament assignat a cada entrada.
- CONCEPTES: creades 13 fitxes de fonaments de deep learning, tokenització, atenció i raonament numèric documental.
- MODELS: creades 6 fitxes per a Transformer, WaveNet, GPT, GPT-2, nanoGPT i FinBERT.
- CLASSIFICACIÓ: FinQA, TAT-QA, DocFinQA i els recursos d’avaluació s’han registrat com a datasets, benchmarks o casos d’aplicació; no s’han etiquetat incorrectament com a models.
- ENLLAÇOS: afegides relacions entre la font bruta, les fitxes creades i les fitxes existents de LLM i RAG.
- VALIDACIÓ: revisats frontmatter, rutes de wikilinks i fonts de les 19 fitxes noves.

## 2026-08-07 — Autors i relacions

- REFERÈNCIES: afegides les fitxes de Mike Caulfield i Robin Sloan, citats dins del cos de les fitxes de models.
- AUTORS: creades 11 fitxes a `1. Wiki/1.1. autors/`.
- ENLLAÇOS: afegides relacions bidireccionals entre autors, models i conceptes.
- NORMALITZACIÓ: substituït el camp antic `autor` per `authors` en les fitxes de models.
- CORRECCIÓ: normalitzat `Matuschak` i corregida la grafia anterior `Matuschack`.
- PLANTILLA: afegit el camp `authors` a `plantilla_model.md`.

## 2026-08-07 — README de carpetes

- README: revisats i ampliats els README existents de Raw, Wiki, Skills, Dashboards i Templates.
- README: creats els README que faltaven a l’arrel, `1. Wiki/` i `4. Templates/`.
- VALIDACIÓ: confirmada l’existència i el contingut dels README principals de la branca.

## 2026-08-07 — Adaptació de skills d’obsidian-wiki

- ARQUITECTURA: adaptat el model Raw → Wiki → Esquema a l’estructura d’ia_knowledge.
- SKILLS: incorporades les operatives d’ingesta, actualització, consulta, context, deduplicació, enllaços, taxonomia, dashboards, síntesi, recerca, captura, exportació, importació, reconstrucció, validació i manteniment.
- ADAPTACIÓ: substituïdes les rutes genèriques de concepts, entities i references per les carpetes pròpies del projecte.
- ABAST: excloses les skills específiques d’historials d’agents i de gestió de diversos vaults.
