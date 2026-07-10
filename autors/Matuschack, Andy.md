---
site: https://notes.andymatuschak.org/
tags:
  - autor
---
# ANDY MATUSCHACK
## Models

```dataview

TABLE
	font, tags
FROM "models"
	WHERE contains(autor, this.file.link)
	SORT file.name ASC
 
```
