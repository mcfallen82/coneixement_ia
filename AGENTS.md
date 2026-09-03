# AGENTS.md - Governança de la wiki d'aprenentatge d'IA

## 1. Objectiu i abast

Aquest repositori és una wiki d'aprenentatge acumulatiu sobre intel·ligència artificial, aprenentatge automàtic, aprenentatge profund, models generatius, enginyeria de prompts i del context, sistemes de coneixement i automatització. Les finances i l'economia només s'hi utilitzen com a exemples d'aplicació.

## 2. Governança

Aquest és l'únic document principal de governança. S'ha de llegir abans d'actuar. Quan una skill contradigui aquest document, preval AGENTS.md.

El repositori principal és `main`. Les modificacions es fan en branques `agent/...` i s'integren mitjançant pull request.

## 3. Estructura obligatòria

```text
1. Wiki/
|-- 1.1. autors/
|-- 1.2. conceptes/
|-- 1.3. models/
`-- 1.4. llibres/
2. Skills/
3. Dashboards/
4. Templates/
index.md
log.md
hot.md
.manifest.json
scripts/wiki_lint.py
graph/
scripts/graph_scan.py
.github/workflows/wiki-lint.yml
```

- `1. Wiki/` conté fitxes permanents d'autors, conceptes, models i llibres o fonts bibliogràfiques processades.
- `2. Skills/` conté procediments reutilitzables.
- `3. Dashboards/` conté consultes i vistes.
- `4. Templates/` conté plantilles i documents de suport.
- Les fonts originals es mantenen fora del repositori públic i es referencien mitjançant URLs, bibliografia i el camp `sources`.
- Les configuracions personals d'editors, IDE o gestors de coneixement també es mantenen fora del repositori públic.
- `scripts/wiki_lint.py` és la validació executable; no substitueix la revisió humana.

## 4. Contracte de les fitxes

Tota fitxa permanent Markdown dins de `1. Wiki/`, excepte els README, ha de tenir frontmatter YAML amb:

```yaml
---
title: Nom de la fitxa
category: conceptes
tags: []
sources: []
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

`category` ha de coincidir amb la carpeta. Les fonts han de ser verificables i, sempre que sigui possible, han de ser URLs o referències bibliogràfiques externes.

## 4.1. Contracte de fonts externes

Cada font utilitzada per crear o actualitzar coneixement ha de registrar, quan sigui possible:

- títol;
- autor o organisme;
- URL o referència bibliogràfica;
- tipus de font;
- data de publicació o consulta;
- fitxes creades o actualitzades.

No s'han de pujar al repositori públic còpies locals de papers, articles, llibres, transcripcions, dossiers de recerca o notes privades de treball. Si una font no té URL pública, es pot conservar una referència bibliogràfica suficient per identificar-la.

## 4.2. Independència de l'eina local

Markdown és el format canònic compartit. El projecte no depèn d'un editor, IDE, gestor de notes ni plugin concret.

- No es versionen carpetes de configuració específiques d'aplicacions.
- No es pressuposa que els col·laboradors utilitzin la mateixa eina local.
- Les funcionalitats essencials han de continuar disponibles mitjançant Markdown, scripts del repositori o estàndards oberts.
- Els enllaços interns han de ser comprensibles i validables sense requerir configuració privada d'un editor.

## 5. Flux operatiu únic

```text
font externa -> classificació -> cerca de duplicats
             -> creació/actualització -> relacions -> índex
             -> log + hot + manifest -> wiki_lint -> revisió humana
```

Una operació d'escriptura només es considera completa quan:

1. la procedència externa queda registrada;
2. s'han creat o actualitzat les fitxes necessàries;
3. s'han actualitzat les fonts i els wikilinks;
4. s'han actualitzat `index.md`, `log.md`, `hot.md` i `.manifest.json` quan el canvi és significatiu;
5. `scripts/wiki_lint.py` retorna `PASS`;
6. s'han revisat manualment les advertències.

## 6. Regles de seguretat

- No eliminis ni fusionis fitxes sense còpia i aprovació explícita.
- No sobreescriguis fitxes existents sense comparar-les.
- No inventis autors, models, dates, arquitectures ni fonts.
- No copiïs al repositori públic materials originals que només siguin necessaris com a font de treball.
- No incorporis configuracions personals d'aplicacions al control de versions.
- Les operacions massives han de començar amb una validació en mode només lectura.

## 7. Enllaços i compatibilitat Markdown

Els wikilinks han d'apuntar a fitxers reals o a una destinació externa explícita. Els dashboards han de funcionar com a Markdown estàtic i/o com a guies per executar `scripts/wiki_lint.py` i `scripts/graph_scan.py`; no han de dependre de plugins o extensions privades d'un programa concret.

## 8. Registre i manifest

Cada canvi estructural o ingesta significativa s'ha d'afegir a `log.md`. `.manifest.json` ha d'indicar la font externa o bibliogràfica, el tipus, l'estat i les fitxes creades o actualitzades.

## 9. Validació obligatòria

Abans de donar una tasca per acabada:

- executa `python scripts/wiki_lint.py`;
- comprova estructura, README, YAML, categories, wikilinks, manifest, duplicats i estructura interna de skills;
- tracta els errors com a bloquejants;
- documenta les advertències i decisions pendents.

## 10. Capa gràfica lleugera

La wiki manté Markdown com a font principal i utilitza la carpeta `graph/` com a representació derivada. Les relacions acceptades es registren a `graph/relations.json` i s'han de poder rastrejar fins a fitxes i fonts verificables.