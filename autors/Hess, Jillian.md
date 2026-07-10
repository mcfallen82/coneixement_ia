---
site: https://jillianhess.substack.com/
tags:
  - autor
---
# JILLIAN HESS

## Models

```dataview

TABLE
	font, tags
FROM "models"
	WHERE contains(autor, this.file.link)
	SORT file.name ASC
 
```
