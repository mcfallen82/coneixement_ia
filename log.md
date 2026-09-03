# Log del projecte

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
- Adaptats `research-config.md` i `ruta-zero-to-hero-ia.md`.
- Actualitzat `scripts/wiki_lint.py` perquè la carpeta de materials bruts deixi de ser obligatòria.
- Substituïdes les referències operatives a eines locals per formulacions neutres: editor Markdown, IDE, gestor de coneixement o eina compatible.
- Substituïdes les referències al tutorial local Zero to Hero per fonts externes oficials d'Andrej Karpathy.

### Noves regles

- Les fonts originals no s'han d'emmagatzemar al repositori públic.
- Les configuracions personals d'editors, IDE o gestors de coneixement no s'han de versionar.
- Markdown és el format canònic compartit.
- Cada fitxa ha de conservar la procedència a través del camp `sources`, URLs, referències bibliogràfiques i, quan calgui, metadades al manifest.

### Objectiu

Preparar el repositori per a contribucions públiques sense exposar materials de treball privats ni configuracions personals, i evitar que el projecte depengui d'una aplicació concreta.

## Historial anterior

El detall exhaustiu de les operacions anteriors s'ha condensat en aquesta conversió estructural. La història del projecte continua representada pels commits i pull requests del repositori.