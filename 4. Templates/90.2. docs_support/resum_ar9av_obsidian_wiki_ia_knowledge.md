# Ar9av/obsidian-wiki aplicat a una wiki d’aprenentatge d’IA

> **Document canònic i consolidat.** Aquesta versió integra les idees generalitzables dels documents anteriors i substitueix qualsevol adaptació específica a un projecte concret.

## Objectiu

Aquest document explica com traslladar a una wiki d’aprenentatge d’intel·ligència artificial les idees de **Karpathy** i **Ar9av/obsidian-wiki**.

La proposta combina:

- fonts originals conservades localment;
- síntesis en Markdown;
- fitxes de conceptes, autors i models;
- instruccions persistents per a l’agent;
- skills per repetir tasques;
- índex, registre i manifest per mantenir la coherència;
- revisió humana amb Obsidian i control de versions amb Git.

La wiki es converteix així en una memòria d’aprenentatge acumulativa, revisable i navegable.

## 1. De la idea de Karpathy a una implementació operativa

La idea general pot representar-se així:

```text
Font d’aprenentatge
      ↓
Lectura i classificació
      ↓
Extracció de conceptes, autors, models i afirmacions
      ↓
Comparació amb fitxes existents
      ↓
Creació o actualització de la wiki
      ↓
Enllaços, índex, registre i manifest
```

La diferència respecte d’un RAG convencional és que la wiki conserva una síntesi persistent. La informació útil no es genera de nou en cada consulta, sinó que queda transformada en pàgines que es poden revisar i ampliar.

```text
RAG convencional:
pregunta → recuperació de fragments → resposta

Wiki mantinguda amb agent:
font → lectura → síntesi → pàgina persistent → actualització futura
```

Això no elimina la necessitat de consultar les fonts originals. La font continua sent l’origen de verificació; la wiki n’organitza i n’acumula el coneixement.

## 2. Què aporta Ar9av/obsidian-wiki

Ar9av converteix la idea d’una wiki mantinguda per un model de llenguatge en un sistema de treball concret, amb fitxers, processos i controls.

La diferència principal és:

```text
Karpathy = patró mental i arquitectònic
Ar9av    = implementació operativa amb fitxers, agents i procediments
```

Els components més útils són:

| Component | Funció |
|---|---|
| `AGENTS.md` | Defineix les normes que l’agent ha de seguir |
| Skills | Converteixen tasques repetitives en procediments reutilitzables |
| `index.md` | Ofereix un mapa de navegació |
| `log.md` | Conserva la memòria dels canvis importants |
| `.manifest.json` | Registra les fonts processades i evita repeticions |
| Wikilinks | Connecten fitxes i faciliten la navegació humana |
| Git | Permet revisar, comparar i recuperar canvis |
| Validació | Detecta enllaços trencats, duplicats i incoherències |

Aquests components no tenen tots el mateix nivell d’importància. La base és una bona estructura de fitxes i fonts; el manifest, les validacions i els taulers només aporten valor quan la wiki ha crescut prou.

## 3. Paper de cada eina

```text
Obsidian  = llegir, navegar, revisar i pensar
Agent     = transformar fonts i mantenir fitxers
AGENTS.md = criteri estable de treball
Skills    = procediments repetibles
Git       = historial i auditoria
```

Obsidian és la interfície de lectura i revisió. L’agent pot crear i actualitzar fitxers, però les decisions semàntiques importants —què és un concepte, què és una interpretació i què mereix una pàgina pròpia— han de continuar sent revisables per l’usuari.

## 4. El paper de les skills

Una skill no és una pregunta puntual ni un simple prompt. És un procediment reutilitzable que especifica:

- quan s’ha d’utilitzar;
- quins fitxers ha de llegir;
- quins passos ha de seguir;
- quins fitxers pot modificar;
- quina sortida ha de generar;
- quins controls ha d’executar.

Per a una wiki d’aprenentatge d’IA, les skills bàsiques poden ser:

| Skill | Funció |
|---|---|
| Ingesta | Convertir una font nova en fitxes i notes |
| Actualització | Integrar informació nova en una pàgina existent |
| Enllaçat | Afegir connexions internes amb criteri |
| Revisió | Detectar duplicats, contradiccions i enllaços trencats |
| Consulta | Respondre a partir del coneixement ja acumulat |
| Síntesi | Connectar idees de diverses fonts |

El principi de deduplicació és essencial:

> Abans de crear una fitxa nova, cal comprovar si el concepte ja existeix amb un altre nom o en una pàgina relacionada.

Si el concepte ja existeix, s’ha d’actualitzar la fitxa i afegir-hi la nova font. Només cal crear una pàgina nova quan hi hagi una unitat de coneixement clarament diferenciada.

## 5. Arquitectura mínima de la wiki

