# Guia per crear wikis amb grafs de coneixement

## Objectiu

Aquesta guia explica com convertir una wiki de Markdown, com 'ia_knowledge', en una xarxa de coneixement útil per a la navegació, la consulta assistida per LLM i, eventualment, un sistema GraphRAG.

El punt de partida és una col·lecció de fitxes amb frontmatter, fonts i wikilinks. El resultat esperat és una estructura en què els nodes, les relacions i la procedència de cada afirmació siguin prou clars perquè una persona o un agent puguin explorar-la, validar-la i ampliar-la.

La guia complementa [[AGENTS]]. No substitueix la governança del repositori ni converteix automàticament tots els wikilinks existents en relacions semàntiques.

## Idea central

Una wiki té tres capes relacionades:

~~~text
Documents i fonts
      ↓
Fitxes permanents
      ↓
Graf de coneixement
      ↓
Recuperació i assistència amb LLM
~~~

- La font conserva el material d’origen.
- La fitxa explica una unitat de coneixement.
- El graf explicita com es relacionen les fitxes.
- El LLM utilitza el graf i les fonts per respondre o proposar noves connexions.

Un enllaç entre dues notes és un indici de relació. Es converteix en una aresta útil quan en coneixem el significat, la direcció, l’origen i, si és necessari, la confiança.

## Conceptes previs

Aquesta guia parteix de les fitxes següents:

- [[grafs_i_models_de_llenguatge]]
- [[GraphRAG]]
- [[graph_of_thoughts]]
- [[xarxes_neuronals_de_graf]]
- [[ontologies_associatives]]
- [[RAG]]
- [[frontmatter]]
- [[LLM]]

Cal mantenir separades quatre idees:

| Idea | Funció |
|---|---|
| Graf de coneixement | Representa entitats, conceptes, fets i relacions |
| GraphRAG | Utilitza un graf per recuperar i organitzar context per a un LLM |
| Graph of Thoughts | Organitza passos de treball o raonament d’un LLM |
| GNN | Aprèn representacions sobre nodes i arestes amb una xarxa neuronal |

Una wiki amb grafs utilitza principalment la primera idea. Pot preparar el terreny per a GraphRAG, però no és GraphRAG per defecte.

## Nivells de maduresa

No cal construir un graf formal des del primer dia. És més segur avançar per nivells:

| Nivell | Característiques | Resultat |
|---|---|---|
| 0. Col·lecció | Documents sense estructura comuna | Arxiu de fonts |
| 1. Wiki connectada | Fitxes amb frontmatter i wikilinks | Navegació bàsica |
| 2. Graf tipat | Relacions amb tipus i direcció | Mapa semàntic lleuger |
| 3. Graf traçable | Arestes amb font, data i confiança | Coneixement auditable |
| 4. Graf consultable | Exportació, índex i recuperació de subgrafs | Assistència amb LLM |
| 5. GraphRAG | Graf, comunitats, recuperació i avaluació | Sistema de preguntes sobre corpus |

Per a 'ia_knowledge', l’objectiu immediat és consolidar els nivells 2 i 3 abans d’introduir una infraestructura GraphRAG completa.

## Què és un node?

Un node és una unitat identificable del coneixement. En aquesta wiki, els nodes principals són:

- un autor;
- un concepte;
- un model o una arquitectura;
- una font;
- una tècnica;
- una aplicació;
- una pregunta oberta;
- una afirmació que cal verificar.

Cada node hauria de tenir un identificador estable. En una wiki Markdown, el camí relatiu o el nom del fitxer pot actuar com a identificador, però el títol visible no sempre és suficient perquè pot canviar.

Exemple de node:

~~~yaml
node_id: "1. Wiki/1.2. conceptes/GraphRAG.md"
node_type: "concept"
title: "GraphRAG"
status: "reviewed"
sources:
  - "https://microsoft.github.io/graphrag/"
~~~

## Què és una aresta?

Una aresta és una relació entre dos nodes. Ha de respondre, com a mínim, aquestes preguntes:

1. Quin és el node d’origen?
2. Quin és el node de destinació?
3. Quin tipus de relació expressen?
4. En quina direcció es llegeix?
5. Quina font la sustenta?
6. És una dada documentada o una interpretació?

Exemple:

~~~yaml
source: "GraphRAG"
relation: "amplia"
target: "RAG"
direction: "directed"
source_evidence:
  - "https://microsoft.github.io/graphrag/"
confidence: "high"
claim_type: "documented"
~~~

La frase resultant és:

> GraphRAG amplia RAG.

És més informativa que un enllaç genèric entre dues fitxes.

## Vocabulari mínim de relacions

Cal començar amb un vocabulari petit i estable. Les relacions s’han d’ampliar només quan aparegui una necessitat real.

