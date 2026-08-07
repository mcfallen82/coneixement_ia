# Plantilla per crear Wikis locals amb Obsidian, Codex i AGENTS.md

Aquest document serveix com a guia reutilitzable per crear una nova wiki local temàtica treballant amb **Obsidian** i **Codex**.

La idea és poder pujar aquest fitxer en una nova conversa de ChatGPT, afegir-hi unes quantes dades sobre la temàtica concreta, i demanar que generi un `AGENTS.md` adaptat.

---

## 1. Objectiu general

Vull construir una wiki local temàtica en markdown.

La wiki ha de funcionar com un sistema persistent de coneixement:

- Les fonts originals es guarden localment.
- L'agent llegeix les fonts.
- L'agent crea o actualitza pàgines estructurades.
- L'agent manté un índex.
- L'agent registra els canvis.
- L'agent detecta duplicats, variants, contradiccions o buits.
- Obsidian serveix per navegar i revisar la wiki.
- Codex serveix per modificar fitxers locals seguint les instruccions d'un `AGENTS.md`.

El sistema no ha de dependre d'anar copiant i enganxant continguts entre aplicacions. La carpeta local és el centre del projecte.

---

## 2. Eines utilitzades

Treballo sempre amb aquestes eines:

| Eina | Funció |
|---|---|
| Obsidian | Obrir la carpeta com a vault, llegir, navegar i revisar la wiki |
| Codex | Agent local que llegeix i modifica fitxers dins la carpeta |
| ChatGPT | Pensar l'estructura, generar o millorar `AGENTS.md`, revisar criteris |
| Markdown | Format principal de tots els documents |
| Git | Opcional, però recomanat per conservar historial i poder desfer canvis |

La nova wiki s'ha de dissenyar assumint que el treball pràctic es farà en local amb **Obsidian + Codex**.

---

## 3. Arquitectura conceptual

Tota wiki local hauria de tenir quatre peces principals:

| Peça | Funció |
|---|---|
| `raw/` | Fonts originals, intocables |
| `wiki/` | Coneixement processat i estructurat |
| `index.md` | Mapa navegable de la wiki |
| `log.md` | Registre cronològic de canvis |

El principi bàsic és:

```text
raw/ = font de veritat
wiki/ = coneixement treballat
index.md = mapa
log.md = memòria cronològica
AGENTS.md = instruccions de funcionament de l'agent
```

---

## 4. Estructura mínima inicial

Per començar qualsevol wiki nova, és preferible una estructura simple:

```text
NOM_DE_LA_WIKI/
├── AGENTS.md
├── index.md
├── log.md
├── raw/
│   ├── notes/
│   ├── articles/
│   ├── pdf/
│   └── assets/
├── wiki/
│   ├── fonts/
│   ├── sintesis/
│   └── [carpetes_tematiques]/
└── inbox/
```

No cal crear moltes carpetes al principi. És millor començar amb poques i ampliar-les quan la temàtica ho demani.

---

## 5. Funció de cada carpeta

| Carpeta o fitxer | Funció |
|---|---|
| `AGENTS.md` | Document d'instruccions que Codex ha de seguir |
| `index.md` | Índex general de la wiki |
| `log.md` | Registre de canvis, ingestes i revisions |
| `raw/notes/` | Notes brutes escrites per mi |
| `raw/articles/` | Articles, textos web o documents copiats |
| `raw/pdf/` | PDF originals |
| `raw/assets/` | Imatges, captures, fotografies o altres adjunts |
| `wiki/fonts/` | Fitxes processades de cada font original |
| `wiki/sintesis/` | Resums transversals i documents interpretatius |
| `wiki/[carpetes_tematiques]/` | Pàgines principals segons la temàtica de la wiki |
| `inbox/` | Material pendent de classificar o processar |

---

## 6. Com adaptar les carpetes a cada temàtica

Cada wiki ha de tenir carpetes pròpies segons el tipus de coneixement.

Exemples:

### Wiki de receptes de cuina

```text
wiki/
├── receptes/
├── ingredients/
├── tecniques/
├── autors_restaurants/
├── variants/
├── menus/
├── fonts/
└── sintesis/
```

### Wiki d'inversió

```text
wiki/
├── empreses/
├── sectors/
├── patrons/
├── tesis/
├── errors/
├── fonts/
└── sintesis/
```

### Wiki d'història

```text
wiki/
├── casos/
├── personatges/
├── esdeveniments/
├── llocs/
├── cronologies/
├── fonts/
└── sintesis/
```

### Wiki de lectura i llibres

