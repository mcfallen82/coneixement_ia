# Capa gràfica consultable

Aquesta carpeta conté la implementació del graf de coneixement de `coneixement_ia`.

Markdown continua sent la font principal. El graf és una representació derivada que ajuda a identificar nodes i relacions, separar enllaços candidats de relacions revisades, detectar destinacions inexistents i experimentar amb camins, hubs i components.

La capa no introdueix una base de dades, un servidor, un LLM ni GraphRAG. Es pot executar amb la biblioteca estàndard de Python. `graph_scan.py` construeix i valida el graf; `graph_query.py` hi afegeix una primera capa GraphQA local i determinista.

## Fitxers

- relations.json: registre curat de relacions tipades revisades manualment.
- relation-vocabulary.yaml: vocabulari inicial i regles bàsiques.
- graph.json: sortida generada opcionalment per l’escàner.
- scripts/graph_scan.py: construeix i valida el graf.
- scripts/graph_query.py: consulta nodes, camins, subgrafs i procedència.
- tests/test_graph_query.py: comprova el comportament del motor de consulta.

## Execució

Des de l’arrel del repositori:

    python scripts/graph_scan.py --check
    python scripts/graph_scan.py --output graph/graph.json
    python scripts/graph_scan.py --stats

## Consultes GraphQA

Per defecte, les consultes només utilitzen relacions `accepted`. Això evita presentar un wikilink candidat com a coneixement validat.

```bash
python scripts/graph_query.py neighbors GraphRAG
python scripts/graph_query.py path G-Retriever RAG --max-depth 3
python scripts/graph_query.py subgraph RAG --depth 2
python scripts/graph_query.py explain-edge GraphRAG RAG
```

Les quatre operacions responen preguntes diferents:

| Ordre | Pregunta |
| --- | --- |
| `neighbors NODE` | Quines relacions entren i surten del node? |
| `path A B` | Quin és el camí dirigit més curt entre A i B? |
| `subgraph NODE` | Quin veïnat envolta el node fins a una profunditat concreta? |
| `explain-edge A B` | Quina procedència, confiança i tipus de reclamació justifiquen la relació? |

Cada ordre accepta `--json` per obtenir una sortida estructurada i `--include-candidates` per incloure, de manera explícita, els wikilinks encara no validats. Els nodes es poden indicar mitjançant `node_id`, títol, nom de fitxer o ruta. Si un nom és ambigu, el programa demana un identificador més específic.

El subgraf recorre relacions en ambdós sentits perquè descriu un veïnat. La cerca de camins, en canvi, respecta la direcció semàntica de les arestes.

## Proves

```bash
python -m unittest discover -s tests -v
```

El mode check retorna PASS quan les relacions acceptades tenen tipus vàlid i apunten a fitxers existents. Els wikilinks sense relació tipada es conserven com a arestes candidates.

## Contracte inicial

Cada node té node_id, node_type i path.

Cada aresta té source, target, relation, status, claim_type, confidence i evidence quan existeix.

Les relacions acceptades es mantenen manualment a relations.json. Les arestes candidates serveixen per trobar connexions que poden ser revisades més endavant.
