---
title: Grafs aplicats als models de llenguatge
node_id: "concept:grafs_i_models_de_llenguatge"
node_type: "concept"
category: conceptes
tags:
  - grafs
  - models-de-llenguatge
  - representacio-del-coneixement
  - GraphRAG
sources:
  - https://arxiv.org/abs/2501.13958
  - https://www.ijcai.org/proceedings/2024/0898.pdf
  - https://microsoft.github.io/graphrag/
  - https://arxiv.org/abs/1609.02907
  - https://arxiv.org/abs/1704.01212
  - https://arxiv.org/abs/2402.07630
  - https://arxiv.org/abs/2011.07743
  - https://theaioperator.io/p/graph-engineering-decoded-two-definitions
related_concepts:
  - "[[RAG]]"
  - "[[GraphRAG]]"
  - "[[GraphQA]]"
  - "[[graph_of_thoughts]]"
  - "[[xarxes_neuronals_de_graf]]"
  - "[[ontologies_associatives]]"
  - "[[embeddings]]"
  - "[[graph_engineering]]"
related_models:
  - "[[G-Retriever]]"
status: reviewed
created: 2026-08-07
updated: 2026-09-18
---

# Grafs aplicats als models de llenguatge

## Definició

Un graf és una estructura formada per nodes i arestes. Aplicat als models de llenguatge, permet representar explícitament entitats, relacions, dependències, documents o passos de raonament.

La paraula «grafs» descriu diverses aplicacions relacionades però diferents:

- **graf de coneixement:** organitza fets i relacions;
- **GraphRAG:** recupera i utilitza informació estructurada en un RAG;
- **Graph of Thoughts:** organitza operacions de raonament d'un LLM;
- **GNN:** aprèn representacions a partir de nodes, arestes i topologia;
- **GraphQA:** formula la resposta de preguntes com un problema de recuperació o raonament sobre un graf;
- **graph engineering:** decideix si el graf ha de modelar coneixement o topologia d'agents segons el tipus de fallada.

## Per què és important?

Els fragments de text recuperats individualment poden contenir informació rellevant però perdre la relació entre les parts. Un graf fa explícita aquesta estructura.

Això és útil per a preguntes multi-salt, exploració de wikis, anàlisi de dependències, coneixement empresarial i sistemes que han de justificar d'on prové una resposta.

## Intuïció

Una RAG vectorial s'assembla a buscar pàgines semblants en una biblioteca. Un sistema gràfic, a més, conserva les connexions entre les pàgines, els conceptes i les entitats.

Per exemple:

`[[RAG]] → utilitza → [[embeddings]]`

`[[GraphRAG]] → amplia → [[RAG]]`

`[[GraphQA]] → pregunta_sobre → subgraf`

`[[G-Retriever]] → combina → recuperació + GNN + LLM`

Aquestes connexions poden ajudar a respondre preguntes que requereixen seguir una cadena de dependències.

## Com funciona de manera simplificada?

1. S'extreuen entitats, conceptes i relacions dels documents.
2. Es normalitzen noms i tipus de relació.
3. Es construeix un graf amb nodes, arestes i metadades.
4. La consulta identifica nodes o relacions rellevants.
5. Es recupera un subgraf, una comunitat o un camí.
6. Opcionalment, una GNN codifica la topologia i propaga informació entre nodes.
7. El LLM rep la informació seleccionada i redacta la resposta.
8. El sistema conserva les fonts que sustenten els elements recuperats.

## GNN: aprendre sobre l'estructura del graf

Una **Graph Neural Network (GNN)** és una xarxa neuronal que aprèn representacions de nodes o grafs combinant la informació pròpia de cada node amb la dels seus veïns.

La intuïció general és el **message passing**:

[
missatges dels veïns ightarrow agregació ightarrow actualització del node
]

Amb diverses capes, un node pot incorporar informació de diversos salts. Les GNN s'utilitzen en classificació de nodes, predicció d'enllaços, classificació de grafs i representació de subgrafs.

Punt clau: una GNN **aprèn sobre el graf**; GraphRAG **recupera context des del graf**. Són peces diferents i es poden combinar.

→ Vegeu [[xarxes_neuronals_de_graf]].

## GraphQA: preguntar al graf

**GraphQA (Graph Question Answering)** és la tasca de respondre preguntes a partir d'informació representada com a graf.

