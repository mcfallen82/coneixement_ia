# Log del projecte

## 2026-09-03 — Conversió a model públic basat en fonts externes

### Operació

S'ha eliminat la dependència d'una carpeta pública de materials bruts i s'ha adoptat un model de traçabilitat basat en **fonts externes verificables**, URLs i referències bibliogràfiques.

### Canvis principals

- Eliminats del repositori públic els materials originals i dossiers de treball que no formen part de la wiki permanent.
- Actualitzats `README.md`, `AGENTS.md` i `index.md`.
- Adaptat `3. Dashboards/dashboard_fonts.md`.
- Adaptades les skills `wiki-ingest` i `wiki-research`.
- Adaptats `research-config.md` i `ruta-zero-to-hero-ia.md`.
- Actualitzat `scripts/wiki_lint.py` perquè la carpeta de materials bruts deixi de ser obligatòria.
- Substituïdes les referències al tutorial local Zero to Hero per fonts externes oficials d'Andrej Karpathy.
- Mantinguda la font externa de l'article *Graph Engineering Decoded: Two Definitions, One Test*: https://theaioperator.io/p/graph-engineering-decoded-two-definitions

### Nova regla

Les fonts originals no s'han d'emmagatzemar al repositori públic. Cada fitxa ha de conservar la procedència a través del camp `sources`, URLs, referències bibliogràfiques i, quan calgui, metadades al manifest.

### Objectiu

Preparar el repositori per a contribucions públiques sense exposar materials de treball privats ni convertir GitHub en un arxiu de còpies de fonts.

## Historial anterior

El detall exhaustiu de les operacions anteriors s'ha condensat en aquesta conversió estructural. La història del projecte continua representada pels commits i pull requests del repositori.
