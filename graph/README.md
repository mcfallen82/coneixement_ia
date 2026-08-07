# Capa gràfica lleugera

Aquesta carpeta conté la primera implementació del graf de coneixement de ia_knowledge.

Markdown continua sent la font principal. El graf és una representació derivada que ajuda a identificar nodes i relacions, separar enllaços candidats de relacions revisades, detectar destinacions inexistents i experimentar amb camins, hubs i components.

La capa no introdueix una base de dades, un servidor ni GraphRAG. Es pot executar amb la biblioteca estàndard de Python.

## Fitxers

- relations.json: registre curat de relacions tipades revisades manualment.
- relation-vocabulary.yaml: vocabulari inicial i regles bàsiques.
- graph.json: sortida generada opcionalment per l’escàner.
- scripts/graph_scan.py: construeix i valida el graf.

## Execució

Des de l’arrel del repositori:

    python scripts/graph_scan.py --check
    python scripts/graph_scan.py --output graph/graph.json
    python scripts/graph_scan.py --stats

El mode check retorna PASS quan les relacions acceptades tenen tipus vàlid i apunten a fitxers existents. Els wikilinks sense relació tipada es conserven com a arestes candidates.

## Contracte inicial

Cada node té node_id, node_type i path.

Cada aresta té source, target, relation, status, claim_type, confidence i evidence quan existeix.

Les relacions acceptades es mantenen manualment a relations.json. Les arestes candidates serveixen per trobar connexions que poden ser revisades més endavant.
