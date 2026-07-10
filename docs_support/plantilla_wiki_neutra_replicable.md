# Plantilla neutra per crear una wiki local amb Obsidian + agents

> Punt de partida replicable per construir una wiki markdown mantinguda amb ajuda d'un LLM, Codex IDE o qualsevol agent capaç de llegir i modificar fitxers.

---

## 1. Objectiu

Aquesta plantilla defineix una estructura mínima per crear una wiki local, viva i reutilitzable per a qualsevol projecte.

No està pensada per a un domini concret. Pot servir per a:

- recerca personal;
- estudis i lectures;
- projectes professionals;
- documentació interna;
- anàlisi d'empreses;
- cuina, viatges, història o qualsevol sistema de coneixement;
- seguiment de decisions, fonts i síntesis.

La idea central és convertir fonts disperses en coneixement persistent:

```text
Fonts brutes
   ↓
Lectura assistida per LLM
   ↓
Pàgines markdown estructurades
   ↓
Enllaços interns i índexs
   ↓
Consulta, revisió i actualització contínua
```

A diferència d'una conversa puntual amb un model, la wiki conserva el resultat del treball: síntesis, decisions, fonts, criteris, canvis i connexions.

---

## 2. Principi de disseny

La wiki ha de començar petita.

El risc habitual és voler crear massa carpetes, massa plantilles i massa processos abans de tenir ús real. Aquesta plantilla parteix d'una idea més pràctica:

```text
Crear només l'estructura necessària perquè el projecte pugui créixer sense perdre ordre.
```

Per tant, el sistema inicial ha de fer cinc coses bé:

1. Guardar fonts originals sense tocar-les.
2. Convertir fonts en notes útils.
3. Mantenir un índex navegable.
4. Registrar canvis importants.
5. Permetre que un agent segueixi instruccions estables.

---

## 3. Estructura inicial recomanada

```text
NomDelProjecte/
├── index.md
├── log.md
├── AGENTS.md
├── .manifest.json
├── _raw/
│   ├── documents/
│   ├── articles/
│   ├── notes/
│   └── converses/
├── notes/
│   ├── index_notes.md
│   └── exemple_nota.md
├── concepts/
│   ├── index_concepts.md
│   └── exemple_concepte.md
├── sources/
│   ├── index_sources.md
│   └── exemple_font.md
├── outputs/
│   ├── summaries/
│   ├── decisions/
│   └── reports/
├── skills/
│   ├── ingest.md
│   ├── update_note.md
│   ├── cross_link.md
│   ├── lint.md
│   └── query.md
└── templates/
    ├── template_note.md
    ├── template_concept.md
    ├── template_source.md
    └── template_decision.md
```

Aquesta estructura és deliberadament neutra. El nom de les carpetes es pot adaptar, però convé mantenir la funció de cada capa.

---

## 4. Funció de cada fitxer i carpeta

| Element | Funció |
|---|---|
| `index.md` | Porta d'entrada de la wiki. Ha de permetre entendre què hi ha i com navegar-hi. |
| `log.md` | Registre cronològic dels canvis rellevants. Dona traçabilitat. |
| `AGENTS.md` | Instruccions estables per a l'agent que manté la wiki. |
| `.manifest.json` | Registre tècnic de fonts processades. Evita duplicacions. |
| `_raw/` | Fonts originals sense modificar. |
| `notes/` | Notes elaborades a partir de fonts, idees o treball propi. |
| `concepts/` | Conceptes reutilitzables que poden aparèixer en moltes notes. |
| `sources/` | Fitxes de fonts: llibres, articles, vídeos, documents, webs o converses. |
| `outputs/` | Resultats finals: resums, informes, decisions, revisions o entregables. |
| `skills/` | Procediments reutilitzables per a l'agent. |
| `templates/` | Plantilles markdown per crear pàgines consistents. |

---

## 5. Fitxer `AGENTS.md`

