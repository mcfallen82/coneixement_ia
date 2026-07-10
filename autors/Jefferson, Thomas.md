---
site:
tags:
  - autor
---
# THOMAS JEFFERSON

## Models

```dataview

TABLE
	font, tags
FROM "models"
	WHERE contains(autor, this.file.link)
	SORT file.name ASC
 
```
