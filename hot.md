# Hot

## Conversió a projecte públic

- 2026-09-03: eliminada la carpeta pública de materials bruts.
- 2026-09-03: eliminada la configuració local `.obsidian/` i desacoblada la documentació operativa de qualsevol editor concret.
- La traçabilitat passa a basar-se en **fonts externes verificables**, URLs i referències bibliogràfiques.
- Markdown és el format canònic compartit; cada col·laborador pot utilitzar l'editor, IDE o gestor de coneixement que prefereixi.
- `.gitignore` exclou configuracions locals d'editors i gestors de coneixement.
- `README.md`, `AGENTS.md`, `index.md`, `dashboard_fonts.md`, `wiki-ingest`, `wiki-research` i `wiki_lint.py` s'han adaptat al nou model.
- Els nous col·laboradors no han de pujar còpies locals de fonts ni configuracions personals d'aplicacions.

## Documentació canònica

- La plantilla canònica és `4. Templates/90.2. docs_support/plantilla_wiki_neutra_replicable.md`.
- El document de suport canònic és `4. Templates/90.2. docs_support/resum_ar9av_wiki_ia_knowledge.md`.

## Prova activa: metadades gràfiques de la wiki

Les fitxes de `1. Wiki/` incorporen `node_id` i `node_type`. Executa `python scripts/graph_scan.py --check` i `--stats` abans i després d'afegir coneixement nou. Les relacions semàntiques acceptades continuen al registre `graph/relations.json`.

## Prioritats actuals

- Revisar que totes les fitxes tinguin fonts externes verificables.
- Revisar progressivament les relacions candidates abans de convertir-les en acceptades.
- Mantenir `3. Dashboards/dashboard_wiki.md` sincronitzat quan s'afegeixin autors, conceptes, models o llibres.
- Mantenir `wiki_lint.py` i `graph_scan.py --check` sense errors després de cada reorganització.