El fitxer `AGENTS.md` és la constitució operativa de la wiki. Ha de dir a l'agent com ha de treballar.

### Contingut recomanat

```markdown
# Agent Instructions — Wiki del projecte

Aquest repositori és una wiki markdown mantinguda amb ajuda d'un agent.

## Objectiu

Transformar fonts brutes, notes i converses en coneixement persistent, navegable i verificable.

## Principis generals

- No modifiquis mai els fitxers dins `_raw/`, excepte si l'usuari ho demana explícitament.
- No dupliquis informació si ja existeix una nota adequada.
- Quan afegeixis informació nova, intenta connectar-la amb notes, conceptes o fonts existents.
- Separa clarament font, resum, interpretació i decisió.
- No inventis dades ni cites.
- Si una afirmació depèn d'una font concreta, indica'n l'origen.
- Si trobes contradiccions entre notes, marca-les en lloc d'esborrar-les.
- Actualitza `index.md` quan creïs una pàgina rellevant.
- Actualitza `log.md` quan facis canvis estructurals o afegeixis una font important.
- Mantén els noms de fitxer clars, breus i estables.

## Flux general d'ingesta

Quan processis una font nova:

1. Identifica el tipus de font.
2. Comprova si ja ha estat processada al `.manifest.json`.
3. Crea o actualitza una fitxa dins `sources/`.
4. Extreu les idees útils.
5. Crea o actualitza notes dins `notes/`.
6. Crea conceptes dins `concepts/` només si són reutilitzables.
7. Afegeix enllaços interns quan aportin context.
8. Actualitza `index.md` si cal.
9. Registra el canvi a `log.md`.
10. Actualitza `.manifest.json`.

## Estil de les notes

- Markdown clar.
- Paràgrafs breus.
- Títols `##` quan ajudin.
- Llistes només quan simplifiquin la lectura.
- Enllaços interns amb format `[[Nom de la nota]]`.
- Evita notes massa llargues; si una nota creix massa, divideix-la.

## Criteri de qualitat

Una bona nota ha de respondre:

- Quina idea conserva?
- D'on prové?
- Per què és útil?
- Amb què es connecta?
- Què podria canviar en el futur?
```

---

## 6. Fitxer `index.md`

L'índex ha de ser el mapa de la wiki, no un simple llistat infinit.

### Exemple base

```markdown
# Índex del projecte

## Objectiu de la wiki

Aquesta wiki recull fonts, notes, conceptes i resultats relacionats amb [tema general del projecte].

## Àrees principals

- [[index_notes]] — Notes elaborades
- [[index_concepts]] — Conceptes reutilitzables
- [[index_sources]] — Fonts processades
- [[log]] — Registre de canvis

## Notes destacades

- [[exemple_nota]]

## Conceptes destacats

- [[exemple_concepte]]

## Últimes actualitzacions

- YYYY-MM-DD — Breu descripció del canvi.
```

### Regla pràctica

L'índex no ha de contenir-ho tot. Ha de contenir allò que ajuda a orientar-se.

---

## 7. Fitxer `log.md`

El log dona memòria operativa. No cal registrar cada coma, però sí els canvis importants.

### Exemple base

```markdown
# Log del projecte

## YYYY-MM-DD

### Afegit

- S'ha creat l'estructura inicial de la wiki.
- S'han afegit les carpetes `_raw/`, `notes/`, `concepts/`, `sources/`, `outputs/`, `skills/` i `templates/`.

### Modificat

- S'ha actualitzat `index.md` amb les primeres seccions.

### Pendent

