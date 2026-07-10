---
site: https://www.eleanorkonik.com/
tags:
  - autor
---
# ELEANOR KONIK
## Models

```dataview

TABLE
	font, tags
FROM "models"
	WHERE contains(autor, this.file.link)
	SORT file.name ASC
 
```
