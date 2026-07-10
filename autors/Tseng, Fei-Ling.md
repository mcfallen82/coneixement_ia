---
site: https://feeei.substack.com/
tags:
  - autor
---
# Fei-Ling, Tseng
## Models

```dataview

TABLE
	font, tags
FROM "models"
	WHERE contains(autor, this.file.link)
	SORT file.name ASC
 
```