Un sistema GraphQA pot:

1. identificar les entitats de la pregunta;
2. localitzar nodes del graf;
3. recuperar camins o subgrafs;
4. fer raonament multi-salt;
5. generar una resposta amb evidència.

GraphQA és una **tasca**, no una arquitectura concreta. Pot resoldre's amb consultes simbòliques, recuperació de subgrafs, GNN, LLM o combinacions d'aquestes tècniques.

El treball de **G-Retriever** és especialment útil per entendre aquesta combinació: introdueix un benchmark GraphQA sobre grafs textuals i un sistema RAG que selecciona un subgraf connectat abans de passar-lo a un LLM.

→ Vegeu [[GraphQA]] i [[G-Retriever]].

## Diferència entre les principals aplicacions

| Aplicació | Què representa el graf? | Funció principal |
|---|---|---|
| Graf de coneixement | Entitats, fets i relacions | Organitzar coneixement |
| GraphRAG | Coneixement extret de documents i comunitats | Recuperar context per a un LLM |
| Graph of Thoughts | Passos i dependències del raonament | Orquestrar prompts i operacions |
| GNN | Nodes, arestes i atributs com a dades d'entrada | Aprendre representacions gràfiques |
| GraphQA | Nodes, relacions, camins o subgrafs rellevants per una pregunta | Respondre sobre dades relacionals |
| Graph engineering | Coneixement o topologia d'agents | Triar quin graf resol la fallada real |

## Exemple aplicat a anàlisi documental

En una col·lecció d'informes, els nodes podrien ser empreses, productes, riscos, directius, períodes i documents. Les arestes podrien expressar:

- una empresa desenvolupa un producte;
- un risc afecta una empresa;
- un document descriu un esdeveniment;
- un directiu ocupa un càrrec;
- una dada pertany a un període.

Una pregunta com «Quins riscos relacionats amb el producte X apareixen en documents diferents?» es beneficia de seguir relacions entre productes, riscos i fonts.

Si el graf és gran, GraphRAG pot ajudar a recuperar context. Si volem aprendre patrons estructurals, una GNN pot generar representacions. Si formulem una pregunta concreta sobre camins o relacions, entrem en el terreny de GraphQA.

## Relacions

- [[RAG]]
- [[ontologies_associatives]]
- [[GraphRAG]]
- [[GraphQA]]
- [[graph_of_thoughts]]
- [[xarxes_neuronals_de_graf]]
- [[G-Retriever]]
- [[LLM]]
- [[embeddings]]
- [[graph_engineering]]

## Aplicacions

- wikis i segons cervells;
- GraphRAG sobre documents privats;
- GraphQA i preguntes multi-salt;
- sistemes de recomanació;
- detecció de relacions entre empreses, persones i esdeveniments;
- agents que necessiten memòria estructurada;
- anàlisi de dependències en codi i processos;
- aprenentatge sobre cadenes de subministrament o xarxes empresarials amb GNN.

## Limitacions i errors habituals

- confondre un conjunt de wikilinks amb un graf semàntic complet;
- crear relacions sense indicar-ne el significat;
- donar per certa una relació extreta automàticament;
- ignorar la procedència, la data i la confiança de cada aresta;
- pensar que una estructura de graf elimina les al·lucinacions;
- assumir que GraphRAG sempre supera una RAG vectorial;
- confondre GraphQA amb GraphRAG;
- assumir que qualsevol problema sobre grafs necessita una GNN.

## Fonts

- [A Survey of Graph Retrieval-Augmented Generation](https://arxiv.org/abs/2501.13958).
- [A Survey of Graph Meets Large Language Model](https://www.ijcai.org/proceedings/2024/0898.pdf).
- [GraphRAG — documentació oficial](https://microsoft.github.io/graphrag/).
- [Semi-Supervised Classification with Graph Convolutional Networks — Kipf & Welling](https://arxiv.org/abs/1609.02907).
- [Neural Message Passing for Quantum Chemistry — Gilmer et al.](https://arxiv.org/abs/1704.01212).
- [G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering](https://arxiv.org/abs/2402.07630).
- [Beyond I.I.D.: Three Levels of Generalization for Question Answering on Knowledge Bases — GrailQA](https://arxiv.org/abs/2011.07743).
