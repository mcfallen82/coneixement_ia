# Dashboard d'auditoria

Aquest dashboard no depen de Dataview ni de plugins d'Obsidian. Serveix com a guia de revisio manual i com a recordatori de les comprovacions executables.

## Entrada rapida

- [Dashboard de la wiki](dashboard_wiki.md): revisio de cobertura de `1. Wiki`.
- [Fonts de la wiki](dashboard_fonts.md): estat de fonts brutes i llibres.
- [Graf](graf.md): control de nodes, wikilinks i relacions.
- [Registre](../log.md): historial d'operacions.
- [Manifest](../.manifest.json): traçabilitat operativa.

## Comprovacio principal

Executa des de l'arrel del repositori:

```bash
python scripts/wiki_lint.py
python scripts/graph_scan.py --check
```

Si l'entorn no te `python` al PATH, usa el Python disponible de l'entorn de treball o afegeix-lo abans d'executar les comprovacions.

## Fitxes sense fonts

Revisa les fitxes de `1. Wiki/` que tinguin `sources: []`, `sources: null` o cap camp `sources`.

Prioritat:

- fitxes en `1. Wiki/1.3. models/`
- fitxes en `1. Wiki/1.4. llibres/`
- fitxes en `1. Wiki/1.1. autors/` creades a partir de fonts externes
- fitxes usades com a hubs conceptuals
- fitxes que provenen de materials de `0. Raw/`

## Fitxes en esborrany

Revisa les fitxes amb `status: draft`. Una fitxa pot continuar en esborrany, pero ha de tenir una definicio clara, fonts o una nota explicita de pendent.

## Camps antics

No s'han d'introduir camps antics com:

- `estat`
- `autor`
- `concepts/`
- `entities/`
- `references/`

Si apareixen a la validacio, cal migrar-los als camps actuals.

## Fonts pendents

Les fonts de `0. Raw/` no sempre tenen frontmatter. El seu estat canonic s'ha de contrastar amb `.manifest.json`, `log.md` i les fitxes resultants.

Una font nomes es pot considerar `processed` si les fitxes creades o actualitzades estan indicades al manifest.

## Fitxers de seguiment

Cada operacio significativa ha d'actualitzar, quan pertoqui:

- `index.md`: entrada navegable si el canvi crea una nova area o font important;
- `hot.md`: prioritat o activitat recent si el canvi modifica la cua viva;
- `log.md`: registre narratiu del canvi;
- `.manifest.json`: traçabilitat mecanica de fonts, fitxes i comprovacions.

## Revisio de dashboards

Quan s'afegeixin fitxes a `1. Wiki/`, comprova si cal actualitzar:

- `dashboard_wiki.md`, si canvia el conjunt d'autors, conceptes, models o llibres;
- `dashboard_aprenentatge.md`, si canvia una ruta de lectura;
- `dashboard_fonts.md`, si canvia l'estat d'una font;
- `graf.md`, si canvia la interpretacio de nodes o relacions.
