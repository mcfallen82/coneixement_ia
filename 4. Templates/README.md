# 4. Templates

Aquesta carpeta agrupa dos tipus de recursos reutilitzables del projecte:

1. **plantilles per donar forma a les peces de coneixement**;
2. **documents base per dissenyar noves bases de coneixement assistides per IA**.

El contingut de `4. Templates/` no és coneixement temàtic permanent de la wiki. La seva funció és definir **com representar el coneixement** i **com construir el sistema que el contindrà**.

## Què hi trobaràs?

| Carpeta | Funció | Quan utilitzar-la |
|---|---|---|
| [`90.1. templates_fitxes/`](90.1.%20templates_fitxes/) | Plantilles per crear fitxes homogènies de conceptes, models, autors, fonts i resums. | Quan crees una peça nova de coneixement o normalitzes una fitxa existent. |
| [`90.2. docs_support/`](90.2.%20docs_support/) | Biblioteca de patrons per crear una nova base de coneixement vinculada a una IA o agent. | Quan vols definir arquitectura, governança, recerca, procedència, grafs o fluxos d'una wiki nova sobre qualsevol domini. |

## Diferència entre `90.1` i `90.2`

```text
90.2 docs_support
      ↓
defineix el sistema
      ↓
90.1 templates_fitxes
      ↓
defineix la forma de les peces
      ↓
Wiki especialitzada en un domini
```

`90.2` respon preguntes com **“quina arquitectura necessita aquesta nova base de coneixement?”**. `90.1` respon **“quina estructura ha de tenir aquesta fitxa?”**.

## Relació amb la resta del projecte

- [`1. Wiki/`](../1.%20Wiki/) conté el coneixement permanent del projecte actual.
- [`2. Skills/`](../2.%20Skills/) descriu procediments operatius reutilitzables.
- [`AGENTS.md`](../AGENTS.md) defineix la governança del repositori actual.
- [`3. Dashboards/`](../3.%20Dashboards/) ajuda a revisar l'estat del coneixement generat.

Els documents de `90.2` poden reutilitzar patrons d'aquests components, però s'han de redactar de forma **generalitzable** perquè serveixin per iniciar projectes nous i no només per descriure `coneixement_ia`.

## Principi general

**`90.1` dona forma al coneixement; `90.2` dona forma al sistema de coneixement.**

Cap plantilla o document de suport substitueix la verificació de fonts ni la revisió humana.