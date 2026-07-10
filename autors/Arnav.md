---
site: https://github.com/Ar9av
tags:
  - autor
---
# AR9AV
## Models

```dataview

TABLE
	font, tags
FROM "models"
	WHERE contains(autor, this.file.link)
	SORT file.name ASC
 
```
