# 4. Templates

Aquesta carpeta agrupa les **estructures reutilitzables** del projecte. Té dues funcions diferenciades: ajudar a crear peces de coneixement homogènies i conservar documents base per dissenyar noves bases de coneixement assistides per IA.

El contingut de `4. Templates/` no és coneixement temàtic permanent de la wiki. La seva funció és definir **com representar coneixement** i **com construir el sistema que el contindrà**.

## Què hi trobaràs?

| Carpeta | Funció | Quan utilitzar-la |
|---|---|---|
| [`90.1. templates_fitxes/`](90.1.%20templates_fitxes/) | Plantilles per crear fitxes homogènies de conceptes, models, autors, fonts i resums. | Quan crees o normalitzes peces de coneixement dins d'una wiki. |
| [`90.2. docs_support/`](90.2.%20docs_support/) | Biblioteca de documents base per dissenyar i crear noves bases de coneixement vinculades a una IA sobre qualsevol domini. | Quan vols definir l'arquitectura, governança, recerca, relacions, validació i fluxos d'una wiki nova. |

## Dues capes complementàries

```text
90.2. docs_support
Dissenya la base de coneixement
        ↓
90.1. templates_fitxes
Defineix com s'escriuen les peces de coneixement
        ↓
Wiki específica del nou domini
```

`90.2` treballa a nivell de **sistema**. Els seus documents han de ser reutilitzables per crear una wiki nova sobre IA, finances, història, dret, ciència o qualsevol altra matèria.

`90.1` treballa a nivell de **document**. Les seves plantilles ajuden a mantenir una estructura coherent un cop la base de coneixement ja té definida la seva arquitectura.

## Relació amb la resta del projecte

- [`1. Wiki/`](../1.%20Wiki/) conté el coneixement permanent d'aquest projecte concret.
- [`2. Skills/`](../2.%20Skills/) descriu els procediments operatius per investigar, ingerir, actualitzar i validar contingut.
- [`90.2. docs_support/`](90.2.%20docs_support/) extreu els patrons generalitzables del projecte perquè puguin servir de base a altres wikis.
- [`AGENTS.md`](../AGENTS.md) defineix la governança del repositori actual.

## Principi general

**Les plantilles defineixen la forma de les peces; `docs_support` defineix el patró del sistema.**

Els documents de `90.2` han de tendir a ser independents del tema i de l'eina local, comprensibles per una persona i útils com a context estructural per a una IA o agent.
