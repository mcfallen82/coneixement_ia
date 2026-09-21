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

Jev és un model de decisió de TypeSafe AI que transforma un **estat no estructurat** i un conjunt de **preguntes tipades** en decisions probabilístiques que un programa pot consumir directament. Va ser anunciat el 15 de setembre de 2026 com el primer “System One Model” públic de l'empresa i es va llançar en accés anticipat.

TypeSafe el presenta amb una analogia útil: una **crida a una funció amb intel·ligència**. L'estat del programa entra en forma de text o dades; les opcions de resposta i el seu esquema s'han definit abans; el model retorna valors tipats i probabilitats, no una explicació redactada.

El terme **System One** és una denominació de TypeSafe inspirada en la distinció de Daniel Kahneman entre judici ràpid i deliberació lenta. Expressa l'objectiu de resoldre judicis immediats i ben delimitats, però no designa, per si sol, una família acadèmica consolidada. El nom **Jev** al·ludeix a l'economista William Stanley Jevons i a la paradoxa de Jevons: TypeSafe sosté que abaratir la intel·ligència automatitzada n'ampliarà la demanda.

## Quin problema resol?

Els models generatius produeixen text token a token fins i tot quan un programa només necessita classificar, puntuar, extreure una categoria o escollir una opció. Aquesta flexibilitat obliga després a interpretar, validar i convertir la cadena generada.

Jev renuncia deliberadament a la generació lliure i s'especialitza en decisions tancades. La seva funció no és substituir un LLM generalista, sinó ocupar la part del flux que TypeSafe descriu com a **“condicionals difusos”**: decisions on una regla escrita a mà seria massa rígida, però on tampoc cal generar una resposta oberta.

Exemples:

- classificar una petició;
- decidir a quina eina o model s'ha d'encaminar;
- puntuar risc, prioritat o qualitat;
- detectar si un fragment compleix una condició semàntica;
- decidir si un cas s'executa, es bloqueja o s'escala.

## Arquitectura i entrenament

TypeSafe descriu tres peces pròpies:

1. una arquitectura orientada a automatització;
2. un mostrejador paral·lel que produeix múltiples decisions en una sola consulta;
3. un mètode d'entrenament anomenat **Reinforcement Learning for Calibrated Decisions (RLCD)**.

Segons l'empresa, RLCD no optimitza principalment la preferència humana per una resposta redactada, com l'RLHF, sinó que intenta produir probabilitats que reflecteixin honestament la incertesa del model en tasques de tipus System One.

Tanmateix, la publicació de llançament no descriu l'arquitectura, les dades ni l'algoritme de RLCD amb prou detall per reproduir-los. Cal tractar aquests elements com a afirmacions tècniques del desenvolupador, no com un mètode acadèmic obert i independentment verificat.

## Entrada i sortida

La interfície documentada admet tres formes principals:

| Tipus | Sortida | Ús |
|---|---|---|
| `noul` | probabilitat d'una afirmació | decisió binària o filtre |
| `choice` | opció guanyadora i distribució entre opcions | encaminament o classificació |
| `score` | posició en una escala ordenada | severitat, prioritat o qualitat |

Diverses preguntes es poden respondre en paral·lel en una sola crida. Aquesta propietat afavoreix descompondre una decisió complexa en judicis simples i combinar-los posteriorment amb codi.

El patró d'integració és:

```text
estat del programa
      ↓
preguntes i opcions definides per endavant
      ↓
Jev: decisions tipades + probabilitats
      ↓
codi: regles, llindars, combinació i acció
```

La decisió final continua pertanyent al programa. Jev aporta judicis semàntics; el codi conserva els càlculs, les invariants i els efectes externs.

## Diferència respecte d'un model generatiu

| Dimensió | LLM generatiu | Jev segons TypeSafe |
|---|---|---|
| Objectiu principal | generar cadenes útils o preferides | prendre decisions probabilístiques calibrades |
| Sortida | text o estructura generada token a token | valors tipats definits abans de la crida |
| Mostreig | seqüencial i autoregressiu | múltiples sortides en paral·lel |
| Flexibilitat | alta: text, codi, explicacions | baixa: només l'espai de resposta declarat |
| Integració | cal analitzar i validar la sortida | la sortida ja té un contracte de tipus |
| Ús natural | conversa, síntesi, creació i raonament obert | classificació, puntuació, encaminament i control |

La menor flexibilitat és precisament la font de l'eficiència i la predictibilitat de la interfície.

## Què aporta de nou

- una interfície nativa de decisions tipades en lloc de generació de text;
- mostreig paral·lel de múltiples preguntes;
- cost i latència baixos segons el desenvolupador i proves independents;
- probabilitats pensades per a classificació, encaminament i controls freqüents;
- separació clara entre judici semàntic i càlcul determinista.

