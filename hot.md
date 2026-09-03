# Hot

## Documentació pública de les skills

- 2026-09-03: revisada tota la carpeta `2. Skills/` per a ús públic.
- Els README de cada skill expliquen ara **què resol, quan utilitzar-la, què fa i quin resultat produeix** abans d'enllaçar al procediment complet.
- `2. Skills/README.md` funciona com a mapa d'entrada amb una taula **necessitat → skill** i enllaços Markdown navegables des de GitHub.
- Eliminades dependències operatives de `0. Raw/` a les skills d'arquitectura, manteniment, consulta, estat, importació i exportació.
- L'arquitectura compartida passa a ser **fonts externes verificables → Wiki → governança i esquema**.
- Les skills afectades utilitzen `coneixement_ia` com a nom actual del projecte, en lloc de `ia_knowledge`.
- `vault-skill-factory` conserva el nom de carpeta històric, però queda explícit que no depèn d'Obsidian ni d'un vault.

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
