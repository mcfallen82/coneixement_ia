# wiki-lint

## Finalitat

Auditar la salut estructural, sintàctica i semàntica de la wiki abans de donar per acabada una ingesta, reorganització o actualització.

## Entrades

- arrel del repositori;
- fitxes de `1. Wiki/`;
- `index.md`, `log.md`, `hot.md` i `.manifest.json`;
- skills, dashboards i plantilles.

## Execució

Des de l’arrel del repositori:

```bash
python scripts/wiki_lint.py
```

La comprovació és només de lectura. Retorna codi 0 amb `PASS` quan no hi ha errors estructurals, encara que pugui informar deute de normalització com a advertiment.

Per exigir la normalització completa:

```bash
python scripts/wiki_lint.py --strict
```

En mode estricte, les fitxes antigues sense frontmatter complet, els wikilinks pendents i els camps obsolets passen a ser errors bloquejants. En entorns sense PyYAML:

```bash
python -m pip install pyyaml
```

## Errors bloquejants

1. Falta una carpeta o fitxer de control obligatori.
2. El frontmatter existent és YAML invàlid o no és un mapa.
3. Hi ha una categoria explícita que no coincideix amb la carpeta.
4. Hi ha títols duplicats dins de la mateixa categoria.
5. `.manifest.json` és invàlid o apunta a rutes inexistents.

## Advertències de normalització

- fitxes sense frontmatter;
- camps obligatoris absents;
- models sense `model_family` o `architecture`;
- fitxes sense fonts o en estat `draft`;
- wikilinks que encara utilitzen noms antics;
- camps o rutes obsolets.

Aquestes advertències són el deute tècnic pendent de la migració. No s’han d’ignorar: s’han d’incorporar progressivament a `hot.md` o al registre.

## Informe

L’script produeix una sortida llegible:

```text
WIKI LINT — YYYY-MM-DD
Fitxes amb frontmatter revisades: n
Errors bloquejants: n
Advertiments de normalització: n
PASS | FAIL
```

## Protocol de correcció

Corregeix automàticament només errors mecànics i reversibles. Les fusions, eliminacions i correccions de significat requereixen revisió humana. Després de qualsevol correcció:

1. executa el mode normal;
2. revisa les advertències;
3. executa `--strict` quan la migració estigui preparada;
4. actualitza `log.md` i `.manifest.json`.
