# graph-layer

## Finalitat

Mantenir una capa gràfica lleugera sobre la wiki Markdown, sense convertir-la encara en una base de dades gràfica ni en un sistema GraphRAG.

## Principis

- Markdown i les fitxes permanents són la font principal.
- El graf és una representació derivada i reconstruïble.
- Les relacions acceptades es registren explícitament a graph/relations.json.
- Els wikilinks no tipats es conserven com a candidats.
- Les inferències han d’indicar claim_type: inferred i una confiança.
- Una relació acceptada amb destinació inexistent és un error bloquejant.

## Flux

1. Executa python scripts/graph_scan.py --check.
2. Revisa les estadístiques de nodes, arestes candidates i components.
3. Afegeix només relacions justificades al registre JSON.
4. Executa python scripts/graph_scan.py --output graph/graph.json per generar una instantània.
5. Reexecuta python scripts/wiki_lint.py i revisa les advertències.
6. Actualitza log.md i .manifest.json si el canvi modifica l’arquitectura.

## Criteris de parada

Atura l’operació si una destinació no existeix, el tipus no forma part del vocabulari, falta la procedència d’una relació documentada, una relació inferida no està marcada com a tal o la modificació exigeix una base de dades, un servei extern o una migració massiva.

## Proves inicials

La capa permet provar recompte de nodes i arestes, detecció d’enllaços trencats, hubs per grau, components connexos, exportació JSON i comparació entre relacions acceptades i wikilinks candidats.

Aquesta skill no autoritza encara la construcció de GraphRAG.
