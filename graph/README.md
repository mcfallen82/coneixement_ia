# Capa gràfica consultable

Aquesta carpeta conté la representació gràfica derivada de `coneixement_ia`.

Markdown continua sent la font principal. El graf és una representació derivada que ajuda a identificar nodes i relacions, separar enllaços candidats de relacions revisades, detectar destinacions inexistents i experimentar amb camins, hubs i components.

La capa no introdueix una base de dades, un servidor ni GraphRAG. Utilitza Python i PyYAML, la mateixa dependència que `wiki_lint.py`.

## Fitxers

- relations.json: registre curat de relacions tipades revisades manualment.
- relation-vocabulary.yaml: vocabulari inicial i regles bàsiques.
- graph.json: sortida generada opcionalment per l’escàner.
- scripts/graph_scan.py: construeix i valida el graf.

## Execució

Des de l’arrel del repositori:

    python scripts/graph_scan.py --check --strict
    python scripts/graph_scan.py --output graph/graph.json
    python scripts/graph_scan.py --stats

El mode estricte retorna `PASS` quan les relacions acceptades són vàlides i no hi ha wikilinks trencats ni ambigus. Els wikilinks sense relació tipada es conserven com a arestes candidates.

Cada parella candidata `source → target` apareix una sola vegada. Els camps `occurrences` i `origins` conserven quantes aparicions s'han detectat i a quines línies. Això evita que el frontmatter i el cos d'una fitxa inflin artificialment els graus del graf.

`--stats` diferencia relacions acceptades, candidates úniques i aparicions de wikilinks. També mostra la cobertura de nodes amb relacions acceptades i compta els nodes aïllats dins dels components.

## Contracte inicial

Cada node té node_id, node_type i path.

Cada aresta té source, target, relation, status, claim_type, confidence i evidence quan existeix.

Les relacions acceptades es mantenen manualment a `relations.json`. El vocabulari canònic és `relation-vocabulary.yaml`; l'escàner el carrega directament i valida les evidències internes. Les arestes candidates serveixen per trobar connexions que poden ser revisades més endavant.
