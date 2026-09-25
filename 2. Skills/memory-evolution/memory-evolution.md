# memory-evolution — revisió de notes a partir d'una incorporació nova

## Finalitat i abast

Després d'ingerir una font o actualitzar una fitxa, revisa si el coneixement nou **aporta context a notes anteriors** i si convé establir-hi una relació. És una adaptació editorial d'[A-MEM](../../1.%20Wiki/1.3.%20models/A-MEM.md), no una execució del seu codi ni una memòria autònoma amb embeddings, base vectorial o servei LLM. L'agent que fa la revisió pot interpretar propostes, però només una connexió comprovada passa a la wiki.

## Activació

- Després d'una ingesta significativa o d'una actualització que introdueix una idea o una font nova.
- Quan una fitxa pot tenir relacions que la revisió inicial ha passat per alt.
- Opcionalment durant una auditoria temàtica; no cal executar-la per canvis purament de format.

Abans, llegeix `AGENTS.md`, la font original, la fitxa modificada, `index.md`, `hot.md` i les fitxes existents que resultin pertinents. Aplica les regles de [wiki-ingest](../wiki-ingest/wiki-ingest.md), [wiki-update](../wiki-update/wiki-update.md), [cross-linker](../cross-linker/cross-linker.md) i [graph-layer](../graph-layer/graph-layer.md).

## Fase 1 — candidates en mode lectura

Des de l'arrel del repositori:

```bash
python scripts/memory_candidates.py --note '1. Wiki/1.3. models/A-MEM.md' --top-k 8
```

El script fa servir freqüències de paraules i similitud cosinus sobre vectors lèxics TF-IDF construïts localment; **no fa servir els embeddings ni el LLM d'A-MEM**. La sortida conté ruta, identificador, puntuació, termes compartits i si ja hi ha un enllaç explícit. No crea fitxers ni xarxes de memòria. La puntuació només ordena lectures; també es poden consultar manualment fitxes amb sinònims que el rànquing no detecta.

## Fase 2 — examen de cada connexió

Per a cada candidata, llegeix el contingut complet i respon:

1. Quina afirmació o concepte concret relaciona les dues fitxes? Cita el passatge i la font que la sustenta.
2. És la mateixa idea, un prerequisit, una aplicació, un contrast o només vocabulari semblant?
3. La nota nova amplia, precisa o contradiu una explicació anterior? Conserva les dues fonts si discrepen.
4. El canvi proposat afecta una **interpretació** o modificaria una cita, una dada o la font històrica? No alteris mai el text de la font original.
5. Hi ha una fitxa canònica existent que s'ha d'actualitzar abans de crear-ne una altra?

Anota internament una taula breu per a la revisió:

| Origen → destí | Relació proposada | Passatge i font | Canvi contextual proposat | Decisió |
|---|---|---|---|---|
| Fitxa nova → existent | tipus del vocabulari o només wikilink | URL o referència i secció | frase concreta a afegir/precisar | acceptar, ajornar o rebutjar |

Els enllaços no necessiten automàticament una aresta tipada. Si la relació és inferida, indica-ho; si no hi ha evidència suficient, rebutja-la o deixa-la pendent.

## Fase 3 — evolució controlada

- Revisa primer el text vigent de la fitxa antiga i conserva `created`, fonts i informació encara vàlida.
- Incorpora només una precisió concreta i atribuïble, amb `updated`, `sources` i enllaços quan escaigui; no reescriguis la fitxa antiga a partir d'una mera proximitat lèxica.
- Enllaça en les dues direccions quan la relació entre model i concepte o autor i obra sigui estructural; respecta els enllaços de ruta completa quan hi ha noms duplicats.
- Si la relació tipada és útil i justificable, registra-la a `graph/relations.json` segons el vocabulari i la política d'evidència. Les candidates no validades continuen com a candidates derivades dels wikilinks.
- Registra una ingesta significativa a `index.md`, `log.md`, `hot.md` i `.manifest.json`. No guardis còpies del paper, la conversa o material privat al repositori.

## Verificació i criteri de parada

Executa `python scripts/wiki_lint.py` i `python scripts/graph_scan.py --check --strict`. Si canvies el graf o l'escàner, executa també `python -m unittest discover -s tests -v`. Revisa manualment que les frases noves indiquin font, que cap connexió sigui purament decorativa i que no s'hagin perdut fets anteriors.

Atura l'acceptació d'una proposta si no pots precisar-ne el significat, la procedència o si altera una afirmació sense contrast. El procediment s'acaba amb una llista breu de relacions acceptades, rebutjades i pendents. **Els resultats del paper d'A-MEM en diàlegs no són una validació d'aquest rànquing ni d'aquesta wiki.**
