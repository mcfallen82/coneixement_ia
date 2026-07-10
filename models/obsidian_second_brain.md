---
autor: "[[Ghelbur, Eugeniu]]"
font: https://github.com/eugeniughelbur/obsidian-second-brain
data: 2026-07-07
tags:
  - model
  - wiki
descripcio: Evolució del patró wiki amb LLM de Karpathy
estat: ok
---
# OBSIDIAN SECOND BRAIN

Evolució ambiciosa del patró **[[llm_wiki|LLM Wiki]]** de **[[Karpathy, Andrej|Karpathy]]** aplicat a **Obsidian**. 

La idea és tenir una *vault* que “es reescriu”. Quan entra una font nova, els sistema afegeix les pàgines corresponetns, actualitza les existents, revisa afirmacions antigues, substitueix informació obsoleta i intenta reconciliar contradiccions.

És una eina per convertir **Obsidian** en un “second brain” orientat a IA, compatible amb **Claude Code**, **Codex CLI**, **Gemini CLI**, **OpenCode**, **Hermes i Pi**.

La diferència principal respecte una *vault* manual és el grau d’automatització. 

Inclou desenes d’ordres per capturar notes, fer recerca, sintetitzar idees, revisar la salut de la *vault*, detectar contradiccions, generar resums de vídeos o podcasts, consultar informació prèvia i fins i tot documentar bases de codi amb *[[obsidian_architect]]*. 

També incorpora agents programats ([[conceptes/Agents_MD|`AGENTS.md`]]) per fer manteniment nocturn, revisions setmanals, comprovacions de contradiccions i controls de qualitat de la *vault*. 

En altres paraules: no és només una estructura de carpetes, sinó un sistema d’agents al voltant d’**Obsidian**.

---
## [[ai_first_vault|AI-first vault]]

Les notes estan pensades perquè una **IA** les pugui recuperar, entendre i reutilitzar millor en el futur. Això implica [[frontmatter]], enllaços interns obligatoris, marques de recència, fonts conservades, nivells de confiança i una estructura més explícita. 

És una diferència de filosofia: **Obsidian** passa a ser una base de coneixement optimitzada perquè un model hi treballi.

El projecte també dona importància a la **recerca vault-first**. Abans d’anar a buscar informació nova a Internet, el sistema primer revisa la *vault*, identifica buits i després proposa cerques externes. Això converteix la *vault* en el punt de partida de qualsevol investigació i evita molta feina.

També té una doble via: una cerca oberta al web i una cerca fonamentada en la pròpia *vault*, pensada per comparar novetats, confirmacions, contradiccions i actualitzacions necessàries.

---
## Aplicació pràctica

Per a una *vault* manual d’**Obsidian**, el més útil és quedar-se amb quatre idees bones: 

- les notes han d’actualitzar coneixement existent, no només acumular-se; 
- cada afirmació important hauria de tenir font, data o nivell de confiança; 
- cal revisar contradiccions i informació antiga; 
- i la vault ha de servir per pensar millor, no només per guardar retalls. 

La versió manual seria: índex clar, notes amb metadades, enllaços interns, registre de canvis, revisions periòdiques i una norma molt simple: 

> *Abans de crear una nota nova, mira si pots millorar una nota existent.*