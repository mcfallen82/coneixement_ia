# wiki-lint

## Finalitat

Auditar la coherència mínima de la wiki abans de publicar canvis.

## Comprovacions

1. Carpetes obligatòries i fitxers operatius.
2. Frontmatter YAML a les fitxes permanents.
3. Camps coherents: title, category, tags, sources, status, created i updated.
4. Absència dels camps antics estat quan es pugui normalitzar.
5. Wikilinks cap a rutes reals i absència de rutes antigues.
6. Fonts no buides en fitxes madures.
7. Categories compatibles amb la carpeta.
8. Models amb família, arquitectura i modalitats quan siguin aplicables.
9. Fitxes orfes, duplicats i sinònims.
10. Consultes Dataview actualitzades.
11. Entrades del manifest amb estat i pàgines relacionades.

## Procediment manual inicial

~~~bash
rg -n "autors/|conceptes/|models/|llibres/|docs_support/|templates/" .
rg -n "^---$|^title:|^category:|^sources:|^status:|^updated:" "1. Wiki"
rg -n "\[\[.*\]\]" "1. Wiki" "4. Templates"
~~~

Les cerques són una primera auditoria; la revisió humana continua sent necessària.
