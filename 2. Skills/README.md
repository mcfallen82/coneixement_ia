# 2. Skills

Procediments reutilitzables per estudiar, mantenir, consultar i exportar la wiki d'aprenentatge d'IA.

Cada skill viu en una carpeta propia. El `README.md` de cada carpeta dona un resum breu i el fitxer `<skill>.md` conserva el procediment complet.

## Ordre d'activacio

Per a una operacio amb escriptura, llegeix i aplica:

1. [[2. Skills/llm-wiki/README|llm-wiki]] - arquitectura i principis;
2. [[2. Skills/wiki-ingest/README|wiki-ingest]] o [[2. Skills/wiki-update/README|wiki-update]] - transformacio;
3. [[2. Skills/wiki-dedup/README|wiki-dedup]] i [[2. Skills/cross-linker/README|cross-linker]] - coherencia;
4. [[2. Skills/impl-validator/README|impl-validator]] - comprovacio de l'objectiu;
5. [[2. Skills/wiki-lint/README|wiki-lint]] - validacio final.

Per a una operacio nomes de lectura, utilitza [[2. Skills/wiki-query/README|wiki-query]] i, si cal, [[2. Skills/wiki-context-pack/README|wiki-context-pack]]. Per a una recerca externa, aplica [[2. Skills/wiki-research/README|wiki-research]] i consulta [[4. Templates/90.2. docs_support/research-config]]. Per a manteniment, utilitza [[2. Skills/daily-update/README|daily-update]] i [[2. Skills/wiki-status/README|wiki-status]].

## Skills per funcio

### Arquitectura i ingesta

- [[2. Skills/llm-wiki/README|llm-wiki]]
- [[2. Skills/wiki-ingest/README|wiki-ingest]]
- [[2. Skills/wiki-update/README|wiki-update]]
- [[2. Skills/wiki-capture/README|wiki-capture]]
- [[2. Skills/wiki-research/README|wiki-research]] - recerca en tres rondes i integracio de fonts.

### Grafs i relacions

- [[2. Skills/graph-layer/README|graph-layer]] - capa grafica lleugera sobre Markdown.

### Consulta i qualitat

- [[2. Skills/wiki-query/README|wiki-query]]
- [[2. Skills/wiki-context-pack/README|wiki-context-pack]]
- [[2. Skills/wiki-status/README|wiki-status]]
- [[2. Skills/wiki-dedup/README|wiki-dedup]]
- [[2. Skills/cross-linker/README|cross-linker]]
- [[2. Skills/tag-taxonomy/README|tag-taxonomy]]
- [[2. Skills/impl-validator/README|impl-validator]]
- [[2. Skills/wiki-lint/README|wiki-lint]]

### Operacions i sortides

- [[2. Skills/wiki-dashboard/README|wiki-dashboard]]
- [[2. Skills/wiki-synthesize/README|wiki-synthesize]]
- [[2. Skills/wiki-export/README|wiki-export]]
- [[2. Skills/wiki-import/README|wiki-import]]
- [[2. Skills/wiki-rebuild/README|wiki-rebuild]]
- [[2. Skills/daily-update/README|daily-update]]
- [[2. Skills/vault-skill-factory/README|vault-skill-factory]]

Les skills descriuen procediments operatius; la governanca continua definida exclusivament a [[AGENTS]]. Qualsevol skill que escrigui fitxers ha d'indicar entrades, sortides, validacio i criteris d'aturada.
