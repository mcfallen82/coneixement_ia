# 2. Skills

Procediments reutilitzables per estudiar, mantenir, consultar i exportar la wiki d’aprenentatge d’IA.

## Ordre d’activació

Per a una operació amb escriptura, llegeix i aplica:

1. [[2. Skills/llm-wiki]] — arquitectura i principis;
2. [[2. Skills/wiki-ingest]] o [[2. Skills/wiki-update]] — transformació;
3. [[2. Skills/wiki-dedup]] i [[2. Skills/cross-linker]] — coherència;
4. [[2. Skills/impl-validator]] — comprovació de l’objectiu;
5. [[2. Skills/wiki-lint]] — validació final.

Per a una operació només de lectura, utilitza [[2. Skills/wiki-query]] i, si cal, [[2. Skills/wiki-context-pack]]. Per a una recerca externa, aplica [[2. Skills/wiki-research]] i consulta [[4. Templates/90.2. docs_support/research-config]]. Per a manteniment, utilitza [[2. Skills/daily-update]] i [[2. Skills/wiki-status]].

## Skills per funció

### Arquitectura i ingesta

- [[2. Skills/llm-wiki]]
- [[2. Skills/wiki-ingest]]
- [[2. Skills/wiki-update]]
- [[2. Skills/wiki-capture]]
- [[2. Skills/wiki-research]] — recerca en tres rondes i integració de fonts.

### Grafs i relacions

- [[2. Skills/graph-layer]] — capa gràfica lleugera sobre Markdown.

### Consulta i qualitat

- [[2. Skills/wiki-query]]
- [[2. Skills/wiki-context-pack]]
- [[2. Skills/wiki-status]]
- [[2. Skills/wiki-dedup]]
- [[2. Skills/cross-linker]]
- [[2. Skills/tag-taxonomy]]
- [[2. Skills/impl-validator]]
- [[2. Skills/wiki-lint]]

### Operacions i sortides

- [[2. Skills/wiki-dashboard]]
- [[2. Skills/wiki-synthesize]]
- [[2. Skills/wiki-export]]
- [[2. Skills/wiki-import]]
- [[2. Skills/wiki-rebuild]]
- [[2. Skills/daily-update]]
- [[2. Skills/vault-skill-factory]]

Les skills descriuen procediments operatius; la governança continua definida exclusivament a [[AGENTS]]. Qualsevol skill que escrigui fitxers ha d’indicar entrades, sortides, validació i criteris d’aturada.
