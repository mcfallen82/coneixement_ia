# Índex de la wiki d’aprenentatge d’IA

## Entrada ràpida

- [Hot](hot.md) — prioritats i continguts en curs.
- [Registre de canvis](log.md).
- [Governança](AGENTS.md).
- [Quadres de comandament](3.%20Dashboards/).
- [Skills](2.%20Skills/).
- [Plantilles](4.%20Templates/).

## Fonts

- [0.1. llibres](0.%20Raw/0.1.%20llibres/) — llibres, tutorials i materials originals.
- [0.2.](0.%20Raw/0.2./) — articles, papers, cursos i documentació.

## Wiki

### Autors

Fitxes sobre investigadors, divulgadors i referents de la IA.

~~~dataview
TABLE title, field, status, updated
FROM "1. Wiki/1.1. autors"
WHERE file.name != "README"
SORT updated DESC
~~~

### Conceptes

Fitxes sobre conceptes, tècniques i processos.

~~~dataview
TABLE title, status, length(sources) AS fonts, updated
FROM "1. Wiki/1.2. conceptes"
WHERE file.name != "README"
SORT updated DESC
~~~

### Models

Fitxes sobre arquitectures i models.

~~~dataview
TABLE title, model_family, architecture, status, updated
FROM "1. Wiki/1.3. models"
WHERE file.name != "README"
SORT updated DESC
~~~

## Organització

- [2. Skills](2.%20Skills/) — procediments reutilitzables.
- [3. Dashboards](3.%20Dashboards/) — vistes i consultes d’Obsidian.
- [90.1. templates_fitxes](4.%20Templates/90.1.%20templates_fitxes/) — plantilles.
- [90.2. docs_support](4.%20Templates/90.2.%20docs_support/) — documents de suport.

La wiki tracta l’aprenentatge general d’intel·ligència artificial. Les finances i l’economia només hi apareixen com a context d’aplicació.
