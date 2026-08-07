---
tags:
  - concepte
estat: ok
---
# 🛠️ Prompt Engineering

## Resum sintètic

El **prompt engineering**, o **enginyeria de prompts**, és el procés sistemàtic de dissenyar, provar, avaluar i millorar instruccions perquè produeixin resultats útils de manera consistent.

Parteix d’un primer prompt i utilitza criteris d’èxit i proves repetibles per identificar errors, comparar versions i introduir millores.

**Pregunta principal:**

> Com dissenyo, provo i milloro una instrucció?

---
## 💡 Idea central

L’enginyeria de prompts transforma una instrucció inicial en un sistema més fiable i reutilitzable.

El procés combina:

```
Dissenyar
   ↓
Provar
   ↓
Avaluar
   ↓
Detectar errors
   ↓
Modificar
   ↓
Comparar
```

La millora necessita tres punts de partida:

- un objectiu clar;
- criteris que defineixin l’èxit;
- una manera de provar els resultats.

---
## 🧩 Elements principals

|Element|Funció|
|---|---|
|**Rol**|Orienta el tipus d’anàlisi|
|**Objectiu**|Defineix la tasca|
|**Font autoritzada**|Delimita les dades utilitzables|
|**Estructura**|Organitza la resposta|
|**Restriccions**|Redueixen desviacions|
|**Criteris**|Defineixen una bona resposta|
|**Format**|Facilita reutilitzar el resultat|

L’enginyeria afegeix una capa de **disseny, experimentació i control de qualitat**.

---
## 🔄 Procés de millora

Una pràctica habitual és:

1. Crear una primera versió.
2. Provar-la amb diversos casos.
3. Comparar els resultats amb els criteris definits.
4. Identificar errors i inconsistències.
5. Modificar una part concreta.
6. Tornar a executar les proves.

El valor apareix en la comparació sistemàtica entre versions.

---
## 🧪 Fase 2 - Prompt Engineering

Aprèn:

- plantilles reutilitzables;
- variables;
- exemples de resposta;
- criteris d’avaluació;
- conjunts de proves;
- control de versions.

Les plantilles i les variables permeten reutilitzar una mateixa estructura amb dades diferents. Les eines d’avaluació faciliten comparar resultats i detectar regressions.

---
## ⚠️ Errors habituals

- modificar moltes instruccions alhora;
- provar el prompt amb un únic exemple;
- valorar les respostes sense criteris definits;
- confondre una resposta bona amb un sistema fiable;
- perdre l’historial de versions;
- afegir complexitat sense comprovar que millora el resultat.

Cada modificació hauria de respondre a un error observat o a un objectiu mesurable.

---
## 🗺️ Lectura pràctica

Exemple aplicat a un extractor SEC:

> Convertir l’extractor en un sistema amb deu documents de prova i una rúbrica comuna.

La rúbrica podria valorar:

- exactitud de les dades;
- fidelitat a les fonts;
- separació entre fets i inferències;
- compliment del format;
- consistència entre documents.

Aquesta pràctica permet comparar versions i comprovar si una modificació produeix una millora real.

---
## 🧭 Frase resum

> El *Prompt Engineering* converteix la millora d’un [[prompt]] en un procés sistemàtic de disseny, prova, avaluació i control de versions.