- Definir les primeres skills específiques del projecte.
```

### Quan s'ha d'actualitzar

Actualitza `log.md` quan:

- s'afegeixi una font important;
- es creï una nova secció de la wiki;
- es canviï una plantilla;
- es corregeixi una contradicció;
- es faci una síntesi rellevant;
- es modifiqui `AGENTS.md`.

---

## 8. Fitxer `.manifest.json`

El manifest és un registre tècnic. Serveix perquè l'agent no processi dues vegades la mateixa font.

### Exemple base

```json
{
  "project": "NomDelProjecte",
  "created": "YYYY-MM-DD",
  "last_updated": "YYYY-MM-DD",
  "sources": [
    {
      "id": "source-0001",
      "title": "Títol de la font",
      "type": "article | llibre | document | video | conversa | web | altre",
      "raw_path": "_raw/articles/titol_font.md",
      "processed_path": "sources/titol_font.md",
      "status": "pendent | processat | revisat",
      "date_added": "YYYY-MM-DD",
      "date_processed": "YYYY-MM-DD",
      "notes_created": [
        "notes/exemple_nota.md"
      ],
      "concepts_created": [
        "concepts/exemple_concepte.md"
      ],
      "checksum_or_url": "opcional"
    }
  ]
}
```

### Criteri mínim

Al principi pot ser molt simple. L'important és registrar:

- què s'ha processat;
- on era la font original;
- quina pàgina s'ha creat;
- quin estat té.

---

## 9. Carpeta `_raw/`

La carpeta `_raw/` conserva les fonts originals.

Regla d'or:

```text
_raw/ és arxiu, no és zona d'edició.
```

Exemples:

```text
_raw/documents/informe_original.pdf
_raw/articles/article_exportat.md
_raw/notes/notes_manuals.txt
_raw/converses/conversa_chatgpt.md
```

Les fonts brutes poden ser desordenades. La wiki elaborada no.

---

## 10. Carpeta `sources/`

Una fitxa de font explica què és una font i què se n'ha extret.

### `templates/template_source.md`

```markdown
---
tipus: font
titol:
autor:
data:
url:
estat: pendent | processat | revisat
tags: []
---

# [Títol de la font]

## Referència

- Autor:
- Data:
- Enllaç o ruta:
- Tipus de font:

## Idea central

Resum breu de la idea principal de la font.

## Punts útils

- Punt 1.
- Punt 2.
- Punt 3.

## Notes creades

- [[Nom de la nota]]

## Conceptes relacionats

- [[Nom del concepte]]

## Observacions

Comentaris sobre qualitat, límits o possibles usos de la font.
```

---

## 11. Carpeta `notes/`

Les notes són el cor de la wiki. Han de ser útils per pensar i reutilitzar.

### `templates/template_note.md`

```markdown
---
tipus: nota
estat: esborrany | revisada | estable
font:
creat: YYYY-MM-DD
actualitzat: YYYY-MM-DD
tags: []
---

# [Títol de la nota]

## Idea central

Explica en poques línies què conserva aquesta nota.

## Desenvolupament

Desenvolupa la idea amb paràgrafs breus.

## Evidència o origen

- Font principal: [[Nom de la font]]
- Fragment, pàgina, secció o referència concreta si existeix.

## Connexions

- [[Concepte relacionat]]
- [[Nota relacionada]]

## Lectura pràctica

Explica com es pot fer servir aquesta nota en el projecte.
```

### Criteri de bona nota

Una nota no és només un resum. És una unitat de coneixement reutilitzable.

---

## 12. Carpeta `concepts/`

Els conceptes són peces que apareixen en molts llocs.

Exemples genèrics:

- `cost_d_oportunitat.md`
- `feedback_loop.md`
- `avantatge_competitiu.md`
- `memoria_persistent.md`
- `sistema_de_decisio.md`

### `templates/template_concept.md`

```markdown
---
tipus: concepte
estat: esborrany | revisat | estable
creat: YYYY-MM-DD
actualitzat: YYYY-MM-DD
tags: []
---

# [Nom del concepte]

## Definició curta

Explicació breu del concepte.

## Intuïció

Explica-ho amb llenguatge planer.

## Exemple

Mostra un exemple concret.

