# Log del projecte

## 2026-09-25 — Revisió transversal de conceptes després d'A-MEM

- Auditades les 46 fitxes de conceptes en l'estat de `main` amb linter i comprovació estricta d'enllaços; sense errors ni advertiments estructurals previs.
- Revisades i actualitzades 10 fitxes: `wiki`, `frontmatter`, `PKM`, `ontologies_associatives`, `RAG`, `second_brain`, `QMD`, `prompt`, `prompting` i `prompt_engineering`.
- Corregides les referències a `0. Raw/` i a Obsidian com a base obligatòria; aclarida la diferència entre wikilinks i relacions acceptades a `graph/relations.json`.
- Descrites les opcions de cerca lèxica, vectorial i híbrida en RAG; diferenciats prompt, prompting i enginyeria de prompts sense fusionar fitxes.
- Explicitats els enllaços als camps `related_concepts` de les fitxes revisades i afegides fonts oficials de GitHub, MediaWiki, W3C i Microsoft Learn. No s'han acceptat noves arestes tipades al graf.
- Pendent: set fitxes de conceptes encara tenen buits tots dos camps de relacions; cal revisar-ne les connexions de forma individual. La presència d'un wikilink al cos no significa per si sola una relació semàntica acceptada.

## 2026-09-25 — Integració operativa inspirada en A-MEM

- Afegida la skill `memory-evolution` com a revisió opcional de fitxes antigues després d’una ingesta significativa.
- Afegit `scripts/memory_candidates.py`, rànquing local TF-IDF en mode lectura que retorna candidates i indicis per a la revisió, sense embeddings semàntics ni escriptures automàtiques.
- Connectat el pas a `wiki-ingest`, `wiki-update`, `cross-linker`, `llm-wiki` i l’índex de skills.
- Actualitzats la fitxa A-MEM, el README de models, l’índex, el dashboard, hot i el manifest; dues proves comproven les candidates, la desambiguació i la manca de mutacions.
- Decisió: cap relació ni canvi contextual entra a la wiki només per semblança lèxica; la persona o agent encarregat verifica semàntica i procedència abans d’acceptar-ho.

## 2026-09-25 — Ingesta d’A-MEM i conceptes de memòria

- Font principal: Xu i col·laboradors, *A-Mem: Agentic Memory for LLM Agents* (NeurIPS 2025); consultats el paper i els repositoris dels autors el 2026-09-25.
- Creat `1. Wiki/1.3. models/A-MEM.md` per explicar notes estructurades, generació d’enllaços, evolució i recuperació; separats resultats del paper i aplicació inferida a una wiki.
- Creat `memoria_agentica.md` i `evolucio_de_la_memoria.md` com a conceptes diferenciats; ampliats LLM Wiki, Zettelkasten, notes permanents, embeddings i RAG amb relacions recíproques i fonts.
- Afegides cinc relacions tipades documentades al graf i actualitzats índex, hot i manifest.
- Límit: l’avaluació publicada tracta memòria conversacional, no aquest repositori ni la fiabilitat de les connexions proposades en una wiki pública.

## 2026-09-25 — Guia d'entrada a la wiki i criteri dels README

- Ampliat `1. Wiki/README.md` amb introducció, descripció de les quatre categories, recorreguts de lectura i pautes per incorporar fitxes.
- Ampliats els README de `1.1. autors`, `1.2. conceptes` i `1.3. models`, i creat el README de `1.4. llibres`, amb el mateix patró de navegació i manteniment.
- Afegit a `AGENTS.md` un format comú per a futures creacions i modificacions de README, amb explicacions útils i enllaços verificables.
- Canvi de documentació i governança; no modifica fitxes permanents, fonts ni relacions del graf.

## 2026-09-21 — Jev, arnesos d'agents i portes de control

### Diagnòstic de novetat

L'article *What Is Jev? The Manual for Agent Harnesses* aporta un bloc que no tenia fitxes canòniques a la wiki: la distinció entre model i arnès, els controls previs a l'acció, el calibratge de probabilitats i Jev com a model de decisió tipada. Les fitxes existents sobre `AGENTS.md`, enginyeria del context, alineament i avaluació cobrien antecedents parcials, però no la seva integració operativa.

