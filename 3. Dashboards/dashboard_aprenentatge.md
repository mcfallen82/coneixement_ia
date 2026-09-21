# Dashboard d'aprenentatge

Aquest dashboard es mante com a Markdown estatic. No requereix Dataview ni cap plugin d'Obsidian.

## Entrada rapida

- [Dashboard de la wiki](dashboard_wiki.md): entrada al contingut de `1. Wiki`.
- [Fonts de la wiki](dashboard_fonts.md): criteris de procedència i fonts externes verificables.
- [Hot](../hot.md): prioritats actuals.
- [Index](../index.md): mapa general de la wiki.
- [Registre](../log.md): canvis estructurals i ingestes.
- [Auditoria](dashboard_auditoria.md): comprovacions de salut del projecte.

## Revisio de fitxes

Per revisar l'estat de la wiki:

```bash
python scripts/wiki_lint.py
python scripts/graph_scan.py --check
```

## Ruta principal

Per orientar una sessio d'aprenentatge, comenca per [dashboard_wiki](dashboard_wiki.md) i tria una de les rutes:

- fonaments de deep learning;
- models de llenguatge;
- recuperacio i grafs;
- wiki, PKM i context;
- agents, arnesos i control;
- llibres i fonts processades.

## Conceptes pendents

Busca a `1. Wiki/1.2. conceptes/`:

- fitxes amb `status: draft`
- fitxes sense fonts verificables
- fitxes amb wikilinks trencats
- fitxes amb camps antics

## Models pendents

Busca a `1. Wiki/1.3. models/`:

- fitxes sense `model_family`
- fitxes sense `architecture`
- fitxes que representen recursos o metodologies i potser no models
- fitxes derivades de fonts externes que necessiten revisio de drets

## Llibres i fonts pendents

Busca a `1. Wiki/1.4. llibres/` i al manifest:

- llibres amb autoria incompleta;
- fonts externes processades sense fitxa permanent;
- fitxes de llibre sense seccio d'aplicacio a IA o sistemes de coneixement;
- fonts pendents o amb traçabilitat incompleta al manifest.

## Fonts prioritaries

La cua de treball viva s'ha de mantenir a `hot.md`. Les fonts originals es mantenen fora del repositori públic i el seu rastre canònic es conserva mitjançant URLs, bibliografia i `.manifest.json`.
