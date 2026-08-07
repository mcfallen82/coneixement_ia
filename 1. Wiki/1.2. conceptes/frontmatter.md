---
title: Frontmatter
node_id: "concept:frontmatter"
node_type: "concept"
category: conceptes
tags:
  - markdown
  - obsidian
  - metadades
sources:
  - https://help.obsidian.md/properties
status: reviewed
created: 2026-08-07
updated: 2026-08-07
---

# Frontmatter

## Definició

El frontmatter és un bloc de metadades situat al principi d’un fitxer Markdown, habitualment escrit en YAML i delimitat per tres guions.

## Per què és important?

Permet que Obsidian, Dataview i altres eines filtrin, ordenin i relacionin notes sense haver d’interpretar tot el text.

## Intuïció

És la fitxa catalogràfica d’un llibre: descriu el document abans d’entrar en el contingut.

## Funcionament

Els noms dels camps han de ser estables. Si unes fitxes utilitzen status i altres estat, les consultes poden perdre resultats.

Exemple de camps: title, category, tags, sources, status, created i updated.

## Exemple

Una consulta Dataview pot mostrar totes les fitxes de category: conceptes i ordenar-les per updated.

## Relacions

- [[README]]
- [[RAG]]
- [[second_brain]]
- [[context_engineering]]

## Aplicacions

- índexs dinàmics;
- revisions;
- seguiment de fonts;
- classificació;
- detecció de pàgines incompletes.

## Limitacions i errors habituals

- YAML mal format;
- camps duplicats;
- dates amb formats diferents;
- confondre metadades amb contingut.

## Fonts

- [Obsidian — Properties](https://help.obsidian.md/properties).
