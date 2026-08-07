---
tags:
  - concepte
estat: ok
---
# ✒️ Context Engineering
## Definició

El **context engineering** és el disseny i la gestió de la informació que un model rep, conserva o recupera durant una tasca.

El context pot incloure:

- instruccions;
- historial de conversa;
- documents i fitxers;
- exemples;
- memòria;
- eines;
- resultats de cerca;
- informació recuperada mitjançant RAG;
- resultats de passos anteriors.

**Anthropic** defineix el *context engineering* com un conjunt d’estratègies per seleccionar i mantenir la informació més útil durant la inferència del model.

**Pregunta principal:**

> Quina informació necessita veure el model, quan i en quin format?

---
## 💡 Idea central

El *context engineering* construeix un entorn d’informació útil per a cada tasca.

La qualitat depèn de seleccionar el context adequat i evitar que la informació irrellevant, redundant o desactualitzada dificulti la resposta.

Més informació disponible no implica necessàriament un resultat millor. A mesura que el context creix, el model pot perdre precisió o capacitat per recuperar detalls rellevants.

---
## 🔄 Els quatre processos principals

### 1. Escriure context

Guarda informació perquè estigui disponible més endavant.

Exemples:

- una nota d’Obsidian;
- un fitxer `AGENTS.md`;
- un registre d’errors;
- una memòria del projecte;
- conclusions d’una anàlisi anterior.

### 2. Seleccionar context

Recupera només la informació rellevant per a la tasca.

```
Pregunta:
Quins riscos té Manhattan Associates?

Context seleccionat:
→ Item 1A del 10-K
→ notes sobre competència
→ última conferència de resultats
```

La selecció és una funció central dels sistemes **RAG**.

### 3. Comprimir context

Condensa informació extensa conservant els elements útils.

Exemples:

- resumir una conversa llarga;
- condensar un informe anual;
- conservar conclusions i fonts;
- eliminar informació redundant;
- resumir resultats intermedis.

La compressió permet continuar processos llargs sense mantenir tota la informació original dins de la finestra de context.

### 4. Aïllar context

Separa informació entre agents, processos o tasques. Exemple projecte **Beagle AI**:

```
Becari
→ extracció factual

Detectiu
→ identificació de patrons

Analista
→ interpretació

Bibliotecari
→ organització
```

Cada agent rep la informació necessària per executar la seva funció.

---
## 🧩 Elements principals

- **Finestra de context:** informació que el model pot consultar durant una resposta.
- **Memòria:** informació conservada per recuperar-la en interaccions futures.
- **[[RAG]]:** recuperació de fragments rellevants des d’una font externa.
- **Segmentació:** divisió d’un document en fragments manejables.
- **Compressió:** reducció del volum mantenint les idees útils.
- **Estat:** informació que descriu la situació actual d’un procés o agent.

---
## ⚠️ Errors habituals

- incorporar tota la informació disponible;
- recuperar fragments poc relacionats amb la pregunta;
- conservar dades obsoletes;
- repetir la mateixa informació en diversos formats;
- comprimir tant que es perd evidència rellevant;
- compartir tot el context entre tots els agents;
- acumular resultats d’eines sense seleccionar-los.

La gestió eficient prioritza la rellevància i la utilitat de cada fragment.

---
## 🗺️ Context Engineering pràctic

### Fase 3 — Context Engineering

Aprèn:

- finestra de context;
- segmentació de documents;
- RAG;
- embeddings;
- memòria;
- eines;
- sistemes d’agents;
- compressió del context.

Aquesta fase connecta directament amb els sistemes d’anàlisi documental, els LLM, els documents financers i les wikis de coneixement.

**Pràctica:**

> Construir un sistema que seleccioni automàticament els fitxers Beagle necessaris segons la pregunta.

Exemple:

```
Pregunta
↓
Identificació de la tasca
↓
Selecció de fitxers
↓
Recuperació de fragments
↓
Resposta amb evidència
```

---
## 🧭 Frase resum

> El *Context Engineering* selecciona, organitza i manté la informació adequada perquè el model disposi del context necessari en cada moment.

---
## 📖 Referències

[LangChain Docs - Context engineering in agents](https://docs.langchain.com/oss/python/langchain/context-engineering)


