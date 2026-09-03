# 🧠 ia_knowledge

## Una wiki oberta per aprendre intel·ligència artificial

**ia_knowledge** és un projecte d’aprenentatge i organització del coneixement sobre intel·ligència artificial. L’objectiu és entendre millor com funcionen la IA, l’aprenentatge automàtic, el *deep learning*, els models de llenguatge i els sistemes de coneixement, i conservar aquest aprenentatge d’una manera ordenada i reutilitzable.

El projecte utilitza **Markdown estàndard** com a format principal. Els documents es poden consultar i editar amb qualsevol editor de text, editor Markdown, IDE o eina de gestió del coneixement compatible.

La configuració personal dels editors i de les eines locals no forma part del repositori públic.

## 🎯 Què permet fer el projecte?

La wiki serveix per:

- entendre els fonaments de la IA moderna;
- estudiar models com Transformers, GPT o FinBERT;
- aclarir conceptes com embeddings, atenció, RAG, retropropagació o tokenització;
- convertir articles, llibres, cursos, vídeos, papers i documentació oficial en coneixement permanent;
- relacionar conceptes, models, autors i fonts;
- consultar ràpidament allò que ja s’ha estudiat;
- aplicar la IA a documents, finances, anàlisi d’empreses i automatització.

## 🗂️ Organització

```text
Fonts externes verificables
      ↓
Lectura i classificació
      ↓
Fitxes permanents
      ↓
Enllaços i relacions
      ↓
Consultes, dashboards i auditoria
```

### 🔗 Fonts externes

Les fonts originals no s’emmagatzemen al repositori públic. La traçabilitat es conserva mitjançant URLs, referències bibliogràfiques i el camp `sources` del frontmatter de cada fitxa.

Quan una font és un article, paper, llibre, vídeo, repositori o documentació oficial, s’ha d’enllaçar a l’origen sempre que sigui possible. Les notes de treball privades o còpies locals de materials no formen part del repositori públic.

### 📚 `1. Wiki/` — coneixement permanent

Conté les fitxes estructurades d’autors, conceptes, models i llibres. Cada fitxa utilitza frontmatter YAML per guardar informació estructurada, incloses les fonts verificables.

### ⚙️ `2. Skills/` — procediments de treball

Descriu com investigar, ingerir, actualitzar, relacionar i validar coneixement. Els procediments han de treballar amb fonts externes i no han de requerir carpetes locals privades ni configuracions específiques d’un editor.

### 📊 `3. Dashboards/` — visió general

Pàgines Markdown de consulta i seguiment de la wiki, dissenyades per continuar sent útils sense dependre d’un programa concret.

### 🧩 `4. Templates/` — plantilles i documentació de suport

Estructures reutilitzables per crear fitxes homogènies i documentar els processos.

### 🕸️ `graph/` — capa gràfica lleugera

Representació derivada de nodes i relacions a partir del Markdown de la wiki.

### 🧪 `scripts/` — comprovacions automàtiques

Eines per revisar frontmatter, categories, enllaços interns, rutes, manifest, duplicats i coherència estructural.

## 🔄 Com s’incorpora una font nova?

1. **Identificar la font externa**: article, llibre, paper, curs, vídeo, documentació, repositori o altra font verificable.
2. **Registrar-ne la referència**: títol, autor o organisme, URL, data i tipus de font.
3. **Extreure’n els conceptes, models i autors** importants.
4. **Comprovar si ja existeixen fitxes relacionades**.
5. **Crear fitxes noves o actualitzar-ne d’existents**.
6. **Afegir les fonts externes al frontmatter i al cos de la fitxa quan sigui útil**.
7. **Actualitzar l’índex, el registre i el manifest** quan el canvi sigui significatiu.
8. **Executar l’auditoria** per detectar errors.

La regla principal és mantenir la traçabilitat: qualsevol afirmació rellevant hauria de poder remetre a una font externa verificable.

## 🔗 Una xarxa d’idees, no un arxiu de documents

El valor del projecte apareix quan les fitxes es connecten entre si. La wiki compila coneixement i en conserva la procedència, però evita convertir el repositori en un magatzem de còpies de fonts o configuracions personals.

## 🧰 Eines locals

Cada persona pot utilitzar l’editor, IDE o gestor de coneixement que prefereixi. Aquestes eines són una capa local i substituïble: **el repositori només defineix el contingut, l’estructura Markdown i les regles compartides del projecte**.

Les carpetes de configuració específiques d’un programa s’han de mantenir fora del control de versions.

## ✅ Governança i manteniment

Les regles generals es troben a [`AGENTS.md`](AGENTS.md). Els canvis importants també s’han de reflectir a [`log.md`](log.md), [`.manifest.json`](.manifest.json) i, quan correspongui, a les skills i plantilles.

## 🚀 Com començar?

1. Llegeix [`AGENTS.md`](AGENTS.md).
2. Revisa algunes fitxes de `1. Wiki/`.
3. Explora els dashboards.
4. Consulta `2. Skills/` abans d’incorporar coneixement nou.
5. Utilitza el validador després de fer canvis.

## 🌱 Objectiu a llarg termini

**ia_knowledge** vol convertir-se en un sistema obert d’aprenentatge sobre IA: una combinació de biblioteca de referències, mapa d’idees, wiki i entorn de treball. L’objectiu final és construir criteri i fer que cada idea quedi ben explicada, connectada i vinculada a fonts verificables.