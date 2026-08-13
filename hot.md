## Frontmatter de conceptes normalitzat

S’han revisat les 39 fitxes conceptuals. Els camps de relació ara tenen un format YAML homogeni i el validador detecta estructures imbricades incorrectes.

## Prova activa: metadades gràfiques de la wiki

Les fitxes de `1. Wiki/` ja incorporen `node_id` i `node_type`. Executa `python scripts/graph_scan.py --check` i `--stats` abans i després d’afegir coneixement nou. Les relacions semàntiques acceptades continuen al registre `graph/relations.json`.

# Hot

## Activitat recent

- 2026-08-13: incorporat article d'Eugeniu Ghelbur sobre graph engineering i creada la fitxa `graph_engineering`.

- 2026-08-13: `0. Raw/` queda com a carpeta plana; els tipus de font es diferencien pel frontmatter.

- 2026-08-13: revisio visual incorporada al lint i `index.md` actualitzat com a punt de revisio frequent.

- 2026-08-13: auditada la governanca; `AGENTS.md` i `wiki_lint.py` ara reflecteixen llibres i la nova estructura de skills.

- 2026-08-13: compactats els README de `2. Skills/`; els procediments complets passen a `<skill>/<skill>.md`.

- 2026-08-13: reorganitzada 2. Skills/ perque cada skill tingui carpeta propia i README.md descriptiu.

- 2026-08-13: normalitzats els avisos de `wiki_lint.py` i corregits els wikilinks trencats del graf; les comprovacions passen amb 0 advertiments i 0 enllaços trencats.

- 2026-08-13: actualitzats els dashboards de wiki, aprenentatge, auditoria, fonts i graf perquè funcionin com a entrada i seguiment estàtic de `1. Wiki`.

- 2026-08-13: ampliada la fitxa de *How Big Things Get Done* i creades les fitxes de Bent Flyvbjerg i Dan Gardner.

- 2026-08-07: posada en marxa de la capa gràfica lleugera basada en Markdown.

- 2026-08-07: recerca i processament de grafs aplicats als models de llenguatge.

- 2026-08-07: recerca pilot sobre ajustament, alineament, LoRA i avaluació de models.

## Prioritats actuals

- Executar `python scripts/graph_scan.py --check` i registrar l’evolució de nodes, arestes candidates i enllaços trencats.
- Revisar progressivament les relacions candidates abans de convertir-les en acceptades.

- Definir tipus, direcció, procedència i confiança de les relacions de la wiki.
- Estudiar l’adaptació del patró d’obsidian-second-brain: escàner determinista, relacions tipades, subgrafs i visualització.
- Estudiar una futura exportació de les fitxes a un graf formal.
- Comparar GraphRAG amb una RAG vectorial en un corpus petit.

- Revisar i completar les fitxes de `1. Wiki/1.2. conceptes/`.
- Mantenir actualitzades les fitxes de models a `1. Wiki/1.3. models/`.
- Mantenir `3. Dashboards/dashboard_wiki.md` sincronitzat quan s'afegeixin autors, conceptes, models o llibres.
- Convertir les notes de lectura en fonts i fitxes relacionades.
- Mantenir `wiki_lint.py` i `graph_scan.py --check` amb 0 errors, 0 advertiments i 0 wikilinks trencats després de cada reorganització.

- Incorporar les fonts i conclusions de la recerca pilot a les fitxes relacionades.
