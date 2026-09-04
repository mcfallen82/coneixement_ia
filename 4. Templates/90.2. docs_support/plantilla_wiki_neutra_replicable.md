# Plantilla canònica per crear una base de coneixement amb IA

> **Document canònic i replicable.** Aquesta plantilla defineix una arquitectura mínima per crear una base de coneixement en Markdown que pugui ser consultada, mantinguda i ampliada amb ajuda d'una IA o agent.

## 1. Objectiu

El patró és independent del domini. Es pot aplicar a recerca, història, finances, dret, ciència, gastronomia, projectes professionals o qualsevol altre camp on calgui transformar fonts disperses en coneixement persistent i traçable.

```text
Fonts verificables
      ↓
Lectura i classificació
      ↓
Fitxes permanents en Markdown
      ↓
Relacions, índexs i metadades
      ↓
Consulta i manteniment amb IA o agents
```

La base de coneixement conserva **síntesis pròpies, estructura, decisions i procedència**. Les fonts originals poden continuar al seu origen extern o, si cal treballar-hi localment, en ubicacions excloses del control de versions.

## 2. Principis de disseny

Una base de coneixement útil ha de:

1. començar amb una arquitectura petita;
2. separar fonts, coneixement processat i procediments;
3. conservar la procedència de les afirmacions;
4. evitar duplicats i noms inconsistents;
5. permetre revisió humana;
6. ser independent de l'editor o gestor de notes;
7. poder ser llegida per una IA sense dependre de configuracions locals.

Markdown és un bon format canònic perquè és llegible, portable, versionable i fàcil de processar.

## 3. Estructura mínima recomanada

```text
NomDelProjecte/
├── README.md
├── index.md
├── AGENTS.md
├── log.md
├── .manifest.json
├── wiki/
│   ├── conceptes/
│   ├── entitats/
│   └── fonts/
├── skills/
│   ├── ingest.md
│   ├── update.md
│   ├── query.md
│   └── lint.md
├── templates/
│   ├── template_concept.md
│   └── template_source.md
├── graph/                  # opcional
└── scripts/                # opcional
```

Els noms es poden adaptar al domini. El que convé preservar és la funció de cada capa.

## 4. Funció dels components

| Component | Funció |
|---|---|
| `README.md` | Explica el projecte a una persona nova. |
| `index.md` | Mapa de navegació i punts d'entrada. |
| `AGENTS.md` | Governança i instruccions persistents per als agents. |
| `log.md` | Registre dels canvis estructurals i decisions importants. |
| `.manifest.json` | Traçabilitat tècnica de fonts, operacions i fitxes afectades. |
| `wiki/` | Coneixement permanent propi del projecte. |
| `skills/` | Procediments repetibles per investigar, actualitzar, validar o consultar. |
| `templates/` | Estructures reutilitzables per crear contingut homogeni. |
| `graph/` | Representació derivada de nodes i relacions, si és necessària. |
| `scripts/` | Validacions i automatitzacions reproduïbles. |

## 5. Política de fonts

Per a cada font rellevant convé registrar:

- títol;
- autor o organisme;
- URL o referència bibliogràfica;
- tipus de font;
- data de publicació o consulta;
- fitxes creades o actualitzades;
- nivell de confiança o limitacions quan sigui pertinent.

### Fonts externes

Quan la font és accessible en línia, la base de coneixement ha de conservar-ne la referència i una síntesi pròpia, no una còpia completa per defecte.

### Materials locals

Si el projecte necessita PDFs, exports, notes privades o altres materials de treball locals, s'han de mantenir en carpetes ignorades per Git o fora del repositori compartit.

Exemple:

```gitignore
local_sources/
data/raw/
*.pdf
```

La política concreta dependrà de la llicència, privacitat i necessitats del projecte.

## 6. Fitxa permanent mínima

```yaml
---
title: Nom
category: concepte
tags: []
sources: []
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Estructura recomanada:

```markdown
# Nom

## Definició
## Importància
## Intuïció
## Funcionament
## Exemple
## Aplicacions
## Limitacions
## Relacions
## Fonts
```

La plantilla s'ha d'adaptar al domini. L'objectiu no és omplir camps mecànicament, sinó crear una unitat de coneixement útil i recuperable.

## 7. AGENTS.md

`AGENTS.md` funciona com la constitució operativa del sistema. Ha de definir, com a mínim:

- objectiu i abast;
- estructura del repositori;
- criteris de qualitat;
- política de fonts;
- regles de creació i actualització;
- tractament de contradiccions;
- validacions obligatòries;
- operacions que requereixen revisió humana.

Exemple de principi:

```text
La IA pot proposar canvis; la governança determina quan es poden incorporar.
```

## 8. Manifest

El manifest evita perdre la traçabilitat del que s'ha processat.

Exemple mínim:

```json
{
  "project": "NomDelProjecte",
  "sources": [
    {
      "id": "source-0001",
      "title": "Títol de la font",
      "type": "article",
      "url": "https://...",
      "status": "processed",
      "pages_created": [],
      "pages_updated": []
    }
  ]
}
```

No cal començar amb un esquema complex. El manifest ha de créixer quan aparegui una necessitat real de control.

## 9. Flux d'ingesta

```text
1. Identificar la font
2. Registrar-ne la procedència
3. Buscar contingut existent
4. Extreure idees i entitats
5. Crear o actualitzar fitxes
6. Afegir relacions
7. Actualitzar índex, log i manifest
8. Executar validacions
9. Revisió humana
```

La regla de no-duplicació és central: **actualitzar una fitxa existent és preferible a crear un segon resum del mateix concepte**.

## 10. Consulta amb IA

Una IA pot utilitzar la base de coneixement de diverses maneres:

- cerca directa sobre Markdown;
- recuperació per metadades;
- embeddings i RAG;
- recuperació sobre graf;
- paquets de context seleccionats;
- agents amb procediments definits a `skills/`.

No cal començar amb RAG o GraphRAG. Una estructura Markdown coherent ja aporta molt valor i permet afegir capes de recuperació més endavant.

## 11. Graf de coneixement opcional

Quan les relacions siguin importants, es poden representar explícitament:

```text
concepte A --utilitza--> concepte B
model X    --creat_per--> autor Y
font Z     --explica--> concepte A
```

El graf ha de ser una representació derivada del coneixement, no una segona font de veritat independent.

## 12. Validació mínima

Abans d'incorporar canvis significatius convé comprovar:

- Markdown i YAML vàlids;
- categories coherents;
- fonts traçables;
- enllaços interns resolubles;
- absència de duplicats evidents;
- manifest consistent;
- cap configuració o material local incorporat accidentalment;
- revisió humana dels canvis semàntics.

## 13. Criteri de maduresa

Una base de coneixement madura no és la que té més fitxers. És la que permet:

- trobar ràpidament una idea;
- entendre d'on prové;
- veure amb què es relaciona;
- detectar què falta o és incert;
- actualitzar coneixement sense perdre coherència;
- donar a una IA context fiable i revisable.

## 14. Resultat esperat

El patró final és:

```text
fonts → coneixement propi → relacions → validació → recuperació amb IA
```

Aquesta arquitectura és deliberadament genèrica. Cada nova base de coneixement ha d'especialitzar categories, plantilles, skills i criteris de fonts segons el seu domini, mantenint separades la **informació d'origen**, el **coneixement processat** i les **regles del sistema**.