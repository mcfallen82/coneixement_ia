# Ar9av/obsidian-wiki i aplicació a Beagle AI

## 1. Objectiu del document

Aquest document resumeix les idees principals del projecte **Ar9av/obsidian-wiki**, les diferències amb el concepte de wiki proposat per **Andrej Karpathy**, i una proposta pràctica per implementar-ne una versió adaptada al projecte **Beagle AI** amb **Codex IDE + Obsidian**.

L'objectiu no és copiar literalment l'estructura d'Ar9av, sinó aprofitar-ne les idees útils per construir una wiki inversora operativa, centrada en:

- empreses;
- filings SEC;
- patrons d'inversió;
- decisions;
- evidències documentals;
- síntesi acumulada.

---

## 2. Idea central del wiki de Karpathy

El wiki de Karpathy parteix d'una idea molt potent:

```text
Fonts brutes
   ↓
LLM les llegeix i les integra
   ↓
Wiki markdown persistent
   ↓
L'usuari consulta, revisa i pregunta
   ↓
El LLM manté el sistema viu
```

La diferència principal respecte a un sistema RAG clàssic és que el coneixement no es recupera de zero cada vegada. En un RAG, el model busca fragments rellevants en el moment de respondre. En canvi, en una wiki mantinguda per un LLM, el coneixement queda **compilat, resumit, enllaçat i actualitzat** en fitxers markdown.

Això converteix la wiki en una mena de memòria persistent:

```text
RAG clàssic:
pregunta → cerca fragments → resposta → la síntesi es perd

Wiki Karpathy:
font → lectura → síntesi → pàgina markdown → actualització futura
```

Per al projecte Beagle AI, aquesta idea és especialment rellevant perquè l'objectiu no és només respondre preguntes sobre empreses, sinó construir una base acumulativa de criteri inversor.

---

## 3. Què aporta Ar9av/obsidian-wiki

Ar9av/obsidian-wiki agafa la idea conceptual de Karpathy i la converteix en un sistema més operatiu.

La seva aportació principal és passar de:

```text
"un LLM manté una wiki"
```

a:

```text
"un conjunt d'agents, instruccions, skills i fitxers de control mantenen una wiki Obsidian"
```

És a dir, Ar9av no només proposa una filosofia de treball, sinó una arquitectura pràctica.

## 3.1. Desenvolupaments principals

| Element | Funció | Interès per Beagle AI |
|---|---|---|
| `AGENTS.md` | Dona instruccions persistents a l'agent | Pot convertir-se en la constitució operativa de Beagle AI |
| Skills markdown | Procediments reutilitzables per a tasques concretes | Permet crear skills per SEC, patrons i decisions |
| `index.md` | Índex central de la wiki | Ajuda a navegar per empreses, patrons i filings |
| `log.md` | Registre cronològic de canvis | Dona traçabilitat a cada ingesta o modificació |
| `.manifest.json` | Registre tècnic de fonts processades | Evita duplicar filings o notes ja ingerides |
| `wiki-ingest` | Ingesta de fonts | Adaptable a filings SEC, articles o notes |
| `wiki-query` | Consulta del wiki amb context | Útil per preguntes sobre patrons, empreses o evidències |
| `wiki-lint` | Revisió d'enllaços i coherència | Molt útil per detectar contradiccions o pàgines orfes |
| `cross-linker` | Crea enllaços interns | Pot connectar empreses, patrons i evidències |
| Git sync | Versionat de la wiki | Permet auditar canvis i revertir errors |

---

## 4. Diferències principals entre Karpathy i Ar9av

La diferència més sintètica és aquesta:

```text
Karpathy = patró mental i arquitectònic
Ar9av    = implementació pràctica i operativa
```

Karpathy descriu tres capes principals:

```text
Fonts brutes
Wiki markdown
Esquema/instruccions per a l'agent
```

Ar9av concreta aquestes capes amb fitxers i processos:

```text
Fonts brutes        → _raw/ o carpetes configurades
Wiki markdown       → pàgines Obsidian
Instruccions        → AGENTS.md + skills
Control operatiu    → index.md + log.md + manifest + lint
Execució            → Codex, Claude Code, Cursor, Gemini, etc.
```

La idea de Karpathy és més simple i filosòfica. La d'Ar9av és més propera a un producte o marc de treball.

