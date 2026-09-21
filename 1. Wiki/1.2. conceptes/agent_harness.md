---
title: Arnès d'agent
category: conceptes
node_id: "concept:agent_harness"
node_type: concept
tags:
  - agents
  - arquitectura
  - control
sources:
  - https://substack.com/home/post/p-216615368
  - https://arxiv.org/abs/2606.10106
related_concepts:
  - "[[1. Wiki/1.2. conceptes/context_engineering]]"
  - "[[1. Wiki/1.2. conceptes/gates_i_guardrails_agents]]"
  - "[[1. Wiki/1.2. conceptes/AGENTS_MD]]"
related_models:
  - "[[1. Wiki/1.3. models/Jev]]"
status: reviewed
created: 2026-09-21
updated: 2026-09-21
---

# Arnès d'agent

## Definició

Un **arnès d'agent** és la capa de programari que envolta un model i el converteix en un sistema capaç d'actuar de manera iterativa sobre un entorn. No és el model: és el conjunt que organitza el bucle, les eines, el context i els controls d'execució.

## Per què és important?

La capacitat real d'un agent no depèn només del model. Dos sistemes amb el mateix model poden comportar-se de manera molt diferent segons quines eines reben, què entra al context, com comproven els resultats i quines accions necessiten autorització.

En termes empresarials, el model s'assembla al criteri d'un analista; l'arnès és el sistema de treball que li assigna dades, permisos, procediments, controls i registre d'auditoria.

## Nucli mínim

La definició acadèmica de Macedo proposa quatre condicions necessàries i conjuntament suficients:

| Element | Funció | Pregunta de comprovació |
|---|---|---|
| Bucle adaptatiu | alterna raonament, acció i observació | el resultat d'un pas pot canviar el següent? |
| Interfície d'eines | permet percebre o modificar l'entorn | el model pot llegir, executar o escriure? |
| Gestió del context | decideix què entra i surt de la finestra del model | el sistema selecciona i comprimeix informació? |
| Control en temps d'execució | verifica, limita o substitueix decisions del model | hi ha algun control que no depengui només de l'obediència del model? |

Memòria, observabilitat, verificadors, reintents, canvi de model, entorns aïllats i regles deterministes reforcen aquestes quatre peces, però no constitueixen requisits independents.

## Distincions útils

- **Model:** produeix prediccions o decisions; no administra per si sol l'entorn.
- **SDK:** ofereix blocs per construir un agent, però pot no tancar el bucle.
- **Marc d'agents:** coordina rols o agents; pot contenir diversos arnesos.
- **Orquestrador:** executa un flux prefixat; un arnès adapta el pas següent a l'observació anterior.
- **Arnès d'avaluació:** mesura un sistema des de fora; l'arnès d'agent controla l'execució mentre ocorre.

## Exemple

Un agent que revisa un 10-K pot:

1. seleccionar les notes financeres rellevants;
2. cridar una eina d'extracció;
3. comprovar si falten dades;
4. recuperar un altre fragment;
5. validar les xifres amb codi;
6. demanar aprovació abans de publicar o modificar el repositori.

El model interpreta el document; l'arnès governa el procés.

## Relació amb les instruccions

Un fitxer [[1. Wiki/1.2. conceptes/AGENTS_MD|AGENTS.md]] és una font d'instruccions persistents dins de l'arnès, però no és l'arnès complet. Les instruccions poden orientar el model; els controls, permisos i verificacions han de poder imposar límits encara que el model interpreti malament una ordre.

## Limitacions i errors habituals

- atribuir al model resultats que provenen del disseny de l'arnès;
- confondre una cadena fixa de passos amb un bucle adaptatiu;
- tractar el context com un historial il·limitat;
- deixar que el mateix model proposi, autoritzi i verifiqui una acció crítica;
- considerar els controls probabilístics com a substituts de regles deterministes, permisos o entorns aïllats.

## Relacions

- utilitza [[1. Wiki/1.2. conceptes/context_engineering|enginyeria del context]];
- incorpora [[1. Wiki/1.2. conceptes/gates_i_guardrails_agents|portes de control i guardrails]];
- pot utilitzar [[1. Wiki/1.3. models/Jev|Jev]] com a classificador o jutge ràpid, però no en depèn.

## Fonts

- [Eugeniu Ghelbur — What Is Jev? The Manual for Agent Harnesses](https://substack.com/home/post/p-216615368), 2026. Font secundària i prova pràctica.
- [Sanderson Oliveira de Macedo — What makes a harness a harness](https://arxiv.org/abs/2606.10106), 2026. Definició acadèmica i criteris T1–T4.
