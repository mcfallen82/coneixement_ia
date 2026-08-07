# 1.2. Conceptes

Aquesta carpeta conté les fitxes permanents sobre les idees, tècniques i processos que cal entendre per estudiar intel·ligència artificial, aprenentatge automàtic, aprenentatge profund, models de llenguatge i sistemes de coneixement.

Les fitxes expliquen els conceptes amb una orientació progressiva: parteixen de la intuïció, incorporen el funcionament essencial i acaben connectant-lo amb models, eines o aplicacions pràctiques.

## Mapa actual de coneixement

La carpeta s’organitza en famílies relacionades. Les fronteres són orientatives: un concepte pot pertànyer a més d’un recorregut.

### 1. Fonaments de l’aprenentatge automàtic

Inclou les idees necessàries per entendre com aprenen els models:

- aprenentatge automàtic i aprenentatge profund;
- xarxes neuronals, paràmetres i arquitectura;
- funcions de pèrdua, gradient i retropropagació;
- ajustament fi i alineament dels models;
- tokenització, embeddings i representacions numèriques.

Aquest bloc explica el pas des de les dades i els paràmetres fins a un model capaç de generalitzar.

### 2. Models de llenguatge i generació

Aquest recorregut ajuda a entendre com els models processen i generen llenguatge:

- models de llenguatge grans (LLM);
- Transformers i mecanismes d’atenció;
- prompting i enginyeria de prompts;
- context i enginyeria del context;
- raonament numèric i tractament de documents.

El punt clau és distingir què aprèn el model durant l’entrenament, què rep en el context i què pot fer gràcies a eines externes.

### 3. Recuperació i ampliació del coneixement

Aquest bloc tracta els sistemes que connecten un model amb informació externa:

- RAG i recuperació augmentada;
- GraphRAG;
- grafs aplicats als models de llenguatge;
- Graph of Thoughts;
- ontologies i relacions semàntiques;
- xarxes neuronals de graf.

La pregunta central és com recuperar informació rellevant i conservar les relacions entre les idees, en lloc de limitar-se a cercar fragments aïllats.

### 4. Agents i estructures de suport

Aquesta família estudia què envolta el model perquè pugui completar tasques:

- agents i fluxos de treball;
- skills com a procediments reutilitzables;
- scaffold o agent harness;
- eines, memòria, estat i delegació;
- guardrails, validació i intervenció humana;
- avaluació del sistema complet.

El concepte de scaffold és especialment important: un agent no és només el model, sinó la combinació entre model, instruccions, context, eines, estat i controls.

### 5. Coneixement personal i organització de la informació

Aquest recorregut connecta la IA amb la construcció d’un sistema d’aprenentatge:

- gestió del coneixement personal (PKM);
- segon cervell;
- Zettelkasten;
- wikis assistides per LLM;
- connexions entre notes, fonts, conceptes i models;
- graf de coneixement i procedència.

Aquest és el bloc que relaciona l’aprenentatge conceptual amb la pràctica d’ia_knowledge.

## Com consultar les fitxes

La llista canònica es genera amb Dataview a l’índex de la wiki:

- [Índex general de la wiki](../../index.md)
- [Dashboard del graf](../../3.%20Dashboards/graf.md)
- [Skill de la capa gràfica](../../2.%20Skills/graph-layer.md)
- [Plantilla de concepte](../../4.%20Templates/90.1.%20templates_fitxes/plantilla_concepte.md)

A Obsidian, la consulta següent mostra les fitxes ordenades per actualització:

~~~dataview
TABLE title, tags, status, length(sources) AS fonts, updated
FROM "1. Wiki/1.2. conceptes"
WHERE file.name != "README"
SORT updated DESC
~~~

La consulta és deliberadament dinàmica. Quan es crea una fitxa vàlida, apareix automàticament sense haver de modificar manualment aquesta pàgina.

## Contracte mínim d’una fitxa

Cada fitxa permanent ha de contenir:

~~~yaml
---
title: Nom del concepte
category: conceptes
node_id: "concept:nom_estable"
node_type: concept
tags: []
sources: []
related_concepts: []
related_models: []
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
~~~

El contingut hauria d’incloure, quan sigui rellevant:

1. definició;
2. importància;
3. intuïció;
4. funcionament;
5. exemple;
6. aplicacions;
7. limitacions i errors habituals;
8. relacions;
9. fonts.

La profunditat depèn del concepte. Una fitxa introductòria pot ser breu; una fitxa fonamental —com LLM, RAG, Transformer, embeddings o context_engineering— ha d’explicar també les connexions i els límits.

## Relacions i capa gràfica

Els wikilinks del text permeten navegar entre fitxes, però una connexió no tipada només és una relació candidata.

Les relacions semàntiques revisades es conserven al registre central de [graph/relations.json](../../graph/relations.json), amb:

- node d’origen i node de destinació;
- tipus de relació;
- procedència o evidència;
- confiança;
- estat de revisió.

Exemples de lectura:

- GraphRAG amplia RAG;
- scaffold utilitza context_engineering;
- scaffold és avaluat amb el sistema complet d’avaluació.

Aquesta separació evita convertir automàticament qualsevol wikilink en una afirmació factual.

## Flux per incorporar un concepte nou

Abans de crear una fitxa:

1. comprova si el concepte ja existeix amb un altre nom o sinònim;
2. identifica la font original i conserva-la a 0. Raw/;
3. decideix si cal crear una fitxa nova o ampliar-ne una d’existent;
4. assigna un node_id estable i node_type: concept;
5. relaciona el concepte amb fitxes existents;
6. afegeix les relacions tipades només quan estiguin justificades;
7. actualitza l’índex, el registre i el manifest si l’operació és significativa;
8. executa les comprovacions del repositori.

Comprova sempre les destinacions dels wikilinks i evita crear fitxes que només repeteixin una altra idea.

## Criteri pedagògic

Una bona fitxa ha de respondre, com a mínim, aquestes preguntes:

- Què és el concepte?
- Quin problema resol?
- Quina intuïció permet entendre’l?
- Com es relaciona amb els conceptes anteriors?
- Quin model o eina el posa en pràctica?
- Quines limitacions té?
- Com es podria aplicar a documents, finances o sistemes de coneixement?

La finalitat de la carpeta és construir un mapa d’idees reutilitzable, no acumular definicions independents.

## Validació

Des de l’arrel del repositori:

~~~bash
python scripts/wiki_lint.py
python scripts/graph_scan.py --check
~~~

Els errors de frontmatter, rutes, categories, nodes o relacions són bloquejants. Les advertències de normalització s’han de revisar progressivament segons les prioritats del projecte.

Per a les normes completes, consulta [AGENTS.md](../../AGENTS.md).
