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
related_concepts: []
related_models: []
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Grafs aplicats als models de llenguatge

## Definició

Un graf és una estructura formada per nodes i arestes. Aplicat als models de llenguatge, permet representar explícitament entitats, relacions, dependències, documents o passos de raonament.

La paraula «grafs» descriu diverses aplicacions relacionades però diferents:

- graf de coneixement: organitza fets i relacions;
- GraphRAG: recupera i utilitza informació estructurada en un RAG;
- Graph of Thoughts: organitza les operacions de raonament d’un LLM;
- GNN: processa representacions gràfiques amb una xarxa neuronal;
- GraphQA: respon preguntes sobre dades en forma de graf.

## Per què és important?

Els fragments de text recuperats individualment poden contenir informació rellevant però perdre la relació entre les parts. Un graf fa explícita aquesta estructura.

Això és útil per a preguntes multi-salt, exploració de wikis, anàlisi de dependències, coneixement empresarial i sistemes que han de justificar d’on prové una resposta.

## Intuïció

Una RAG vectorial s’assembla a buscar pàgines semblants en una biblioteca. Un sistema gràfic, a més, conserva les connexions entre les pàgines, els conceptes i les entitats.

Per exemple, en una wiki:

`[[RAG]] → utilitza → [[LLM]]`

`[[GraphRAG]] → amplia → [[RAG]]`

`[[GraphRAG]] → recupera → subgrafs`

Aquestes connexions poden ajudar a respondre preguntes que requereixen seguir una cadena de dependències.

## Com funciona de manera simplificada?

1. S’extreuen entitats, conceptes i relacions dels documents.
2. Es normalitzen noms i tipus de relació.
3. Es construeix un graf amb nodes, arestes i metadades.
4. La consulta identifica nodes o relacions rellevants.
5. Es recupera un subgraf, una comunitat o un camí.
6. El LLM rep aquesta informació i redacta la resposta.
7. El sistema conserva les fonts que sustenten els elements recuperats.

## Diferència entre les principals aplicacions

| Aplicació | Què representa el graf? | Funció principal |
|---|---|---|
| Graf de coneixement | Entitats, fets i relacions | Organitzar coneixement |
| GraphRAG | Coneixement extret de documents i comunitats | Recuperar context per a un LLM |
| Graph of Thoughts | Passos i dependències del raonament | Orquestrar prompts i operacions |
| GNN | Nodes i arestes com a dades d’entrada | Aprendre representacions gràfiques |
| GraphQA | Preguntes i subgrafs | Respondre sobre dades relacionals |

## Exemple aplicat a anàlisi documental

En una col·lecció d’informes, els nodes podrien ser empreses, productes, riscos, directius, períodes i documents. Les arestes podrien expressar:

- una empresa desenvolupa un producte;
- un risc afecta una empresa;
- un document descriu un esdeveniment;
- un directiu ocupa un càrrec;
- una dada pertany a un període.

Una pregunta com «Quins riscos relacionats amb el producte X apareixen en documents diferents?» es beneficia de seguir relacions entre productes, riscos i fonts.

## Relacions

- [[RAG]]
- [[ontologies_associatives]]
- [[GraphRAG]]
- [[graph_of_thoughts]]
- [[xarxes_neuronals_de_graf]]
- [[G-Retriever]]
- [[LLM]]
- [[embeddings]]

## Aplicacions

- wikis i segons cervells;
- GraphRAG sobre documents privats;
- preguntes multi-salt;
- sistemes de recomanació;
- detecció de relacions entre empreses, persones i esdeveniments;
- agents que necessiten memòria estructurada;
- anàlisi de dependències en codi i processos.

## Limitacions i errors habituals

- confondre un conjunt de wikilinks amb un graf semàntic complet;
- crear relacions sense indicar-ne el significat;
- donar per certa una relació extreta automàticament;
- ignorar la procedència, la data i la confiança de cada aresta;
- pensar que una estructura de graf elimina les al·lucinacions;
- assumir que GraphRAG sempre supera una RAG vectorial.

## Fonts

- [A Survey of Graph Retrieval-Augmented Generation](https://arxiv.org/abs/2501.13958).
- [A Survey of Graph Meets Large Language Model](https://www.ijcai.org/proceedings/2024/0898.pdf).
- [GraphRAG — documentació oficial](https://microsoft.github.io/graphrag/).
