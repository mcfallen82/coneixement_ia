# 🧠 ia_knowledge

## Una wiki personal per aprendre intel·ligència artificial

**ia_knowledge** és un projecte d’aprenentatge i organització del coneixement sobre intel·ligència artificial. L’objectiu és entendre millor com funcionen la IA, l’aprenentatge automàtic, el *deep learning*, els models de llenguatge i els sistemes de coneixement, i conservar aquest aprenentatge d’una manera ordenada i reutilitzable.

La idea és anar més enllà d’acumular enllaços o resums. Cada font es transforma progressivament en coneixement consultable: conceptes explicats amb claredat, fitxes de models, autors relacionats, fonts originals i connexions amb altres idees.

El projecte està pensat per treballar amb **Obsidian**, però els documents són fitxers Markdown normals i es poden consultar o editar amb qualsevol editor de text.

## 🎯 Què permet fer el projecte?

La wiki serveix per:

- entendre els fonaments de la IA moderna;
- estudiar models com els *Transformers*, GPT o FinBERT;
- aclarir conceptes com embeddings, atenció, RAG, retropropagació o tokenització;
- convertir articles, llibres, cursos, vídeos i papers en coneixement permanent;
- relacionar conceptes, models, autors i fonts;
- consultar ràpidament allò que ja s’ha estudiat;
- detectar fitxes incompletes, duplicades o mal connectades;
- aplicar la IA a documents, finances, anàlisi d’empreses i automatització.

La wiki també funciona com un laboratori personal. A mesura que s’hi incorporen noves fonts, el sistema ajuda a identificar què ja existeix, què cal ampliar i quines relacions encara falten.

## 🗂️ Com està organitzat?

El projecte segueix un recorregut senzill:

```text
Fonts originals
      ↓
Lectura i classificació
      ↓
Fitxes permanents
      ↓
Enllaços i relacions
      ↓
Consultes, dashboards i auditoria
```

### 📥 `0. Raw/` — material d’entrada

Aquesta carpeta conté les fonts originals o les seves transcripcions de treball: tutorials, lectures, taules, articles, notes i altres materials que encara s’han de processar completament.

És el punt de partida de qualsevol incorporació. Conservar aquest material permet saber d’on surt cada idea i tornar a consultar la font quan calgui.

El contingut de `Raw/` no és encara la wiki definitiva. És la matèria primera a partir de la qual es creen o s’actualitzen les fitxes permanents.

### 📚 `1. Wiki/` — coneixement permanent

Aquesta és la part central del projecte. Conté les fitxes estructurades que expliquen allò que s’ha après.

- **`1.1. autors/`** — persones, investigadors i divulgadors relacionats amb les fonts o els models.
- **`1.2. conceptes/`** — idees i principis com la gestió del coneixement, els models de llenguatge, l’enginyeria del context, RAG, els embeddings o el Zettelkasten.
- **`1.3. models/`** — arquitectures i models d’intel·ligència artificial, amb informació sobre el seu funcionament, entrenament, aplicacions i limitacions.

Cada fitxa utilitza *frontmatter* YAML per guardar informació estructurada, com ara el títol, la categoria, les fonts, l’estat i les dates de creació i actualització.

El contingut de les fitxes està pensat per ser entenedor i acumulatiu. Una fitxa no hauria de limitar-se a definir un terme: també hauria d’explicar per què és important, amb quins conceptes es relaciona i en quines situacions pràctiques es pot aplicar.

### ⚙️ `2. Skills/` — procediments de treball

Les *skills* descriuen com s’ha de treballar amb la wiki. Són les instruccions operatives que permeten convertir una col·lecció de documents en un sistema coherent.

Inclouen procediments per:

- ingerir noves fonts;
- crear o actualitzar fitxes;
- evitar duplicats;
- construir enllaços interns;
- mantenir una taxonomia d’etiquetes;
- consultar el coneixement existent;
- preparar context per a una tasca;
- sintetitzar informació;
- exportar o importar coneixement;
- reconstruir parts de la wiki;
- validar el projecte i mantenir-lo actualitzat.

Les skills també defineixen què s’ha de revisar abans de donar una tasca per acabada. Això ajuda a conservar les fonts, actualitzar els registres i evitar que el projecte creixi de manera desordenada.

### 📊 `3. Dashboards/` — visió general del sistema

Els *dashboards* són pàgines de consulta per a Obsidian. Permeten veure l’estat de la wiki sense haver de revisar fitxa per fitxa.

Poden mostrar, entre altres elements:

- fitxes actualitzades recentment;
- conceptes o models pendents de completar;
- fonts encara no processades;
- pàgines sense fonts;
- continguts relacionats amb un tema;
- possibles problemes d’estructura o de manteniment.

Aquesta carpeta converteix la wiki en un espai de treball actiu. No només serveix per llegir informació, sinó també per saber quin hauria de ser el pas següent.

### 🧩 `4. Templates/` — plantilles i documentació de suport

Aquesta carpeta conté les estructures reutilitzables del projecte.

Les plantilles ajuden a crear fitxes homogènies per a:

