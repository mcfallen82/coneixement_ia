# wiki-lint

## Finalitat

Auditar la salut estructural i semàntica de la wiki abans de donar per acabada una ingesta o reorganització.

## Comprovacions

### Estructura

- existeixen 0. Raw/, 1. Wiki/, 2. Skills/, 3. Dashboards/ i 4. Templates/;
- els README descriuen el contingut real;
- les rutes de l’índex i de les skills són actuals.

### Fitxes i YAML

- cada fitxa permanent té frontmatter vàlid;
- conté title, category, tags, sources, status, created i updated;
- category coincideix amb la carpeta;
- no hi ha camps antics com estat si es poden normalitzar;
- els models incorporen model_family i architecture quan són aplicables.

### Xarxa de coneixement

- wikilinks cap a fitxers reals;
- cap enllaç a rutes antigues;
- autors, conceptes i models relacionats;
- detecció de fitxes orfes i possibles duplicats.

### Traçabilitat

- fitxes madures amb fonts verificables;
- log.md, hot.md i .manifest.json actualitzats;
- les fonts indiquen fitxes creades o modificades;
- no es confonen dades documentades amb interpretacions.

## Auditoria manual

~~~bash
rg -n "estat:|autor:|concepts/|entities/|references/" .
rg -n "^title:|^category:|^tags:|^sources:|^status:|^created:|^updated:" "1. Wiki"
rg -n "\[\[.*\]\]" "1. Wiki" "2. Skills" "4. Templates"
~~~

Per validar YAML, utilitza un analitzador disponible o revisa manualment les capçaleres. Les cerques són senyals, no una prova suficient.

## Informe

~~~text
# Informe wiki-lint — YYYY-MM-DD
## Errors bloquejants
## Advertiments
## Fitxes orfes
## Duplicats o sinònims
## Enllaços proposats
## Accions recomanades
~~~

Corregeix automàticament només errors mecànics i reversibles. Les fusions, eliminacions i canvis de significat requereixen revisió humana.