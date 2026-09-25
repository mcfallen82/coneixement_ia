# Hot

## Revisió dels conceptes — 2026-09-25

- 46 fitxes auditades; 10 fitxes revisades per coherència editorial i conceptual després de la integració d'A-MEM.
- `wiki`, `frontmatter` i `PKM` segueixen el model públic de Markdown i fonts externes; `RAG` ja no exigeix embeddings en tots els casos.
- `ontologies_associatives` diferencia enllaços candidats, relacions tipades acceptades i ontologies formals; les fitxes de prompts tenen àmbits explícits.
- Queden set fitxes amb els camps `related_concepts` i `related_models` buits; revisar-les abans d'afegir-hi relacions acceptades.

## Integració operativa de la revisió de memòria — 2026-09-25

- Nova skill `memory-evolution`: revisió posterior a ingestes significatives, amb lectura de fitxes anteriors i justificació de canvis.
- `memory_candidates.py` ordena candidates amb TF-IDF lèxic local, sense escriure fitxes ni acceptar relacions.
- La connexió i les revisions continuen subjectes a la font original, a la revisió semàntica i a les validacions del projecte.
- L’adaptació no instal·la ni reprodueix el model A-MEM publicat.

## A-MEM i memòria agentiva — 2026-09-25

- A-MEM té una fitxa de model i s’enllaça amb els conceptes nous de memòria agentiva i evolució de la memòria.
- La generació d’enllaços i l’actualització contextual són operacions automàtiques descrites en el paper; els resultats experimentals provenen de preguntes sobre converses llargues.
- Comparació amb LLM Wiki: les propostes de l’agent poden ajudar a revisar notes, però incorporar-les a una wiki pública exigeix fonts i revisió.
- Pendent de recerca: avaluar qualitat de relacions, procedència i cost total d’ingesta en una wiki documental abans d’adoptar el mecanisme.

## Jev i control d'agents — 2026-09-21

- Noves fitxes canòniques: arnès d'agent, portes de control, calibratge de probabilitats i Jev.
- Un arnès queda delimitat per quatre peces: bucle adaptatiu, eines, gestió del context i control en temps d'execució.
- Jev aporta decisions tipades, paral·leles i ràpides; la seva arquitectura i RLCD no estan prou publicats per reproduir-los.
- La sortida tipada evita errors d'esquema, però no garanteix una decisió correcta ni elimina les al·lucinacions semàntiques.
- El calibratge s'ha de validar per domini i versió; no s'han de copiar llindars d'una altra aplicació.
- Per a accions crítiques, les regles deterministes, els permisos i l'escalat humà continuen sent la base del control.
- Les injeccions amb falsa autoritat poden ser més efectives que les ordres explícites; cal separar intenció, dades externes i proposta d'acció.

## Auditoria de relacions de la wiki — 2026-09-18

- Les relacions acceptades passen de 9 a 40 i cobreixen 38 de les 76 fitxes permanents.
- La cobertura semàntica incorpora els blocs de grafs, fonaments d'aprenentatge profund, LLM i gestió personal del coneixement.
- Les 467 aparicions de wikilinks es consoliden en 347 candidates úniques sense perdre'n la procedència.
- Els wikilinks ambigus a `evergreen_notes` s'han substituït per rutes completes.
- L'escàner carrega el vocabulari des de YAML, valida evidències i compta els nodes aïllats.
- La integració contínua executa el mode estricte i cinc proves sobre el graf real.

## GraphQA i GNN — 2026-09-18

- GraphQA ja té fitxa canònica pròpia i queda definit com una tasca de pregunta-resposta sobre nodes, arestes, camins i subgrafs.
- La fitxa de GNN incorpora *message passing*, GCN, relació amb embeddings, GraphQA i LLM.
- G-Retriever queda documentat com a exemple de combinació entre recuperació de subgrafs, GNN i LLM per a GraphQA.
- La capa gràfica registra relacions acceptades entre GraphQA, GNN i G-Retriever amb fonts externes.
- Distinció operativa: **GNN aprèn sobre el graf; GraphQA pregunta al graf; GraphRAG recupera context del graf**.

## Auditoria estructural — 2026-09-04

- `4. Templates/90.2. docs_support/` queda definit com la **biblioteca de patrons per crear noves bases de coneixement assistides per IA sobre qualsevol domini**.
- `plantilla_wiki_neutra_replicable.md`, `research-config.md` i `guia_creacio_wikis_amb_grafs.md` s'han generalitzat i ja no depenen de `0. Raw/`, Obsidian ni del nom intern antic `ia_knowledge`.
- `patro_wiki_agents_replicable.md` és la nova síntesi canònica del patró de wiki mantinguda amb agents.
- `ruta-zero-to-hero-ia.md` s'ha eliminat de `docs_support` perquè era contingut temàtic d'aprenentatge.
- `.manifest.json` s'ha actualitzat a la versió 5 i `wiki_lint.py` valida ara que les rutes declarades al manifest existeixin.
- El workflow de GitHub Actions s'ha simplificat a `main` i Pull Requests cap a `main`.
- `desktop.ini` s'ha eliminat i queda exclòs al `.gitignore`.

## Arquitectura de Templates

```text
90.1. templates_fitxes
        → forma de les peces de coneixement

90.2. docs_support
        → forma del sistema de coneixement
```

## Documentació canònica de `docs_support`

- `4. Templates/90.2. docs_support/plantilla_wiki_neutra_replicable.md` — arquitectura mínima per crear una nova base de coneixement.
- `4. Templates/90.2. docs_support/patro_wiki_agents_replicable.md` — patró conceptual de wiki mantinguda amb IA o agents.
- `4. Templates/90.2. docs_support/research-config.md` — patró general de recerca i procedència.
- `4. Templates/90.2. docs_support/guia_creacio_wikis_amb_grafs.md` — evolució cap a grafs i recuperació estructurada.

## Model públic

- Les fonts originals es mantenen fora del repositori públic; la traçabilitat es conserva amb URLs, bibliografia i `sources`.
- Markdown és el format canònic compartit.
- Cap editor, IDE, gestor de coneixement o plugin concret és obligatori.
- Les còpies locals de treball i configuracions personals s'han de mantenir fora de Git o en rutes ignorades.

## Validació activa

Després de canvis estructurals o ingestes significatives:

```bash
python scripts/wiki_lint.py
python scripts/graph_scan.py --check --strict
python -m unittest discover -s tests -v
```

GitHub Actions executa aquestes comprovacions als Pull Requests dirigits a `main`.

## Prioritats actuals

- revisar progressivament fitxes antigues amb frontmatter incomplet o fonts insuficients;
- revisar relacions candidates abans de convertir-les en acceptades;
- mantenir `docs_support` generalitzable quan s'hi incorporin nous patrons;
- mantenir el manifest i els scripts de validació sincronitzats amb l'arquitectura real.
