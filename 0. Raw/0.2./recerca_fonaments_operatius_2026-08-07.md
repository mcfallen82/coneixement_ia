# Recerca: fonaments operatius dels LLM

- Data de consulta: 2026-08-07
- Pregunta: quins conceptes falten per entendre el cicle complet d’un sistema basat en LLM?
- Abast: ajustament, alineament, adaptació eficient i avaluació.
- Ronda 1: mapa de fonts primàries sobre RAG, LoRA, Adam, InstructGPT, Self-Instruct i MMLU.
- Ronda 2: contrast de mecanismes, costos, limitacions i diferència entre entrenar, adaptar i avaluar.
- Ronda 3: selecció de fitxes permanents i connexions amb Transformer, atenció i raonament documental.

## Fonts principals

| Font | Tipus | Aportació | Confiança |
|---|---|---|---|
| https://arxiv.org/abs/1706.03762 — Attention Is All You Need | paper original | arquitectura Transformer i atenció | alta |
| https://arxiv.org/abs/2106.09685 — LoRA | paper original | adaptació amb matrius de baix rang | alta |
| https://arxiv.org/abs/2005.11401 — RAG | paper original | combinació de memòria paramètrica i recuperació | alta |
| https://arxiv.org/abs/1412.6980 — Adam | paper original | optimització amb moments adaptatius | alta |
| https://arxiv.org/abs/2203.02155 — InstructGPT | paper original | ajustament supervisat, preferències i RLHF | alta |
| https://arxiv.org/abs/2212.10560 — Self-Instruct | paper original | generació de dades d’instruccions | alta |
| https://arxiv.org/abs/2009.03300 — MMLU | paper original | avaluació multidisciplinària | alta |
| https://platform.openai.com/docs/api-reference/evals | documentació oficial | estructura d’avaluacions i criteris | alta |

## Conclusions

1. El preentrenament, l’ajustament, la recuperació i l’avaluació són processos diferents. Confondre’ls porta a atribuir al model problemes que en realitat provenen de les dades, el context o el sistema.
2. LoRA redueix el cost d’adaptar un model perquè manté congelats els pesos principals i entrena una actualització de baix rang. És una tècnica d’adaptació, no una arquitectura independent.
3. RAG resol una part del problema de coneixement extern mitjançant recuperació, però no garanteix que el model utilitzi bé els fragments recuperats.
4. L’alineament millora la resposta a instruccions i preferències, però pot introduir compromisos entre utilitat, veracitat, seguretat i generalització.
5. Un benchmark general no substitueix una avaluació pròpia. Per a una wiki o una eina d’anàlisi documental calen exemples representatius, criteris explícits i comprovació de fonts.

## Fitxes incorporades

- 1. Wiki/1.2. conceptes/ajust_fi.md
- 1. Wiki/1.2. conceptes/alineament_dels_llm.md
- 1. Wiki/1.2. conceptes/avaluacio_de_models.md
- 1. Wiki/1.3. models/LoRA.md

## Buits pendents

- quantització i inferència eficient;
- mètriques específiques per a RAG;
- contaminació de benchmarks i validesa externa;
- diferència pràctica entre SFT, RLHF i DPO.