### Contrast extern

- la definició d'arnès s'ha contrastat amb Macedo, *What makes a harness a harness* (arXiv:2606.10106), que identifica bucle, eines, context i control com a nucli;
- el calibratge s'ha fonamentat amb Guo et al. (ICML 2017) i s'ha separat de l'exactitud i de la mera sortida tipada;
- les afirmacions sobre Jev s'han comparat amb la documentació oficial de TypeSafe AI i l'avaluació independent preregistrada de Will Kelly;
- la seguretat dels controls s'ha contrastat amb Xiang et al. (2026), que defensa una arquitectura sistèmica amb regles, models i límits d'observació i decisió.

### Canvis

- creades les fitxes `agent_harness.md`, `gates_i_guardrails_agents.md`, `calibratge_de_probabilitats.md` i `Jev.md`;
- ampliades les fitxes d'enginyeria del context, avaluació de models i Eugeniu Ghelbur;
- incorporada la distinció entre compliment d'esquema i correcció semàntica;
- actualitzats l'índex, el dashboard de la wiki, la ruta d'aprenentatge, `hot.md`, el graf i el manifest;
- eliminades del dashboard d'aprenentatge referències residuals a `0. Raw/`, incompatibles amb la política pública actual.

### Criteri operatiu

`model de decisió probabilística ≠ mecanisme de seguretat complet`

Per a accions amb efectes externs: regles deterministes i permisos primer, classificador semàntic després, i escalat humà quan l'impacte o la incertesa ho exigeixin.

## 2026-09-18 — Auditoria i ampliació de les relacions de `1. Wiki`

### Diagnòstic

La wiki contenia 76 fitxes, 467 aparicions de wikilinks i cap destinació inexistent. La capa revisada només tenia 9 relacions acceptades sobre 7 nodes. A més, les candidates repetides al frontmatter i al cos inflaven els graus del graf, i sis enllaços curts a `evergreen_notes` eren ambigus perquè existeix una fitxa de concepte i una de model amb el mateix nom.

### Canvis

- ampliades les relacions acceptades a 40 arestes sobre 38 nodes;
- incorporats els blocs de fonaments d'aprenentatge profund, arquitectura LLM i gestió del coneixement;
- revisada la relació entre G-Retriever i GraphRAG perquè G-Retriever consti com a exemple documentat;
- deduplicades les candidates per origen i destinació, conservant `occurrences` i `origins`;
- separats els wikilinks trencats dels ambigus;
- substituïts sis enllaços ambigus per la ruta completa de la fitxa conceptual `evergreen_notes`;
- convertit `relation-vocabulary.yaml` en la font efectiva dels tipus permesos;
- afegida validació d'evidències internes, relacions duplicades i inverses del vocabulari;
- corregit el recompte de components perquè inclogui nodes aïllats;
- afegides cinc proves d'integració sobre la wiki real;
- activat el mode estricte a GitHub Actions.

### Resultat

```text
NODES: 76
ACCEPTED_EDGES: 40
ACCEPTED_NODES: 38
ACCEPTED_COVERAGE_PCT: 50.0
CANDIDATE_EDGES: 347
CANDIDATE_OCCURRENCES: 467
BROKEN_WIKILINKS: 0
AMBIGUOUS_WIKILINKS: 0
CONNECTED_COMPONENTS: 2
```

Les comprovacions `wiki_lint --strict`, `graph_scan --check --strict` i les cinc proves d'integració retornen `PASS`.

## 2026-09-18 — Incorporació de GraphQA i ampliació de GNN

### Operació

S'ha ampliat el bloc de coneixement sobre grafs i models de llenguatge per distingir clarament tres peces: **GraphQA** com a tasca de preguntes sobre grafs, **GNN** com a família de xarxes neuronals que aprèn sobre topologia i **GraphRAG** com a arquitectura de recuperació augmentada sobre informació gràfica.

### Canvis principals

- creada la fitxa `GraphQA.md` amb definició, flux, relació amb KGQA, GraphRAG i GNN, exemple financer, criteris d'avaluació i fonts;
- ampliada `xarxes_neuronals_de_graf.md` amb *message passing*, GCN, embeddings de graf, limitacions i aplicacions;
- actualitzat `grafs_i_models_de_llenguatge.md` com a mapa canònic del conjunt;
- connectats `GraphRAG.md` i `G-Retriever.md` amb GraphQA i GNN;
- actualitzada la guia replicable de wikis amb grafs;
- afegides relacions tipades i evidència a `graph/relations.json`;
- actualitzats índex, hot i manifest.

