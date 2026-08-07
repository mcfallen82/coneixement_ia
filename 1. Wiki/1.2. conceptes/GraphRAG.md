---
title: GraphRAG
node_id: "concept:graphrag"
node_type: "concept"
category: conceptes
tags:
  - GraphRAG
  - RAG
  - grafs
  - recuperacio
  - models-de-llenguatge
sources:
  - https://microsoft.github.io/graphrag/
  - https://www.microsoft.com/en-us/research/publication/from-local-to-global-a-graph-rag-approach-to-query-focused-summarization/
  - https://arxiv.org/abs/2404.16130
  - https://arxiv.org/abs/2501.13958
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# GraphRAG

## Definició

GraphRAG és una família de sistemes de generació augmentada amb recuperació que utilitza grafs de coneixement i estructures de comunitats per seleccionar i organitzar el context que rep un LLM.

La implementació de Microsoft extreu un graf de coneixement del text, agrupa els nodes en comunitats, genera resums jeràrquics i utilitza aquestes estructures durant la consulta.

## Per què és important?

La RAG tradicional és especialment bona per trobar fragments relacionats amb una pregunta concreta. GraphRAG afegeix una estructura que ajuda a conservar relacions i a respondre preguntes locals i globals sobre un corpus.

## Intuïció

Una cerca vectorial pregunta: «Quins fragments s’assemblen a aquesta consulta?»

GraphRAG pot preguntar també:

- quines entitats apareixen juntes?
- quines relacions connecten aquestes entitats?
- a quina comunitat temàtica pertanyen?
- quin resum global descriu aquesta comunitat?

## Funcionament

### Indexació

1. Es carreguen documents.
2. El LLM extreu entitats, relacions i afirmacions.
3. Les entitats es normalitzen i es connecten.
4. El graf es divideix en comunitats.
5. Es generen resums de les comunitats.
6. Es creen índexs i representacions per a la consulta.

### Consulta

- **Local search:** combina dades del graf i fragments originals al voltant d’entitats concretes.
- **Global search:** treballa amb resums de comunitats per respondre preguntes sobre el conjunt del corpus.
- **DRIFT search:** parteix d’una cerca local i la refina amb informació de comunitats i preguntes de seguiment.
- **Basic search:** ofereix una recuperació més simple dins de l’índex.

## Exemple

En una wiki sobre IA, una pregunta sobre «com es relacionen RAG, embeddings i GraphRAG?» pot recuperar:

- les fitxes d’aquests conceptes;
- les relacions entre elles;
- les fonts originals;
- un resum de la comunitat de recuperació i sistemes de coneixement.

## Relacions

- [[RAG]]
- [[grafs_i_models_de_llenguatge]]
- [[ontologies_associatives]]
- [[LLM]]
- [[embeddings]]
- [[G-Retriever]]

## Aplicacions

- preguntes sobre corpus privats;
- wikis i bases de coneixement;
- síntesi de grans col·leccions documentals;
- anàlisi d’entitats i relacions;
- exploració de temes generals i casos particulars.

## Limitacions i errors habituals

- la construcció del graf pot ser costosa;
- les entitats o relacions extretes poden ser incorrectes;
- els resums de comunitats poden perdre detalls;
- la qualitat depèn de l’esquema, la normalització i les fonts;
- GraphRAG no és sinònim de qualsevol RAG amb wikilinks;
- una implementació no és automàticament millor que la cerca vectorial.

## Fonts

- [GraphRAG — documentació oficial](https://microsoft.github.io/graphrag/).
- [Local, global i DRIFT search](https://microsoft.github.io/graphrag/query/overview/).
- [From Local to Global](https://www.microsoft.com/en-us/research/publication/from-local-to-global-a-graph-rag-approach-to-query-focused-summarization/).
- [A Survey of Graph Retrieval-Augmented Generation](https://arxiv.org/abs/2501.13958).
