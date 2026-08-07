# AGENTS.md — Governança de la wiki d’aprenentatge d’IA

## 1. Objectiu

Aquest repositori és una wiki d’aprenentatge assistida per models de llenguatge. El seu objectiu és ajudar a estudiar, ordenar, relacionar i revisar coneixement sobre:

- intel·ligència artificial;
- aprenentatge automàtic;
- aprenentatge profund;
- models de llenguatge;
- models generatius;
- enginyeria de context;
- sistemes de coneixement;
- programació i automatització relacionades amb la IA;
- eines i fluxos de treball per aprendre i construir aplicacions amb IA.

La wiki és un sistema d’aprenentatge general sobre IA. No és una wiki d’aprenentatge de documents financers, ni un sistema d’aprenentatge de finances o economia. Les aplicacions financeres només es poden incloure quan serveixin com a exemple d’un concepte d’IA i no com a àrea principal de coneixement.

## 2. Font única de governança

Aquest fitxer és l’únic document de governança del repositori.

Qualsevol agent o model de llenguatge que treballi en aquest repositori ha de llegir-lo abans d’actuar i ha de respectar-lo. No s’han de crear fitxers alternatius de governança, com ara `CLAUDE.md`, `GEMINI.md` o altres documents equivalents, llevat que Joan ho demani explícitament.

Els fitxers d’instruccions tècniques de GitHub, Obsidian o altres eines poden conservar-se perquè formen part de la configuració de l’entorn, però no substitueixen aquest document.

## 3. Estructura obligatòria

La wiki utilitza aquesta estructura:

```text
.obsidian/
0. Raw/
├── 0.1. llibres/
└── 0.2./
1. Wiki/
├── 1.1. autors/
├── 1.2. conceptes/
└── 1.3. models/
2. Skills/
3. Dashboards/
4. Templates/
├── 90.1. templates_fitxes/
└── 90.2. docs_support/
index.md
log.md
hot.md
.manifest.json
```

Les carpetes numerades formen part de l’organització visible del vault d’Obsidian. Els noms amb espais s’han de conservar exactament.

## 4. Trasllat de contingut

El contingut existent s’ha de reorganitzar així:

| Ubicació actual | Ubicació nova |
|---|---|
| `autors/` | `1. Wiki/1.1. autors/` |
| `conceptes/` | `1. Wiki/1.2. conceptes/` |
| `models/` | `1. Wiki/1.3. models/` |
| `llibres/` | `0. Raw/0.1. llibres/` |
| `docs_support/` | `4. Templates/90.2. docs_support/` |
| `templates/` | `4. Templates/90.1. templates_fitxes/` |

El trasllat ha de preservar el contingut i l’historial sempre que la tecnologia emprada ho permeti. No s’han de duplicar pàgines sense una raó documentada.

Els altres documents d’arrel s’han de mantenir, especialment:

- configuració d’Obsidian;
- configuració de GitHub;
- fitxers de projecte;
- documentació general;
- fitxers de configuració i automatització.

## 5. Tipus de contingut

- `0. Raw/`: materials d’origen i fonts d’aprenentatge. No s’ha de modificar una font original per convertir-la en una síntesi.
- `1. Wiki/`: fitxes permanents sobre autors, conceptes i models d’IA.
- `2. Skills/`: procediments reutilitzables per treballar amb la wiki i estudiar IA.
- `3. Dashboards/`: vistes, consultes i quadres de comandament d’Obsidian.
- `4. Templates/`: plantilles de fitxes i documents de suport.
- `index.md`: mapa de navegació principal.
- `log.md`: registre cronològic dels canvis.
- `hot.md`: continguts prioritaris o en curs.
- `.manifest.json`: registre estructurat de fonts i operacions d’ingestió.

## 6. Treball amb models de llenguatge

Abans de crear una fitxa nova, cal:

1. llegir `index.md` i `hot.md`;
2. localitzar fitxes relacionades;
3. comprovar si el concepte ja existeix amb un altre nom;
4. decidir si cal crear, actualitzar o enllaçar una pàgina;
5. mantenir la procedència de la informació;
6. actualitzar l’índex i el registre quan el canvi afecti l’estructura o el coneixement permanent.

La wiki ha d’acumular coneixement. Les actualitzacions han de reduir duplicacions i millorar les connexions entre fitxes.

## 7. Fitxes de la wiki

Les fitxes permanents han d’utilitzar frontmatter YAML quan el format del contingut ho permeti:

```yaml
---
title: Nom de la fitxa
category: conceptes
tags:
  - inteligencia-artificial
sources: []
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

La categoria ha de correspondre a una carpeta de `1. Wiki/`. Les fonts han d’identificar documents, enllaços o altres fitxes que sustenten el contingut.

Una fitxa ha de distingir, quan sigui necessari:

- definició;
- intuïció;
- funcionament;
- exemple;
- aplicacions;
- limitacions;
- relacions amb altres conceptes;
- fonts i qüestions obertes.

## 8. Estil

La redacció principal és en català, amb terminologia tècnica explicada en llenguatge planer. Es poden conservar els noms propis, els noms de models i les expressions tècniques en anglès quan siguin l’estàndard del sector.

Les explicacions han de construir criteri: primer intuïció, després detall tècnic, exemple pràctic i limitacions. No s’han de presentar hipòtesis com si fossin fets demostrats.

## 9. Obsidian i enllaços

Els enllaços interns han de ser compatibles amb Obsidian i han de reflectir la ubicació real de la fitxa. Les consultes Dataview han d’utilitzar les carpetes noves i s’han de revisar després d’un trasllat.

No s’han de modificar automàticament les carpetes `.obsidian/` ni els fitxers de configuració de GitHub si el canvi no és necessari per a aquesta reorganització.

## 10. Registre dels canvis

Qualsevol canvi estructural o ingesta significativa ha d’afegir una entrada a `log.md` amb:

- data;
- operació;
- carpetes o fitxers afectats;
- resultat;
- incidències pendents.

Quan es processi una font, també s’ha d’actualitzar `.manifest.json`.

## 11. Validació abans de publicar

Abans de donar una feina per acabada cal comprovar:

- que les carpetes obligatòries existeixen;
- que no s’han perdut fitxers en els trasllats;
- que l’índex apunta a les ubicacions noves;
- que no hi ha enllaços interns evidents cap a les rutes antigues;
- que el YAML és vàlid en les fitxes modificades;
- que `log.md` i `.manifest.json` descriuen l’operació;
- que els fitxers d’Obsidian i GitHub no s’han eliminat.

Qualsevol incidència no resolta s’ha d’explicar al registre i a la proposta de canvi.
