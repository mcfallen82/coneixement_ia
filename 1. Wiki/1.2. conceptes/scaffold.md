---
title: Scaffold
node_id: "concept:scaffold"
node_type: "concept"
category: conceptes
tags:
  - inteligencia-artificial
  - agents
  - models-de-llenguatge
  - arquitectura
  - educacio
sources:
  - https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
  - https://www.anthropic.com/engineering/building-effective-agents
  - https://openai.github.io/openai-agents-python/agents/
  - https://openai.github.io/openai-agents-python/tools/
  - https://arxiv.org/abs/2604.03515
  - https://arxiv.org/abs/2605.05716
  - https://academic.oup.com/book/58946/chapter/493003498
related_concepts:
  - "[[context_engineering]]"
  - "[[skills]]"
  - "[[avaluacio_de_models]]"
  - "[[prompt_engineering]]"
related_models: []
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Scaffold

## Definició

En intel·ligència artificial, un **scaffold** és l’estructura de suport que envolta un model perquè pugui completar una tasca dins d’un procés controlat.

En els agents de IA, també s’anomena sovint **agent scaffold** o **agent harness**. Inclou les instruccions, el context, les eines, l’estat, els bucles de control, la delegació i les validacions que permeten que un LLM actuï com a part d’un sistema.

En educació, *scaffolding* descriu un suport temporal i adaptat al nivell de l’aprenent que es retira progressivament quan aquest guanya autonomia.

## Per què és important?

Un LLM no és, per si sol, un agent complet. El model pot generar i interpretar text, però necessita una estructura que decideixi:

- quin objectiu ha de perseguir;
- quina informació rep;
- quines eines pot utilitzar;
- com conserva l’estat;
- com comprova el resultat;
- quines accions requereixen aprovació humana.

Per això, el comportament d’un agent depèn del model i del *scaffold* que l’envolta. Quan s’avalua un agent, no s’hauria d’atribuir automàticament tot el resultat al model.

## Intuïció

La metàfora és la bastida d’un edifici. La bastida no és l’edifici ni substitueix els materials, però permet treballar-hi amb més ordre i seguretat.

En un sistema d’IA:

- el **model** és el motor de generació i interpretació;
- el **scaffold** és el sistema de treball;
- les **eines** són els instruments per consultar o actuar;
- les **validacions** són els controls de qualitat;
- l’**aplicació** és el resultat que rep l’usuari.

## Funcionament

Un scaffold típic pot seguir aquest cicle:

1. rep l’objectiu i el context inicial;
2. prepara instruccions i informació rellevant;
3. demana al model el següent pas;
4. executa una eina o actualitza l’estat;
5. observa el resultat;
6. repeteix, delega o modifica el pla;
7. valida la sortida;
8. retorna el resultat o demana aprovació.

Els components habituals són:

- instruccions, plantilles i prompts;
- recuperació de documents i gestió del context;
- eines locals o externes;
- memòria i estat de sessió;
- planificació i bucles d’execució;
- subagents i handoffs;
- sortides estructurades;
- guardrails, proves i intervenció humana.

No tots els scaffolds necessiten tots aquests components. La configuració adequada depèn de la tasca.

## Exemple

Per analitzar una memòria anual, un LLM sense scaffold rep una petició i redacta una resposta.

Amb un scaffold documental, el sistema pot:

1. carregar la memòria i les instruccions del projecte;
2. recuperar les seccions sobre ingressos, marges i deute;
3. extreure les dades en un esquema estructurat;
4. calcular ràtios amb una eina;
5. comprovar les xifres contra la font;
6. generar l’anàlisi amb una plantilla;
7. marcar les afirmacions sense evidència.

El resultat és més traçable perquè el procés separa recuperació, càlcul, redacció i validació.

## Aplicacions

- agents de programació amb fitxers, terminal i proves;
- assistents d’anàlisi documental;
- wikis i sistemes de coneixement;
- automatització amb eines externes;
- fluxos multiagent;
- tutors d’aprenentatge adaptatiu;
- sistemes amb aprovació humana per a accions sensibles.

En ia_knowledge, AGENTS.md, les skills, el frontmatter, el manifest, els validadors i la capa gràfica formen conjuntament un scaffold de coneixement.

## Diferències amb conceptes propers

| Concepte | Funció |
|---|---|
| Model | Genera i interpreta informació |
| Prompt | Dona una instrucció concreta |
| Eina | Permet consultar o actuar |
| Agent | Sistema que utilitza un model dins d’un procés per assolir un objectiu |
| Scaffold | Arquitectura operativa que organitza el model, el context, les eines i els controls |
| Framework | Llibreria o entorn per construir aplicacions i scaffolds |
| Skill | Procediment reutilitzable que pot formar part del scaffold |
| RAG | Tècnica o subsistema de recuperació que pot formar part del scaffold |

## Limitacions i errors habituals

- confondre el scaffold amb el model;
- atribuir al model una millora que prové de les eines o del flux;
- afegir planificació, memòria o autoreflexió sense una hipòtesi que es pugui provar;
- crear una arquitectura massa complexa per a una tasca senzilla;
- no controlar els permisos i les accions amb efectes externs;
- no avaluar el sistema complet;
- confondre el sentit d’agent scaffold amb el scaffolding pedagògic;
- utilitzar la metàfora com si fos una definició tècnica universal.

## Relacions

- [[context_engineering]]
- [[skills]]
- [[avaluacio_de_models]]
- [[prompt_engineering]]
- [[RAG]]
- [[AGENTS.md]]

## Fonts

- [Anthropic — Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents).
- [Anthropic — Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents).
- [OpenAI Agents SDK — Agents](https://openai.github.io/openai-agents-python/agents/).
- [OpenAI Agents SDK — Tools](https://openai.github.io/openai-agents-python/tools/).
- [Inside the Scaffold: A Source-Code Taxonomy of Coding Agent Architectures](https://arxiv.org/abs/2604.03515).
- [More Is Not Always Better: Cross-Component Interference in LLM Agent Scaffolding](https://arxiv.org/abs/2605.05716).
- [Can AI-Based Scaffolding Promote Students’ Robust Learning?](https://academic.oup.com/book/58946/chapter/493003498).