### Fonts externes principals

- Kipf & Welling — *Semi-Supervised Classification with Graph Convolutional Networks*.
- Gilmer et al. — *Neural Message Passing for Quantum Chemistry*.
- He et al. — *G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering*.
- Gu et al. — *Beyond I.I.D.: Three Levels of Generalization for Question Answering on Knowledge Bases (GrailQA)*.

### Criteri conceptual

`GNN = model d'aprenentatge sobre grafs`

`GraphQA = tasca de pregunta-resposta sobre grafs`

`GraphRAG = recuperació estructurada per donar context a un LLM`

Aquestes peces es poden combinar, però no són sinònims.

## 2026-09-04 — Auditoria estructural i consolidació de `docs_support`

### Objectiu

Auditar el projecte després de la conversió a repositori públic i assegurar que l'arquitectura, la documentació, els scripts i els fitxers de control siguin coherents amb dos principis:

1. `coneixement_ia` és una wiki pública d'aprenentatge d'IA basada en fonts externes verificables;
2. `4. Templates/90.2. docs_support/` és una biblioteca de patrons reutilitzables per crear **noves bases de coneixement assistides per IA sobre qualsevol domini**.

### Problemes detectats

- `plantilla_wiki_neutra_replicable.md` encara proposava `_raw/`, l'emmagatzematge de fonts originals dins del repositori i una arquitectura específica d'Obsidian.
- `research-config.md` continuava configurat específicament per a intel·ligència artificial i utilitzava el nom antic `ia_knowledge`.
- `guia_creacio_wikis_amb_grafs.md` conservava referències operatives a `0. Raw/`, Obsidian i `ia_knowledge`.
- `.manifest.json` encara apuntava a `ruta-zero-to-hero-ia.md`, eliminat en redefinir `docs_support`.
- el document canònic `resum_ar9av_wiki_ia_knowledge.md` era específic del projecte actual i no prou general per al nou contracte de `docs_support`.
- `.github/workflows/wiki-lint.yml` encara escoltava la branca obsoleta `agent/reorganitza-wiki-llm`.
- `desktop.ini` estava versionat accidentalment.
- `scripts/wiki_lint.py` validava el JSON del manifest però no comprovava que les rutes declarades a `pages_created` o `pages_updated` existissin.
- els scripts encara contenien terminologia interna antiga (`ia_knowledge`) i una dependència nominal d'Obsidian en la descripció del resolutor de wikilinks.

### Correccions aplicades

- Reescrita `plantilla_wiki_neutra_replicable.md` com a plantilla canònica independent del domini i de l'eina local.
- Generalitzat `research-config.md` com a patró de recerca per rondes adaptable a qualsevol àmbit.
- Generalitzada `guia_creacio_wikis_amb_grafs.md` i eliminades les dependències de `0. Raw/`, Obsidian i del nom intern antic.
- Creat `patro_wiki_agents_replicable.md` com a síntesi canònica del patró de wiki amb agents.
- Eliminat `resum_ar9av_wiki_ia_knowledge.md`, substituït pel document replicable anterior.
- Eliminat `ruta-zero-to-hero-ia.md` de `docs_support` perquè era una ruta d'aprenentatge temàtica.
- Actualitzats `4. Templates/README.md`, `90.2. docs_support/README.md`, `index.md` i `AGENTS.md` amb el nou contracte de `docs_support`.
- Actualitzat `.manifest.json` a la versió 5 i eliminades rutes obsoletes.
- Enfortit `scripts/wiki_lint.py` perquè comprovi les rutes declarades pel manifest.
- Simplificat el workflow de CI a `main` i Pull Requests cap a `main`.
- Eliminat `desktop.ini` i afegit al `.gitignore`.
- Actualitzats els scripts per utilitzar `coneixement_ia` i terminologia neutral respecte de l'editor.

### Resultat arquitectònic

`4. Templates/` queda dividit conceptualment així:

