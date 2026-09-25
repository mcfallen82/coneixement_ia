# 🧠 Evolució assistida de la memòria

## Per què existeix?

Aquesta skill afegeix una revisió de **notes relacionades després d'una ingesta**. Pren la idea d'A-MEM —una nota nova pot canviar com interpretem les antigues— i l'adapta a una wiki pública de coneixement sobre IA. El resultat és una proposta verificable de connexions i millores contextuals.

## 🗂️ Contingut i encaix

- [Procediment complet](memory-evolution.md): selecció de candidates, comprovació semàntica, revisió de notes antigues i acceptació de canvis.
- [Script de candidates](../../scripts/memory_candidates.py): llegeix fitxes Markdown i retorna coincidències lèxiques en JSON, sense escriure al repositori.
- [Model A-MEM](../../1.%20Wiki/1.3.%20models/A-MEM.md): font de la inspiració; l'adaptació d'aquí no reprodueix els seus embeddings ni els seus experiments.

S'utilitza **després** de [wiki-ingest](../wiki-ingest/README.md) o [wiki-update](../wiki-update/README.md), i **abans** de consolidar enllaços amb [cross-linker](../cross-linker/README.md) i relacions tipades amb [graph-layer](../graph-layer/README.md). La wiki i les fonts verificables continuen sent la referència principal.

## 🧭 Com començar

Des de l'arrel, executa `python scripts/memory_candidates.py --note '1. Wiki/1.3. models/A-MEM.md' --top-k 5`. Llegeix les fitxes candidates i aplica el [procediment](memory-evolution.md) només a les relacions que puguis explicar i justificar amb fonts. Un valor de semblança no acredita cap relació conceptual.

## ✍️ Manteniment

En modificar aquest procés, conserva la sortida en mode lectura, l'absència de serveis obligatoris i la distinció entre una proposta automàtica i una relació acceptada. Verifica les rutes, els exemples i les [normes del projecte](../../AGENTS.md).
