---
title: Us de grafs a obsidian-second-brain
category: raw
raw_type: research_dossier
source_type: repository_review
processing_status: processed
status: processed
created: 2026-08-07
updated: 2026-08-13
previous_path: "0. Raw/0.2. altres fonts/recerca_grafs_obsidian_second_brain_2026-08-07.md"
tags:
  - grafs
  - wikis
  - Obsidian
  - segon-cervell
  - GraphRAG
  - enllaços-tipats
sources:
  - "https://github.com/eugeniughelbur/obsidian-second-brain/blob/main/scripts/link_graph.py"
  - "https://github.com/eugeniughelbur/obsidian-second-brain/blob/main/commands/obsidian-visualize.md"
  - "https://github.com/eugeniughelbur/obsidian-second-brain/blob/main/commands/obsidian-connect.md"
  - "https://github.com/eugeniughelbur/obsidian-second-brain/blob/main/SKILL.md"
  - "https://github.com/eugeniughelbur/obsidian-second-brain/blob/main/architecture.md"
---

# Ús de grafs a `obsidian-second-brain`

## Identificació de la font

Aquest dossier resumeix la utilització documentada dels grafs al repositori [obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain). La revisió s’ha centrat en el script `scripts/link_graph.py`, les ordres `obsidian-visualize` i `obsidian-connect`, la skill principal, les regles d’un vault orientat a IA i el document d’arquitectura.

El projecte no tracta el graf com una base de dades separada des del primer moment. Parteix dels fitxers Markdown i dels wikilinks d’Obsidian, i hi afegeix una capa de lectura, anàlisi i visualització. Aquesta decisió permet començar amb una wiki connectada i evolucionar gradualment cap a un graf semàntic o un sistema GraphRAG.

## 1. Graf d’enllaços determinista

El fitxer `scripts/link_graph.py` construeix un graf del vault en una sola passada.

### Nodes

Cada fitxer Markdown pot actuar com un node. El resultat conserva:

- camí relatiu;
- títol;
- tipus de nota;
- carpeta;
- nombre d’enllaços entrants;
- nombre d’enllaços sortints;
- grau total.

El camí del fitxer funciona com a identificador més estable que el títol visible, perquè el títol pot canviar.

### Arestes

Cada wikilink resolt es converteix en una aresta dirigida:

```text
nota_origen → nota_destinació
```

L’script resol aliases, rutes relatives, extensions `.md`, accents i guions llargs. També exclou codi, exemples de documentació i enllaços a fitxers o carpetes reals que no són notes.

### Estadístiques

El resultat JSON inclou:

- nombre de nodes;
- nombre d’arestes;
- hubs principals;
- nodes orfes;
- enllaços trencats o destinacions inexistents;
- grau d’entrada i sortida de cada node.

La idea important és separar el recompte exacte —que fa l’script— de la interpretació —que pot fer l’agent o l’usuari—.

## 2. Relacions tipades com a capa semàntica

El repositori afegeix una capa de relacions semàntiques al graf bàsic de wikilinks. Les relacions s’emmagatzemen en el frontmatter, dins d’un bloc `relations:`.

Exemple documentat:

```yaml
relations:
  supersedes:
    - "[[ADR-006]]"
  depends_on:
    - "[[Projecte]]"
```

La relació deixa de ser simplement «A enllaça amb B» i passa a expressar «A depèn de B» o «A substitueix B».

El script coneix, entre d’altres, les relacions següents:

| Relació | Inversa esperada |
|---|---|
| `supersedes` | `superseded_by` |
| `depends_on` | `required_by` |
| `caused` | `caused_by` |
| `decided_by` | `decides` |
| `relates_to` | ella mateixa |
| `contradicts` | ella mateixa |

La capa tipada no substitueix els wikilinks ni duplica el recompte de connectivitat. Els wikilinks proporcionen navegació i grau; les relacions tipades aporten significat.

També es valida:

- tipus de relació desconegut;
- destinació inexistent;
- aresta cap al mateix node;
- relació inversa absent;
- contradiccions com dues notes que es proclamen mútuament predecessores.

## 3. Visualització amb `obsidian-visualize`

L’ordre `obsidian-visualize` utilitza el graf determinista per generar un fitxer JSON Canvas compatible amb Obsidian.

El procés documentat és:

1. llegir les regles del vault;
2. executar `link_graph.py`;
3. generar nodes i arestes del canvas;
4. situar els hubs al centre;
5. agrupar els nodes per tipus;
6. diferenciar visualment conceptes, projectes, entitats, fonts i notes diàries;
7. situar els orfes als marges;
8. desar el resultat com `atlas.canvas` o com un canvas específic del tema;
9. registrar l’operació i les estadístiques.

La visualització no és només decorativa. El resum associat ha d’identificar:

- hubs i centralitat;
- nodes pont entre clústers;
- orfes;
- clústers densos;
- components aïllats;
- asimetries de centralitat;
- possibles punts únics de dependència de la navegació.

