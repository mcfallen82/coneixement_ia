# 90.2. docs_support

Aquesta carpeta conté **documents base per crear noves bases de coneixement vinculades a una IA**.

No està pensada per conservar contingut temàtic específic de `coneixement_ia`, sinó per reunir **arquitectures, patrons, criteris i guies reutilitzables** que permetin construir una nova wiki sobre qualsevol domini: finances, història, medicina, dret, recerca personal, documentació professional, ciència o qualsevol altre corpus de coneixement.

Els documents d'aquesta carpeta es deriven de la documentació, experiència i patrons acumulats al projecte i es reformulen perquè siguin **neutres respecte del tema i replicables**.

## Funció de la carpeta

`docs_support` proporciona el **scaffold inicial** d'una nova base de coneixement:

```text
Tema o domini nou
        ↓
Documents base de docs_support
        ↓
Arquitectura + governança + recerca + relacions
        ↓
Nova wiki
        ↓
IA o agent que la consulta, manté i amplia
```

Un document pertany aquí quan ajuda a definir:

- estructura i categories d'una nova wiki;
- governança i instruccions per a agents;
- política de fonts i procedència;
- processos d'ingesta, actualització i validació;
- representació de nodes i relacions;
- estratègies de recuperació amb IA;
- criteris replicables en dominis diferents.

## Què no hi ha d'anar

Aquesta carpeta **no és una biblioteca de contingut temàtic**.

No hi corresponen:

- rutes d'estudi sobre una tecnologia concreta;
- resums d'un curs o llibre específic;
- fitxes de conceptes, autors o models;
- contingut útil només dins de la wiki actual;
- còpies de fonts originals o dossiers de treball.

Aquest contingut correspon a `1. Wiki/`, a fonts externes o a altres espais específics del projecte.

## Documents actuals

| Document | Funció | Ús en una nova base de coneixement |
|---|---|---|
| [`plantilla_wiki_neutra_replicable.md`](plantilla_wiki_neutra_replicable.md) | Defineix l'arquitectura mínima d'una base de coneixement Markdown mantinguda amb IA o agents. | Punt de partida per decidir estructura, governança, manifest, skills, plantilles i flux d'ingesta. |
| [`patro_wiki_agents_replicable.md`](patro_wiki_agents_replicable.md) | Resumeix el patró general de wiki mantinguda amb agents, fonts verificables, Git i revisió humana. | Document conceptual per entendre com encaixen les peces del sistema abans d'implementar-lo. |
| [`research-config.md`](research-config.md) | Defineix un patró de recerca per rondes, jerarquia de fonts, procedència i confiança. | Base per adaptar una política de recerca al domini concret de la nova wiki. |
| [`guia_creacio_wikis_amb_grafs.md`](guia_creacio_wikis_amb_grafs.md) | Explica com evolucionar d'una wiki connectada a un graf de coneixement tipat i traçable. | Referència per incorporar nodes, relacions i recuperació estructurada amb IA o GraphRAG quan sigui necessari. |

## Com utilitzar aquests documents

Quan es crea una nova base de coneixement:

1. defineix el domini, l'objectiu i les preguntes que haurà de resoldre;
2. utilitza aquests documents com a base arquitectònica;
3. adapta categories, metadades, fluxos i criteris de fonts;
4. genera l'estructura inicial de la wiki;
5. defineix instruccions persistents per a la IA o agent;
6. crea skills i plantilles específiques del domini;
7. valida que el sistema sigui comprensible tant per persones com per agents.

Els documents no s'han de copiar mecànicament: són **patrons de disseny que cal especialitzar**.

## Relació amb `90.1. templates_fitxes/`

- [`90.1. templates_fitxes/`](../90.1.%20templates_fitxes/) proporciona **formats per crear peces de coneixement**.
- `90.2. docs_support/` proporciona **documents per dissenyar el sistema que les contindrà**.

En una nova wiki, `90.2` ajuda a decidir l'arquitectura; `90.1` ajuda a donar forma a les fitxes.

## Criteri de qualitat

Un document de `docs_support` ha de ser:

- **replicable** en més d'un domini;
- **independent de l'eina local**;
- **comprensible per una persona** sense conèixer la història del projecte;
- **útil per a una IA o agent** com a context estructural;
- **traçable** en les seves decisions de disseny;
- prou general per servir de base i prou concret per poder-se implementar.

## Principi general

**`90.2. docs_support/` és la biblioteca de patrons per crear noves bases de coneixement assistides per IA.**

La seva unitat de treball no és una fitxa temàtica, sinó una peça d'arquitectura, governança, recerca o disseny reutilitzable.