# Guia per crear bases de coneixement amb grafs

## Objectiu

Aquesta guia explica com evolucionar una base de coneixement en Markdown cap a una xarxa de coneixement útil per a la navegació, la consulta assistida per LLM i, eventualment, sistemes de recuperació com GraphRAG.

El punt de partida és una col·lecció de fitxes amb metadades, fonts i enllaços interns. El resultat esperat és una estructura on els nodes, les relacions i la procedència siguin prou clars perquè una persona o un agent puguin explorar-la, validar-la i ampliar-la.

La guia és independent del domini i de l'editor utilitzat.

## Idea central

```text
Fonts verificables
      ↓
Fitxes permanents
      ↓
Graf de coneixement
      ↓
Recuperació i assistència amb IA
```

- la font conserva l'origen de l'evidència;
- la fitxa explica una unitat de coneixement;
- el graf explicita com es relacionen les fitxes;
- la IA utilitza fitxes, relacions i fonts per recuperar context.

Un enllaç intern és un indici de relació. Es converteix en una aresta útil quan en coneixem el significat, la direcció, la procedència i, quan cal, el nivell de confiança.

## Nivells de maduresa

| Nivell | Característiques | Resultat |
|---|---|---|
| 0. Col·lecció | documents sense estructura comuna | arxiu de materials |
| 1. Wiki connectada | fitxes amb metadades i enllaços | navegació bàsica |
| 2. Graf tipat | relacions amb tipus i direcció | mapa semàntic |
| 3. Graf traçable | arestes amb font i confiança | coneixement auditable |
| 4. Graf consultable | recuperació de nodes i subgrafs | assistència estructurada amb IA |
| 5. GraphRAG | graf + recuperació + avaluació | sistema de preguntes sobre corpus |

No cal arribar al nivell 5. La complexitat s'ha d'afegir només quan resolgui un problema real.

## Què és un node?

Un node és una unitat identificable del coneixement. Segons el domini pot representar:

- persona;
- organització;
- concepte;
- model;
- producte;
- lloc;
- esdeveniment;
- font;
- decisió;
- pregunta oberta.

Cada node ha de tenir un identificador estable.

Exemple:

```yaml
node_id: "concept:cost_oportunitat"
node_type: "concept"
title: "Cost d'oportunitat"
status: "reviewed"
sources:
  - "https://..."
```

## Què és una aresta?

Una aresta és una relació entre dos nodes. Ha de permetre respondre:

1. quin és l'origen?;
2. quin és el destí?;
3. quin tipus de relació expressa?;
4. és dirigida?;
5. quina evidència la sustenta?;
6. és documentada o inferida?

Exemple:

```yaml
source: "concept:rag"
relation: "utilitza"
target: "concept:embeddings"
claim_type: "documented"
confidence: "high"
evidence:
  - "https://..."
```

## Vocabulari de relacions

Comença amb pocs tipus i amplia'ls només quan sigui necessari.

Exemples genèrics:

| Relació | Lectura |
|---|---|
| `es_un` | A és un tipus de B |
| `part_de` | A forma part de B |
| `utilitza` | A fa servir B |
| `amplia` | A amplia B |
| `depen_de` | A necessita B |
| `creat_per` | A s'associa amb el seu creador |
| `explica` | A explica B |
| `avalua` | A avalua B |
| `aplicat_a` | A s'aplica a B |
| `contrasta_amb` | A contrasta amb B |
| `exemple_de` | A és un exemple de B |

Evita `relacionat_amb` quan es pugui expressar una relació més precisa.

## Enllaços i relacions tipades

Els enllaços interns continuen sent útils per a la navegació humana, però no indiquen necessàriament causalitat, jerarquia o direcció.

Es poden combinar tres mecanismes:

1. enllaços dins del text;
2. camps de metadades per relacions simples;
3. un registre d'arestes per relacions que necessiten procedència o confiança.

Exemple:

```yaml
related_concepts:
  - "RAG"
relations:
  - target: "RAG"
    type: "amplia"
    confidence: "high"
```

Quan el nombre de relacions creixi, és millor separar el graf de les fitxes abans d'inflar excessivament el frontmatter.

## Procedència i confiança

El graf ha de distingir entre:

- relació explícita en una font;
- relació inferida a partir de diverses fonts;
- connexió pedagògica;
- hipòtesi pendent de verificar.

Exemple:

```yaml
claim_type: "documented"   # documented | inferred | pedagogical | open
confidence: "high"         # high | medium | low
evidence:
  - source: "https://..."
    summary: "Resum de l'evidència rellevant"
    accessed: "YYYY-MM-DD"
```