El projecte recomana distingir entre centralitat calculada i interpretació humana. El recompte de graus prové de l’script; la identificació d’un pont o el significat d’un clúster requereix una anàlisi posterior.

## 4. Connexió entre dominis amb `obsidian-connect`

L’ordre `obsidian-connect` utilitza el graf per connectar dos dominis diferents.

Per a cada domini:

1. busca notes relacionades pel títol, les etiquetes i el contingut;
2. recupera els enllaços entrants i sortints;
3. construeix un clúster local;
4. busca enllaços compartits, etiquetes o persones comunes;
5. traça un camí directe si existeix;
6. busca una proximitat semàntica si no hi ha camí explícit.

La sortida esperada no és una llista d’associacions vagues. Ha d’oferir connexions accionables, com ara:

- analogies estructurals;
- transferències de mètodes;
- idees que apareixen en la intersecció dels dos dominis.

Aquesta funció correspon a una utilització del graf com a eina de pensament, no a GraphRAG. El graf ajuda a descobrir camins i ponts; l’agent interpreta aquests camins.

## 5. Relació amb una wiki orientada a IA

La filosofia general d’`obsidian-second-brain` considera que:

- les fonts alimenten notes permanents;
- les notes es connecten mitjançant wikilinks;
- els scripts fan el treball determinista;
- les ordres i els agents interpreten el graf;
- les regles d’IA obliguen a conservar fonts, context, enllaços i confiança.

En aquest model, el graf és una vista computable de la wiki. No és necessàriament la font principal de veritat. La informació continua vivint en les notes i en les fonts; el graf explicita les connexions entre aquestes unitats.

## 6. Patrons reutilitzables per a `ia_knowledge`

La incorporació més útil per al projecte `ia_knowledge` és el patró següent:

```text
Markdown + wikilinks
        ↓
escàner determinista
        ↓
nodes, arestes, hubs i orfes
        ↓
relacions tipades i procedència
        ↓
subgrafs, consultes i visualitzacions
        ↓
assistència d’un LLM
```

Això suggereix una evolució en cinc passos:

1. mantenir fitxes i wikilinks navegables;
2. calcular un graf bàsic sense dependre de la interpretació del LLM;
3. introduir un vocabulari reduït de relacions tipades;
4. afegir procedència, confiança i validació;
5. exportar subgrafs o context estructurat només quan les preguntes ho justifiquin.

No s’ha d’interpretar aquesta font com una prova que `ia_knowledge` ja tingui implementat el mateix sistema. El repositori font ofereix un patró operatiu i codi reutilitzable conceptualment; l’adaptació al projecte actual requeriria respectar les seves rutes, el frontmatter i el validador propi.

## 7. Distincions importants

| Element | Funció |
|---|---|
| Wikilink | Navegació i connexió explícita entre notes |
| Graf d’enllaços | Representació computable dels wikilinks resolts |
| Relació tipada | Significat semàntic i direcció d’una connexió |
| Canvas | Visualització espacial del graf |
| `obsidian-connect` | Descobriment de camins i ponts entre dominis |
| GraphRAG | Recuperació de context gràfic per a un LLM |
| GNN | Aprenentatge neuronal sobre nodes i arestes |

Una wiki amb un escàner de wikilinks no és automàticament un sistema GraphRAG. El valor de GraphRAG apareix quan el graf, la recuperació, el corpus, les preguntes i l’avaluació formen un sistema integrat.

## 8. Limitacions i riscos

- els wikilinks poden expressar relacions massa vagues;
- els noms duplicats dificulten la resolució de nodes;
- els enllaços trencats alteren els recomptes de grau;
- una relació tipada pot ser incorrecta encara que la destinació existeixi;
- una relació inversa absent no sempre és un error semàntic;
- la centralitat no equival a importància conceptual;
- un canvas pot fer visible l’estructura sense explicar-ne el significat;
- les connexions proposades per un agent han de mantenir-se revisables;
- els grafs grans poden requerir filtres, subgrafs o indexació.

## Fonts revisades

- [`scripts/link_graph.py`](https://github.com/eugeniughelbur/obsidian-second-brain/blob/main/scripts/link_graph.py) — extracció determinista, resolució de wikilinks i validació de relacions tipades.
- [`obsidian-visualize`](https://github.com/eugeniughelbur/obsidian-second-brain/blob/main/commands/obsidian-visualize.md) — generació de canvas, centralitat, clústers, ponts i orfes.
- [`obsidian-connect`](https://github.com/eugeniughelbur/obsidian-second-brain/blob/main/commands/obsidian-connect.md) — connexió de dominis i descobriment de camins.
- [`SKILL.md`](https://github.com/eugeniughelbur/obsidian-second-brain/blob/main/SKILL.md) — filosofia d’un vault orientat a IA i propagació de connexions.
- [`architecture.md`](https://github.com/eugeniughelbur/obsidian-second-brain/blob/main/architecture.md) — arquitectura general, separació entre scripts, ordres i vault.
