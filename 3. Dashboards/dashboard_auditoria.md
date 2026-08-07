# Dashboard d’auditoria

Aquest dashboard utilitza els camps normalitzats de la wiki. Els resultats són indicadors de revisió, no substitueixen `python scripts/wiki_lint.py`.

## Fitxes sense fonts

~~~dataview
TABLE title, category, status, updated
FROM "1. Wiki"
WHERE file.name != "README" AND (sources = null OR length(sources) = 0)
SORT category ASC, title ASC
~~~

## Fitxes en esborrany

~~~dataview
TABLE title, category, status, updated
FROM "1. Wiki"
WHERE file.name != "README" AND status = "draft"
SORT updated ASC, title ASC
~~~

## Camps antics

~~~dataview
TABLE file.link, status, updated
FROM "1. Wiki"
WHERE file.name != "README" AND estat != null
SORT file.path ASC
~~~

Aquesta consulta ha de retornar zero resultats. Si en retorna, cal revisar la fitxa i executar la validació.

## Fonts pendents

~~~dataview
TABLE file.link, source_type, status, updated
FROM "0. Raw"
WHERE status = "unread" OR status = "pending"
SORT updated ASC
~~~

Les fonts Raw no sempre tenen frontmatter; el seu estat canònic és el registrat a `.manifest.json`.