---

## 5. El concepte més important: les skills

La part més interessant d'Ar9av per a Beagle AI és el concepte de **skill**.

Una skill és una instrucció especialitzada que diu a l'agent com ha d'executar una tasca recurrent. No és només un prompt puntual, sinó un procediment reusable.

Exemple conceptual:

```text
Quan l'usuari demani processar un filing SEC:
1. identifica empresa, ticker i període;
2. extreu només fragments rellevants;
3. actualitza la pàgina de l'empresa;
4. crea o actualitza la pàgina del filing;
5. connecta evidències amb patrons;
6. registra el canvi al log.
```

Això és molt important perquè Beagle AI no necessita només respostes bones. Necessita **processos repetibles**.

---

## 6. Skills recomanades per Beagle AI

Per a un producte mínim viable, no caldria crear moltes skills. Jo començaria amb quatre.

| Skill | Funció |
|---|---|
| `beagle-sec-ingest` | Processar 10-K, 10-Q i documents proxy |
| `beagle-company-update` | Actualitzar la pàgina d'una empresa |
| `beagle-pattern-update` | Relacionar evidències noves amb patrons Beagle |
| `beagle-investment-review` | Crear revisions o decisions inversores estructurades |

Més endavant es podrien afegir:

| Skill futura | Funció |
|---|---|
| `beagle-lint` | Buscar incoherències, contradiccions o enllaços trencats |
| `beagle-synthesis` | Generar síntesis transversals entre empreses i patrons |
| `beagle-evidence-map` | Crear mapa d'evidències documentals per patró |
| `beagle-decision-log` | Registrar compres, vendes, canvis de tesi i seguiments |

---

## 7. Estructura recomanada per al vault Beagle AI

No copiaria tota l'estructura d'Ar9av perquè és massa generalista. Per Beagle AI convé una estructura petita, clara i orientada a inversió.

Proposta inicial:

```text
BeagleAI/
├── index.md
├── log.md
├── AGENTS.md
├── .manifest.json
├── _raw/
│   ├── filings/
│   ├── articles/
│   └── notes_chatgpt/
├── companies/
│   ├── MPTI.md
│   ├── MANH.md
│   └── MEDP.md
├── filings/
│   ├── MPTI_2025_10K.md
│   └── MANH_2025_10K.md
├── patterns/
│   ├── P-NEG-06.md
│   ├── P-NEG-05.md
│   └── index_patterns.md
├── extractors/
│   ├── SEC_10K.md
│   ├── SEC_10Q.md
│   └── Conference_Call.md
├── decisions/
│   ├── 2026-07-03_MANH_review.md
│   └── 2026-07-03_MPTI_followup.md
└── synthesis/
    ├── company_pattern_matrix.md
    └── sec_evidence_map.md
```

## 7.1. Funció de cada carpeta

| Carpeta | Funció |
|---|---|
| `_raw/` | Fonts brutes: filings, articles, notes exportades, converses |
| `companies/` | Una pàgina viva per empresa |
| `filings/` | Una pàgina processada per document SEC |
| `patterns/` | Patrons Beagle, errors, senyals i criteris |
| `extractors/` | Plantilles o instruccions per extreure informació |
| `decisions/` | Decisions de compra, venda, revisió o seguiment |
| `synthesis/` | Matrius i síntesis transversals |

La clau és evitar una arquitectura massa extensa al principi. El valor estarà en la qualitat de les pàgines i en la consistència de les skills.

---

## 8. Flux de treball amb Codex IDE + Obsidian

El flux pràctic hauria de ser aquest:

```text
1. Guardar el filing, article o nota a _raw/
2. Obrir el projecte amb Codex IDE
3. Demanar a Codex que apliqui una skill concreta
4. Codex llegeix AGENTS.md
5. Codex processa la font
6. Codex actualitza pàgines markdown
7. Codex crea enllaços interns
8. Codex actualitza index.md
9. Codex registra el canvi a log.md
10. Revisió humana a Obsidian
11. Commit amb Git
```

El paper d'Obsidian és visual i analític. El paper de Codex és operatiu.

```text
Obsidian = llegir, navegar, revisar, pensar
Codex IDE = modificar, reestructurar, aplicar processos, mantenir coherència
Git = auditar i versionar
```