## Rendiment declarat per TypeSafe

A la publicació de llançament, TypeSafe declara:

- latència de servei entre **70 i 500 ms**;
- preu de **0,042 dòlars per milió de tokens d'entrada** i sortida sense cost mesurable;
- entre **40 i 200 vegades** més velocitat en consultes amb forma de System One;
- fins a **193,6 vegades** més velocitat i **444,6 vegades** menys cost en els seus fluxos d'avaluació.

Aquestes xifres no s'han de llegir com un benchmark general. La mateixa empresa adverteix que els guanys més elevats representen l'extrem favorable, que els fluxos van ser creats pel seu equip i que les probabilitats de referència provenen d'altres models, no sempre d'una veritat de base observable. Preu, latència i disponibilitat també poden canviar després de l'accés anticipat.

## Limitacions documentades

Jev 1.13 presenta dificultats amb:

- aritmètica, recompte, dates i representacions numèriques;
- negacions, indirecció i raonament de diversos salts;
- context extens amb informació irrellevant;
- generació de text o explicacions;
- contingut adversari i afirmacions falses d'autoritat;
- coherència entre preguntes separades que una persona podria considerar complements lògics.

L'absència de generació lliure garanteix que la sortida respecti l'esquema, però **no garanteix que la decisió sigui certa**. “Sense errors de tipus” i “sense al·lucinacions” no són afirmacions equivalents.

La formulació “no pot al·lucinar” utilitzada al llançament s'ha d'interpretar en un sentit restringit: Jev no pot inventar una clau o un tipus fora de l'esquema permès. Sí que pot assignar una probabilitat incorrecta o seleccionar una opció equivocada. La mateixa publicació reconeix que el 0% d'errors mostrat per TypeSafe en aquest punt és una garantia d'ajust a l'esquema, no una mesura empírica de veracitat.

## Evidència disponible

- TypeSafe publica preu, latència, metodologia pròpia i limitacions. També reconeix que la demostració comparativa utilitza un estat breu favorable, que els fluxos els va construir el seu equip i que les acceleracions màximes són l'extrem alt del que espera observar.
- Les avaluacions de flux de TypeSafe mantenen el mateix graf de computació per a tots els models i comparen les respostes amb probabilitats de referència obtingudes de models externs. Això mesura adequació al flux dissenyat, no exactitud contra una veritat de base independent.
- L'article de Ghelbur informa d'una prova de 300 crides i d'atacs contra una porta de control. És evidència pràctica útil, però no substitueix una avaluació externa extensa.
- L'avaluació independent de Will Kelly utilitza 123.805 peticions i 28 prediccions preregistrades. Mostra que el calibratge i la robustesa depenen fortament del domini i que les injeccions basades en autoritat poden moure les respostes.

## Aplicacions adequades

- encaminament entre models o eines;
- etiquetatge i classificació de gran volum;
- priorització de casos;
- filtres semàntics de baix impacte;
- processament massiu de registres o documents mitjançant classificacions independents;
- aplicacions en temps real on la latència d'un LLM generatiu seria excessiva;
- jutges o verificadors auxiliars de prompts, sortides o traces;
- una capa probabilística dins de [[1. Wiki/1.2. conceptes/gates_i_guardrails_agents|portes de control]] amb regles deterministes i escalat humà.

## Quan no utilitzar-lo com a decisor únic

- càlculs, comparacions de dates o regles exactes;
- decisions legals, financeres o operatives vinculants;
- accions irreversibles o amb secrets;
- tasques que exigeixen justificació textual;
- dominis sense un conjunt de prova propi;
- entorns on l'estat pot contenir instruccions hostils i no hi ha cap altra capa de contenció.

## Exemple financer

Jev podria rebre fragments d'un 10-K i respondre en paral·lel si contenen indicis de deteriorament de marges, dependència d'un client, canvi comptable o risc de liquiditat. Les probabilitats permetrien prioritzar els fragments que ha de revisar l'analista.

El repartiment correcte del treball seria:

- **Jev:** classificació semàntica i priorització;
- **Python:** extracció, recomptes, dates i càlculs;
- **LLM generatiu:** explicació i síntesi amb cites;
- **analista:** interpretació i decisió d'inversió.

## Fonts

- [TypeSafe AI — Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev), 2026. Font oficial.
- [TypeSafe AI — Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13), 2026. Limitacions oficials.
- [Will Kelly — An adversarial evaluation of Jev](https://github.com/willkelly/jev-evaluation), 2026. Avaluació independent.
- [Eugeniu Ghelbur — What Is Jev? The Manual for Agent Harnesses](https://substack.com/home/post/p-216615368), 2026. Síntesi i prova pràctica.
