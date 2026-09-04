# 90.2. docs_support

Aquesta carpeta conté **documents base per crear noves bases de coneixement vinculades a una IA**.

No està pensada per conservar contingut temàtic específic de `coneixement_ia`, sinó per reunir **arquitectures, patrons, criteris i guies reutilitzables** que permetin construir una nova wiki sobre qualsevol domini: intel·ligència artificial, finances, història, medicina, dret, recerca personal, documentació professional o qualsevol altre corpus de coneixement.

Els documents d'aquesta carpeta es deriven de la documentació, experiència i patrons acumulats al projecte i es reformulen perquè siguin **neutres respecte del tema i replicables**.

## Quina funció compleix aquesta carpeta?

El seu objectiu és proporcionar el **scaffold inicial** d'una nova base de coneixement:

```text
Tema o domini nou
        ↓
Documents base de `docs_support`
        ↓
Definició de l'arquitectura, governança i fluxos
        ↓
Creació de la nova wiki
        ↓
Connexió amb una IA o agent que la pugui llegir, mantenir i ampliar
```

Per tant, un document pertany a `90.2. docs_support/` quan ajuda a respondre preguntes com:

- com hauria d'estar estructurada una nova wiki;
- quines metadades i convencions necessita;
- com s'han de conservar les fonts i la procedència;
- com s'ha d'organitzar la ingesta i actualització de coneixement;
- com pot una IA consultar, mantenir o ampliar la base;
- com es poden representar relacions i grafs de coneixement;
- com es valida la coherència del sistema;
- com es pot replicar el patró en un domini diferent.

## Què no hi ha d'anar?

Aquesta carpeta **no és una biblioteca de contingut d'aprenentatge específic** ni un repositori de resums temàtics.

No hi haurien d'anar, per exemple:

- rutes d'estudi sobre una tecnologia concreta;
- resums d'un curs o llibre específic;
- fitxes de conceptes, autors o models;
- contingut que només tingui sentit dins de la wiki actual;
- còpies de fonts originals o dossiers de treball.

Aquest tipus de coneixement correspon a `1. Wiki/`, a les fonts externes corresponents o a altres espais específics del projecte.

## Documents actuals

| Document | Funció | Ús en una nova base de coneixement |
|---|---|---|
| [`plantilla_wiki_neutra_replicable.md`](plantilla_wiki_neutra_replicable.md) | Defineix una arquitectura general de wiki Markdown mantinguda amb ajuda d'agents. | Punt de partida per decidir estructura, índexs, manifest, skills, plantilles i flux d'ingesta d'un projecte nou. |
| [`resum_ar9av_wiki_ia_knowledge.md`](resum_ar9av_wiki_ia_knowledge.md) | Sintetitza el patró de wiki mantinguda amb agents, fonts verificables, Git i revisió humana. | Document conceptual per entendre com interactuen la base de coneixement, els agents i el control de versions. |
| [`research-config.md`](research-config.md) | Defineix criteris per investigar, prioritzar fonts i conservar procedència. | Base per adaptar una política de recerca al domini concret de la nova wiki. |
| [`guia_creacio_wikis_amb_grafs.md`](guia_creacio_wikis_amb_grafs.md) | Explica com evolucionar d'una wiki connectada a un graf de coneixement tipat i traçable. | Referència per incorporar nodes, relacions, procedència i una futura recuperació assistida per LLM o GraphRAG. |

## Com utilitzar aquests documents

Quan es crea una nova base de coneixement, aquests documents no s'han de copiar mecànicament. El procés recomanat és:

1. definir el domini, objectiu i tipus de coneixement que es vol conservar;
2. utilitzar aquests documents com a base arquitectònica;
3. adaptar categories, metadades, fluxos i criteris de fonts al nou domini;
4. generar l'estructura inicial de la nova wiki;
5. definir instruccions persistents per a l'agent o IA que hi treballarà;
6. crear les skills i plantilles específiques que necessiti el nou projecte;
7. validar que el sistema continua sent comprensible per a una persona i no només per a l'agent.

## Relació amb `90.1. templates_fitxes/`

Les dues subcarpetes tenen funcions diferents:

- [`90.1. templates_fitxes/`](../90.1.%20templates_fitxes/) proporciona **formats per crear peces de coneixement**;
- `90.2. docs_support/` proporciona **documents per dissenyar el sistema que les contindrà**.

Una nova wiki pot reutilitzar o adaptar les plantilles de `90.1`, però primer necessita una arquitectura i unes regles de funcionament. Aquesta és la funció de `90.2`.

## Criteri de qualitat

Un bon document de `docs_support` ha de ser:

- **replicable** en més d'un domini;
- **independent de l'eina local** sempre que sigui possible;
- **comprensible per una persona** sense conèixer la història del projecte;
- **útil per a una IA o agent** com a instrucció o context estructural;
- **traçable**, distingint patrons derivats, decisions de disseny i fonts externes;
- prou general per servir de base, però prou concret per poder-se implementar.

## Principi general

**`90.2. docs_support/` és la biblioteca de patrons per crear noves bases de coneixement assistides per IA.**

La seva unitat de treball no és una fitxa temàtica, sinó una peça d'arquitectura, governança, recerca o disseny que pugui reutilitzar-se per construir una nova wiki sobre qualsevol matèria.