La plantilla general de referència és [`plantilla_wiki_neutra_replicable`](./plantilla_wiki_neutra_replicable).

La seva arquitectura conceptual és:

```text
_raw/       → fonts originals
sources/    → fitxes de fonts
notes/      → idees desenvolupades
concepts/   → conceptes reutilitzables
outputs/    → síntesis, informes i resultats
skills/     → procediments de treball
index.md    → mapa de la wiki
log.md      → registre de canvis
AGENTS.md   → instruccions de l’agent
```

En aquest repositori, aquesta arquitectura genèrica es concreta en les carpetes numerades del projecte. La documentació específica del repositori i el seu [`AGENTS.md`](../../AGENTS) tenen prioritat sobre qualsevol exemple genèric.

## 6. Flux d’ingesta d’una font

El flux recomanat és:

1. Guardar la font a `0. Raw/` o a la carpeta d’entrada definida pel projecte.
2. Identificar-ne el títol, autor, tipus, data i origen.
3. Llegir l’índex i les fitxes relacionades.
4. Comprovar si la font o el concepte ja s’havien processat.
5. Extreure conceptes, autors, models, afirmacions i qüestions obertes.
6. Separar informació documentada, interpretació i hipòtesi.
7. Crear o actualitzar les fitxes permanents.
8. Afegir fonts i wikilinks que aportin context real.
9. Actualitzar l’índex, el registre i el manifest quan correspongui.
10. Executar la validació disponible.
11. Fer una revisió humana abans de donar el canvi per tancat.

La sortida adequada no és necessàriament un resum llarg de la font. És el conjunt mínim de fitxes que permet conservar-ne el coneixement reutilitzable.

## 7. Com ha de treballar l’agent

L’agent ha d’actuar com un editor disciplinat:

- llegir primer `AGENTS.md`;
- consultar les fitxes existents abans de crear-ne;
- conservar les fonts originals sense modificar-les;
- no presentar inferències com a fets;
- indicar l’origen de les afirmacions importants;
- marcar contradiccions en lloc d’eliminar-les;
- proposar canvis amb una sortida revisable;
- informar dels fitxers creats, actualitzats i pendents;
- evitar canvis destructius sense autorització explícita.

Una ordre de treball adequada és:

```text
Llegeix AGENTS.md i les skills pertinents. Processa la font indicada,
comprova si ja existeixen fitxes equivalents, actualitza només el
coneixement necessari, revisa els enllaços i informa dels canvis.
No modifiquis les fonts originals.
```

## 8. Separar dades, interpretació i síntesi

Cada pàgina hauria de distingir tres nivells:

| Nivell | Significat |
|---|---|
| Dada documentada | Informació que apareix explícitament en una font |
| Interpretació | Lectura explicativa basada en una o més dades |
| Síntesi o hipòtesi | Connexió nova que cal revisar o contrastar |

Aquesta separació és especialment important en una wiki d’aprenentatge, perquè evita confondre el que diu un autor amb la interpretació que en fa l’agent o l’usuari.

## 9. Full de ruta

### Fase 1 — Wiki mínima

- Crear l’estructura bàsica.
- Definir `AGENTS.md`.
- Crear l’índex i el registre.
- Processar unes quantes fonts de prova.
- Revisar manualment les primeres fitxes.

### Fase 2 — Skills inicials

- Formalitzar la ingesta.
- Formalitzar l’actualització de notes.
- Definir criteris d’enllaçat.
- Crear una revisió de coherència.
- Definir el flux de consulta.

### Fase 3 — Traçabilitat

- Mantenir el manifest.
- Aplicar una convenció de noms.
- Registrar canvis rellevants.
- Relacionar cada fitxa amb les fonts corresponents.
- Fer revisions periòdiques de duplicats i contradiccions.

### Fase 4 — Especialització

- Afegir carpetes pròpies del domini.
- Crear plantilles específiques.
- Crear taulers o consultes.
- Connectar la wiki amb scripts o eines externes.
- Automatitzar només els processos que ja siguin estables.

No convé començar per una infraestructura complexa. Primer cal demostrar que les fitxes, les fonts i els processos generen valor real.

## 10. Resultat esperat

Una wiki d’aprenentatge ben dissenyada ha de permetre:

- recuperar què s’ha après i d’on prové;
- connectar conceptes relacionats;
- distingir fonts, explicacions i interpretacions;
- detectar buits i contradiccions;
- actualitzar coneixement sense crear duplicats;
- consultar el sistema sense començar sempre des de zero;
- conservar la revisió i el criteri de l’usuari.

La formulació resumida és:

```text
Fonts → fitxes de fonts → notes → conceptes → connexions → síntesi → revisió
```

L’objectiu no és acumular més documents, sinó construir una base de coneixement cada vegada més clara, traçable i reutilitzable.