```text
90.1. templates_fitxes
        ↓
forma de les peces de coneixement

90.2. docs_support
        ↓
forma del sistema de coneixement
```

El flux replicable de `docs_support` és:

```text
domini nou
    ↓
patrons de docs_support
    ↓
arquitectura + governança + recerca + relacions
    ↓
nova base de coneixement
    ↓
IA o agent
```

### Validació

La validació automàtica del projecte continua definida per:

```bash
python scripts/wiki_lint.py
python scripts/graph_scan.py --check
```

El workflow de GitHub Actions executa ambdues comprovacions per als Pull Requests dirigits a `main`.

### Pendents no bloquejants

- continuar normalitzant fitxes antigues que encara generin advertiments de frontmatter o fonts;
- revisar progressivament les relacions candidates del graf;
- mantenir els documents de `docs_support` generalitzables quan s'hi incorporin nous patrons.

## 2026-09-03 — Documentació pública de `2. Skills/`

### Operació

S'ha revisat la carpeta `2. Skills/` per eliminar dependències operatives del model antic basat en `0. Raw/` i fer que cada skill sigui comprensible per a lectors externs que arriben al repositori des de GitHub.

### Canvis principals

- Reescrit `2. Skills/README.md` com a mapa funcional amb una taula **necessitat → skill**, flux recomanat i enllaços Markdown navegables des de GitHub.
- Ampliats els README de totes les carpetes de skills amb finalitat, moment d'ús, funcions, resultat esperat i accés al procediment complet.
- Eliminades referències operatives a `0. Raw/` de `llm-wiki`, `daily-update`, `wiki-query`, `wiki-status`, `wiki-import` i `wiki-export`.
- Substituïda l'arquitectura antiga `Raw → Wiki → Esquema` per `Fonts externes → Wiki → Governança i esquema`.
- Substituït el nom intern `ia_knowledge` per `coneixement_ia` als procediments afectats.
- Aclarit que `vault-skill-factory` conserva un nom històric però no depèn d'Obsidian ni d'un vault.
- Els imports temporals es mantenen fora del repositori públic o en ubicacions locals ignorades per Git; els exports inclouen per defecte coneixement propi de la wiki, no còpies de materials externs.

### Objectiu

Fer que les skills funcionin com una documentació pública autosuficient: una persona externa ha de poder entendre què resol cada procediment abans d'obrir-ne la implementació detallada.

## 2026-09-03 — Conversió a projecte públic basat en fonts externes i Markdown neutre

### Operació

S'ha eliminat la dependència d'una carpeta pública de materials bruts i també la configuració específica de l'entorn local. El projecte adopta un model de traçabilitat basat en **fonts externes verificables** i un model d'edició basat en **Markdown estàndard**, independent de l'eina utilitzada per cada col·laborador.

### Canvis principals

- Eliminats del repositori públic els materials originals i dossiers de treball que no formen part de la wiki permanent.
- Eliminada la carpeta de configuració local `.obsidian/` i els fitxers associats de preferències, plugins, tema, graf i workspace.
- Actualitzats `README.md`, `AGENTS.md` i `.gitignore` perquè cap editor o gestor de coneixement concret sigui requisit del projecte.
- Adaptat `3. Dashboards/dashboard_fonts.md`.
- Adaptades les skills `wiki-ingest` i `wiki-research`.
- Adaptats els documents de suport i `scripts/wiki_lint.py` al model de fonts externes.
- Substituïdes les referències operatives a eines locals per formulacions neutres.

### Noves regles

- Les fonts originals no s'han d'emmagatzemar al repositori públic.
- Les configuracions personals d'editors, IDE o gestors de coneixement no s'han de versionar.
- Markdown és el format canònic compartit.
- Cada fitxa ha de conservar la procedència a través del camp `sources`, URLs, referències bibliogràfiques i, quan calgui, metadades al manifest.

### Objectiu

Preparar el repositori per a contribucions públiques sense exposar materials de treball privats ni configuracions personals, i evitar que el projecte depengui d'una aplicació concreta.

## Historial anterior

El detall exhaustiu de les operacions anteriors s'ha condensat en aquestes fites estructurals. La història completa continua representada pels commits i Pull Requests del repositori.
