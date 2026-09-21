---
title: Portes de control i guardrails d'agents
category: conceptes
node_id: "concept:gates_i_guardrails_agents"
node_type: concept
tags:
  - agents
  - seguretat
  - control
sources:
  - https://substack.com/home/post/p-216615368
  - https://docs.typesafe.ai/model-jaggedness/jev-1.13
  - https://arxiv.org/abs/2603.30016
related_concepts:
  - "[[1. Wiki/1.2. conceptes/agent_harness]]"
  - "[[1. Wiki/1.2. conceptes/calibratge_de_probabilitats]]"
  - "[[1. Wiki/1.2. conceptes/avaluacio_de_models]]"
  - "[[1. Wiki/1.2. conceptes/context_engineering]]"
related_models:
  - "[[1. Wiki/1.3. models/Jev]]"
status: reviewed
created: 2026-09-21
updated: 2026-09-21
---

# Portes de control i guardrails d'agents

## Definició

Una **porta de control** (*gate*) intercepta una acció proposada per un agent i decideix si es pot executar, s'ha d'escalar a una persona o s'ha de denegar. Un **guardrail** és una categoria més àmplia: qualsevol límit, política, comprovació o mecanisme de contenció que redueix comportaments no desitjats.

## Per què és important?

Quan un agent només genera text, un error pot quedar en una resposta. Quan utilitza eines, el mateix error pot esborrar dades, publicar informació, executar una ordre o enviar un missatge. El control ha d'actuar abans de l'efecte extern.

## Arquitectura per capes

| Capa | Mecanisme | Adequada per a |
|---|---|---|
| 1 | regles deterministes | secrets, ordres prohibides, límits numèrics i permisos invariants |
| 2 | permisos i entorn aïllat | restringir recursos, rutes, xarxa i capacitat de modificació |
| 3 | classificador probabilístic | ambigüitat semàntica, intenció, severitat o encaminament |
| 4 | intervenció humana | decisions irreversibles, vinculants o amb baixa confiança |
| 5 | registre i revisió | calibratge, regressions, incidents i traçabilitat |

La idea central és la **defensa en profunditat**: cap jutge probabilístic hauria de ser l'única barrera davant d'una acció d'alt impacte.

## Funcionament recomanat

1. Aplicar primer les regles que el codi pot resoldre exactament.
2. Minimitzar i separar el context no fiable abans d'avaluar l'acció.
3. Formular cada decisió semàntica en una dimensió clara.
4. Registrar entrada, decisió, probabilitat, versió i resultat real.
5. Executar inicialment en mode observació, sense bloquejar.
6. Fixar llindars amb dades pròpies i segons el cost dels falsos positius i falsos negatius.
7. Escalar els casos ambigus o crítics.

## Injecció de prompts i dades hostils

Un text recuperat d'un web, correu o document pot contenir instruccions que intentin alterar l'agent. La documentació de Jev admet que el model no tracta l'estat com a hostil per defecte. L'avaluació independent citada per l'article mostra, a més, que una falsa afirmació d'autoritat pot ser més efectiva que una ordre explícita d'ignorar instruccions.

Això reforça tres mesures:

- separar la intenció de l'usuari de les dades externes;
- limitar què pot observar i decidir el classificador;
- mantenir regles, permisos i intervenció humana fora del model.

La literatura recent sobre agents segurs coincideix a combinar controls basats en regles i models dins d'una arquitectura que restringeix l'espai d'acció.

## Fallada oberta o tancada

- **Fallada oberta:** si el control falla, es continua o es torna al mecanisme normal de permisos. Redueix interrupcions, però pot deixar passar riscos.
- **Fallada tancada:** si falla o hi ha dubte, s'atura i s'escala. És preferible quan l'acció té efectes externs importants.

La decisió no és universal: depèn de l'impacte, la reversibilitat i el mecanisme alternatiu disponible.

## Exemple financer

En un agent que prepara una valoració:

- el codi comprova que els percentatges i dates siguin vàlids;
- un classificador detecta si una hipòtesi és extraordinària o manca de suport;
- una persona aprova la publicació de l'informe;
- el registre conserva les fonts, els supòsits i les decisions.

## Errors habituals

- anomenar “segur” un sistema perquè la sortida compleix l'esquema;
- utilitzar la probabilitat com si fos una garantia;
- definir llindars sense calibratge local;
- enviar al jutge el raonament del mateix agent que vol ser aprovat;
- confiar només en filtres de text contra injeccions;
- instal·lar el control com a eina opcional que el mateix agent pot decidir no cridar.

## Fonts

- [Eugeniu Ghelbur — What Is Jev? The Manual for Agent Harnesses](https://substack.com/home/post/p-216615368), 2026.
- [TypeSafe AI — Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13), limitacions oficials i contingut adversari.
- [Xiang et al. — Architecting Secure AI Agents](https://arxiv.org/abs/2603.30016), 2026. Defensa sistèmica davant la injecció indirecta de prompts.
