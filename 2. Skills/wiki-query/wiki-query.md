# wiki-query

## Finalitat

Respondre preguntes utilitzant el coneixement compilat de `1. Wiki/`, sense inventar informació i sense modificar el repositori.

## Protocol de recuperació

1. Llegeix `AGENTS.md` i `index.md`.
2. Cerca primer títols, tags, resums i noms d'autors o models.
3. Revisa les fitxes directament relacionades.
4. Segueix els wikilinks quan calgui entendre una relació.
5. Si la wiki no resol la pregunta o cal contrastar l'origen, consulta les URLs o referències bibliogràfiques registrades a `sources` i al manifest; activa `wiki-research` si cal una recerca nova.
6. Sintetitza la resposta i indica les fitxes utilitzades.

## Regles

- Aquesta skill és de lectura: no modifica la wiki.
- Distingeix entre informació present a la wiki i inferències.
- Si les fonts discrepen, exposa la discrepància.
- Si no hi ha prou informació, indica-ho i proposa quina font o fitxa caldria incorporar.

## Resposta recomanada

~~~text
Resposta breu
## Evidència a la wiki
## Relacions rellevants
## Incerteses o buits
## Fitxes consultades
~~~

Per a consultes complexes, construeix una taula d'evidències: afirmació, fitxa o font, confiança i observacions.
