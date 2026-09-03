# 🧠 coneixement_ia

## Wiki oberta per aprendre i organitzar coneixement sobre intel·ligència artificial

**coneixement_ia** és un projecte obert d’aprenentatge i organització del coneixement sobre intel·ligència artificial. L’objectiu és entendre millor com funcionen la IA, l’aprenentatge automàtic, el *deep learning*, els models de llenguatge i els sistemes de coneixement, i convertir aquest aprenentatge en una wiki clara, connectada i reutilitzable.

El projecte està pensat per a persones que volen **aprendre IA amb criteri**, consultar conceptes de manera ràpida i contribuir a una base de coneixement compartida. El contingut principal és Markdown estàndard i es pot llegir o editar amb qualsevol editor compatible.

> **Vols contribuir?** Les correccions, ampliacions, noves fitxes, fonts i millores són benvingudes. Consulta [`CONTRIBUTING.md`](CONTRIBUTING.md) i proposa els canvis mitjançant un Pull Request.

---

## 🎯 Què trobaràs aquí?

La wiki serveix per:

- entendre els fonaments de la IA moderna;
- estudiar models com Transformers, GPT o FinBERT;
- aclarir conceptes com embeddings, atenció, RAG, retropropagació o tokenització;
- convertir articles, llibres, cursos, vídeos, papers i documentació oficial en coneixement permanent;
- relacionar conceptes, models, autors i fonts;
- consultar ràpidament allò que ja s’ha estudiat;
- aplicar IA a documents, finances, anàlisi d’empreses, automatització i sistemes de coneixement.

La idea central és senzilla: **no acumular documents, sinó transformar fonts en coneixement explicat, verificable i connectat**.

## 🚀 Per on començar?

Si és la primera vegada que visites el projecte:

1. Explora [`1. Wiki/`](1.%20Wiki/) per consultar conceptes, models, autors i altres fitxes permanents.
2. Revisa [`index.md`](index.md) per tenir una visió general del contingut disponible.
3. Consulta [`2. Skills/`](2.%20Skills/) si vols entendre com s’investiga, s’incorpora i es valida coneixement.
4. Mira [`3. Dashboards/`](3.%20Dashboards/) per veure l’estat i les connexions de la wiki.
5. Si vols contribuir, llegeix [`CONTRIBUTING.md`](CONTRIBUTING.md) i [`AGENTS.md`](AGENTS.md).

No cal utilitzar Obsidian ni cap eina concreta: el repositori defineix el contingut, l’estructura Markdown i les regles compartides; les configuracions personals dels editors queden fora del projecte públic.

## 🗂️ Com està organitzat?

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

### 📚 `1. Wiki/` — coneixement permanent

És el nucli del projecte. Conté fitxes estructurades de conceptes, models, autors, llibres i altres peces de coneixement. Les fitxes utilitzen frontmatter YAML per conservar metadades i fonts verificables.

### ⚙️ `2. Skills/` — procediments de treball

Descriu com investigar, ingerir, actualitzar, relacionar i validar coneixement. Aquestes instruccions ajuden a mantenir criteris comuns quan la wiki creix.

### 📊 `3. Dashboards/` — visió general

Pàgines de consulta i seguiment que permeten detectar contingut recent, fitxes incompletes, fonts, relacions i altres elements útils per mantenir el sistema.

### 🧩 `4. Templates/` — plantilles i documentació de suport

Estructures reutilitzables per crear fitxes homogènies i documentar els processos del projecte.

### 🕸️ `graph/` — capa gràfica lleugera

Representació derivada dels nodes i relacions de la wiki a partir del Markdown.

### 🧪 `scripts/` — validacions automàtiques

Eines per revisar frontmatter, categories, enllaços interns, rutes, manifest, duplicats i coherència estructural.

## 🔗 Fonts i traçabilitat

Les fonts originals no s’emmagatzemen al repositori públic. La traçabilitat es conserva mitjançant URLs, referències bibliogràfiques i camps com `sources` al frontmatter.