| Relació | Lectura | Exemple |
|---|---|---|
| 'és_un' | A és una categoria o tipus de B | GPT és un model de llenguatge |
| 'part_de' | A forma part de B | atenció és part de Transformer |
| 'utilitza' | A fa servir B | GraphRAG utilitza un graf |
| 'amplia' | A afegeix capacitats a B | GraphRAG amplia RAG |
| 'depèn_de' | A necessita B | RAG depèn d’un LLM |
| 'creat_per' | A s’associa amb el seu autor | GPT creat per OpenAI |
| 'explicat_per' | Una font o autor explica A | un curs explica embeddings |
| 'avalua' | A mesura o comprova B | MMLU avalua models |
| 'aplicat_a' | A s’utilitza en un àmbit | RAG aplicat a wikis |
| 'contrasta_amb' | A presenta una diferència rellevant respecte de B | GraphRAG contrasta amb RAG vectorial |
| 'exemple_de' | A il·lustra B | G-Retriever exemple de GraphQA |
| 'requereix_verificacio' | La relació encara no està confirmada | una afirmació pendent |

S’han d’evitar relacions vagues com 'relacionat_amb' quan sigui possible. Si no es pot especificar millor, es pot utilitzar provisionalment, però cal marcar-la com a relació de baixa precisió.

## Wikilinks i relacions tipades

Els wikilinks continuen sent útils perquè faciliten la navegació a Obsidian:

~~~markdown
[[GraphRAG]]
~~~

Però un wikilink no indica necessàriament si la relació és causal, jeràrquica, temporal o simplement bibliogràfica.

Es recomana utilitzar tres mecanismes complementaris:

1. **Wikilinks** dins del text per a la navegació humana.
2. **Frontmatter** per a relacions simples i filtrables.
3. **Registre d’arestes** quan calgui procedència, confiança, dates o múltiples relacions.

Exemple de frontmatter lleuger:

~~~yaml
related_concepts:
  - "[[RAG]]"
  - "[[ontologies_associatives]]"
relations:
  - target: "[[RAG]]"
    type: "amplia"
    confidence: "high"
~~~

Quan les relacions creixin, convé conservar-les en un fitxer o taula específica. No s’ha d’inflar el frontmatter amb una ontologia completa si la wiki encara no la necessita.

## Procedència i confiança

El graf ha de distingir entre:

- una relació explícita en una font;
- una relació inferida a partir de diverses fonts;
- una connexió pedagògica creada per facilitar l’aprenentatge;
- una hipòtesi pendent de verificar.

Es recomana utilitzar els camps següents:

~~~yaml
claim_type: "documented"   # documented | inferred | pedagogical | open
confidence: "high"         # high | medium | low
evidence:
  - source: "https://arxiv.org/abs/2404.16130"
    quote_or_summary: "El mètode organitza el corpus amb un graf i resums de comunitats."
    accessed: "2026-08-07"
~~~

La confiança no és una probabilitat matemàtica. És una etiqueta de treball que indica fins a quin punt la relació està ben sustentada i revisada.

## Flux per crear o ampliar una wiki amb graf

### 1. Conservar la font

Guardar l’article, paper, tutorial o documentació a '0. Raw/'. Registrar-ne l’origen i evitar que una URL sigui l’única còpia del coneixement.

### 2. Identificar nodes

Extreure autors, conceptes, models, tècniques, fonts i aplicacions. Comparar-los amb les fitxes existents abans de crear-ne cap de nova.

### 3. Normalitzar identitats

Unificar variants com «large language model», «LLM» i «model de llenguatge de gran escala» quan designin la mateixa entitat. No fusionar termes que només siguin semblants.

### 4. Proposar relacions

Per a cada relació, especificar origen, tipus, destinació, font i confiança. Les relacions inferides han de quedar marcades com a inferides.

### 5. Revisar les arestes

Comprovar que la relació té sentit en tots dos sentits. Si A 'utilitza' B, això no implica automàticament que B 'utilitza' A. Crear la relació inversa només si és útil i correcta.

### 6. Actualitzar fitxes i índex

Afegir els wikilinks necessaris, actualitzar 'index.md', 'log.md', 'hot.md' i '.manifest.json' quan el canvi sigui significatiu.

### 7. Validar

Executar 'python scripts/wiki_lint.py' i fer una revisió humana de relacions, fonts, duplicats i enllaços.

## Com pot ajudar un agent?

Un agent pot assistir en cinc funcions:

| Funció | Pregunta que resol |
|---|---|
| Descobriment | Quins nodes nous apareixen a la font? |
| Normalització | Aquest node ja existeix amb un altre nom? |
| Proposta | Quines relacions sembla que hi ha? |
| Verificació | Quina font sustenta cada relació? |
| Manteniment | Quines arestes o fitxes han quedat obsoletes? |

L’agent no hauria d’escriure directament una relació inferida com si fos un fet. La sortida recomanada és una proposta revisable:

~~~yaml
- source: "[[GraphRAG]]"
  relation: "amplia"
  target: "[[RAG]]"
  evidence:
    - "https://microsoft.github.io/graphrag/"
  claim_type: "documented"
  confidence: "high"
  action: "accept"
~~~

Per a una relació dubtosa:

~~~yaml
- source: "[[G-Retriever]]"
  relation: "és_un"
  target: "[[GraphRAG]]"
  claim_type: "inferred"
  confidence: "low"
  action: "review"
  reason: "Comparteixen recuperació sobre grafs, però no són necessàriament la mateixa família metodològica."