```text
wiki/
├── llibres/
├── autors/
├── idees/
├── cites/
├── temes/
├── fonts/
└── sintesis/
```

La nova conversa haurà d'ajudar a definir aquestes carpetes segons la temàtica concreta.

---

## 7. Preguntes que cal respondre abans de generar un AGENTS.md temàtic

Abans de crear el `AGENTS.md`, cal definir aquestes dades:

### 7.1. Tema de la wiki

Quina és la temàtica principal?

Exemples:

- Receptes de cuina
- Història
- Inversió
- Lectures
- Viatges
- Projectes personals
- Aprenentatge d'una disciplina
- Recerca acadèmica

### 7.2. Objectiu pràctic

Per a què ha de servir la wiki?

Exemples:

- Recuperar coneixement ràpidament
- Crear una base de receptes
- Analitzar empreses
- Detectar patrons
- Preparar articles
- Construir un dataset
- Organitzar lectures
- Planificar projectes

### 7.3. Tipus principals de pàgina

Quins tipus de documents tindrà la wiki?

Exemples:

- Recepta
- Ingredient
- Tècnica
- Empresa
- Sector
- Patró
- Cas històric
- Personatge
- Llibre
- Autor
- Idea
- Font
- Síntesi

### 7.4. Camps obligatoris

Quins apartats ha de tenir sempre cada pàgina principal?

Exemple per receptes:

- Ingredients
- Explicació recepta

Exemple per empreses:

- Descripció del negoci
- Tesi d'inversió
- Riscos
- Fonts

Exemple per llibres:

- Resum
- Idees principals
- Cites destacades
- Relació amb altres lectures

### 7.5. Camps opcionals

Quins apartats poden existir si hi ha informació disponible?

Exemples:

- Autor
- Cost
- Temps
- Dificultat
- Data
- Font original
- Notes personals
- Variants
- Contradiccions
- Preguntes pendents

### 7.6. Regles de qualitat

Què ha de comprovar l'agent abans de donar per bona una pàgina?

Exemples:

- Que no faltin camps obligatoris
- Que les fonts estiguin indicades
- Que no inventi dades
- Que separi fets, hipòtesis i opinions
- Que detecti duplicats
- Que marqui incerteses
- Que actualitzi `index.md` i `log.md`

### 7.7. Estil d'escriptura

Com ha d'escriure l'agent?

Exemples:

- En català
- Clar i pràctic
- Sintètic
- Sense literatura innecessària
- Amb taules quan sigui útil
- Amb apartats constants
- Amb enllaços interns d'Obsidian

---

## 8. Estructura recomanada d'un AGENTS.md

Un bon `AGENTS.md` temàtic hauria de tenir aquests apartats:

```text
# AGENTS.md

## Objectiu
## Principi bàsic
## Estructura de carpetes
## Convencions de noms
## Tipus de pàgina
## Format de la pàgina principal
## Camps obligatoris
## Camps opcionals
## Format de pàgines secundàries
## Format de fitxa de font
## Flux d'ingesta
## Criteris per crear pàgines noves
## Criteris per actualitzar pàgines existents
## Duplicats, variants i contradiccions
## Control de qualitat
## Flux de consulta
## Flux de manteniment
## Estil d'escriptura
## Regla d'or
```

No tots els apartats han de ser llargs. La idea és que siguin clars i operatius.

---

## 9. Plantilla genèrica d'AGENTS.md

Aquesta és una plantilla base que s'ha d'adaptar a cada temàtica.

```markdown
# AGENTS.md

## Objectiu

Aquesta carpeta és una Wiki local sobre [TEMA].

La funció de l'agent és mantenir una wiki persistent en markdown a partir de fonts guardades a `raw/`.

L'agent ha de:
- llegir fonts noves,
- extreure informació rellevant,
- crear o actualitzar pàgines dins `wiki/`,
- mantenir enllaços interns,
- detectar duplicats, variants, contradiccions o buits,
- actualitzar `index.md`,
- registrar cada operació a `log.md`.

## Principi bàsic

`raw/` és la font original.  
`wiki/` és el coneixement processat.  
`index.md` és el mapa.  
`log.md` és la memòria cronològica.

L'agent pot modificar `wiki/`, `index.md` i `log.md`.

L'agent no pot modificar, reescriure ni eliminar fitxers dins `raw/`, excepte si l'usuari ho demana explícitament.

## Estructura de carpetes

- `raw/notes/`: notes brutes de l'usuari.
- `raw/articles/`: articles o textos copiats.
- `raw/pdf/`: PDF originals.
- `raw/assets/`: imatges o adjunts.
- `wiki/fonts/`: fitxes processades de fonts originals.
- `wiki/sintesis/`: síntesis transversals.
- `wiki/[TIPUS_1]/`: pàgines de [TIPUS_1].
- `wiki/[TIPUS_2]/`: pàgines de [TIPUS_2].
- `wiki/[TIPUS_3]/`: pàgines de [TIPUS_3].
- `inbox/`: material pendent de classificar.

## Convencions de noms

Usa noms de fitxer simples, en minúscules, sense accents i amb guions baixos.

Exemples:
- `wiki/[carpeta]/nom_de_pagina.md`
- `wiki/fonts/2026_07_01_nom_de_la_font.md`

## Tipus de pàgina

Cada pàgina ha de tenir un tipus clar.

Tipus possibles:
- `[TIPUS_1]`
- `[TIPUS_2]`
- `[TIPUS_3]`
- `font`
- `sintesi`

## Format de la pàgina principal

Cada pàgina principal ha de començar amb un bloc YAML:

```yaml
---
tipus: [TIPUS]
estat: esborrany | revisat | pendent_revisio
creat: YYYY-MM-DD
actualitzat: YYYY-MM-DD
fonts:
  - ruta/de/la/font/original