---

## 9. Exemple de flux SEC per Beagle AI

Quan s'afegeix un 10-K nou:

```text
_raw/filings/MPTI_2025_10K.html
```

La skill `beagle-sec-ingest` hauria de fer això:

```text
1. Identificar empresa, ticker, any fiscal i tipus de document.
2. Separar seccions importants: Business, Risk Factors, MD&A, Financial Statements, Notes.
3. Extreure només fragments útils per a Beagle AI.
4. Crear o actualitzar filings/MPTI_2025_10K.md.
5. Actualitzar companies/MPTI.md.
6. Relacionar evidències amb patterns/.
7. Marcar possibles contradiccions amb tesis prèvies.
8. Actualitzar synthesis/company_pattern_matrix.md si cal.
9. Afegir entrada a log.md.
```

La sortida no hauria de ser un resum general del 10-K. Hauria de ser una extracció orientada a decisió inversora.

---

## 10. Quina informació hauria d'extreure Beagle AI d'un filing

Per cada 10-K o 10-Q, l'extractor hauria de prioritzar:

| Bloc | Pregunta |
|---|---|
| Model de negoci | Com guanya diners l'empresa? |
| Drivers | Quins factors expliquen creixement o caiguda? |
| Marges | Hi ha millora, deteriorament o canvi estructural? |
| Cash flow | El benefici es converteix en caixa? |
| Balanç | Hi ha deute, dilució o risc financer? |
| Segments | Quines parts del negoci són més rellevants? |
| Riscos | Quins riscos nous apareixen? |
| Management | Quins incentius o canvis directius són importants? |
| Adquisicions | Hi ha compres que alteren la qualitat del negoci? |
| Patrons Beagle | Quins patrons positius o negatius s'activen? |

Aquesta extracció ha d'estar sempre separada en tres capes:

```text
Dada documental
Interpretació
Hipòtesi inversora
```

Això evita barrejar evidència amb conclusió.

---

## 11. Proposta de contingut per a AGENTS.md

El fitxer `AGENTS.md` hauria de funcionar com la constitució de la wiki.

Exemple inicial:

```markdown
# Beagle AI — Agent Instructions

Aquest vault és una wiki d'anàlisi d'empreses, filings SEC, patrons d'inversió i decisions.

## Principis

- No facis resums generals si no aporten valor inversor.
- No dupliquis informació ja existent.
- No modifiquis fonts brutes dins `_raw/`.
- Cada afirmació important ha de tenir evidència o origen.
- Separa dades, interpretació i hipòtesi.
- Actualitza sempre `index.md` i `log.md`.
- Si una nova font contradiu una pàgina existent, marca-ho explícitament.

## Tipus de pàgines

- `companies/`: una pàgina per empresa.
- `filings/`: una pàgina per document processat.
- `patterns/`: una pàgina per patró Beagle.
- `decisions/`: una pàgina per decisió o revisió inversora.
- `synthesis/`: anàlisi transversal.

## Flux SEC

Quan processis un 10-K o 10-Q:

1. Identifica empresa, ticker, període i tipus de document.
2. Extreu només fragments rellevants.
3. Crea o actualitza la pàgina del filing.
4. Actualitza la pàgina de l'empresa.
5. Connecta evidències amb patrons Beagle.
6. Registra contradiccions o canvis de tesi.
7. Actualitza `index.md` i `log.md`.
```

Aquest fitxer hauria d'anar evolucionant a mesura que el sistema maduri.

---

## 12. Què importaria d'Ar9av i què deixaria fora

## 12.1. Importaria ara

| Element | Motiu |
|---|---|
| Skills markdown | Són la peça més útil per fer processos repetibles |
| `AGENTS.md` | Dona criteri estable a Codex |
| `index.md` | Fa navegable la wiki |
| `log.md` | Dona traçabilitat |
| `.manifest.json` | Evita duplicacions quan hi hagi molts documents |
| Git | Permet auditar canvis |
| `wiki-lint` conceptual | Ajuda a detectar inconsistències |
| Enllaços interns | Connecten empreses, patrons i evidències |

## 12.2. Deixaria per més endavant

