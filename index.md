# Índex de la wiki d’aprenentatge d’IA

## Entrada ràpida

- [Hot](hot.md) — prioritats i continguts en curs.
- [Registre de canvis](log.md).
- [Governança](AGENTS.md).
- [Quadres de comandament](3.%20Dashboards/).
- [Skills](2.%20Skills/).
- [Plantilles](4.%20Templates/).

## Fonts

- [0.1. llibres](0.%20Raw/0.1.%20llibres/) — llibres, tutorials i materials originals.
- [0.2.](0.%20Raw/0.2./) — articles, papers, cursos i documentació.

## Wiki

### Autors

Fitxes sobre investigadors, divulgadors i referents de la IA.

~~~dataview
TABLE title, field, status, updated
FROM "1. Wiki/1.1. autors"
WHERE file.name != "README"
SORT updated DESC
~~~

### Conceptes

Fitxes sobre conceptes, tècniques i processos.

~~~dataview
TABLE title, status, length(sources) AS fonts, updated
FROM "1. Wiki/1.2. conceptes"
WHERE file.name != "README"
SORT updated DESC
~~~

### Models

Fitxes sobre arquitectures i models.

~~~dataview
TABLE title, model_family, architecture, status, updated
FROM "1. Wiki/1.3. models"
WHERE file.name != "README"
SORT updated DESC
~~~

## Grafs aplicats als models de llenguatge

- [Recerca sobre grafs aplicats als LLM](0.%20Raw/0.2./recerca_grafs_models_llm_2026-08-07.md) — dossier brut processat.
- [Grafs aplicats als models de llenguatge](1.%20Wiki/1.2.%20conceptes/grafs_i_models_de_llenguatge.md) — mapa general.
- [GraphRAG](1.%20Wiki/1.2.%20conceptes/GraphRAG.md) — recuperació augmentada amb grafs.
- [Graph of Thoughts](1.%20Wiki/1.2.%20conceptes/graph_of_thoughts.md) — orquestració del raonament.
- [Xarxes neuronals de graf](1.%20Wiki/1.2.%20conceptes/xarxes_neuronals_de_graf.md) — GNN.
- [G-Retriever](1.%20Wiki/1.3.%20models/G-Retriever.md) — marc de GraphQA.

## Recerca incorporada

- [Dossier de recerca: fonaments operatius dels LLM](0.%20Raw/0.2./recerca_fonaments_operatius_2026-08-07.md) — ajustament, alineament, LoRA i avaluació.

## Organització

- [2. Skills](2.%20Skills/) — procediments reutilitzables.
- [3. Dashboards](3.%20Dashboards/) — vistes i consultes d’Obsidian.
- [90.1. templates_fitxes](4.%20Templates/90.1.%20templates_fitxes/) — plantilles.
- [90.2. docs_support](4.%20Templates/90.2.%20docs_support/) — documents de suport.

La wiki tracta l’aprenentatge general d’intel·ligència artificial. Les finances i l’economia només hi apareixen com a context d’aplicació.
