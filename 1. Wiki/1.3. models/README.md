# 🤖 Models — arquitectures i implementacions

## Del principi tècnic al sistema concret

Aquesta carpeta presenta arquitectures, famílies i models concrets relacionats amb la IA, com [Transformer](transformer.md), [GPT](GPT.md) i [FinBERT](FinBERT.md). També conserva fitxes de propostes i implementacions de sistemes de coneixement, com [Obsidian Wiki](obsidian_wiki.md) i la memòria agentiva [A-MEM](A-MEM.md). Aquesta diversitat fa necessari identificar **què és exactament cada entrada** abans de comparar-ne capacitats.

Les fitxes expliquen el problema abordat, els components coneguts, les dades i l'objectiu d'entrenament quan es documenten, les entrades i sortides, els usos i els límits. En una arquitectura o un sistema de wiki, alguns d'aquests apartats poden no ser aplicables: cal explicar-ne el motiu, sense omplir camps amb conjectures.

## 🗂️ Què hi trobaràs?

- **Arquitectures i famílies:** principis de disseny que poden sustentar múltiples implementacions.
- **Models concrets:** sistemes o variants amb una descripció atribuïble a documentació o publicacions.
- **Enfocaments de coneixement:** patrons i projectes que organitzen informació i agents, sense atribuir-los automàticament un entrenament propi.
- **Relacions i evidència:** enllaços a [conceptes](../1.2.%20conceptes/), [autors](../1.1.%20autors/) i fonts per aclarir l'origen de cada afirmació.

## 🧭 Com llegir una fitxa de model

Comença pel problema que pretén resoldre i distingeix l'arquitectura general de la seva realització concreta. Revisa després la font i la data de les afirmacions, els conceptes previs, les modalitats, l'entrenament si escau i les limitacions. Això permet comparar models amb criteris equivalents i detectar què encara no està documentat. Torna al [mapa de la wiki](../README.md) si necessites canviar de categoria.

## ✍️ Com crear o actualitzar una fitxa

1. Comprova si ja hi ha una entrada sobre la mateixa família, arquitectura, model o implementació i defineix l'abast de la fitxa.
2. Usa la [plantilla de model](../../4.%20Templates/90.1.%20templates_fitxes/plantilla_model.md) i el frontmatter obligatori indicat a [`AGENTS.md`](../../AGENTS.md); afegeix `model_family`, `architecture`, `modalities`, `training_objective`, `authors` i relacions quan siguin aplicables i estiguin confirmats.
3. Explica amb fonts què se sap de l'entrenament, el funcionament i les prestacions. Marca les inferències com a tals i no inventis dades absents.
4. Enllaça els conceptes previs i models relacionats; revisa que la descripció i els enllaços continuïn vàlids quan hi hagi documentació nova.
