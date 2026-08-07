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
  - https://www.ijcai.org/proceedings/2024/0898.pdf
related_concepts: []
related_models: []
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Xarxes neuronals de graf

## Definició

Una xarxa neuronal de graf (GNN) és una xarxa neuronal dissenyada per processar dades formades per nodes i relacions. Cada node actualitza la seva representació combinant la seva informació amb la dels nodes veïns.

## Per què és important?

Moltes dades reals no són una seqüència ni una graella: xarxes socials, molècules, mapes, dependències de programari i grafs de coneixement són estructures relacionals.

Les GNN poden aprendre patrons que depenen tant del contingut d’un node com de la seva posició i connexions dins del graf.

## Intuïció

En una xarxa d’empreses, una empresa pot tenir una característica pròpia, però també pot estar influïda per proveïdors, competidors o clients relacionats. Una GNN agrega informació dels veïns i aprèn una representació contextual.

## Funcionament simplificat

1. Cada node rep una representació inicial.
2. La xarxa recull informació dels nodes veïns.
3. Combina la informació pròpia i la rebuda.
4. Repiteix el procés durant diverses capes.
5. Utilitza les representacions per predir nodes, arestes o propietats del graf.

## Relació amb els LLM

Un LLM treballa principalment amb seqüències de tokens. Una GNN treballa amb una estructura de relacions explícites. Es poden combinar:

- el LLM interpreta text i genera representacions riques;
- la GNN processa la topologia;
- un mòdul de fusió combina semàntica i estructura.

Aquesta combinació és diferent de GraphRAG: GraphRAG pot recuperar informació gràfica sense que el LLM formi part d’una GNN.

## Tasques habituals

- classificació de nodes;
- predicció d’enllaços;
- classificació de grafs;
- raonament sobre grafs de coneixement;
- predicció de propietats de molècules o xarxes.

## Relacions

- [[grafs_i_models_de_llenguatge]]
- [[G-Retriever]]
- [[embeddings]]
- [[xarxes_neuronals]]
- [[ontologies_associatives]]

## Limitacions i errors habituals

- massa capes poden difuminar les representacions dels nodes;
- la qualitat depèn de la topologia i dels atributs del graf;
- els grafs incomplets o sorollosos generen aprenentatges defectuosos;
- una GNN no substitueix automàticament un LLM;
- no s’ha de confondre una GNN amb un graf de coneixement o amb GraphRAG.

## Fonts

- [Graph Neural Networks: Foundations, Frontiers, and Applications](https://arxiv.org/abs/1812.08434).
- [A Survey of Graph Meets Large Language Model](https://www.ijcai.org/proceedings/2024/0898.pdf).
