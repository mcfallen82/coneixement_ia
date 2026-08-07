# Dashboard d’auditoria

## Fitxes sense fonts

~~~dataview
TABLE title, category, status, updated
FROM "1. Wiki"
WHERE file.name != "README" AND (sources = null OR length(sources) = 0)
SORT category ASC, title ASC
~~~

## Fitxes sense estat normalitzat

~~~dataview
TABLE file.link, estat
FROM "1. Wiki"
WHERE estat != null
SORT file.path ASC
~~~

## Fonts pendents

~~~dataview
TABLE title, source_type, status, updated
FROM "0. Raw"
WHERE status = "unread" OR status = "pending"
SORT updated ASC
~~~
