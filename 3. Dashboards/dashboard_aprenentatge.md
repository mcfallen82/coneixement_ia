# Dashboard d’aprenentatge

## Fitxes actualitzades recentment

~~~dataview
TABLE title, category, status, updated
FROM "1. Wiki"
WHERE file.name != "README"
SORT updated DESC
LIMIT 20
~~~

## Conceptes pendents de completar

~~~dataview
TABLE title, status, length(sources) AS fonts, updated
FROM "1. Wiki/1.2. conceptes"
WHERE file.name != "README" AND (status = "draft" OR length(sources) = 0)
SORT updated ASC
~~~

## Models pendents

~~~dataview
TABLE title, model_family, architecture, status
FROM "1. Wiki/1.3. models"
WHERE file.name != "README" AND status != "complete"
SORT title ASC
~~~
