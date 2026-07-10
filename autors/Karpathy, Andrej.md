---
site: https://gist.github.com/karpathy/
tags:
  - autor
---
# ANDREJ KARPATHY
## Models
```dataview

TABLE
	font, tags
FROM "models"
	WHERE contains(autor, this.file.link)
	SORT file.name ASC
 
```
