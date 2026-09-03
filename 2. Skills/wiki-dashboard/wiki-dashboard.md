# wiki-dashboard

## Finalitat

Crear vistes consultables per controlar l'estat i l'evolucio de la wiki sense dependre de plugins d'Obsidian.

## Vistes recomanades

- fitxes modificades recentment;
- conceptes sense fonts;
- models pendents de completar;
- autors amb obres relacionades;
- fonts encara no processades;
- fitxes per tags o categories;
- fitxes orfes.

## Implementacio sense plugins

Els dashboards han de ser Markdown estatic i no han de dependre de Dataview, Canva, Kanban ni altres plugins d'Obsidian. Quan calgui una comprovacio dinamica, referencia `scripts/wiki_lint.py`, `scripts/graph_scan.py`, `hot.md`, `log.md` i `.manifest.json`.

Utilitza les rutes actuals i els camps `title`, `category`, `sources`, `status` i `updated` com a criteris de revisio. Si en el futur s'afegeix una eina de consulta, ha de ser opcional i no pot convertir-se en dependencia obligatoria del projecte.

## Validacio

Comprova que cada vista sigui llegible sense plugins, que no depengui de camps antics i que els fitxers referenciats existeixin.
