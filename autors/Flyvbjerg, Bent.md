---
site:
tags:
  - autor
---
# Bent Flyvbjerg

# Llibres

```dataview

TABLE
	font, tags
FROM "llibres"
	WHERE contains(autor, this.file.link)
	SORT file.name ASC
 
```

