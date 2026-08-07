# Ar9av/obsidian-wiki aplicat a una wiki d’aprenentatge d’IA

## Objectiu

Aquest document adapta les idees de Karpathy i Ar9av a una wiki general d’aprenentatge d’intel·ligència artificial. No és una arquitectura per a Beagle AI ni per a l’anàlisi de documents financers.

## Idea central

~~~text
Font d’aprenentatge
      ↓
Lectura i classificació
      ↓
Extracció de conceptes, autors i models
      ↓
Comparació amb fitxes existents
      ↓
Creació o actualització de la wiki
      ↓
Wikilinks, índex, registre i manifest
~~~

La diferència respecte d’un RAG és que la wiki conserva una síntesi revisable i acumulativa. La font es manté com a origen; el coneixement útil es converteix en fitxes permanents connectades.

## Què convé importar d’Ar9av

| Element | Funció a ia_knowledge |
|---|---|
| AGENTS.md | Criteri estable i únic de governança |
| Skills | Procediments repetibles per ingerir, actualitzar i auditar |
| index.md | Mapa navegable de fonts i fitxes |
| log.md | Traçabilitat dels canvis |
| .manifest.json | Estat de les fonts i relació amb les pàgines |
| Wikilinks | Xarxa de relacions entre conceptes, autors i models |
| Git | Historial, revisió i recuperació |

## Flux d’ingesta

1. Guardar la font a 0. Raw/.
2. Identificar títol, autor, tipus, data i URL.
3. Llegir l’índex i hot.md.
4. Extreure conceptes, autors, models i afirmacions.
5. Buscar fitxes existents, sinònims i actualitzacions.
6. Crear o actualitzar les pàgines permanents.
7. Separar dades documentades, interpretació i qüestions obertes.
8. Afegir fonts i wikilinks.
9. Actualitzar index.md, log.md i .manifest.json.
10. Executar wiki-lint i fer revisió humana.

## Tipus de fonts

El procés és aplicable a llibres, tutorials, papers, articles, cursos, vídeos, documentació oficial, repositoris de codi i notes personals. Cada tipus pot generar una síntesi pròpia, però les idees reutilitzables han d’acabar en fitxes de conceptes, autors o models.

## Principi de deduplicació

Crear una fitxa nova només quan la informació representa una unitat de coneixement clarament diferenciada. Si ja existeix el concepte, s’actualitza la fitxa i es conserva la font anterior.

## Aplicació pràctica

Per a un tutorial sobre GPT, la sortida adequada és conservar el tutorial a 0. Raw/, crear o actualitzar fitxes com [[1. Wiki/1.2. conceptes/embeddings]], [[1. Wiki/1.2. conceptes/attention]] i [[1. Wiki/1.3. models/gpt]], i deixar una pàgina de síntesi que expliqui la ruta d’estudi.

## Resultat esperat

~~~text
Obsidian = lectura, navegació i revisió
Agent = transformació i manteniment
AGENTS.md = governança
Skills = procediments
Git = historial
Wiki = coneixement persistent
~~~
