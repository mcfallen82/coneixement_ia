# 💡 Conceptes — el vocabulari per entendre la IA

## Idees fonamentals i marcs de treball

Aquesta carpeta explica els mecanismes, tècniques i nocions que reapareixen en models i aplicacions. Hi trobaràs des de [xarxes neuronals](xarxes_neuronals.md), [atenció](attention.md) i [embeddings](embeddings.md) fins a [RAG](RAG.md), agents i organització del coneixement. Les fitxes ajuden a respondre **què significa una idea i quan és útil**, abans d'entrar en una arquitectura concreta.

Un concepte pot tenir usos diferents segons el context. Per això les definicions s'acompanyen d'intuïció, funcionament i límits; una etiqueta compartida per dues fonts no implica necessàriament el mateix mecanisme.

## 🗂️ Què conté una fitxa de concepte?

- **Definició i importància:** el problema que ajuda a entendre o resoldre.
- **Intuïció i funcionament:** explicació per capes, amb el detall tècnic que el tema requereixi.
- **Exemples i aplicacions:** casos concrets, com l'anàlisi documental o les dades financeres quan siguin pertinents.
- **Relacions, limitacions i fonts:** enllaços a prerequisits, conceptes propers i [models](../1.3.%20models/) que els utilitzen, amb evidència verificable.

## 🧭 Com estudiar amb aquesta carpeta

Comença per una fitxa que resolgui la teva pregunta; segueix els enllaços als prerequisits si apareixen termes nous, i passa als models quan ja entenguis el mecanisme. Per exemple, els embeddings i l'atenció faciliten la lectura de la fitxa de [Transformer](../1.3.%20models/transformer.md). El [README de la wiki](../README.md) mostra com es connecten totes les categories.

## ✍️ Com crear o ampliar un concepte

1. Comprova noms alternatius i fitxes existents: actualitza una explicació canònica quan la idea ja hi és.
2. Parteix de la [plantilla de concepte](../../4.%20Templates/90.1.%20templates_fitxes/plantilla_concepte.md) i inclou el frontmatter obligatori (`title`, `category`, `tags`, `sources`, `status`, `created` i `updated`).
3. Separa les afirmacions de la font de les teves inferències; aporta exemples propis i explica quan la tècnica falla o no s'aplica.
4. Afegeix relacions pertinents i valida fonts i enllaços segons [`AGENTS.md`](../../AGENTS.md). Ajusta la profunditat a la dificultat del concepte.
