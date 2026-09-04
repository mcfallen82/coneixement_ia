# Patró replicable de wiki mantinguda amb agents

> **Document canònic i consolidat.** Aquest document resumeix les idees generalitzables per construir una base de coneixement en Markdown mantinguda amb ajuda d'una IA o agent, sense dependre d'un editor o domini concret.

## Objectiu

El patró serveix per transformar fonts verificables en coneixement persistent, connectat i revisable.

```text
Font externa o bibliogràfica
        ↓
Lectura i classificació
        ↓
Extracció de conceptes, entitats i afirmacions
        ↓
Comparació amb coneixement existent
        ↓
Creació o actualització de fitxes
        ↓
Relacions + índex + manifest + validació
```

## Components principals

| Component | Funció |
|---|---|
| `AGENTS.md` | Governança persistent per a la IA o agent. |
| Skills | Procediments repetibles. |
| Plantilles | Estructures homogènies per al coneixement. |
| `index.md` | Porta d'entrada i mapa de navegació. |
| `log.md` | Memòria dels canvis rellevants. |
| `.manifest.json` | Traçabilitat tècnica de fonts i operacions. |
| Enllaços interns | Connexions navegables entre fitxes. |
| Graf opcional | Relacions tipades i consultables. |
| Git | Historial, comparació i revisió. |
| Validació | Comprovacions automàtiques i revisió humana. |

## Independència de l'eina

```text
Editor Markdown / IDE / gestor de coneixement = lectura i edició
IA o agent                                    = transformació i manteniment
AGENTS.md                                     = criteri estable
Skills                                        = procediments
Git                                           = historial i auditoria
```

La interfície local és substituïble. El repositori compartit conserva Markdown, scripts, plantilles, metadades i governança, no configuracions personals d'aplicacions.

## Arquitectura mínima

Una implementació pot adoptar una estructura semblant a:

```text
wiki/         → coneixement permanent
skills/       → procediments
templates/    → estructures reutilitzables
graph/        → relacions derivades, opcional
scripts/      → validacions, opcional
index.md      → mapa
log.md        → registre
AGENTS.md     → governança
```

Les categories concretes s'han d'adaptar al domini.

## Flux d'ingesta

1. Identificar la font, autor o organisme, data i referència.
2. Revisar l'índex i les fitxes relacionades.
3. Comprovar si el coneixement ja existeix.
4. Extreure conceptes, entitats, afirmacions i qüestions obertes.
5. Separar dades documentades, interpretacions i hipòtesis.
6. Crear o actualitzar fitxes.
7. Afegir fonts i relacions.
8. Actualitzar índex, registre i manifest quan correspongui.
9. Executar validacions.
10. Fer revisió humana dels canvis semàntics.

## Criteri de qualitat

Cada peça de coneixement ha de distingir:

| Nivell | Significat |
|---|---|
| Dada documentada | Informació explícita en una font. |
| Interpretació | Lectura explicativa sustentada per dades. |
| Inferència o hipòtesi | Connexió que necessita revisió o contrast. |

La IA pot ajudar a sintetitzar i connectar, però no ha d'esborrar aquesta distinció.

## Política de fonts

El sistema ha de conservar la procedència amb URLs, referències bibliogràfiques i metadades. Les còpies locals de treball, quan siguin necessàries, s'han de mantenir fora del repositori compartit o en ubicacions ignorades per Git.

## Relació amb RAG i grafs

Aquest patró no exigeix RAG, embeddings ni GraphRAG. Aquestes capes s'afegeixen quan la mida o les preguntes del corpus ho justifiquen.

Progressió possible:

```text
Markdown estructurat
      ↓
cerca i metadades
      ↓
RAG vectorial
      ↓
graf tipat
      ↓
GraphRAG o recuperació híbrida
```

## Resultat esperat

Una base de coneixement ben dissenyada permet:

- recuperar què se sap;
- identificar d'on prové;
- veure amb què es relaciona;
- detectar buits i contradiccions;
- actualitzar sense duplicar;
- proporcionar a una IA context revisable i traçable.

El patró final és:

```text
fonts → fitxes → connexions → validació → recuperació amb IA
```

Aquest document defineix el patró general. Les noves bases de coneixement han d'especialitzar categories, plantilles, skills, política de fonts i validacions segons el seu domini.