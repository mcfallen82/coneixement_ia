# wiki-dashboard

## Finalitat

Crear vistes consultables per controlar l’estat i l’evolució de la wiki.

## Vistes recomanades

- fitxes modificades recentment;
- conceptes sense fonts;
- models pendents de completar;
- autors amb obres relacionades;
- fonts encara no processades;
- fitxes per tags o categories;
- fitxes orfes.

## Dataview

~~~dataview
TABLE title, status, updated
FROM "1. Wiki/1.2. conceptes"
WHERE file.name != "README"
SORT updated DESC
~~~

Utilitza les rutes actuals i els camps title, category, sources, status i updated. Si es fan servir Bases, conserva les consultes en 3. Dashboards/ i explica els camps requerits.

## Validació

Comprova que cada vista retorna resultats, que no depèn de camps antics i que els fitxers referenciats existeixen.