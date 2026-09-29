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

La base de coneixement conserva **síntesis pròpies, estructura, decisions i procedència**. Les fonts originals poden continuar al seu origen extern o guardar-se a `raw/` dins del projecte. En projectes locals o privats, `raw/` pot formar part del control de versions quan la llicència i la confidencialitat ho permetin.

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
├── raw/                    # opcional: originals externs o documents locals
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
| `raw/` | Fonts originals incorporades al projecte, si s'activa aquesta opció; els originals es mantenen separats de les fitxes elaborades. |
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

Quan la font és accessible en línia, registra'n l'URL, la data de consulta i una síntesi pròpia. Si convé conservar-ne l'original i se'n tenen els drets, desa'l a `raw/` i vincula-hi la fitxa de font. Si l'original roman al web, conserva'n l'enllaç estable i indica quan es va consultar.

### Documents locals i carpeta `raw/`

En crear el projecte, decideix si cal conservar les fonts originals. Si és així, **crea `raw/` a l'arrel** i incorpora-hi els PDFs, transcripcions, exportacions o altres documents locals i les còpies permeses de fonts externes. Conserva els noms originals quan siguin útils i assigna un identificador estable a cada font. Registra a `wiki/fonts/` la procedència, la ruta relativa `raw/...`, la data i les fitxes derivades. Una carpeta buida es pot materialitzar amb `raw/.gitkeep`.

`raw/` **no s'ha d'excloure de Git per defecte**: en projectes locals o privats es pot versionar. Decideix per a cada projecte o fitxer si es comparteix, s'ignora o es manté fora del repositori segons la llicència, la privacitat, les dades sensibles i la mida. No estableixis una regla global com `*.pdf` que amagui fonts autoritzades.

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
      "raw_path": null,
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
2. Registrar-ne la procedència i, si es conserva l'original, la ruta `raw/...`
3. Buscar contingut existent
4. Extreure idees i entitats
5. Crear o actualitzar fitxes
6. Afegir relacions
7. Actualitzar índex, log i manifest
8. Executar validacions
9. Revisió humana
```

La regla de no-duplicació és central: **actualitzar una fitxa existent és preferible a crear un segon resum del mateix concepte**.

### Ordres explícites per ingerir documentació

En adaptar `skills/ingest.md` i `AGENTS.md` al projecte, inclou instruccions operatives per als dos casos següents:

1. **Font externa (URL, article, informe o base documental):** obre i llegeix la font original; verifica títol, autor, data, URL i drets de reutilització. Registra-la a `wiki/fonts/` i al manifest. Si el projecte conserva originals i la còpia és permesa, crea `raw/` si encara no existeix, desa-hi el fitxer i registra'n la ruta. Contrasta el contingut amb les fitxes existents, incorpora només les aportacions verificables, enllaça les fitxes afectades i actualitza índex i `log.md`.
2. **Document local (fitxer aportat, PDF, nota, transcripció o exportació):** llegeix el fitxer proporcionat o la ruta local indicada; no pressuposis que ja és a `raw/`. Si se'n conservarà l'original, crea `raw/` si cal, copia-hi el fitxer amb un nom identificable i registra'n la ruta, l'origen i la data a `wiki/fonts/` i al manifest. Extreu-ne el contingut, comprova duplicitats i contradiccions, crea o actualitza les fitxes pertinents i els seus enllaços, i actualitza índex i `log.md`.

Per a tots dos casos, comprova que cada afirmació rellevant es pugui remuntar a la font (URL o ruta local), registra les limitacions, valida enllaços i metadades i sotmet els canvis semàntics a revisió humana.

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
- criteri de versionat de `raw/` aplicat fitxer per fitxer i absència de dades sensibles o material sense drets incorporat accidentalment;
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