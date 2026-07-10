---
site:
tags:
  - autor
---

# NOM_AUTOR

# Models

```dataview

TABLE
	font, tags
FROM "models"
	WHERE autor = this.file.link
	SORT file.name ASC
 
```