## Relació amb altres conceptes

- [[Concepte A]]
- [[Concepte B]]

## Importància pràctica

Explica per què aquest concepte val la pena conservar.
```

---

## 13. Carpeta `outputs/`

Aquesta carpeta guarda resultats finals o semielaborats.

Pot contenir:

```text
outputs/summaries/
outputs/decisions/
outputs/reports/
```

### `templates/template_decision.md`

```markdown
---
tipus: decisio
estat: esborrany | presa | revisada
data: YYYY-MM-DD
tags: []
---

# [Decisió o revisió]

## Context

Quina situació motiva aquesta decisió?

## Opcions considerades

- Opció 1.
- Opció 2.
- Opció 3.

## Evidència utilitzada

- [[Font o nota 1]]
- [[Font o nota 2]]

## Decisió

Explica la decisió presa o la conclusió provisional.

## Riscos o dubtes

- Punt pendent.
- Incertesa.
- Condició que podria fer canviar la decisió.

## Revisió futura

Quan o sota quines condicions caldria revisar aquesta decisió?
```

---

## 14. Carpeta `skills/`

Les skills són procediments reutilitzables. No són notes de contingut; són instruccions operatives.

Una skill ha de respondre:

```text
Quan s'utilitza?
Quins fitxers ha de mirar?
Quins passos ha de seguir?
Quina sortida ha de generar?
Què ha d'actualitzar?
```

### 14.1. `skills/ingest.md`

```markdown
# Skill — Ingesta de fonts

## Quan utilitzar-la

Quan l'usuari afegeixi una font nova a `_raw/` i demani processar-la.

## Objectiu

Convertir una font bruta en una o més pàgines útils dins la wiki.

## Passos

1. Identifica el tipus de font.
2. Comprova si ja existeix al `.manifest.json`.
3. Llegeix la font sense modificar-la.
4. Crea una fitxa dins `sources/`.
5. Extreu les idees principals.
6. Crea notes dins `notes/` si hi ha idees reutilitzables.
7. Crea conceptes dins `concepts/` només si seran útils en altres contextos.
8. Afegeix enllaços interns.
9. Actualitza `index.md` si la font és important.
10. Actualitza `log.md`.
11. Actualitza `.manifest.json`.

## Sortida esperada

- Una fitxa de font.
- Una o més notes útils.
- Enllaços interns coherents.
- Registre al log.
```

### 14.2. `skills/update_note.md`

```markdown
# Skill — Actualització de nota

## Quan utilitzar-la

Quan una font nova ampliï, corregeixi o contradigui una nota existent.

## Objectiu

Mantenir una nota viva sense duplicar informació.

## Passos

1. Localitza la nota existent.
2. Identifica què aporta la informació nova.
3. Afegeix només allò que millori la nota.
4. Conserva contradiccions importants amb una secció específica.
5. Actualitza el camp `actualitzat` del YAML.
6. Afegeix connexions noves si cal.
7. Registra el canvi a `log.md` si és rellevant.

## Regla important

No substitueixis una nota antiga només perquè hi ha informació nova. Integra, compara i preserva la traçabilitat.
```

### 14.3. `skills/cross_link.md`

```markdown
# Skill — Enllaçat intern

## Quan utilitzar-la

Quan s'hagin creat o actualitzat diverses notes i calgui millorar la navegació.

## Objectiu

Connectar notes, fonts i conceptes sense crear soroll.

## Passos

1. Revisa els títols de `notes/`, `concepts/` i `sources/`.
2. Identifica mencions naturals a conceptes existents.
3. Afegeix enllaços `[[...]]` només quan aportin context real.
4. Evita enllaçar cada repetició d'una paraula.
5. Afegeix una secció `## Connexions` si la nota no en té.
6. Revisa possibles pàgines orfes.

## Criteri

