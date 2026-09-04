# Hot

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
python scripts/graph_scan.py --check
```

GitHub Actions executa aquestes comprovacions als Pull Requests dirigits a `main`.

## Prioritats actuals

- revisar progressivament fitxes antigues amb frontmatter incomplet o fonts insuficients;
- revisar relacions candidates abans de convertir-les en acceptades;
- mantenir `docs_support` generalitzable quan s'hi incorporin nous patrons;
- mantenir el manifest i els scripts de validació sincronitzats amb l'arquitectura real.
