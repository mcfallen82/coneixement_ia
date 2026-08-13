---
title: Recerca sobre grafs aplicats als models de llenguatge
category: raw
raw_type: research_dossier
source_type: recerca_web
processing_status: processed
status: processed
created: 2026-08-07
updated: 2026-08-13
previous_path: "0. Raw/0.2. altres fonts/recerca_grafs_models_llm_2026-08-07.md"
tags:
  - recerca
  - grafs
  - models-de-llenguatge
  - GraphRAG
---

# Recerca sobre grafs aplicats als models de llenguatge

## Pregunta i abast

Com s’apliquen els grafs als models de llenguatge i quines idees convé incorporar a una wiki d’aprenentatge sobre LLM?

La recerca cobreix quatre usos diferents:

1. representar coneixement i relacions explícites;
2. recuperar context estructurat amb GraphRAG;
3. organitzar processos de raonament amb Graph of Thoughts;
4. combinar LLM amb xarxes neuronals de graf i tasques de GraphQA.

Data de consulta: 7 d’agost de 2026.

## Ronda 1 — mapa general

### 1. Grafs com a representació del coneixement

Un graf representa objectes com a nodes i relacions com a arestes. En un graf de coneixement, els nodes poden ser persones, empreses, documents, conceptes o esdeveniments, i les arestes expressen relacions com «és un», «depèn de», «participa en» o «és citat per».

Aquesta estructura conserva relacions que es poden perdre quan els documents es redueixen a fragments independents. És especialment útil quan una pregunta exigeix seguir diversos salts entre entitats.

### 2. GraphRAG

GraphRAG construeix un graf de coneixement a partir de text no estructurat, identifica comunitats i genera resums jeràrquics. En la consulta, pot combinar informació del graf i fragments originals.

La cerca local és adequada per preguntes centrades en una entitat. La cerca global utilitza resums de comunitats per respondre preguntes sobre els temes generals d’un corpus. La cerca DRIFT amplia una consulta local amb informació de comunitats i preguntes de seguiment.

### 3. Graph of Thoughts

Graph of Thoughts aplica la metàfora del graf al procés de raonament. Cada unitat intermèdia de pensament és un node i les dependències entre passos són arestes. Això permet ramificar, combinar, revisar i reutilitzar resultats intermedis.

És una estratègia d’orquestració de prompts i operacions. No modifica necessàriament els paràmetres del LLM ni converteix el model en una xarxa neuronal de graf.

### 4. GNN i GraphQA

Les xarxes neuronals de graf processen directament dades amb estructura de graf. G-Retriever combina recuperació sobre grafs, xarxes neuronals de graf i un LLM per respondre preguntes sobre grafs textuals.

La recuperació pot seleccionar un subgraf rellevant en lloc d’una col·lecció de fragments. G-Retriever formula aquesta selecció com un problema d’optimització basat en arbres de Steiner amb premis, amb l’objectiu de mantenir connectivitat i rellevància sense superar el context del LLM.

## Ronda 2 — contrast i limitacions

### Diferències que cal mantenir

- Un graf de coneixement és una representació de dades.
- GraphRAG és una arquitectura o pipeline de recuperació i generació.
- Graph of Thoughts és una estratègia d’orquestració del raonament.
- Una GNN és una família de xarxes neuronals per a dades relacionals.
- G-Retriever és un marc de GraphQA que combina recuperació, GNN i LLM.

No s’han de barrejar aquestes capes en una única fitxa anomenada «model de graf».

### Avantatges potencials

- preservació de relacions i dependències;
- recuperació de context multi-salt;
- millor cobertura de preguntes locals i globals;
- possibilitat d’explicar quines entitats i relacions han sustentat una resposta;
- connexió natural amb wikis, ontologies i sistemes de coneixement.

### Costos i riscos

- l’extracció d’entitats i relacions amb un LLM pot introduir errors;
- els grafs poden acumular duplicats, relacions espúries i informació obsoleta;
- la construcció d’un índex GraphRAG pot ser més costosa que una RAG vectorial simple;
- les comunitats i els resums són una interpretació del corpus, no una veritat independent;
- una connexió gràfica no garanteix que la informació recuperada sigui rellevant;
- cal conservar les fonts originals per poder verificar les afirmacions;
- els resultats de recerca encara evolucionen i no són comparables automàticament entre implementacions.

## Ronda 3 — síntesi per al projecte

### Fitxes permanents creades o actualitzades

- [[grafs_i_models_de_llenguatge]]: mapa general de les capes.
- [[GraphRAG]]: recuperació augmentada basada en grafs.
- [[graph_of_thoughts]]: raonament i orquestració en forma de graf.
- [[xarxes_neuronals_de_graf]]: GNN i processament de dades relacionals.
- [[G-Retriever]]: marc específic per a GraphQA.
- [[RAG]] i [[ontologies_associatives]]: relacions amb fitxes ja existents.

### Aplicació a la wiki

La wiki d’IA pot interpretar les fitxes com un graf de coneixement lleuger:

- cada fitxa és un node;
- cada wikilink és una relació;
- el frontmatter descriu tipus, estat, fonts i metadades;
- les seccions de relacions expliquen el significat de les connexions;
- les fonts Raw permeten verificar el camí entre una afirmació i el document d’origen.

Aquesta estructura encara no és un GraphRAG executable. És una base preparada per a una futura exportació a un graf, una base de dades de grafs o un sistema híbrid de recuperació.

## Fonts consultades

1. Microsoft GraphRAG — documentació general: https://microsoft.github.io/graphrag/
2. Microsoft GraphRAG — consulta local, global i DRIFT: https://microsoft.github.io/graphrag/query/overview/
3. Microsoft Research, *From Local to Global*: https://www.microsoft.com/en-us/research/publication/from-local-to-global-a-graph-rag-approach-to-query-focused-summarization/
4. Edge et al., *From Local to Global*: https://arxiv.org/abs/2404.16130
5. Besta et al., *Graph of Thoughts*: https://arxiv.org/abs/2308.09687
6. Implementació oficial de Graph of Thoughts: https://github.com/spcl/graph-of-thoughts
7. He et al., *G-Retriever*: https://arxiv.org/abs/2402.07630
8. Zhang et al., *A Survey of Graph Retrieval-Augmented Generation*: https://arxiv.org/abs/2501.13958
9. Li et al., *A Survey of Graph Meets Large Language Model*: https://www.ijcai.org/proceedings/2024/0898.pdf
10. Xu et al., *Retrieval-Augmented Generation with Knowledge Graphs*: https://arxiv.org/abs/2404.17723
11. Repositori oficial de Microsoft GraphRAG: https://github.com/microsoft/graphrag

## Confiança i buits

La confiança és alta per a la definició general de GraphRAG, Graph of Thoughts i G-Retriever perquè hi ha documentació oficial i papers primaris. És mitjana per a comparacions de rendiment entre implementacions, ja que depenen dels conjunts de dades, configuracions i mètriques.

Queden oberts:

- com exportar les fitxes d’Obsidian a un graf formal;
- quina combinació de cerca vectorial i cerca gràfica convé al projecte;
- com avaluar la qualitat de les entitats, relacions i resums;
- quan compensa GraphRAG davant d’una RAG vectorial més simple;
- com incorporar temporalitat, procedència i confiança a cada relació.