Un bon enllaç ajuda a pensar. Un mal enllaç només decora.
```

### 14.4. `skills/lint.md`

```markdown
# Skill — Revisió de coherència

## Quan utilitzar-la

Quan la wiki hagi crescut o abans de tancar una fase del projecte.

## Objectiu

Detectar problemes d'ordre, duplicació, contradicció o enllaços trencats.

## Revisar

- Notes duplicades.
- Notes massa llargues.
- Notes sense font.
- Conceptes repetits amb noms diferents.
- Enllaços trencats.
- Fonts processades però no registrades al manifest.
- Entrades importants no reflectides a `index.md`.
- Canvis rellevants no registrats a `log.md`.

## Sortida esperada

Un informe breu dins `outputs/reports/` amb:

- problemes detectats;
- recomanacions;
- canvis aplicats;
- canvis pendents.
```

### 14.5. `skills/query.md`

```markdown
# Skill — Consulta de la wiki

## Quan utilitzar-la

Quan l'usuari faci una pregunta que es pugui respondre amb el coneixement acumulat a la wiki.

## Objectiu

Respondre utilitzant notes existents, fonts i conceptes, sense reinventar la resposta des de zero.

## Passos

1. Identifica la pregunta.
2. Busca notes relacionades.
3. Busca conceptes relacionats.
4. Revisa fonts si cal evidència.
5. Respon separant:
   - informació documentada;
   - interpretació;
   - dubtes o límits.
6. Si la resposta revela una síntesi nova, proposa crear una nota.

## Sortida esperada

