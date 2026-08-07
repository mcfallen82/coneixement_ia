# Graf de la wiki

Aquesta pàgina és una vista humana de la capa gràfica lleugera. El graf es deriva dels fitxers Markdown i del registre de relacions revisades.

## Comprovació ràpida

    python scripts/graph_scan.py --check
    python scripts/graph_scan.py --stats

## Lectura de les arestes

- Acceptades: relacions tipades i revisades a graph/relations.json.
- Candidates: wikilinks existents encara sense una interpretació semàntica validada.
- Trencades: wikilinks que no es poden resoldre dins de 1. Wiki/.

## Consultes inicials amb Dataview

~~~dataview
TABLE title, category, status, updated, node_id
FROM "1. Wiki"
WHERE file.name != "README"
SORT updated DESC
~~~

## Proves recomanades

1. Executa l’escàner abans i després d’incorporar una fitxa.
2. Comprova si augmenten els nodes orfes o els enllaços trencats.
3. Revisa els hubs abans d’afegir relacions genèriques.
4. Genera graph/graph.json només com a instantània de treball.
5. Compara les respostes d’una consulta basada en wikilinks amb una consulta basada en relacions acceptades.

El dashboard no substitueix les vistes natives de graf d’Obsidian. Afegeix una capa de mesura i revisió que aquestes vistes no proporcionen.
