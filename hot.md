## Nou concepte: Scaffold

La fitxa de [Scaffold](1.%20Wiki/1.2.%20conceptes/scaffold.md) explica l’arquitectura que envolta un LLM perquè actuï dins d’un procés controlat. La prioritat de prova és comparar quins components —context, eines, validació, memòria o delegació— aporten valor real.

## Frontmatter de conceptes normalitzat

S’han revisat les 39 fitxes conceptuals. Els camps de relació ara tenen un format YAML homogeni i el validador detecta estructures imbricades incorrectes.

## Prova activa: metadades gràfiques de la wiki

Les fitxes de `1. Wiki/` ja incorporen `node_id` i `node_type`. Executa `python scripts/graph_scan.py --check` i `--stats` abans i després d’afegir coneixement nou. Les relacions semàntiques acceptades continuen al registre `graph/relations.json`.

# Hot

## Activitat recent

- 2026-08-07: posada en marxa de la capa gràfica lleugera basada en Markdown.

- 2026-08-07: recerca i processament de grafs aplicats als models de llenguatge.

- 2026-08-07: recerca pilot sobre ajustament, alineament, LoRA i avaluació de models.

## Prioritats actuals

- Executar `python scripts/graph_scan.py --check` i registrar l’evolució de nodes, arestes candidates i enllaços trencats.
- Revisar progressivament les relacions candidates abans de convertir-les en acceptades.

- Definir tipus, direcció, procedència i confiança de les relacions de la wiki.
- Estudiar l’adaptació del patró d’obsidian-second-brain: escàner determinista, relacions tipades, subgrafs i visualització.
- Estudiar una futura exportació de les fitxes a un graf formal.
- Comparar GraphRAG amb una RAG vectorial en un corpus petit.

- Revisar i completar les fitxes de `1. Wiki/1.2. conceptes/`.
- Mantenir actualitzades les fitxes de models a `1. Wiki/1.3. models/`.
- Convertir les notes de lectura en fonts i fitxes relacionades.
- Revisar enllaços interns i consultes Dataview després de cada reorganització.

- Incorporar les fonts i conclusions de la recerca pilot a les fitxes relacionades.
