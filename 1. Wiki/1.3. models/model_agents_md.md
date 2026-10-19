---
title: Model AGENTS.md
category: models
node_id: "model:model_agents_md"
node_type: "model"
model_family: agent_context
architecture: agents_md_generator
authors:
  - "[[Ghelbur, Eugeniu]]"
tags:
  - model
  - agents
sources:
  - https://github.com/eugeniughelbur/agents-md
  - https://arxiv.org/abs/2602.11988v3
related_concepts:
  - "[[1. Wiki/1.2. conceptes/AGENTS_MD]]"
status: active
created: 2026-05-30
updated: 2026-10-19
---
# MODEL AGENTS.MD

Eina per generar i mantenir fitxers [[1. Wiki/1.2. conceptes/AGENTS_MD|`AGENTS.md`]]  dins d’un repositori. 

La proposta del repositori és evitar dos problemes típics: començar un `AGENTS.md` des de zero i, sobretot, que l’agent inventi informació. L’eina escaneja el repositori, detecta allò que pot saber —estructura, scripts, ordres, fitxers de configuració— i genera o refresca un `AGENTS.md`. Quan no pot inferir una cosa amb seguretat, deixa un espai pendent perquè l’usuari l’ompli. 

Aquesta part és importantíssima: el bon `AGENTS.md` no és el més llarg, sinó el més fiable. Segons el **README**, la utilitat funciona com a **CLI** amb `npx @eugeniughelbur/agents-md` o directament des de **GitHub**, i també com a habilitat per a **Claude Code**.

## Contracte de marcadors

La idea tècnica més interessant és el **contracte de marcadors**. 

El fitxer separa les parts generades automàticament de les parts escrites a mà mitjançant comentaris HTML del tipus 

`<!-- agents-md:begin id=commands -->` i `<!-- agents-md:end id=commands -->`. 

En futures execucions, l’eina només actualitza les zones marcades i conserva tota la resta. Si troba un `AGENTS.md` escrit a mà sense marcadors, no l’esborra: crea un `AGENTS.generated.md`. Això converteix el fitxer en document viu però segur: es pot regenerar sense perdre les instruccions pròpies.

També és rellevant la seva filosofia de **font única**. 

El repositori recomana utilitzar `AGENTS.md` com a document principal i, si cal compatibilitat amb **Claude Code**, crear un enllaç simbòlic `CLAUDE.md` cap al mateix fitxer. Així s’evita tenir instruccions duplicades i divergents per a cada eina. A més, el **CLI** no necessita clau d’**API**, no fa crides de xarxa i llegeix només metadades del repositori; pot mirar `.env.example`, però no valors secrets reals.

Per a una vault manual d’**Obsidian** o un projecte personal, la lliçó pràctica és molt bona: el `AGENTS.md` hauria de ser curt, verificable i orientat a acció. 

No hauria de contenir tota la teoria del projecte, sinó les regles que ajuden l’agent a no espatllar res: estructura de carpetes, criteris per crear o modificar notes, format del [[frontmatter]], convencions d’enllaços interns, ordres útils, límits i coses prohibides. Cal verificar quina informació aporta valor abans d’ampliar-lo: generar un document fidel al repositori i demostrar que millora l’agent són comprovacions diferents.

## Contrast amb l'evidència sobre fitxers de context

L'estudi de Gloaguen et al. (v3, setembre de 2026) no avalua aquest generador concret. Aporta un motiu per provar el document resultant en lloc d'assumir que automatitzar-ne la creació millora l'èxit. Vegeu [[1. Wiki/1.2. conceptes/AGENTS_MD|AGENTS.md]] per als resultats i límits de l'estudi.

Una comparació local pot mantenir model, eines i tasques fixos i variar només les instruccions opcionals. Cal mesurar èxit, errors i cost; mai retirar permisos o límits obligatoris per fer la prova. És una proposta d'avaluació, no un resultat obtingut en aquest projecte.

## Fonts

- [Generador agents-md — repositori de l’autor](https://github.com/eugeniughelbur/agents-md). Font de la descripció funcional existent.
- Gloaguen et al., [Evaluating AGENTS.md](https://arxiv.org/abs/2602.11988v3), v3 del 2026-09-29; consultada el 2026-10-19. Contrast empíric general.
