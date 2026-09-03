# Patró de wiki mantinguda amb agents aplicat a l'aprenentatge d'IA

> **Document canònic i consolidat.** Aquesta versió recull les idees generalitzables de wikis Markdown mantingudes amb agents sense dependre d'un editor o gestor de coneixement concret.

## Objectiu

Aquest document explica com construir una wiki d'aprenentatge d'intel·ligència artificial basada en Markdown, fonts externes verificables, agents i control de versions.

La proposta combina:

- fonts externes verificables;
- síntesis en Markdown;
- fitxes de conceptes, autors i models;
- instruccions persistents per a l'agent;
- skills per repetir tasques;
- índex, registre i manifest per mantenir la coherència;
- revisió humana amb qualsevol editor compatible;
- control de versions amb Git.

## 1. Patró operatiu

```text
Font externa
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

La wiki conserva una síntesi persistent. La font externa continua sent l'origen de verificació i la wiki n'organitza el coneixement reutilitzable.

## 2. Components principals

| Component | Funció |
|---|---|
| `AGENTS.md` | Defineix les normes que l'agent ha de seguir |
| Skills | Converteixen tasques repetitives en procediments reutilitzables |
| `index.md` | Ofereix un mapa de navegació |
| `log.md` | Conserva la memòria dels canvis importants |
| `.manifest.json` | Registra fonts i operacions |
| Wikilinks | Connecten fitxes i faciliten la navegació |
| Git | Permet revisar, comparar i recuperar canvis |
| Validació | Detecta enllaços trencats, duplicats i incoherències |

## 3. Independència de l'eina

```text
Editor Markdown / IDE / gestor de coneixement = lectura i revisió
Agent                                      = transformació i manteniment
AGENTS.md                                  = criteri estable de treball
Skills                                     = procediments repetibles
Git                                        = historial i auditoria
```

La interfície local és substituïble. El repositori només comparteix Markdown, scripts, plantilles, metadades i regles de governança. Les configuracions personals de cada aplicació queden fora del control de versions.

## 4. Arquitectura mínima

La plantilla general de referència és [`plantilla_wiki_neutra_replicable`](./plantilla_wiki_neutra_replicable).

```text
1. Wiki/      → coneixement permanent
2. Skills/    → procediments de treball
3. Dashboards/→ consulta i seguiment
4. Templates/ → estructures reutilitzables
graph/        → relacions derivades
index.md      → mapa de la wiki
log.md        → registre de canvis
AGENTS.md     → instruccions de l'agent
```

Les fonts originals no es guarden al repositori públic; es mantenen com a referències externes verificables.

## 5. Flux d'ingesta

1. Identificar la font, l'autor o organisme, la data, el tipus i l'URL o referència bibliogràfica.
2. Llegir l'índex i les fitxes relacionades.
3. Comprovar si la font o el concepte ja s'havien processat.
4. Extreure conceptes, autors, models, afirmacions i qüestions obertes.
5. Separar informació documentada, interpretació i hipòtesi.
6. Crear o actualitzar les fitxes permanents.
7. Afegir fonts i enllaços interns útils.
8. Actualitzar índex, registre i manifest quan correspongui.
9. Executar les validacions disponibles.
10. Fer una revisió humana abans de tancar el canvi.

## 6. Criteri de qualitat

Cada pàgina ha de distingir:

| Nivell | Significat |
|---|---|
| Dada documentada | Informació explícita d'una font |
| Interpretació | Lectura explicativa basada en dades |
| Síntesi o hipòtesi | Connexió nova que cal revisar o contrastar |

## 7. Resultat esperat

Una wiki d'aprenentatge ben dissenyada ha de permetre recuperar què s'ha après i d'on prové, connectar conceptes, detectar buits i contradiccions, actualitzar coneixement sense duplicar-lo i conservar la revisió humana.

```text
Fonts externes → fitxes → connexions → síntesi → revisió
```

L'objectiu és construir una base de coneixement cada vegada més clara, traçable, oberta i independent de l'eina local.