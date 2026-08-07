---
node_id: "model:model_agents_md"
node_type: "model"
authors:
  - "[[Ghelbur, Eugeniu]]"
font: https://github.com/eugeniughelbur/agents-md
data: 2026-05-30
tags:
  - model
  - agents
descripcio: Eina per generar i mantenir fitxers "AGENTS.md" dins d'un repositori
estat: pendent millora
---
# MODEL AGENTS.MD

Eina per generar i mantenir fitxers [[conceptes/Agents_MD|`AGENTS.md`]]  dins d’un repositori. 

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

No hauria de contenir tota la teoria del projecte, sinó les regles que ajuden l’agent a no espatllar res: estructura de carpetes, criteris per crear o modificar notes, format del [[frontmatter]], convencions d’enllaços interns, ordres útils, límits i coses prohibides. El perill és inflar-lo massa: estudis recents sobre fitxers de context per agents indiquen que instruccions innecessàries poden reduir l’eficàcia i augmentar el cost, i que són habituals problemes com excés de context, instruccions conflictives o filtració de normes massa específiques