tags:
  - etiqueta
---
```

Després ha de seguir aquesta estructura:

# Títol

## [Camp obligatori 1]

Contingut.

## [Camp obligatori 2]

Contingut.

## [Camp opcional 1]

Contingut si existeix.

## [Camp opcional 2]

Contingut si existeix.

## Fonts

- `raw/...`

## Dubtes o punts pendents

Si no n'hi ha, escriu:

_Cap dubte pendent._

## Flux d'ingesta

Quan l'usuari demani processar una font:

1. Llegeix la font dins `raw/`.
2. Identifica quin tipus d'informació conté.
3. Crea una fitxa de font dins `wiki/fonts/`.
4. Crea pàgines noves només si cal.
5. Actualitza pàgines existents si la font aporta informació nova.
6. Afegeix enllaços interns.
7. Detecta duplicats, variants, contradiccions o buits.
8. Actualitza `index.md`.
9. Afegeix una entrada nova a `log.md`.

## Criteris per crear pàgines noves

Crea una pàgina nova quan:

- la informació té prou entitat pròpia,
- serà reutilitzable en el futur,
- no existeix ja una pàgina equivalent,
- l'usuari vol conservar-la com a element independent.

No creïs pàgines noves per fragments menors que poden anar dins una pàgina existent.

## Criteris per actualitzar pàgines existents

Actualitza una pàgina existent quan:

- la nova font aporta matisos,
- hi ha dades noves,
- hi ha una variant clara,
- hi ha una correcció,
- hi ha una contradicció que cal registrar.

No substitueixis informació anterior sense deixar rastre si el canvi és important.

## Duplicats, variants i contradiccions

Quan dues pàgines o fonts siguin semblants, determina si són:

- duplicats,
- variants,
- complements,
- contradiccions.

No fusionis automàticament sense explicar el criteri.

Si hi ha contradicció:

- indica les fonts implicades,
- explica la tensió,
- proposa una resolució si és raonable,
- marca-ho com a pendent si no es pot resoldre.

## Control de qualitat

Abans de donar per bona una pàgina, comprova:

- que té els camps obligatoris,
- que les fonts estan indicades,
- que no hi ha dades inventades,
- que les incerteses estan marcades,
- que els enllaços interns són útils,
- que `index.md` i `log.md` s'han actualitzat si cal.

## Flux de consulta

Quan l'usuari faci una pregunta:

1. Llegeix primer `index.md`.
2. Identifica les pàgines rellevants.
3. Llegeix les pàgines necessàries de `wiki/`.
4. Consulta `raw/` només si cal verificar fonts originals.
5. Respon amb una síntesi clara.
6. Si la resposta genera coneixement reutilitzable, proposa crear una pàgina nova dins `wiki/sintesis/`.

## Flux de manteniment

Quan l'usuari demani revisar la salut de la wiki:

1. Busca pàgines sense fonts.
2. Busca pàgines sense enllaços interns.
3. Busca pàgines duplicades.
4. Busca variants no connectades.
5. Busca contradiccions pendents.
6. Busca fonts processades que no apareixen a `index.md`.
7. Proposa accions concretes abans de fer canvis massius.

## Estil d'escriptura

- Escriu en català.
- Sigues clar i pràctic.
- Prioritza estructura i traçabilitat.
- No inventis dades.
- No amaguis incerteses.
- Marca les pàgines incompletes com a `pendent_revisio`.

## Regla d'or

Cada nova font ha de fer que la wiki sigui més útil, més connectada i més fiable.
```

