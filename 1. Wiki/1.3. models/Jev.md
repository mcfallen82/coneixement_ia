---
title: Jev
category: models
node_id: "model:jev"
node_type: model
model_family: system_one_decision_model
architecture: no publicada; mostreig paral·lel de decisions tipades
tags:
  - model
  - classificacio
  - agents
modalities:
  - text
  - dades estructurades
training_objective: Reinforcement Learning for Calibrated Decisions (RLCD), segons TypeSafe AI
authors: []
developer: TypeSafe AI
release_date: 2026-09-15
sources:
  - https://typesafe.ai/blog/introducing-system-one-models-and-jev
  - https://docs.typesafe.ai/model-jaggedness/jev-1.13
  - https://github.com/willkelly/jev-evaluation
  - https://substack.com/home/post/p-216615368
related_concepts:
  - "[[1. Wiki/1.2. conceptes/calibratge_de_probabilitats]]"
  - "[[1. Wiki/1.2. conceptes/gates_i_guardrails_agents]]"
  - "[[1. Wiki/1.2. conceptes/agent_harness]]"
  - "[[1. Wiki/1.2. conceptes/avaluacio_de_models]]"
related_models: []
status: reviewed
created: 2026-09-21
updated: 2026-09-21
---

# Jev

## Què és?

Jev és un model de decisió de TypeSafe AI que transforma un estat no estructurat i un conjunt de preguntes tipades en probabilitats o puntuacions estructurades. Va ser anunciat el 15 de setembre de 2026 com el primer “System One Model” públic de l'empresa.

El terme **System One** és una denominació comercial inspirada en la distinció de Daniel Kahneman entre judici ràpid i deliberació lenta. No designa, per si sol, una categoria acadèmica establerta de models.

## Quin problema resol?

Els models generatius produeixen text token a token fins i tot quan el programa només necessita classificar, puntuar o escollir una opció. Jev renuncia a generar text i optimitza la interfície per a decisions tancades, de baixa latència i fàcils d'integrar en codi.

## Arquitectura i entrenament

TypeSafe afirma que Jev utilitza una arquitectura pròpia, un mostrejador paral·lel i un mètode anomenat **Reinforcement Learning for Calibrated Decisions (RLCD)**. No hi ha prou detall públic per descriure'n l'arquitectura interna ni reproduir l'entrenament. Per tant, aquestes característiques s'han de tractar com a afirmacions del desenvolupador, no com un resultat acadèmic independentment verificat.

## Entrada i sortida

La interfície documentada admet tres formes principals:

| Tipus | Sortida | Ús |
|---|---|---|
| `noul` | probabilitat d'una afirmació | decisió binària o filtre |
| `choice` | opció guanyadora i distribució entre opcions | encaminament o classificació |
| `score` | posició en una escala ordenada | severitat, prioritat o qualitat |

Diverses preguntes es poden respondre en paral·lel en una sola crida. Aquesta propietat afavoreix descompondre una decisió complexa en judicis simples i combinar-los posteriorment amb codi.

## Què aporta de nou

- una interfície nativa de decisions tipades en lloc de generació de text;
- mostreig paral·lel de múltiples preguntes;
- cost i latència baixos segons el desenvolupador i proves independents;
- probabilitats pensades per a classificació, encaminament i controls freqüents;
- separació clara entre judici semàntic i càlcul determinista.

## Limitacions documentades

Jev 1.13 presenta dificultats amb:

- aritmètica, recompte, dates i representacions numèriques;
- negacions, indirecció i raonament de diversos salts;
- context extens amb informació irrellevant;
- generació de text o explicacions;
- contingut adversari i afirmacions falses d'autoritat;
- coherència entre preguntes separades que una persona podria considerar complements lògics.

L'absència de generació lliure garanteix que la sortida respecti l'esquema, però **no garanteix que la decisió sigui certa**. “Sense errors de tipus” i “sense al·lucinacions” no són afirmacions equivalents.

## Evidència disponible

- TypeSafe publica preu, latència, metodologia pròpia i limitacions, però reconeix biaixos possibles en les seves avaluacions.
- L'article de Ghelbur informa d'una prova de 300 crides i d'atacs contra una porta de control. És evidència pràctica útil, però no substitueix una avaluació externa extensa.
- L'avaluació independent de Will Kelly utilitza 123.805 peticions i 28 prediccions preregistrades. Mostra que el calibratge i la robustesa depenen fortament del domini i que les injeccions basades en autoritat poden moure les respostes.

## Aplicacions adequades

- encaminament entre models o eines;
- etiquetatge i classificació de gran volum;
- priorització de casos;
- filtres semàntics de baix impacte;
- una capa probabilística dins de [[1. Wiki/1.2. conceptes/gates_i_guardrails_agents|portes de control]] amb regles deterministes i escalat humà.

## Quan no utilitzar-lo com a decisor únic

- càlculs, comparacions de dates o regles exactes;
- decisions legals, financeres o operatives vinculants;
- accions irreversibles o amb secrets;
- tasques que exigeixen justificació textual;
- dominis sense un conjunt de prova propi;
- entorns on l'estat pot contenir instruccions hostils i no hi ha cap altra capa de contenció.

## Exemple financer

Jev podria classificar fragments d'un 10-K segons si contenen indicis de deteriorament de marges, risc de client o canvi comptable. Python hauria d'extreure i calcular les xifres; un analista hauria de revisar qualsevol conclusió que afecti una decisió d'inversió.

## Fonts

- [TypeSafe AI — Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev), 2026. Font oficial.
- [TypeSafe AI — Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13), 2026. Limitacions oficials.
- [Will Kelly — An adversarial evaluation of Jev](https://github.com/willkelly/jev-evaluation), 2026. Avaluació independent.
- [Eugeniu Ghelbur — What Is Jev? The Manual for Agent Harnesses](https://substack.com/home/post/p-216615368), 2026. Síntesi i prova pràctica.
