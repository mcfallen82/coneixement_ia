# wiki-ingest

## Finalitat

Convertir una font d'aprenentatge en coneixement permanent, traçable i connectat dins de `coneixement_ia`.

## Abans de començar

1. Llegeix `AGENTS.md`, `index.md`, `hot.md` i aquesta skill.
2. Identifica la font: article, llibre, tutorial, paper, vídeo, documentació, repositori, conversa o dades estructurades.
3. Registra la font externa: títol, autor o organisme, URL o referència bibliogràfica, data, tipus i estat de processament.
4. No copiïs al repositori públic el material original ni notes privades de treball.

## Modes

- **Referència externa:** registrar una font sense transformar-la encara en fitxa.
- **Ingesta normal:** extreure i crear o actualitzar fitxes.
- **Reingesta:** processar només els canvis d'una font ja registrada.
- **Ingesta de projecte:** resumir decisions, arquitectura i aprenentatges d'un repositori, no copiar-ne el codi.

## Flux operatiu

1. Llegeix la font completa o delimita clarament les parts analitzades.
2. Extreu conceptes, models, autors, eines, afirmacions, exemples, limitacions i preguntes obertes.
3. Busca fitxes existents, sinònims i grafies alternatives a `1. Wiki/`.
4. Classifica cada element:
   - autor → `1. Wiki/1.1. autors/`;
   - concepte → `1. Wiki/1.2. conceptes/`;
   - model → `1. Wiki/1.3. models/`;
   - llibre o font bibliogràfica estable → `1. Wiki/1.4. llibres/` quan sigui pertinent;
   - font externa sense fitxa pròpia → URL o referència al camp `sources` i al manifest.
5. Decideix si cal crear una fitxa, actualitzar-ne una, afegir un enllaç o conservar només la referència externa.
6. Redacta amb intuïció abans del detall tècnic.
7. Afegeix `sources` al frontmatter i una secció final de fonts quan sigui útil.
8. Connecta la fitxa amb wikilinks reals.
9. Actualitza `index.md`, `log.md`, `hot.md` i `.manifest.json` quan el canvi sigui significatiu.
10. Executa `wiki-lint` i revisa manualment les pàgines creades.

## Regla de no-duplicació

La wiki compila coneixement. No creïs un resum nou si una fitxa existent pot incorporar la informació.

## Manifest mínim

~~~json
{
  "source": {
    "title": "Títol de la font",
    "url": "https://...",
    "source_type": "article"
  },
  "status": "processed",
  "ingested_at": "YYYY-MM-DD",
  "pages_created": [],
  "pages_updated": []
}
~~~

## Validació

Comprova frontmatter, categoria, fonts, wikilinks, rutes, dates i correspondència entre les fitxes i el manifest.
