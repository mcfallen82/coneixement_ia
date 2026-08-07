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

La comprovació és només de lectura i retorna codi 0 amb `PASS` o codi 1 amb `FAIL`. En entorns sense PyYAML:

```bash
python -m pip install pyyaml
```

## Comprovacions bloquejants

1. Existeixen les carpetes i fitxers de control obligatoris.
2. Cada fitxa permanent té frontmatter YAML vàlid.
3. Cada fitxa té `title`, `category`, `tags`, `sources`, `status`, `created` i `updated`.
4. `category` coincideix amb la carpeta i els models tenen `model_family` i `architecture`.
5. Els wikilinks apunten a fitxers reals.
6. `.manifest.json` és JSON vàlid i les rutes registrades existeixen.
7. No hi ha camps o rutes obsolets: `estat:`, `autor:`, `concepts/`, `entities/` o `references/`.
8. No hi ha títols duplicats dins de la mateixa categoria.

## Advertències

- fitxes amb `status: draft`;
- fitxes sense fonts;
- fonts no processades;
- fitxes sense relacions;
- README o dashboards sense resultats verificables.

Les advertències no bloquegen, però s’han d’incloure a l’informe.

## Informe

L’script produeix una sortida llegible:

```text
WIKI LINT — YYYY-MM-DD
Errors: n
Advertiments: n
PASS | FAIL
```

## Protocol de correcció

Corregeix només errors mecànics i reversibles automàticament. Les fusions, eliminacions i correccions de significat requereixen revisió humana. Després de qualsevol correcció, torna a executar l’script i revisa manualment les advertències.
