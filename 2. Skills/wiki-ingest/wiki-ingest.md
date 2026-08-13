# wiki-ingest

## Finalitat

Convertir una font d’aprenentatge en coneixement permanent, traçable i connectat dins de ia_knowledge.

## Abans de començar

1. Llegeix AGENTS.md, index.md, hot.md i aquesta skill.
2. Identifica la font: article, llibre, tutorial, paper, vídeo, documentació, repositori, conversa o dades estructurades.
3. Conserva la font o una còpia de treball a 0. Raw/ o 0. Raw/.
4. Registra títol, autor, data, URL, tipus i estat de processament.

## Modes

- **Font bruta:** conservar el material sense transformar-lo.
- **Ingesta normal:** extreure i crear o actualitzar fitxes.
- **Reingesta:** processar només els canvis d’una font ja registrada.
- **Ingesta de projecte:** resumir decisions, arquitectura i aprenentatges d’un repositori, no copiar-ne el codi.

## Flux operatiu

1. Llegeix la font completa o delimita clarament les parts analitzades.
2. Extreu conceptes, models, autors, eines, afirmacions, exemples, limitacions i preguntes obertes.
3. Busca fitxes existents, sinònims i grafies alternatives a 1. Wiki/.
4. Classifica cada element:
   - autor → 1. Wiki/1.1. autors/;
   - concepte → 1. Wiki/1.2. conceptes/;
   - model → 1. Wiki/1.3. models/;
   - font o dada factual → 0. Raw/.
5. Decideix si cal crear una fitxa, actualitzar-ne una, afegir un enllaç o conservar només la font.
6. Redacta la fitxa amb intuïció abans del detall tècnic. Inclou exemple, aplicacions, limitacions i relacions quan siguin pertinents.
7. Afegeix sources al frontmatter i una secció final de fonts. No presentis una interpretació com si fos una dada de la font.
8. Connecta la fitxa amb wikilinks reals i comprova les relacions inverses quan siguin importants.
9. Actualitza index.md, log.md, hot.md i .manifest.json.
10. Executa wiki-lint i revisa manualment les pàgines creades.

## Regla de no-duplicació

La wiki compila coneixement. No creïs un resum nou si una fitxa existent pot incorporar la informació. Crea una fitxa només quan hi hagi una unitat de coneixement diferenciada.

## Manifest mínim

~~~json
{
  "path": "0. Raw/font.md",
  "source_type": "article",
  "status": "processed",
  "ingested_at": "YYYY-MM-DD",
  "pages_created": [],
  "pages_updated": []
}
~~~

## Validació

Comprova frontmatter, categoria, fonts, wikilinks, rutes, dates i correspondència entre les fitxes i el manifest.
