---
site: https://github.com/eugeniughelbur/
tags:
  - autor
---
# EUGENIU GHELBUR
## Models

```dataview

TABLE
	font, tags
FROM "models"
	WHERE contains(autor, this.file.link)
	SORT file.name ASC
 
```
