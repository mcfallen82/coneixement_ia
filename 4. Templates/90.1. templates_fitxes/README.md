# 90.1. templates_fitxes

Aquesta carpeta conté les **plantilles de producció de contingut** de la wiki. Serveixen perquè les fitxes mantinguin una estructura recognoscible, metadades comparables i una traçabilitat mínima sense convertir la redacció en un formulari rígid.

## Quina plantilla necessito?

| Document | Funció | Utilitza'l quan... |
|---|---|---|
| [`plantilla_concepte.md`](plantilla_concepte.md) | Estructura una explicació pedagògica d'un concepte: definició, importància, intuïció, funcionament, exemples, aplicacions i limitacions. | Incorporis una idea, tècnica o mecanisme que mereix una fitxa permanent a `1. Wiki/1.2. conceptes/`. |
| [`plantilla_model.md`](plantilla_model.md) | Documenta un model o arquitectura amb família, arquitectura, modalitats, entrenament, autors, punts forts, limitacions i models relacionats. | Estudiïs un model concret, una arquitectura o una família de models a `1. Wiki/1.3. models/`. |
| [`plantilla_autor.md`](plantilla_autor.md) | Organitza informació sobre una persona rellevant: àmbit, afiliació, obres, contribucions i conceptes relacionats. | Un investigador, autor o divulgador sigui prou recurrent per convertir-se en node propi de la wiki. |
| [`plantilla_font.md`](plantilla_font.md) | Registra una font amb tipus, autor, URL, data, conceptes i models extrets, resum i aplicació pràctica. | Calgui conservar una fitxa explícita d'una font, més enllà d'una simple URL al camp `sources`. |
| [`plantilla_resum_dinamic.md`](plantilla_resum_dinamic.md) | Versió operativa i flexible per resumir articles, vídeos, llibres, repositoris o documents de manera ràpida i escanejable. | Necessitis una síntesi reutilitzable abans de decidir si el contingut s'ha de convertir en fitxes permanents. |
| [`plantilla_resum_dinamic_original.md`](plantilla_resum_dinamic_original.md) | Versió extensa de referència, amb criteris detallats d'estil, estructura i ús de seccions. | Necessitis consultar la lògica completa que hi ha darrere de la plantilla resumida o ajustar-ne el criteri editorial. |

## Diferència entre una fitxa i un resum

Una **fitxa permanent** representa una unitat de coneixement que ha de continuar sent útil encara que canviïn les fonts que l'han originat.

Un **resum** representa principalment una lectura o una font concreta i ajuda a capturar-ne les idees abans d'integrar-les a la wiki.

```text
Font externa
    ↓
Resum o lectura
    ↓
Extracció d'idees
    ↓
Fitxes permanents
```

Per això, un resum no s'ha de convertir automàticament en una nova fitxa si el coneixement ja es pot incorporar a una pàgina existent.

## Metadades i traçabilitat

Les plantilles de conceptes, models i autors inclouen camps com `node_id`, `node_type`, `sources`, relacions i estat. Aquests camps permeten:

- identificar les fitxes de manera estable;
- connectar-les amb el graf de coneixement;
- conservar la procedència;
- distingir contingut `draft` de contingut més madur;
- facilitar validacions i consultes automàtiques.

## Com utilitzar-les

1. Comprova primer si ja existeix una fitxa equivalent.
2. Tria la plantilla segons la **naturalesa del coneixement**, no segons el format de la font.
3. Conserva les metadades útils i elimina camps només quan realment no siguin aplicables.
4. Adapta les seccions al tema: una plantilla és una guia, no una obligació de farcir apartats buits.
5. Registra les fonts verificables i les relacions amb altres fitxes.
6. Aplica les skills pertinents de [`2. Skills/`](../../2.%20Skills/) i les regles d'[`AGENTS.md`](../../AGENTS.md).

## Principi general

**La plantilla ha de fer més fàcil entendre i reutilitzar una fitxa, no simplement uniformitzar-ne l'aspecte.**