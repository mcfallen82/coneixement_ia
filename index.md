# INDEX CONEIXEMENT, MODELS I LLIBRES

## Entrada ràpida

- [[kanban]]
- [[dashboard.canvas]]

# Models

```dataview

TABLE
	autor, descripcio, estat
FROM "models"
	SORT estat ASC
 
```

## Llibres

```dataview

TABLE WITHOUT ID
	titol, autor, descripcio, tags
FROM "llibres"
	SORT file.name ASC
```
# Autors

```dataview

TABLE
	autor, site
FROM "autors"
	SORT file.name ASC
 
```