| Element | Motiu |
|---|---|
| Vector search | Encara no cal si el vault és petit |
| Multi-vault complex | Pot afegir fricció al MVP |
| Dashboards avançats | Primer cal tenir dades bones |
| Automatització web intensa | Pot embrutar la base amb massa soroll |
| Rebuild complet | Només quan el sistema estigui desordenat |
| Bases complexes d'Obsidian | Útil més endavant, no al primer cicle |

---

## 13. Roadmap d'implementació

## Fase 1 — Wiki manual assistida

Objectiu: tenir una estructura simple i usable.

Tasques:

```text
1. Crear vault BeagleAI.
2. Crear carpetes bàsiques.
3. Crear index.md.
4. Crear log.md.
5. Crear AGENTS.md.
6. Afegir 2 o 3 empreses de prova.
7. Afegir 2 o 3 patrons Beagle.
```

Resultat esperat:

```text
Una wiki navegable i revisable a Obsidian.
```

## Fase 2 — Skills pròpies

Objectiu: convertir tasques repetitives en procediments.

Skills inicials:

```text
beagle-sec-ingest
beagle-company-update
beagle-pattern-update
beagle-investment-review
```

Resultat esperat:

```text
Codex pot actualitzar pàgines seguint normes estables.
```

## Fase 3 — Auditoria i coherència

Objectiu: evitar degradació del sistema.

Afegir:

```text
.manifest.json
beagle-lint
company_pattern_matrix.md
sec_evidence_map.md
```

Resultat esperat:

```text
El sistema sap què s'ha processat, què està connectat i on hi ha contradiccions.
```

## Fase 4 — Cerca avançada i síntesi

Objectiu: fer consultes més potents quan la wiki creixi.

Possibles eines:

```text
Dataview
Obsidian Bases
BM25 local
embeddings locals
consultes de graf
```

Resultat esperat:

```text
La wiki pot respondre preguntes transversals entre empreses, documents i patrons.
```

---

## 14. Exemple de consulta futura

Quan el sistema estigui madur, hauries de poder preguntar:

```text
Quines empreses han activat el patró P-NEG-06?
```

I el sistema hauria de respondre mirant:

```text
patterns/P-NEG-06.md
companies/*.md
filings/*.md
synthesis/company_pattern_matrix.md
```

Una altra consulta útil:

```text
Quines evidències SEC indiquen que MANH manté qualitat de negoci malgrat la caiguda de valoració?
```

El sistema hauria de trobar:

```text
companies/MANH.md
filings/MANH_10K.md
filings/MANH_10Q.md
patterns/patrons_qualitat.md
decisions/revisions_MANH.md
```

Això és molt més potent que tenir resums dispersos.

---

## 15. Principi de disseny per al MVP

El principi fonamental hauria de ser aquest:

```text
No crear més estructura de la necessària.
Crear només la que permeti repetir millor el procés d'anàlisi.
```

El risc principal és construir una wiki massa sofisticada abans de tenir prou ús real. Per tant, la prioritat hauria de ser:

```text
1. Bones fonts.
2. Bones extraccions.
3. Bones pàgines d'empresa.
4. Bons enllaços amb patrons.
5. Bon registre de decisions.
```

No cal començar amb un sistema perfecte. Cal començar amb un sistema que millori cada vegada que s'utilitza.

---

## 16. Conclusió

Ar9av/obsidian-wiki és interessant perquè mostra com portar a la pràctica la intuïció de Karpathy: una wiki viva, mantinguda per agents, escrita en markdown i consultable per humans.

Per Beagle AI, la millor adaptació no és copiar-ho tot, sinó quedar-se amb cinc idees:

```text
1. Markdown com a base de coneixement persistent.
2. Obsidian com a interfície de revisió i navegació.
3. Codex IDE com a executor de canvis.
4. AGENTS.md com a constitució operativa.
5. Skills com a processos repetibles.
```

La formulació final seria:

```text
Obsidian = lectura i pensament
Codex IDE = manteniment i transformació
AGENTS.md = criteri estable
Skills = procediments repetibles
Git = auditoria
Filings SEC = fonts brutes
Patrons Beagle = intel·ligència acumulada
```

La direcció bona per Beagle AI és passar de:

```text
fer anàlisis puntuals amb IA
```

a:

```text
construir una memòria inversora operativa
```

Aquesta és la gran aportació del patró Karpathy + Ar9av aplicada al teu projecte.
