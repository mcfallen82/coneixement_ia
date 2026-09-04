# 90.2. docs_support

Aquesta carpeta conté **documents de suport del sistema**: expliquen com dissenyar, investigar, ampliar i connectar una wiki de coneixement mantinguda amb Markdown, agents i control de versions.

A diferència de `90.1. templates_fitxes/`, aquí no hi ha principalment estructures per omplir, sinó **guies de criteri i arquitectura**. Serveixen per entendre per què el projecte està organitzat d'una determinada manera i per replicar-ne parts en altres projectes.

## Mapa dels documents

| Document | Què explica | Quan és útil |
|---|---|---|
| [`plantilla_wiki_neutra_replicable.md`](plantilla_wiki_neutra_replicable.md) | Plantilla general per dissenyar una wiki Markdown mantinguda amb ajuda d'agents: estructura mínima, índex, manifest, skills, plantilles i flux d'ingesta. | Quan vols crear una wiki nova o entendre quins components mínims necessita un sistema de coneixement persistent. |
| [`resum_ar9av_wiki_ia_knowledge.md`](resum_ar9av_wiki_ia_knowledge.md) | Síntesi canònica del patró aplicat a `coneixement_ia`: fonts externes, fitxes permanents, agents, skills, Git, traçabilitat i revisió humana. | Quan vols entendre ràpidament l'arquitectura conceptual del projecte sense entrar en tots els detalls operatius. |
| [`research-config.md`](research-config.md) | Configuració de criteris per a la recerca externa: prioritats temàtiques, jerarquia de fonts, qualitat i forma de conservar la procedència. | Quan actives `wiki-research` o vols decidir quines fonts mereixen incorporar-se i amb quin nivell de confiança. |
| [`guia_creacio_wikis_amb_grafs.md`](guia_creacio_wikis_amb_grafs.md) | Guia per evolucionar des d'una wiki amb frontmatter i wikilinks fins a un graf de coneixement tipat, traçable i eventualment consultable per LLM. | Quan treballes amb nodes, relacions, procedència, `graph/relations.json` o vols entendre el camí cap a GraphRAG. |
| [`ruta-zero-to-hero-ia.md`](ruta-zero-to-hero-ia.md) | Ruta d'aprenentatge inspirada en *Neural Networks: Zero to Hero* d'Andrej Karpathy, des d'autograd i backpropagation fins a Transformers, GPT i tokenització. | Quan vols seguir una seqüència pedagògica per entendre els fonaments tècnics que apareixen a la wiki. |

## Com es relacionen entre si

Els documents es poden llegir com quatre capes complementàries:

```text
Arquitectura general
plantilla_wiki_neutra_replicable
            ↓
Patró aplicat al projecte
resum_ar9av_wiki_ia_knowledge
            ↓
Procediments especialitzats
research-config + guia de grafs
            ↓
Ruta d'aprenentatge
ruta-zero-to-hero-ia
```

No cal llegir-los en aquest ordre. La taula anterior permet entrar directament pel problema que vols resoldre.

## Relació amb les skills

Aquests documents donen **context i criteri**; les skills defineixen **accions repetibles**.

Exemples:

- [`research-config.md`](research-config.md) complementa [`wiki-research`](../../../2.%20Skills/wiki-research/README.md).
- [`guia_creacio_wikis_amb_grafs.md`](guia_creacio_wikis_amb_grafs.md) complementa [`graph-layer`](../../../2.%20Skills/graph-layer/README.md).
- [`plantilla_wiki_neutra_replicable.md`](plantilla_wiki_neutra_replicable.md) ajuda a entendre l'arquitectura que després executen skills com `wiki-ingest`, `wiki-update`, `wiki-lint` o `wiki-query`.

## Què és canònic?

- `plantilla_wiki_neutra_replicable.md` és la referència general per replicar l'arquitectura d'una wiki.
- `resum_ar9av_wiki_ia_knowledge.md` és la síntesi canònica de com aquest patró s'aplica a `coneixement_ia`.
- Les guies especialitzades desenvolupen àrees concretes i no han de duplicar la governança definida a [`AGENTS.md`](../../../AGENTS.md).

## Principi general

**La documentació de suport explica el sistema; la Wiki conserva el coneixement; les Skills executen els procediments.**

Markdown és el format canònic compartit. Els documents han de continuar sent útils encara que cada col·laborador utilitzi un editor, IDE o gestor de coneixement diferent.