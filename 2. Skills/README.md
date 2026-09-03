# 2. Skills

Aquesta carpeta conté els **procediments reutilitzables** que expliquen com investigar, incorporar, consultar, mantenir i validar coneixement dins de `coneixement_ia`.

Una *skill* no és un programa autònom ni un plugin: és un protocol de treball en Markdown. Cada carpeta conté:

- un `README.md`, pensat com a porta d'entrada per a persones que volen entendre la funció de la skill;
- un fitxer `<skill>.md`, amb el procediment operatiu complet.

`AGENTS.md` continua sent la norma superior del repositori. Les skills expliquen **com executar una tasca concreta** sense substituir la governança general.

## Quina skill necessito?

| Necessitat | Skill |
|---|---|
| Entendre l'arquitectura i les regles de la wiki | [llm-wiki](llm-wiki/README.md) |
| Investigar un tema amb fonts externes | [wiki-research](wiki-research/README.md) |
| Convertir una font en fitxes permanents | [wiki-ingest](wiki-ingest/README.md) |
| Incorporar informació nova a fitxes existents | [wiki-update](wiki-update/README.md) |
| Capturar una decisió, conversa o descobriment | [wiki-capture](wiki-capture/README.md) |
| Respondre una pregunta amb el coneixement de la wiki | [wiki-query](wiki-query/README.md) |
| Preparar context acotat per a una altra tasca o agent | [wiki-context-pack](wiki-context-pack/README.md) |
| Detectar fitxes duplicades | [wiki-dedup](wiki-dedup/README.md) |
| Afegir connexions útils entre fitxes | [cross-linker](cross-linker/README.md) |
| Normalitzar etiquetes | [tag-taxonomy](tag-taxonomy/README.md) |
| Validar si un canvi compleix el seu objectiu | [impl-validator](impl-validator/README.md) |
| Auditar estructura, YAML i coherència | [wiki-lint](wiki-lint/README.md) |
| Consultar l'estat i els pendents de la wiki | [wiki-status](wiki-status/README.md) |
| Crear dashboards llegibles sense plugins | [wiki-dashboard](wiki-dashboard/README.md) |
| Mantenir la capa de graf derivada del Markdown | [graph-layer](graph-layer/README.md) |
| Crear una síntesi transversal de diverses fitxes | [wiki-synthesize](wiki-synthesize/README.md) |
| Exportar la wiki a formats reutilitzables | [wiki-export](wiki-export/README.md) |
| Importar un paquet o graf compatible | [wiki-import](wiki-import/README.md) |
| Arxivar, reconstruir o restaurar un conjunt de fitxes | [wiki-rebuild](wiki-rebuild/README.md) |
| Fer una revisió periòdica del projecte | [daily-update](daily-update/README.md) |
| Convertir coneixement madur en una nova skill | [vault-skill-factory](vault-skill-factory/README.md) |

## Flux habitual d'escriptura

Per incorporar o modificar coneixement, l'ordre recomanat és:

1. [llm-wiki](llm-wiki/README.md) — comprovar arquitectura i principis;
2. [wiki-research](wiki-research/README.md), [wiki-ingest](wiki-ingest/README.md) o [wiki-update](wiki-update/README.md) — investigar i transformar;
3. [wiki-dedup](wiki-dedup/README.md) i [cross-linker](cross-linker/README.md) — revisar coherència i connexions;
4. [impl-validator](impl-validator/README.md) — comprovar que s'ha assolit l'objectiu;
5. [wiki-lint](wiki-lint/README.md) — validació estructural final.

Les fonts originals es consulten externament i es registren mitjançant URLs, referències bibliogràfiques i camps `sources`. El repositori públic no necessita una carpeta de còpies locals de fonts.