~~~

## Plantilla d’assistència

Quan es demani a un agent que ampliï una wiki amb grafs, la instrucció hauria d’incloure:

~~~text
1. Llegeix AGENTS.md i les fitxes conceptuals relacionades.
2. Conserva la font a 0. Raw/.
3. Identifica nodes nous i nodes ja existents.
4. Proposa relacions tipades, dirigides i amb fonts.
5. Separa fets, inferències, connexions pedagògiques i dubtes.
6. No creïs fitxes duplicades.
7. Actualitza wikilinks, índex, registre i manifest.
8. Executa wiki_lint i informa dels advertiments.
9. No modifiquis main.
~~~

La resposta de l’agent ha d’indicar:

- fitxers creats o actualitzats;
- nodes identificats;
- relacions acceptades;
- relacions pendents de revisió;
- fonts utilitzades;
- errors i advertiments de validació.

## Criteris de qualitat

Una wiki amb grafs és més robusta quan:

- cada node té una identitat clara;
- les relacions tenen un vocabulari controlat;
- les arestes tenen direcció quan correspon;
- les fonts es poden rastrejar;
- les inferències estan etiquetades;
- els wikilinks apunten a fitxers reals;
- no hi ha duplicats semàntics evidents;
- la xarxa ajuda a respondre preguntes, no només a generar molts enllaços;
- les relacions antigues es poden revisar quan canvien les fonts.

La densitat de connexions no és una mètrica suficient. Una xarxa petita amb relacions precises és més útil que una xarxa gran plena d’enllaços genèrics.

## Consultes i aplicacions

Amb una estructura gràfica mínima es poden construir consultes com:

- quins models utilitzen atenció?;
- quins conceptes expliquen GraphRAG?;
- quines fonts sustenten una relació?;
- quins nodes no tenen fonts?;
- quins conceptes tenen moltes connexions però cap fitxa pròpia?;
- quines relacions estan pendents de verificació?;
- quin camí connecta RAG amb GraphRAG i G-Retriever?

Aquestes consultes es poden implementar inicialment amb Dataview, scripts senzills o cerques de wikilinks. La migració a una base de dades de grafs només és necessària quan la mida o la complexitat ho justifiquin.

## Quan cal GraphRAG?

Una wiki no necessita GraphRAG només perquè contingui molts wikilinks. GraphRAG pot ser útil quan:

- el corpus és prou gran per fer difícil la navegació manual;
- les preguntes requereixen seguir diverses relacions;
- les preguntes globals depenen de comunitats o temes;
- es necessita recuperar context estructurat i fonts;
- la qualitat de la recuperació vectorial és insuficient;
- existeix una política d’avaluació i actualització del graf.

Abans d’implementar-lo, cal disposar d’un conjunt de preguntes de prova, respostes esperades, fonts de referència i mètriques de qualitat. Un graf mal normalitzat pot fer més costosa la recuperació sense millorar-ne la precisió.

## Auditoria específica del graf

A més de 'wiki_lint', una auditoria gràfica hauria de revisar:

| Comprovació | Pregunta |
|---|---|
| Nodes orfes | Hi ha fitxes sense cap relació útil? |
| Arestes trencades | Totes les destinacions existeixen? |
| Relacions vagues | Es pot substituir 'relacionat_amb' per un tipus precís? |
| Direcció | La relació es llegeix correctament? |
| Procedència | Hi ha una font o justificació? |
| Duplicats | Dues fitxes descriuen el mateix node? |
| Components aïllats | Hi ha grups sense connexió amb la resta? |
| Relacions pendents | Quines connexions requereixen revisió humana? |
| Evolució | La data o la versió de la font encara és vigent? |

Aquestes comprovacions ajuden a decidir si el problema és de contingut, de model de dades o de recuperació.

## Errors habituals

- confondre molts wikilinks amb un graf semàntic;
- crear una relació per a cada coaparició de termes;
- utilitzar noms diferents per al mateix node;
- inferir causalitat perquè dues idees apareixen juntes;
- ignorar la direcció de les relacions;
- barrejar fonts, conceptes, models i aplicacions dins la mateixa categoria;
- convertir una connexió pedagògica en una afirmació científica;
- afegir una infraestructura GraphRAG abans de definir preguntes i criteris d’avaluació;
- deixar que l’agent actualitzi relacions sense una sortida revisable;
- oblidar la procedència i la data de les afirmacions.

## Resultat esperat

El resultat no és només una visualització atractiva. És una wiki en què:

1. les fitxes expliquen el coneixement;
2. les relacions expliquen l’estructura;
3. les fonts expliquen l’origen;
4. la confiança explica el grau de certesa;
5. l’agent ajuda a descobrir i mantenir connexions;
6. l’usuari conserva el control sobre les decisions semàntiques.

Aquesta base permet evolucionar gradualment des d’una wiki connectada cap a un graf consultable i, només quan sigui justificat, cap a un sistema GraphRAG.
