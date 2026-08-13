# Dashboard de fonts

Aquesta pagina resumeix les fonts de treball de la wiki i orienta el pas de `0. Raw/` cap a fitxes permanents de `1. Wiki/`. Es mante com a Markdown estatic i no depen de plugins d'Obsidian.

## Entrada rapida

- [Dashboard de la wiki](dashboard_wiki.md): fitxes permanents ja navegables.
- [Dashboard d'auditoria](dashboard_auditoria.md): comprovacions de salut i seguiment.
- [Taula de lectures](../0.%20Raw/Taula_Lectures.md): pla de lectures original processat.
- [Recerca sobre How Big Things Get Done](../0.%20Raw/recerca_how_big_things_get_done_2026-08-13.md): dossier de fonts per al llibre i els seus autors.
- [Graph Engineering Decoded](../0.%20Raw/graph_engineering_decoded_two_definitions_2026-08-11.md): article d'Eugeniu Ghelbur integrat com a concepte.

## Fonts brutes principals

| Font | Tipus | Estat | Sortida principal |
| --- | --- | --- | --- |
| [Taula_Lectures](../0.%20Raw/Taula_Lectures.md) | pla de lectures | processed | conceptes i models fundacionals |
| [Tutorial_Zero_to_Hero_LLMs](../0.%20Raw/Tutorial_Zero_to_Hero_LLMs.md) | tutorial | raw_ingested | pendent de processament complet |
| [recerca_fonaments_operatius](../0.%20Raw/recerca_fonaments_operatius_2026-08-07.md) | recerca web | processed | ajust fi, alineament, LoRA i avaluacio |
| [recerca_grafs_models_llm](../0.%20Raw/recerca_grafs_models_llm_2026-08-07.md) | recerca web | processed | grafs, GraphRAG, Graph of Thoughts, GNN i G-Retriever |
| [recerca_grafs_obsidian_second_brain](../0.%20Raw/recerca_grafs_obsidian_second_brain_2026-08-07.md) | recerca web | reviewed | patro d'escaner i relacions tipades |
| [graph_engineering_decoded](../0.%20Raw/graph_engineering_decoded_two_definitions_2026-08-11.md) | article | processed | graph engineering |
| [recerca_how_big_things_get_done](../0.%20Raw/recerca_how_big_things_get_done_2026-08-13.md) | recerca web | processed | llibre i fitxes d'autors |

## Llibres processats

- [How Big Things Get Done](../1.%20Wiki/1.4.%20llibres/how_big_things_get_done.md): projectes, estimacio, risc, modularitat i execucio.

## Ruta recomanada

1. Revisar la font bruta i comprovar si el manifest la marca com a `processed`, `reviewed` o `raw_ingested`.
2. Confirmar si ja hi ha fitxes permanents associades a `1. Wiki/`.
3. Crear o ampliar fitxes nomes quan la font aporti coneixement estable per a la wiki.
4. Actualitzar `index.md`, `hot.md`, `log.md` i `.manifest.json` quan el canvi sigui significatiu.
5. Executar `python scripts/wiki_lint.py` i `python scripts/graph_scan.py --check`.

## Pendent

- Processar o descartar explicitament fonts que continuen com a `raw_ingested`.
- Revisar si cada llibre de `1. Wiki/1.4. llibres/` te autors amb fitxa propia.
- Mantenir aquest dashboard sincronitzat quan s'incorporin noves fonts a `0. Raw/`.
