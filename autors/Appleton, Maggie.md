---
site: https://maggieappleton.com/
tags:
  - autor
---
# MAGGIE APPLETON

## Models

```dataview

TABLE
	font, tags
FROM "models"
	WHERE contains(autor, this.file.link)
	SORT file.name ASC
 
```