---

## 10. Flux de treball per crear una nova wiki local

### Pas 1: Definir la temàtica

Escriu en una nova conversa:

```text
Vull crear una wiki local sobre [TEMA]. Treballo amb Obsidian i Codex en local. Vull que m'ajudis a definir l'estructura de carpetes i a crear un AGENTS.md temàtic.
```

Afegeix:

- objectiu de la wiki,
- tipus de documents que tindrà,
- camps obligatoris,
- camps opcionals,
- exemples de fonts,
- estil desitjat.

### Pas 2: Crear la carpeta local

Exemple:

```text
C:\Users\[usuari]\Documents\Nom_Wiki
```

### Pas 3: Crear estructura mínima

```text
Nom_Wiki/
├── AGENTS.md
├── index.md
├── log.md
├── raw/
│   ├── notes/
│   ├── articles/
│   ├── pdf/
│   └── assets/
├── wiki/
│   ├── fonts/
│   └── sintesis/
└── inbox/
```

Després s'afegeixen les carpetes temàtiques.

### Pas 4: Obrir la carpeta amb Obsidian

A Obsidian:

```text
Open folder as vault
```

Seleccionar la carpeta de la wiki.

### Pas 5: Obrir Codex dins la carpeta

En PowerShell:

```powershell
cd "$env:USERPROFILE\Documents\Nom_Wiki"
codex
```

### Pas 6: Primera prova amb Codex

Dins Codex:

```text
Llegeix AGENTS.md i explica'm quin flux de treball aplicaràs en aquesta carpeta. No modifiquis cap fitxer encara.
```

### Pas 7: Primera ingesta

Guardar una font dins `raw/notes/` o `raw/articles/`.

Després demanar a Codex:

```text
Processa la font raw/notes/[nom_fitxer].md seguint AGENTS.md.

Objectiu:
1. Crear una fitxa de font a wiki/fonts/.
2. Crear o actualitzar les pàgines temàtiques necessàries.
3. Actualitzar index.md.
4. Afegir una entrada a log.md.

No modifiquis cap fitxer dins raw/.
Abans de fer canvis massius, mostra'm el pla.
```

### Pas 8: Revisió a Obsidian

Revisar:

```text
wiki/
index.md
log.md
```

Corregir manualment o demanar a Codex que ajusti l'estructura.

---

## 11. Com ha d'assessorar la nova conversa

Quan es pugi aquest document a una nova conversa, ChatGPT haurà de:

1. Preguntar o inferir la temàtica de la nova wiki.
2. Identificar els tipus principals de pàgina.
3. Proposar una estructura mínima de carpetes.
4. Definir camps obligatoris i opcionals.
5. Generar un `AGENTS.md` complet però simple.
6. Donar instruccions per crear la carpeta local.
7. Explicar com obrir-la a Obsidian.
8. Explicar com executar Codex dins la carpeta.
9. Donar una primera ordre de prova per Codex.
10. Donar una primera ordre d'ingesta.

La nova conversa ha d'evitar crear una arquitectura massa gran al principi. La prioritat és començar amb un flux funcional i ampliar-lo després.

---

## 12. Prompt reutilitzable per a una nova conversa

Es pot copiar aquest prompt en una nova conversa:

```text
Vull crear una nova wiki local temàtica treballant amb Obsidian i Codex en local.

T'adjunto una plantilla general sobre com vull construir aquestes wikis.

La nova wiki serà sobre: [TEMA]

Objectiu pràctic de la wiki:
[EXPLICA OBJECTIU]

Tipus de pàgines que crec que necessitaré:
[LLISTA INICIAL]

Camps obligatoris de la pàgina principal:
[CAMPS]

Camps opcionals:
[CAMPS]

Fonts que utilitzaré:
[NOTES, ARTICLES, PDF, LLIBRES, VÍDEOS, ETC.]

Vull que em donis:
1. Una estructura de carpetes mínima.
2. Una explicació de com crear-la en local.
3. Un AGENTS.md complet però tan simple com sigui possible.
4. El primer prompt que hauré d'escriure a Codex.
5. El flux de treball inicial per començar.

No dissenyis una arquitectura massa complicada. Vull començar simple i ampliar després.
```

---

## 13. Regla final

La wiki no ha de néixer perfecta.

Ha de néixer amb aquest bucle funcionant:

```text
font nova → ingesta amb Codex → pàgines wiki → revisió a Obsidian → consulta → síntesi reutilitzable
```

Quan aquest bucle funciona, la wiki ja és útil. La sofisticació ve després.
