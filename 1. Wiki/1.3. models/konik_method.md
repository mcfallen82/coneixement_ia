---
title: Konik Method
category: models
node_id: "model:konik_method"
node_type: "model"
model_family: image_generation_workflow
architecture: cookbook_method
authors:
  - "[[Ghelbur, Eugeniu]]"
tags:
  - model
  - imatge
sources:
  - https://github.com/eugeniughelbur/gpt-image-cookbook
status: active
created: 2026-05-30
updated: 2026-08-13
---
# GPT IMAGE COOKBOOK

Caixa d’eines per generar imatges amb **IA** de manera més estructurada que no pas escrivint prompts improvisats. El repositori combina tres peces: 

- Galeria de *[[prompt]]*
- Habilitat agentiva en format `SKILL.md` 
- Interfície de línia d’ordres en Python anomenada `gic`. 

L’objectiu és treballar amb diversos proveïdors d’imatge —**OpenAI `gpt-image-2`**, **Google Imagen** i **Flux** via **fal.ai** o **Replicate**— sota una mateixa lògica de treball.

La idea important és que la generació d’imatges es tracta com una recepta reutilitzable, no com un acte creatiu puntual. En lloc de demanar “fes-me una imatge bonica”, el projecte afavoreix *prompts* més sistemàtics: estil visual, composició, ús del color, relació entre subjectes, proporció, format, referències visuals, variants i criteris de qualitat. 

Això encaixa molt amb una manera de treballar tipus *cookbook*: acumules patrons que funcionen, els classifiques i els reaprofites segons el cas.

El projecte també dona suport a diversos fluxos visuals: *text-to-image*, edició amb imatge de referència, *inpainting* i treball amb múltiples imatges de referència. Això vol dir que no serveix només per crear una imatge des de zero, sinó també per iterar sobre una identitat visual, modificar elements concrets o mantenir certa coherència entre diferents peces. 

Aquesta part és especialment interessant per a sistemes de treball on vols repetir una estètica: portades, icones, infografies, personatges, escenes o materials visuals d’una mateixa línia gràfica.

La capa `SKILL.md` és rellevant perquè converteix el repositori en una eina utilitzable per agents com **Claude Code**, **Codex**, **OpenClaw** o **Hermes**. 

En lloc de tenir només *scripts*, el projecte inclou instruccions perquè un agent sàpiga quan activar la generació d’imatges, com preparar el *prompt*, com escollir proveïdor, com gestionar referències i com retornar resultats. Dit d’una altra manera: el repositori no només guarda exemples, sinó que intenta codificar un procediment de treball visual.

Per a una *vault* manual d’*Obsidian*, la lectura pràctica seria aquesta: no cal copiar tota la part tècnica, però sí la filosofia. Pots crear una carpeta de “receptes visuals” amb notes per a estils, prompts reutilitzables, formats d’imatge, criteris de composició, paletes, exemples bons i errors habituals. Si fas servir **Obsidian** per pensar i documentar projectes, aquest repositori apunta cap a una idea potent: tractar la generació d’imatges com una biblioteca de processos visuals acumulatius, no com una conversa efímera amb un model.
