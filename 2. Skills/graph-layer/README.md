# graph-layer

Skill per mantenir una **capa de graf lleugera i reconstruïble** sobre les fitxes Markdown.

## Quan utilitzar-la

Quan es vulguin estudiar nodes, relacions, hubs, components o enllaços candidats sense convertir el projecte en una base de dades gràfica ni en un sistema GraphRAG.

## Què fa

- tracta Markdown com a font principal;
- valida `node_id`, `node_type` i les relacions acceptades;
- manté les relacions revisades a `graph/relations.json`;
- utilitza `scripts/graph_scan.py` per comprovar i generar el graf derivat;
- diferencia relacions documentades, candidates i inferides.

## Resultat esperat

Un graf que es pot regenerar a partir de la wiki i que no introdueix una nova font de veritat paral·lela.

## Procediment complet

Vegeu [graph-layer.md](graph-layer.md).