Quan una font és un article, paper, llibre, vídeo, repositori o documentació oficial, s’enllaça a l’origen sempre que sigui possible. Les notes privades de treball, còpies locals de materials i configuracions personals d’editors no formen part del repositori.

La regla principal és que **qualsevol afirmació rellevant hauria de poder remetre a una font externa verificable**.

## 🔄 Com s’incorpora coneixement nou?

El flux habitual és:

1. Identificar una font externa verificable.
2. Registrar-ne títol, autor o organisme, URL, data i tipus de font.
3. Extreure’n els conceptes, models i autors rellevants.
4. Comprovar si ja existeixen fitxes relacionades.
5. Crear fitxes noves o actualitzar-ne d’existents.
6. Afegir fonts i relacions internes.
7. Actualitzar els registres del projecte quan correspongui.
8. Executar les validacions abans de donar el canvi per acabat.

## 🤝 Com contribuir

Les contribucions són benvingudes. Pots ajudar, per exemple, amb:

- noves fitxes de conceptes o models;
- ampliacions i millores de contingut existent;
- correccions d’errors;
- incorporació de noves fonts verificables;
- millores de wikilinks i relacions;
- millores de skills, plantilles o scripts.

### Procés de contribució

1. Fes un **fork** del repositori.
2. Crea una branca per al canvi.
3. Fes les modificacions seguint les convencions del projecte.
4. Revisa que les fonts, el YAML i els wikilinks siguin correctes.
5. Obre un **Pull Request** cap a `main`.
6. El mantenidor revisarà la proposta i pot demanar ajustos abans d’aprovar-la.

Tota contribució ha de passar per Pull Request i revisió humana abans d’incorporar-se a `main`. La plantilla de Pull Request t’ajudarà a comprovar els punts principals abans d’enviar el canvi.

Per als criteris complets, consulta:

- [`CONTRIBUTING.md`](CONTRIBUTING.md) — què s’accepta i com contribuir;
- [`AGENTS.md`](AGENTS.md) — regles operatives i estructurals del projecte;
- [`LICENSE`](LICENSE) — condicions d’ús, reutilització i contribució.

Si detectes un error però encara no tens una solució preparada, també pots obrir una **Issue** explicant el problema o proposant una millora.

## 🔗 Una xarxa d’idees, no un arxiu de documents

El valor del projecte apareix quan les fitxes es connecten entre si. Un concepte pot explicar diversos models, un autor pot estar relacionat amb diferents fonts i una mateixa idea pot tenir aplicacions en contextos diferents.

Per exemple:

```text
Transformer
├── utilitza → atenció
├── necessita → embeddings
├── es relaciona amb → models de llenguatge
└── dona lloc a → GPT
```

L’objectiu és que la wiki ajudi a entendre **què és una idea, d’on prové, amb què es relaciona i quan resulta útil**.

## ✅ Governança

Les regles generals del projecte es troben a [`AGENTS.md`](AGENTS.md). Les contribucions externes es regeixen per [`CONTRIBUTING.md`](CONTRIBUTING.md) i pel procés de revisió del repositori.

Els canvis significatius també s’han de reflectir a [`log.md`](log.md), [`.manifest.json`](.manifest.json) i, quan correspongui, a les skills i plantilles afectades.

## 📜 Llicència

El projecte utilitza una llicència dual:

- contingut original de coneixement i documentació: **CC0 1.0**;
- codi original: **MIT**.

Els materials de tercers mantenen els seus drets i llicències originals. Consulta [`LICENSE`](LICENSE) per als detalls.

## 🌱 Objectiu a llarg termini

**coneixement_ia** vol convertir-se en una base de coneixement oberta i útil per aprendre IA de manera progressiva, connectar idees i aplicar-les a problemes reals.

El projecte no pretén ser una enciclopèdia exhaustiva. Prioritza contingut **clar, verificable, connectat i pràctic**, i vol millorar a mesura que noves fonts, correccions i contribucions aporten més criteri al conjunt.

**Si trobes una fitxa que pots millorar, una font que falta o una connexió que val la pena afegir, la contribució és benvinguda.**