La confiança és una etiqueta operativa, no una probabilitat matemàtica.

## Flux per crear o ampliar el graf

### 1. Registrar la font

Conserva la URL o referència bibliogràfica. Si necessites una còpia local de treball, mantén-la fora del repositori compartit o en una ruta ignorada per Git.

### 2. Identificar nodes

Extreu les entitats i conceptes rellevants i comprova si ja existeixen.

### 3. Normalitzar identitats

Unifica sinònims i variants només quan realment designen la mateixa entitat.

### 4. Proposar relacions

Per a cada relació especifica origen, tipus, destinació, evidència i confiança.

### 5. Revisar les arestes

No assumeixis que una relació és simètrica. Les relacions inverses només s'han de crear quan siguin correctes i útils.

### 6. Actualitzar fitxes i índex

Afegeix els enllaços necessaris i actualitza els registres del projecte quan el canvi sigui significatiu.

### 7. Validar

Comprova destinacions, tipus de relació, duplicats, procedència i consistència de les metadades.

## Com pot ajudar una IA o agent?

| Funció | Pregunta |
|---|---|
| Descobriment | Quins nodes nous apareixen? |
| Normalització | Aquest node ja existeix amb un altre nom? |
| Proposta | Quines relacions sembla que hi ha? |
| Verificació | Quina font sustenta cada relació? |
| Manteniment | Quines relacions han quedat obsoletes? |

L'agent ha de proposar les relacions inferides com a candidates revisables, no escriure-les com a fets consolidats.

## Plantilla d'instrucció per a un agent

```text
1. Llegeix la governança i les fitxes relacionades.
2. Registra la procedència de les fonts.
3. Identifica nodes nous i existents.
4. Proposa relacions tipades i dirigides.
5. Separa fets, inferències i dubtes.
6. No creïs duplicats.
7. Actualitza índex, registre i manifest quan calgui.
8. Executa les validacions.
9. Presenta els canvis perquè puguin ser revisats.
```

## Criteris de qualitat

Una base de coneixement amb graf és més robusta quan:

- cada node té identitat clara;
- les relacions utilitzen vocabulari controlat;
- les arestes tenen direcció quan correspon;
- la procedència és rastrejable;
- les inferències estan etiquetades;
- els enllaços apunten a destinacions reals;
- no hi ha duplicats semàntics evidents;
- la xarxa ajuda a recuperar coneixement, no només a generar connexions.

La densitat del graf no és un objectiu en si mateix.

## Quan cal GraphRAG?

GraphRAG pot ser útil quan:

- el corpus és massa gran per navegar-lo manualment;
- les preguntes necessiten seguir múltiples relacions;
- cal recuperar context estructurat;
- la recuperació vectorial sola és insuficient;
- existeixen preguntes de prova i criteris d'avaluació.

Abans d'implementar-lo, el graf ha d'estar prou normalitzat i auditable.

## Auditoria específica del graf

| Comprovació | Pregunta |
|---|---|
| Nodes orfes | Hi ha nodes sense relacions útils? |
| Arestes trencades | Totes les destinacions existeixen? |
| Relacions vagues | Es poden fer més precises? |
| Direcció | La relació es llegeix correctament? |
| Procedència | Hi ha una font o justificació? |
| Duplicats | Dues fitxes descriuen el mateix node? |
| Components aïllats | Hi ha grups desconnectats? |
| Relacions pendents | Quines requereixen revisió humana? |
| Evolució | La font o versió continua vigent? |

## Errors habituals

- confondre molts enllaços amb un graf semàntic;
- crear una relació per cada coaparició;
- inferir causalitat sense evidència;
- ignorar la direcció;
- barrejar tipus de node incompatibles;
- convertir una connexió pedagògica en una afirmació factual;
- construir GraphRAG abans de definir les preguntes que ha de resoldre;
- deixar que un agent incorpori relacions sense revisió;
- perdre la procedència de les afirmacions.

## Resultat esperat

El resultat no és només una visualització. És una base de coneixement on:

1. les fitxes expliquen el coneixement;
2. les relacions expliquen l'estructura;
3. les fonts expliquen l'origen;
4. la confiança explica la certesa;
5. la IA ajuda a descobrir i recuperar connexions;
6. la revisió humana conserva el control semàntic.

Aquesta arquitectura permet evolucionar gradualment des d'una wiki connectada cap a un graf consultable i, només quan sigui justificat, cap a GraphRAG.