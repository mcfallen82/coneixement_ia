---
title: Calibratge de probabilitats
category: conceptes
node_id: "concept:calibratge_de_probabilitats"
node_type: concept
tags:
  - avaluacio
  - probabilitat
  - classificacio
sources:
  - https://proceedings.mlr.press/v70/guo17a.html
  - https://github.com/willkelly/jev-evaluation
  - https://substack.com/home/post/p-216615368
related_concepts:
  - "[[1. Wiki/1.2. conceptes/avaluacio_de_models]]"
  - "[[1. Wiki/1.2. conceptes/softmax_i_cross_entropy]]"
  - "[[1. Wiki/1.2. conceptes/gates_i_guardrails_agents]]"
related_models:
  - "[[1. Wiki/1.3. models/Jev]]"
status: reviewed
created: 2026-09-21
updated: 2026-09-21
---

# Calibratge de probabilitats

## Definició

Un classificador està **calibrat** quan les probabilitats que anuncia coincideixen amb les freqüències observades. Entre molts casos als quals assigna un 80%, aproximadament un 80% haurien de ser correctes.

## Per què és important?

L'exactitud respon “quantes decisions encerta?”. El calibratge respon “podem interpretar el 0,8 com un 80%?”. Aquesta segona pregunta és essencial per fixar llindars, decidir quan escalar i comparar el cost d'errors diferents.

## Intuïció financera

Un analista pot encertar moltes previsions i, alhora, expressar una confiança mal calibrada. Si totes les idees es presenten com a gairebé segures, el percentatge no ajuda a dimensionar posicions ni a prioritzar revisions. Un bon calibratge converteix la confiança en informació operativa.

## Probabilitat i confiança

No sempre són el mateix:

- la **probabilitat** s'associa a una opció concreta;
- una mesura de **confiança** pot descriure com de concentrada és tota la distribució entre opcions;
- un 0,51 contra 0,49 té un guanyador, però separa molt poc les alternatives;
- un 0,98 contra 0,02 mostra una decisió molt més concentrada.

Cal documentar la definició exacta que utilitza cada API. No s'ha d'inventar una “confiança” a partir d'una probabilitat i després comparar-la amb una mètrica definida d'una altra manera.

## Com s'avalua

1. Reunir casos amb resultat conegut i separats del disseny del prompt.
2. Agrupar prediccions en intervals de probabilitat.
3. Comparar probabilitat mitjana i freqüència real de cada interval.
4. Mesurar també exactitud, discriminació, cobertura i cost dels errors.
5. Repetir l'avaluació quan canviïn el domini, el prompt, el model o les dades.

L'**error esperat de calibratge** (ECE) resumeix les diferències entre confiança i exactitud per intervals, però depèn de com es construeixen aquests intervals. També són útils la puntuació de Brier, diagrames de fiabilitat i corbes risc-cobertura.

## Calibratge local i canvi de domini

El calibratge no és una propietat universal del model. Pot funcionar en el domini per al qual ha estat entrenat o ajustat i degradar-se fora de distribució. L'avaluació independent de Jev trobà bon comportament relatiu en encaminament de tiquets, però fracàs complet en un problema formal de 3-SAT. Això no invalida el model: delimita el seu domini útil.

## Llindars segons el cost

Un llindar no s'ha de copiar d'un article. S'ha d'estimar amb:

- cost d'autoritzar una acció perillosa;
- cost d'aturar una acció segura;
- disponibilitat d'una revisió humana;
- reversibilitat de l'acció;
- cobertura desitjada.

Per això, una decisió vinculant pot exigir revisió humana encara que la probabilitat sigui alta, mentre que l'encaminament entre dos models pot tolerar més error.

## Errors habituals

- confondre probabilitats de *softmax* amb probabilitats calibrades;
- avaluar només l'exactitud mitjana;
- traslladar un llindar entre tipus de pregunta o dominis;
- validar amb els mateixos exemples utilitzats per ajustar el sistema;
- interpretar una sortida tipada com a prova de correcció;
- ignorar els casos rebutjats o escalats en informar del rendiment.

## Relacions

- forma part de [[1. Wiki/1.2. conceptes/avaluacio_de_models|l'avaluació de models]];
- ajuda a configurar [[1. Wiki/1.2. conceptes/gates_i_guardrails_agents|portes de control]];
- les probabilitats poden provenir d'una distribució com la descrita a [[1. Wiki/1.2. conceptes/softmax_i_cross_entropy]], però encara poden necessitar recalibratge.

## Fonts

- [Guo et al. — On Calibration of Modern Neural Networks](https://proceedings.mlr.press/v70/guo17a.html), ICML 2017.
- [Will Kelly — An adversarial evaluation of Jev](https://github.com/willkelly/jev-evaluation), 2026. Avaluació independent preregistrada.
- [Eugeniu Ghelbur — What Is Jev? The Manual for Agent Harnesses](https://substack.com/home/post/p-216615368), 2026.
