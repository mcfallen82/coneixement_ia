---
title: Obsidian Wiki
category: models
node_id: "model:obsidian_wiki"
node_type: "model"
model_family: knowledge_management
architecture: obsidian_agent_wiki
authors:
  - "[[Arnav]]"
tags:
  - model
  - wiki
sources:
  - https://github.com/Ar9av/obsidian-wiki/tree/main
status: active
created: 2026-06-30
updated: 2026-08-13
---
# OBSIDIAN WIKI

Implementació operativa i “productitzada” de la idea de **[[llm_wiki|Wiki amb LLM de Karpathy]]**. **Arnav** ofereix un marc tècnic perquè diversos agents d’**IA** puguin crear, mantenir, consultar i revisar un *vault* d’**Obsidian**. 

La idea base és: el coneixement s'ha d'acumular en fitxers *Markdown* interconnectats, visibles a **Obsidian** i controlats per l’usuari. La *vault* s'ha de convertir en un [[second_brain]] que recorda allò que has après, ho connecta amb el que ja sabies i respon quan li preguntes.

---
## 🛠️ Caixa d'eines

La diferència principal amb el model conceptual de **Karpathy** és que aquí hi ha una capa d’eines concretes:
- Instal·lació amb `pip`, 
- configuració de *vault*, 
- ordres de terminal, 
- fitxers d’instruccions per agents 
- i habilitats especialitzades. 

El sistema pot inicialitzar l’estructura de la *vault*, crear índexs, mantenir registres, detectar canvis, revisar enllaços trencats i consultar el contingut.

També és compatible amb molts entorns d’agents ([[1. Wiki/1.2. conceptes/AGENTS_MD|`AGENTS.md`]]) — **Claude Code**, **Cursor**, **Windsurf**, **Codex**, **Gemini CLI**, **Kiro** i altres— cadascun amb els seus fitxers de context o directoris d’habilitats.

---
## 🌊 Flux de treball

El flux de treball està dividit en quatre fases: 

**Ingesta** ➡️ **Extracció d’informació** ➡️ **Fusió** ➡️ **Esquema**. 

Els processos són els següents:

1. **Ingesta:** L’agent llegeix materials diversos: *Markdown*, PDF, registres de conversa, transcripcions, imatges o notes en brut. 
2. **Extracció:** L'agent extreu conceptes, entitats, afirmacions, relacions i preguntes obertes.
3. **Fusió:** Fusiona aquest coneixement amb el que ja existeix: si una pàgina ja existeix, l’actualitza; si el concepte és nou, en crea una de nova.
4. **Esquema:** L'esquema de la *wiki* no queda fixat des del principi, sinó que evoluciona amb les fonts i els dominis que s’hi incorporen.

---

## ⚙️ Mecanismes de millora

El projecte afegeix mecanismes que fan la *vault* més robusta: 

- un `.manifest.json` per saber quines fonts ja han estat ingerides i processar només els canvis;
- una carpeta `_raw/` per deixar-hi captures o notes pendents; 
- eines de revisió per trobar pàgines òrfenes, contradiccions, metadades incompletes o enllaços trencats;
- taxonomia de tags; 
- traçabilitat de les afirmacions; 
- exportació del graf de coneixement; 
- i consulta escalonada, on el sistema mira primer títols, etiquetes i resums abans d’obrir pàgines senceres.

També pot incorporar cerca semàntica opcional amb [[QMD]], però el repositori diu que sense QMD continua funcionant amb cerques locals més simples.

---
## 💪 Aplicació pràctica

Per a una *vault* manual d’**Obsidian**, la lectura pràctica és aquesta: **[[Arnav]]** converteix la intuïció del model de **[[llm_wiki|Karpathy]]** en una caixa d’eines. No és imprescindible adoptar-ho tot. El nucli que val la pena copiar manualment és:
- Fonts originals separades
- Notes *Markdown* interconnectades
- Índex, registre
- Carpeta d’entrada `_raw/`
- Metadades bàsiques
- Revisió periòdica d’enllaços
- Una norma clara per decidir quan es crea una nota nova o quan s’actualitza una d’existent. 

La part més sofisticada —agents, ordres, manifest, sincronització, cerca semàntica i auditoria automàtica— pot quedar per a una segona fase, quan la *vault* ja tingui prou volum per justificar automatització.

---
## 📖 Documents de suport

**[Plantilla Wiki Obsidian Neutra](../../4.%20Templates/90.2.%20docs_support/plantilla_wiki_neutra_replicable.md)** - Plantilla per a la creació de *wikis* neutres per a qualsevol tipus de **[[LLM]]**
**[Plantilla Wiki Obsidian Beagle AI](../../4.%20Templates/90.2.%20docs_support/resum_ar9av_obsidian_wiki_beagle_ai.md)** - Plantilla per a la posada en marxa del projecte **Beagle AI**.

---
## Referències

Models derivats o inspirats en **Obsidian Wiki**

**[[1. Wiki/1.3. models/obsidian_second_brain_karpathy_rebuilt|Obsidian Second Brain]]**