- conceptes;
- models;
- autors;
- fonts;
- resums i altres documents de suport.

També hi ha documentació general sobre el funcionament de la wiki, les rutes d’aprenentatge i els criteris que cal seguir per incorporar informació nova.

Una plantilla no pretén limitar l’explicació. Serveix com a punt de partida perquè les fitxes comparteixin una estructura mínima i siguin més fàcils de consultar.

### 🕸️ `graph/` — capa gràfica lleugera

La wiki conserva Markdown com a font principal i construeix una representació derivada dels nodes i les relacions. El registre `graph/relations.json` conté només les relacions tipades revisades; els wikilinks encara no classificats es marquen com a candidats. L’escàner permet comptar nodes, detectar enllaços trencats, trobar hubs i exportar una instantània JSON per a proves futures.

Aquesta capa és deliberadament petita: no introdueix cap base de dades ni GraphRAG. Consulta el [dashboard del graf](3.%20Dashboards/graf.md) i la [skill graph-layer](2.%20Skills/graph-layer.md) per començar.

### 🧪 `scripts/` — comprovacions automàtiques

El projecte inclou eines per revisar-ne l’estat tècnic. El validador principal comprova aspectes com:

- existència i validesa del *frontmatter* YAML;
- categories correctes;
- fitxes incompletes;
- camps antics;
- títols duplicats;
- enllaços interns;
- rutes inexistents;
- coherència del manifest.

L’auditoria diferencia entre errors bloquejants i advertiments de normalització. D’aquesta manera, es poden detectar problemes reals sense impedir l’evolució gradual de la wiki.

## 🔄 Com s’incorpora una font nova?

El flux recomanat és el següent:

1. **Identificar la font**: article, llibre, paper, curs, vídeo, documentació o nota personal.
2. **Guardar el material original** a `0. Raw/`.
3. **Classificar-lo** i registrar-ne l’origen i la data.
4. **Extreure’n els conceptes, models i autors** importants.
5. **Comprovar si ja existeixen fitxes relacionades**.
6. **Crear fitxes noves o actualitzar-ne d’existents**.
7. **Afegir fonts i enllaços interns**.
8. **Actualitzar l’índex, el registre i el manifest**.
9. **Executar l’auditoria** per detectar errors.

La regla més important és mantenir la traçabilitat: qualsevol idea rellevant hauria de poder relacionar-se amb la font que l’ha originada.

## 🔗 Una xarxa d’idees, no un arxiu de documents

El valor del projecte apareix quan les fitxes es connecten entre si.

Un model pot estar relacionat amb diversos conceptes. Un concepte pot explicar el funcionament de diversos models. Un autor pot haver creat una font que introdueix una idea i una altra que la desenvolupa.

Per exemple:

```text
Transformer
├── utilitza → atenció
├── necessita → embeddings
├── es relaciona amb → models de llenguatge
└── dona lloc a → GPT
```

Aquestes connexions permeten navegar pel coneixement i entendre no només què és una idea, sinó també d’on prové, què explica i quines conseqüències té.

## ✅ Governança i manteniment

Les regles generals del projecte es troben a [`AGENTS.md`](AGENTS.md). Aquest document defineix:

- com s’han de processar les fonts;
- quina estructura han de tenir les fitxes;
- com s’han de mantenir els enllaços;
- quins registres s’han d’actualitzar;
- quines comprovacions són obligatòries abans d’acabar una tasca.

Els canvis importants també s’han de reflectir a:

- [`log.md`](log.md), que resumeix l’evolució del projecte;
- [`.manifest.json`](.manifest.json), que relaciona les fonts amb les fitxes creades o actualitzades;
- les skills i plantilles corresponents, quan el nou coneixement modifica el funcionament general de la wiki.

## 🚀 Com començar?

Si és la primera vegada que visites el projecte, aquest és un bon ordre:

1. Llegeix [`AGENTS.md`](AGENTS.md) per entendre les regles generals.
2. Consulta els README de les carpetes principals.
3. Revisa algunes fitxes de `1. Wiki/` per veure’n l’estructura.
4. Explora els dashboards per conèixer l’estat actual.
5. Consulta `2. Skills/` abans d’incorporar una font nova.
6. Utilitza el validador després de fer canvis.

El projecte està pensat per créixer a poc a poc. És preferible incorporar una font, entendre-la bé, connectar-la amb el coneixement existent i deixar-la ben documentada que acumular molts materials sense processar.

## 🌱 Objectiu a llarg termini

**ia_knowledge** vol convertir-se en un sistema personal d’aprenentatge sobre IA: una combinació de biblioteca, mapa d’idees, quadern de notes i entorn de treball.

L’objectiu final és construir criteri. Això significa poder llegir una font nova, situar-la dins del mapa de coneixement, entendre quins problemes resol, comparar-la amb altres enfocaments i aplicar-la a projectes reals.

La wiki no és un catàleg tancat. És un sistema viu que es va fent més útil cada vegada que una nova idea queda ben explicada, ben connectada i fàcil de recuperar.
