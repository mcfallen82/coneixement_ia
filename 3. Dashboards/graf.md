# Graf de la wiki

Aquesta pàgina és una vista humana de la capa gràfica lleugera. El graf es deriva dels fitxers Markdown i del registre de relacions revisades.

## Entrada ràpida

- [Dashboard de la wiki](dashboard_wiki.md): mapa navegable de nodes humans.
- [Dashboard d'auditoria](dashboard_auditoria.md): comprovacions de salut.
- [Relacions acceptades](../graph/relations.json): registre de relacions tipades.
- [Vocabulari de relacions](../graph/relation-vocabulary.yaml): relacions permeses.

## Comprovació ràpida

```bash
python scripts/graph_scan.py --check --strict
python scripts/graph_scan.py --stats
```

## Lectura de les arestes

- Acceptades: relacions tipades i revisades a `graph/relations.json`.
- Candidates: parelles úniques de wikilinks encara sense una interpretació semàntica validada.
- Trencades: wikilinks que no es poden resoldre dins de `1. Wiki/`.
- Ambigües: wikilinks curts que poden apuntar a més d'una fitxa.

Les candidates conserven `occurrences` i `origins`, però només compten una vegada en els graus i els hubs.

## Tipus de nodes

| Carpeta | node_type | Ús |
| --- | --- | --- |
| `1. Wiki/1.1. autors/` | `author` | persones i referents |
| `1. Wiki/1.2. conceptes/` | `concept` | idees, tècniques i processos |
| `1. Wiki/1.3. models/` | `model` | models, arquitectures i marcs |
| `1. Wiki/1.4. llibres/` | `source` | llibres i fonts bibliogràfiques processades |

## Revisió manual

Abans d'afegir relacions acceptades:

- comprova que `source` i `target` existeixen;
- usa només relacions presents a `graph/relation-vocabulary.yaml`;
- registra evidència quan la relació sigui documentada;
- conserva `claim_type`, `confidence` i `status`.

## Proves recomanades

1. Executa l'escàner abans i després d'incorporar una fitxa.
2. Comprova si augmenten els nodes orfes o els enllaços trencats o ambigus.
3. Revisa els hubs abans d'afegir relacions genèriques.
4. Genera `graph/graph.json` només com a instantània de treball.
5. Compara les respostes d'una consulta basada en wikilinks amb una consulta basada en relacions acceptades.

El dashboard aporta una capa de mesura i revisió independent de l'editor utilitzat.
