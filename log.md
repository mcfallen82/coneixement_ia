# Log del projecte

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
