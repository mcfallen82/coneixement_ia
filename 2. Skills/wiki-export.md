# wiki-export

## Finalitat

Exportar la xarxa de fitxes d’ia_knowledge a formats reutilitzables.

## Nodes

Cada fitxa de 1. Wiki/ és un node amb ruta, title, category, tags, status, sources i updated.

## Enllaços

Extreu els wikilinks i les relacions dels camps related_concepts, related_models, authors i related_authors. Conserva origen, destí i tipus de relació quan sigui conegut.

## Formats

- graph.json: nodes i edges per a eines pròpies;
- graph.graphml: intercanvi amb eines de graf;
- Markdown resumit: exportació llegible;
- OKF: només si es respecta l’esquema i el mapatge de frontmatter.

## Seguretat

No exportis fitxers de 0. Raw/ per defecte si contenen còpies completes de fonts. Indica quines categories i fitxes s’han exportat i conserva la procedència.