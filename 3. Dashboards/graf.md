# Graf de la wiki

Aquesta pagina es una vista humana de la capa grafica lleugera. El graf es deriva dels fitxers Markdown i del registre de relacions revisades.

## Entrada rapida

- [Dashboard de la wiki](dashboard_wiki.md): mapa navegable de nodes humans.
- [Dashboard d'auditoria](dashboard_auditoria.md): comprovacions de salut.
- [Relacions acceptades](../graph/relations.json): registre de relacions tipades.
- [Vocabulari de relacions](../graph/relation-vocabulary.yaml): relacions permeses.

## Comprovacio rapida

```bash
python scripts/graph_scan.py --check
python scripts/graph_scan.py --stats
```

## Lectura de les arestes

- Acceptades: relacions tipades i revisades a `graph/relations.json`.
- Candidates: wikilinks existents encara sense una interpretacio semantica validada.
- Trencades: wikilinks que no es poden resoldre dins de `1. Wiki/`.

## Tipus de nodes

| Carpeta | node_type | Us |
| --- | --- | --- |
| `1. Wiki/1.1. autors/` | `author` | persones i referents |
| `1. Wiki/1.2. conceptes/` | `concept` | idees, tecniques i processos |
| `1. Wiki/1.3. models/` | `model` | models, arquitectures i marcs |
| `1. Wiki/1.4. llibres/` | `source` | llibres i fonts bibliografiques processades |

## Revisio manual

Abans d'afegir relacions acceptades:

- comprova que `source` i `target` existeixen;
- usa nomes relacions presents a `graph/relation-vocabulary.yaml`;
- registra evidencia quan la relacio sigui documentada;
- conserva `claim_type`, `confidence` i `status`.

## Proves recomanades

1. Executa l'escaner abans i despres d'incorporar una fitxa.
2. Comprova si augmenten els nodes orfes o els enllacos trencats.
3. Revisa els hubs abans d'afegir relacions generiques.
4. Genera `graph/graph.json` nomes com a instantania de treball.
5. Compara les respostes d'una consulta basada en wikilinks amb una consulta basada en relacions acceptades.

El dashboard no substitueix les vistes natives de graf d'Obsidian. Afegeix una capa de mesura i revisio que aquestes vistes no proporcionen.
