---
tags:
  - concepte
estat: ok
---
# 💬 Prompting

## Resum sintètic

El **prompting** és l’acte de donar una instrucció, pregunta o conjunt d’indicacions a un model d’intel·ligència artificial.

Un **[[prompt]]** és el missatge concret que rep el model. El prompting consisteix a formular aquest missatge de manera que el model entengui què ha de fer i quin resultat s’espera.

**Pregunta principal:**

> Què li demano al model?

---
## 💡 Idea central

Un bon *prompting* transforma una intenció en una petició clara i accionable.

La qualitat de la resposta depèn sobretot de cinc elements:

- objectiu;
- informació disponible;
- tasca concreta;
- format de sortida;
- criteris o límits.

La claredat aporta més valor que la longitud.

---
## 🏗️ Prompting pràctic

Les habilitats principals són:

- escriure instruccions clares;
- delimitar la tasca;
- indicar el format de resposta;
- aportar exemples quan siguin útils;
- definir restriccions;
- separar dades, interpretacions i inferències;
- revisar i concretar les respostes.

Una estructura senzilla és:

```
Objectiu
+
Informació
+
Tasca
+
Format
+
Criteris
```

Exemple:

> Analitza aquest fragment d’un informe anual. Identifica els principals riscos operatius i presenta’ls en una taula amb les columnes: risc, causa i impacte. Diferencia la informació explícita de les inferències.

---
## 🔄 Prompting iteratiu

La primera resposta pot servir com a punt de partida.

Un procés habitual és:

```
Explorar
   ↓
Seleccionar
   ↓
Aprofundir
   ↓
Revisar
   ↓
Transformar
```

Exemple:

1. Explica el model de negoci.
2. Identifica els principals riscos.
3. Desenvolupa el risc més rellevant.
4. Revisa quines conclusions tenen menys evidència.
5. Converteix el resultat en una nota Markdown.

Una bona pràctica és crear tres versions d’un mateix *prompt* i comparar els resultats.

---
## ⚠️ Errors habituals

### Pensar que un prompt llarg és millor

Un prompt extens pot afegir precisió, però també pot introduir:

- contradiccions;
- informació irrellevant;
- redundància;
- prioritats poc clares.

L’objectiu és aportar informació útil.

### Demanar un rol sense definir la tasca

Una tasca concreta orienta millor el resultat que una descripció genèrica.

> Analitza els factors que expliquen l’evolució del marge brut i diferencia els factors temporals dels estructurals.

### Donar molts documents sense definir què cal buscar

La pregunta ha d’indicar quina informació és rellevant.

> Compara els factors de risc dels informes de 2024 i 2025 i identifica els canvis principals.

### Confiar en una única resposta

La revisió permet:

- detectar omissions;
- corregir errors;
- ampliar idees;
- demanar evidències;
- reformular conclusions.

---
## 🧩 Conceptes destacats

- **Prompt:** missatge o instrucció enviada al model.
- **Prompting:** activitat de formular prompts i utilitzar les respostes per avançar en una tasca.
- **Format de sortida:** estructura esperada de la resposta.
- **Restricció:** límit aplicat al contingut o a la forma.
- **Iteració:** nova petició que concreta, amplia o revisa una resposta anterior.

---
## 🗺️ Lectura pràctica

Abans d’enviar un prompt, comprova:

1. Què vull obtenir?
2. Quina informació necessita el model?
3. Quina tasca ha de realitzar?
4. Com vull rebre la resposta?
5. Quins criteris ha de respectar?

La pràctica més útil és començar amb una petició clara i afegir precisió només quan sigui necessària.

---
## 🧭 Frase resum

> El prompting converteix una intenció en una petició clara i utilitza la conversa per construir progressivament una resposta útil.

---
## Similars i evolucions

[[prompt_engineering]]
[[context_engineering]]
