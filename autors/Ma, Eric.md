---
site: https://ericmjl.github.io/
tags:
  - autor
---
# ERIC MA
## Models

```dataview

TABLE
	font, tags
FROM "models"
	WHERE contains(autor, this.file.link)
	SORT file.name ASC
 
```
