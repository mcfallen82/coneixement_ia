---
title: Xarxes neuronals de graf
node_id: "concept:xarxes_neuronals_de_graf"
node_type: "concept"
category: conceptes
tags:
  - grafs
  - xarxes-neuronals
  - aprenentatge-profund
  - GNN
sources:
  - https://arxiv.org/abs/1812.08434
  - https://arxiv.org/abs/1609.02907
  - https://arxiv.org/abs/1704.01212
  - https://www.ijcai.org/proceedings/2024/0898.pdf
related_concepts:
  - "[[grafs_i_models_de_llenguatge]]"
  - "[[GraphQA]]"
  - "[[GraphRAG]]"
  - "[[embeddings]]"
  - "[[xarxes_neuronals]]"
  - "[[ontologies_associatives]]"
related_models:
  - "[[G-Retriever]]"
status: reviewed
created: 2026-08-07
updated: 2026-09-18
---

# Xarxes neuronals de graf

## Definició

Una **xarxa neuronal de graf (GNN)** és una família de xarxes neuronals dissenyada per aprendre sobre dades formades per **nodes, arestes i atributs**. En lloc de processar una seqüència o una graella fixa, una GNN aprofita la topologia del graf i actualitza la representació de cada node amb informació dels seus veïns.

## Per què és important?

Moltes dades reals són relacionals: xarxes socials, molècules, mapes, dependències de programari, cadenes de subministrament, participacions empresarials i grafs de coneixement.

Una GNN pot aprendre patrons que depenen alhora de:

- les característiques pròpies d'un node;
- els seus veïns;
- el tipus o pes de les arestes;
- l'estructura local i, acumulant capes, una part més àmplia del graf.

## Intuïció

Imagina una empresa dins d'una xarxa de proveïdors, clients i competidors. Mirar només les seves dades és com analitzar-la aïlladament. Una GNN permet que la seva representació incorpori informació de les empreses connectades.

És semblant a una anàlisi de risc de cadena de subministrament: el risc d'un node pot dependre de riscos que es troben un o diversos salts més enllà.

## Message passing: la idea central

Una manera general d'entendre moltes GNN modernes és el **message passing**.

Per a cada node (v), en una capa (k):

[
m_v^{(k)} = AGGREGATEleft({h_u^{(k-1)} : u in N(v)}ight)
]

[
h_v^{(k)} = UPDATEleft(h_v^{(k-1)}, m_v^{(k)}ight)
]

On:

- (h_v^{(k)}) és la representació del node (v) a la capa (k);
- (N(v)) és el conjunt de veïns;
- (AGGREGATE) combina els missatges dels veïns;
- (UPDATE) integra la informació rebuda amb l'estat propi.

Gilmer et al. van formalitzar aquesta visió amb les **Message Passing Neural Networks (MPNNs)**. Kipf i Welling van mostrar un cas molt influent amb les **Graph Convolutional Networks (GCN)**, on la informació dels veïns es propaga mitjançant una regla de convolució sobre el graf.

## Funcionament simplificat

1. Cada node rep una representació inicial, per exemple atributs numèrics o embeddings.
2. Cada node rep missatges dels seus veïns.
3. Els missatges s'agreguen amb una regla com suma, mitjana o atenció.
4. La representació del node s'actualitza.
5. El procés es repeteix durant diverses capes.
6. Les representacions finals s'utilitzen per predir nodes, arestes o propietats globals del graf.

Amb una capa, un node veu principalment els veïns immediats. Amb dues capes pot incorporar informació de dos salts, i així successivament.

## Què pot predir una GNN?

| Tasca | Exemple |
|---|---|
| Classificació de nodes | classificar empreses segons un risc |
| Predicció d'enllaços | estimar si dues entitats poden estar relacionades |
| Classificació de grafs | classificar una molècula o una xarxa sencera |
| Regressió | predir una propietat numèrica |
| Embeddings de graf | obtenir vectors que resumeixen estructura i contingut |
| Suport a GraphQA | representar subgrafs rellevants per respondre preguntes |

## Relació amb embeddings

Els embeddings tradicionals poden representar cada element amb un vector. Una GNN afegeix un pas important: el vector d'un node es transforma tenint en compte **qui l'envolta i com està connectat**.

Això permet distingir dos nodes amb atributs semblants però situats en contextos relacionals diferents.

## Relació amb els LLM

Un LLM treballa principalment amb seqüències de tokens. Una GNN treballa amb una estructura de relacions explícites.

Es poden combinar de diverses maneres:

- el LLM converteix text de nodes o arestes en embeddings;
- la GNN propaga informació per la topologia;
- el LLM genera la resposta final;
- una capa de fusió combina representacions textuals i gràfiques.

Aquesta combinació és diferent de **GraphRAG**: GraphRAG és una arquitectura de recuperació sobre grafs i pot funcionar sense entrenar una GNN.

## Relació amb GraphQA

GraphQA és una **tasca**; una GNN és una **família de models**.

Una GNN pot ajudar a GraphQA perquè codifica la topologia i propaga informació entre nodes. Però un sistema GraphQA també pot utilitzar consultes simbòliques, recorreguts, recuperació de subgrafs o un LLM sense GNN.

G-Retriever és un exemple de sistema que combina recuperació de subgrafs, components de GNN i un LLM per treballar amb preguntes sobre grafs textuals.

## Exemple aplicat a finances

Suposa una xarxa amb:

- empreses;
- clients;
- proveïdors;
- administradors;
- productes;
- riscos.

Una GNN podria aprendre una representació d'una empresa que combini els seus atributs amb informació dels seus proveïdors i clients. Això podria servir per detectar concentració de riscos, similituds estructurals o relacions que no emergeixen mirant cada empresa de manera independent.

Aquest ús requereix dades de graf prou netes i un objectiu de predicció clar; una GNN no converteix automàticament una wiki en un sistema d'anàlisi predictiva.

## Limitacions i errors habituals

- **oversmoothing:** amb massa capes, les representacions de nodes diferents poden tornar-se massa semblants;
- **oversquashing:** molta informació distant pot quedar comprimida en vectors massa petits;
- la qualitat depèn fortament de la topologia i dels atributs;
- els grafs incomplets o sorollosos propaguen errors;
- afegir capes no equival sempre a capturar millor dependències llunyanes;
- una GNN no substitueix un graf de coneixement, un LLM ni GraphRAG;
- el cost computacional pot créixer en grafs grans i densos.

## Relacions

- [[grafs_i_models_de_llenguatge]]
- [[GraphQA]]
- [[GraphRAG]]
- [[G-Retriever]]
- [[embeddings]]
- [[xarxes_neuronals]]
- [[ontologies_associatives]]

## Fonts

- [Semi-Supervised Classification with Graph Convolutional Networks — Kipf & Welling](https://arxiv.org/abs/1609.02907).
- [Neural Message Passing for Quantum Chemistry — Gilmer et al.](https://arxiv.org/abs/1704.01212).
- [Graph Neural Networks: Foundations, Frontiers, and Applications](https://arxiv.org/abs/1812.08434).
- [A Survey of Graph Meets Large Language Model](https://www.ijcai.org/proceedings/2024/0898.pdf).
