# Índex de la wiki d'aprenentatge d'IA

## Entrada ràpida

- [Hot](hot.md): prioritats i continguts en curs.
- [Registre de canvis](log.md).
- [Governança](AGENTS.md).
- [Quadres de comandament](3.%20Dashboards/).
- [Dashboard de la wiki](3.%20Dashboards/dashboard_wiki.md).
- [Skills](2.%20Skills/).
- [Plantilles](4.%20Templates/).

## Fonts externes

Les fonts originals no s'emmagatzemen al repositori públic. La procedència es conserva mitjançant URLs, referències bibliogràfiques i els camps `sources` de les fitxes.

Criteris:

- prioritzar papers originals, documentació oficial, repositoris oficials i fonts primàries;
- registrar títol, autor o organisme, URL i data quan sigui possible;
- evitar còpies locals de materials originals o dossiers privats de recerca;
- mantenir la traçabilitat entre cada fitxa i les fonts que la sustenten.

## Wiki

### Autors

- [Carpeta d'autors](1.%20Wiki/1.1.%20autors/)

### Conceptes

- [Carpeta de conceptes](1.%20Wiki/1.2.%20conceptes/)

### Models

- [Carpeta de models](1.%20Wiki/1.3.%20models/)

### Llibres

- [Carpeta de llibres](1.%20Wiki/1.4.%20llibres/)
- [How Big Things Get Done](1.%20Wiki/1.4.%20llibres/how_big_things_get_done.md)

## Grafs aplicats als models de llenguatge

- [Grafs aplicats als models de llenguatge](1.%20Wiki/1.2.%20conceptes/grafs_i_models_de_llenguatge.md)
- [Graph engineering](1.%20Wiki/1.2.%20conceptes/graph_engineering.md)
- [GraphRAG](1.%20Wiki/1.2.%20conceptes/GraphRAG.md)
- [Graph of Thoughts](1.%20Wiki/1.2.%20conceptes/graph_of_thoughts.md)
- [Xarxes neuronals de graf](1.%20Wiki/1.2.%20conceptes/xarxes_neuronals_de_graf.md)
- [G-Retriever](1.%20Wiki/1.3.%20models/G-Retriever.md)
- [Guia per crear wikis amb grafs](4.%20Templates/90.2.%20docs_support/guia_creacio_wikis_amb_grafs.md)
- [Capa gràfica lleugera](3.%20Dashboards/graf.md)

Font externa destacada sobre *graph engineering*: https://theaioperator.io/p/graph-engineering-decoded-two-definitions

## Organització

- [2. Skills](2.%20Skills/): procediments reutilitzables.
- [3. Dashboards](3.%20Dashboards/): guies de revisió i comprovacions.
- [90.1. templates_fitxes](4.%20Templates/90.1.%20templates_fitxes/): plantilles.
- [90.2. docs_support](4.%20Templates/90.2.%20docs_support/): documents de suport.

## Revisió freqüent

Després de qualsevol ingesta o canvi estructural:

- actualitza les fitxes i les seves fonts;
- revisa `index.md`, `log.md`, `hot.md` i `.manifest.json`;
- executa `python scripts/wiki_lint.py`;
- executa `python scripts/graph_scan.py --check`.
