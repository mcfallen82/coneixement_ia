# Recerca sobre el concepte de *scaffold* en intel·ligència artificial

**Data de consulta:** 2026-08-07  
**Pregunta:** Què significa *scaffold* quan es parla de models de llenguatge, agents i aprenentatge amb IA?

## Abast i criteri

La recerca separa dos usos del terme:

1. **Scaffolding pedagògic:** suport temporal que ajuda una persona a completar una tasca que encara no pot fer de manera autònoma.
2. **Agent scaffold o agent harness:** sistema de programari que envolta un model i li permet actuar com a agent mitjançant instruccions, eines, estat, bucles de control, delegació i comprovacions.

La segona accepció és la prioritària per a aquesta wiki, perquè explica per què un mateix LLM pot comportar-se de manera molt diferent segons l’arquitectura que l’envolta.

## Ronda 1 — mapa general

### 1. Scaffold com a arquitectura d’agent

Anthropic descriu un *agent harness* o *scaffold* com el sistema que permet que un model actuï com a agent: rep entrades, coordina crides a eines i retorna resultats. La conseqüència metodològica és important: quan s’avalua un agent, s’avaluen conjuntament el model i l’*harness*.

La guia d’Anthropic sobre agents separa el model augmentat —un LLM amb informació i capacitats addicionals— dels fluxos de treball i dels agents autònoms. Això situa el *scaffold* entre el model i l’aplicació final.

### 2. Components del scaffold

La documentació de l’OpenAI Agents SDK mostra una composició pràctica:

- instruccions o prompt del sistema;
- eines per consultar dades o executar accions;
- context mutable i estat de la sessió;
- delegació entre agents (*handoffs*);
- sortides estructurades;
- guardrails d’entrada, sortida i eines;
- execució, traça i gestió del cicle de vida.

La documentació d’Anthropic sobre Claude Code afegeix altres peces habituals: fitxers de context persistents, skills, subagents, MCP i eines d’intel·ligència de codi.

### 3. Scaffold com a suport pedagògic

En educació, el *scaffolding* és una ajuda ajustada al nivell de l’aprenent i retirada progressivament quan aquest guanya autonomia. Les aplicacions d’IA poden oferir pistes, exemples, comentaris i preguntes de seguiment adaptades al domini o al nivell de domini de l’estudiant.

Aquest ús no descriu l’arquitectura de programari d’un agent, però comparteix una intuïció: l’element central no treballa aïllat, sinó dins d’una estructura de suport que redueix la dificultat de la tasca.

## Ronda 2 — contrast i límits

### No és sinònim de model

El model genera i interpreta informació. El *scaffold* defineix com es presenta el problema, quines eines pot utilitzar, com conserva l’estat, com comprova els resultats i quan pot actuar. Per tant, una millora de l’agent pot provenir del model, del *scaffold* o de la interacció entre tots dos.

### No és sinònim de framework

Un framework és una llibreria o entorn de desenvolupament. Un *scaffold* és la configuració i l’arquitectura operativa concreta que fa servir el model. Un framework pot ajudar a construir molts scaffolds diferents.

### Més components no implica millor agent

Els estudis recents sobre *agent scaffolding* assenyalen que afegir planificació, memòria, recuperació o autoreflexió pot generar interferències entre components. La complexitat només és útil quan resol una limitació identificada i es pot avaluar.

### El scaffold pot introduir riscos

Les eines, els permisos, la memòria i els bucles d’execució amplien la capacitat d’acció però també la superfície d’error. Cal controlar les dades recuperades, les autoritzacions, les accions amb efectes externs i les validacions de les sortides.

## Ronda 3 — aplicació a ia_knowledge

El repositori ja conté diversos elements d’un scaffold de coneixement:

- `AGENTS.md` fixa objectius, contractes i regles;
- les skills descriuen procediments reutilitzables;
- `wiki-ingest` i `wiki-update` organitzen el flux;
- `wiki_lint.py` i `graph_scan.py` validen l’estructura;
- el frontmatter i el manifest mantenen l’estat i la traçabilitat;
- la capa gràfica separa wikilinks candidats de relacions acceptades.

Aquests elements no són el model de llenguatge. Formen l’estructura de suport que orienta l’agent i fa que el resultat sigui més repetible i auditable.

## Síntesi

En el context d’agents, *scaffold* és l’arquitectura de suport que converteix un LLM en un sistema capaç de completar una tasca dins d’un procés controlat. Inclou tant la interfície amb el model com les eines, l’estat, el context, la planificació, la delegació i les comprovacions.

En el context educatiu, és el suport gradual que permet a l’aprenent avançar cap a l’autonomia.

La frontera entre els dos usos és clara: el primer descriu un sistema d’execució; el segon, un sistema d’ajuda a l’aprenentatge. La metàfora comuna és útil, però no s’han de confondre.

## Fonts consultades

1. Anthropic, **Demystifying evals for AI agents** — definició explícita d’*agent harness/scaffold* i implicacions per a l’avaluació.  
   https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
2. Anthropic, **Building Effective AI Agents** — distinció entre LLM augmentat, fluxos de treball i agents.  
   https://www.anthropic.com/engineering/building-effective-agents
3. OpenAI, **Agents SDK — Agents** — instruccions, eines, context, handoffs, guardrails i sortides estructurades.  
   https://openai.github.io/openai-agents-python/agents/
4. OpenAI, **Agents SDK — Tools** — categories d’eines i capacitats d’execució.  
   https://openai.github.io/openai-agents-python/tools/
5. Anthropic, **Extend Claude Code** — context persistent, skills, subagents, MCP i extensions del cicle de l’agent.  
   https://docs.anthropic.com/en/docs/claude-code/features-overview
6. Rombaut, **Inside the Scaffold: A Source-Code Taxonomy of Coding Agent Architectures** — taxonomia de scaffolds d’agents de programació.  
   https://arxiv.org/abs/2604.03515
7. Liu et al., **More Is Not Always Better: Cross-Component Interference in LLM Agent Scaffolding** — riscos d’afegir components sense avaluació.  
   https://arxiv.org/abs/2605.05716
8. Oxford University Press, **Can AI-Based Scaffolding Promote Students’ Robust Learning?** — ús pedagògic i adaptatiu del scaffolding.  
   https://academic.oup.com/book/58946/chapter/493003498

## Confiança i qüestions obertes

- **Alta:** el terme s’utilitza actualment per descriure el sistema d’execució que envolta un LLM en agents; coincideixen fonts oficials d’Anthropic i OpenAI.
- **Mitjana-alta:** la taxonomia dels components és útil, però no hi ha un estàndard universal sobre què ha d’incloure tot scaffold.
- **Oberta:** caldrà comparar, en proves pròpies, quin guany aporta cada component —RAG, planificació, memòria, validació o delegació— davant d’un flux més simple.