Una resposta clara i, si cal, una proposta d'actualització de la wiki.
```

---

## 15. Flux de treball recomanat

```text
1. Afegir font a _raw/
2. Demanar a l'agent que apliqui skills/ingest.md
3. Revisar la fitxa creada a sources/
4. Revisar les notes creades a notes/
5. Afegir o corregir enllaços interns
6. Actualitzar index.md si la font és important
7. Registrar el canvi a log.md
8. Fer commit amb Git si el projecte està versionat
```

En una frase:

```text
Obsidian és per llegir i pensar; l'agent és per transformar i mantenir; Git és per auditar.
```

---

## 16. Com adaptar aquesta estructura a qualsevol projecte

La plantilla és neutra. Per adaptar-la, només cal canviar les carpetes de segon nivell.

### Exemple: projecte de lectures

```text
notes/      → notes de llibres i articles
concepts/   → idees recurrents
sources/    → fitxes de llibres, articles i vídeos
outputs/    → resums i assajos
```

### Exemple: projecte professional

```text
notes/      → notes de treball
concepts/   → processos, criteris, definicions internes
sources/    → documents, correus, reunions, manuals
outputs/    → informes, decisions, entregables
```

### Exemple: projecte creatiu

```text
notes/      → idees, escenes, personatges
concepts/   → temes, món, regles internes
sources/    → referències visuals o narratives
outputs/    → capítols, guions, versions finals
```

### Exemple: projecte d'aprenentatge tècnic

```text
notes/      → lliçons i explicacions
concepts/   → conceptes tècnics
sources/    → tutorials, documentació, papers
outputs/    → exercicis, projectes, síntesis
```

---

## 17. Roadmap d'implementació

## Fase 1 — Wiki mínima

Objectiu: tenir una base usable.

Tasques:

```text
1. Crear el vault o repositori.
2. Crear l'estructura de carpetes.
3. Crear index.md.
4. Crear log.md.
5. Crear AGENTS.md.
6. Crear les plantilles bàsiques.
7. Afegir tres fonts de prova.
```

Resultat esperat:

```text
Una wiki petita, navegable i coherent.
```

## Fase 2 — Skills inicials

Objectiu: fer repetibles les tasques habituals.

Skills mínimes:

```text
ingest.md
update_note.md
cross_link.md
lint.md
query.md
```

Resultat esperat:

```text
L'agent pot treballar seguint procediments estables.
```

## Fase 3 — Traçabilitat

Objectiu: evitar duplicacions i pèrdua de context.

Afegir:

```text
.manifest.json actualitzat
log.md regular
convenció de noms
revisió periòdica amb lint.md
```

Resultat esperat:

```text
La wiki sap què ha processat, què falta revisar i què ha canviat.
```

## Fase 4 — Especialització progressiva

Objectiu: adaptar la wiki al domini real.

Possibles accions:

```text
crear carpetes específiques
crear templates específics
crear skills específiques
crear dashboards a Obsidian
crear consultes Dataview
connectar amb scripts Python
```

Resultat esperat:

```text
La wiki deixa de ser genèrica i es converteix en una eina pròpia del projecte.
```

---

## 18. Convencions de noms

Una convenció simple evita caos.

### Fitxers

```text
minuscules_amb_guions_baixos.md
YYYY-MM-DD_titol_breu.md
nom_concepte.md
index_nom_carpeta.md
```

### Notes

```text
notes/2026-07-08_resum_article_x.md
concepts/memoria_persistent.md
sources/llibre_nom_autor.md
outputs/reports/2026-07-08_revisio_wiki.md
```

### Recomanació

No canviïs noms de fitxer constantment. En una wiki, els noms són infraestructura.

---

## 19. Ús amb Obsidian

Configuració inicial recomanada:

- Activar enllaços interns `[[...]]`.
- Crear un `index.md` com a pàgina d'inici.
- Utilitzar gràfic local només com a suport, no com a substitut de l'ordre.
- Afegir Dataview només quan hi hagi prou metadades útils.
- No obsessionar-se amb dashboards abans de tenir bones notes.

Plugins útils, segons maduresa:

| Plugin | Quan té sentit |
|---|---|
| Dataview | Quan les notes tenen YAML consistent. |
| Templater | Quan crees moltes notes semblants. |
| Kanban | Quan el projecte té tasques o fases. |
| Excalidraw / Canvas | Quan necessites mapes visuals. |
| Git | Quan vols versionar i auditar canvis. |

---

## 20. Ús amb Codex IDE o agents similars

L'agent ha de treballar com un editor disciplinat, no com un generador aleatori de text.

Bones ordres inicials:

```text
Llegeix AGENTS.md i aplica la skill skills/ingest.md a la font _raw/articles/[fitxer].md.
```

```text
Revisa la coherència de notes/ i concepts/ aplicant skills/lint.md. No facis canvis destructius. Genera un informe a outputs/reports/.
```

```text
Actualitza index.md perquè reflecteixi les notes principals creades avui. Registra el canvi a log.md.
```

```text
Aplica skills/cross_link.md a les notes creades aquesta setmana. Afegeix només enllaços que aportin context real.
```

---

## 21. Errors habituals

| Error | Conseqüència | Solució |
|---|---|---|
| Crear massa carpetes al principi | Fricció i abandonament | Començar amb estructura mínima |
| Fer resums massa llargs | Notes poc reutilitzables | Crear notes més petites i connectades |
| No guardar fonts originals | Pèrdua de traçabilitat | Fer servir `_raw/` |
| No tenir `log.md` | No saber què ha canviat | Registrar canvis importants |
| No tenir `AGENTS.md` | Agents inconsistents | Definir principis i fluxos |
| Crear enllaços indiscriminats | Soroll visual | Enllaçar només quan aporti context |
| No revisar duplicats | Wiki inflada | Aplicar `skills/lint.md` periòdicament |

---

## 22. Resum final

Aquesta plantilla converteix una idea simple en un sistema operatiu:

```text
Fonts → notes → conceptes → enllaços → síntesi → revisió
```

La wiki no ha de ser perfecta des del primer dia. Ha de ser prou clara perquè cada nova font la faci millor.

La regla principal és aquesta:

> Una bona wiki no acumula informació; acumula criteri reutilitzable.
