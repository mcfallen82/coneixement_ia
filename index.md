# Index de la wiki d'aprenentatge d'IA

## Entrada rapida

- [Hot](hot.md): prioritats i continguts en curs.
- [Registre de canvis](log.md).
- [Governanca](AGENTS.md).
- [Quadres de comandament](3.%20Dashboards/).
- [Dashboard de la wiki](3.%20Dashboards/dashboard_wiki.md).
- [Skills](2.%20Skills/).
- [Plantilles](4.%20Templates/).

## Revisio frequent

Aquest index s'ha de revisar sovint, especialment despres de qualsevol ingesta, reorganitzacio o canvi estructural. La revisio segueix el flux d'`AGENTS.md`: actualitzar index, log, hot i manifest; executar les comprovacions; i deixar constancia de qualsevol incidencia.

Comprovacions minimes:

- `python scripts/wiki_lint.py`: estructura, YAML, categories, wikilinks, manifest, duplicats, estructura de skills i errors visuals de codificacio.
- `python scripts/graph_scan.py --check`: metadades grafiques, relacions acceptades i wikilinks trencats.
- Revisio visual: titols llegibles, accents no trencats, enllacos comprensibles i absencia de fragments de mojibake o caracters de substitucio.

## Fonts

- [0. Raw](0.%20Raw/): fonts originals i materials de treball en una carpeta plana.
- Els documents Raw es diferencien pel frontmatter: `raw_type`, `source_type`, `processing_status`, `previous_path` i `processed_into`.
- Revisa [0. Raw/README.md](0.%20Raw/README.md) abans d'incorporar o reorganitzar fonts.

## Wiki

### Autors

Fitxes sobre investigadors, divulgadors i referents de la IA.

- [Carpeta d'autors](1.%20Wiki/1.1.%20autors/)
- Revisa les fitxes amb `python scripts/wiki_lint.py`.
- Mantingues `title`, `category`, `sources`, `status`, `created`, `updated`, `node_id` i `node_type` al frontmatter.

### Conceptes

Fitxes sobre conceptes, tecniques i processos.

- [Carpeta de conceptes](1.%20Wiki/1.2.%20conceptes/)
- Prioritza les fitxes en `draft`, sense fonts o amb wikilinks trencats.
- Usa `hot.md` per marcar les revisions mes urgents.

### Models

Fitxes sobre arquitectures i models.

- [Carpeta de models](1.%20Wiki/1.3.%20models/)
- Cada model ha d'incloure `model_family` i `architecture`.
- Revisa especialment els models amb frontmatter antic o fonts pendents.

### Llibres

Fonts bibliografiques processades com a suport de la wiki.

- [Carpeta de llibres](1.%20Wiki/1.4.%20llibres/)
- [How Big Things Get Done](1.%20Wiki/1.4.%20llibres/how_big_things_get_done.md): planificacio, estimacio, modularitat i risc en projectes grans.

## Grafs aplicats als models de llenguatge

- [Recerca sobre grafs aplicats als LLM](0.%20Raw/recerca_grafs_models_llm_2026-08-07.md): dossier brut processat.
- [Graph Engineering Decoded](0.%20Raw/graph_engineering_decoded_two_definitions_2026-08-11.md): article d'Eugeniu Ghelbur sobre les dues definicions de graph engineering.
- [Grafs aplicats als models de llenguatge](1.%20Wiki/1.2.%20conceptes/grafs_i_models_de_llenguatge.md): mapa general.
- [Graph engineering](1.%20Wiki/1.2.%20conceptes/graph_engineering.md): distincio entre graf de coneixement i graf de topologia d'agents.
- [GraphRAG](1.%20Wiki/1.2.%20conceptes/GraphRAG.md): recuperacio augmentada amb grafs.
- [Graph of Thoughts](1.%20Wiki/1.2.%20conceptes/graph_of_thoughts.md): orquestracio del raonament.
- [Xarxes neuronals de graf](1.%20Wiki/1.2.%20conceptes/xarxes_neuronals_de_graf.md): GNN.
- [G-Retriever](1.%20Wiki/1.3.%20models/G-Retriever.md): marc de GraphQA.
- [Guia per crear wikis amb grafs](4.%20Templates/90.2.%20docs_support/guia_creacio_wikis_amb_grafs.md): nodes, arestes, procedencia i assistencia amb agents.
- [Capa grafica lleugera](3.%20Dashboards/graf.md): comprovacions, estadistiques i proves del graf.
- [Us de grafs a una wiki Obsidian externa](0.%20Raw/recerca_grafs_obsidian_second_brain_2026-08-07.md): dossier brut sobre escaner de grafs, relacions tipades i connexio entre dominis.

## Recerca incorporada

- [Recerca sobre *How Big Things Get Done*](0.%20Raw/recerca_how_big_things_get_done_2026-08-13.md): fonts editorials i academiques per ampliar la fitxa del llibre i crear autors.
- [Dossier de recerca: fonaments operatius dels LLM](0.%20Raw/recerca_fonaments_operatius_2026-08-07.md): ajustament, alineament, LoRA i avaluacio.

## Organitzacio

- [2. Skills](2.%20Skills/): procediments reutilitzables amb README breu i procediment complet per skill.
- [3. Dashboards](3.%20Dashboards/): guies de revisio i comprovacions sense plugins.
- [90.1. templates_fitxes](4.%20Templates/90.1.%20templates_fitxes/): plantilles.
- [90.2. docs_support](4.%20Templates/90.2.%20docs_support/): documents de suport.

La wiki tracta l'aprenentatge general d'intel.ligencia artificial. Les finances i l'economia nomes hi apareixen com a context d'aplicacio.
