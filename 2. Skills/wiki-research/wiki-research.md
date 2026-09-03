# wiki-research

## Finalitat

Activar una recerca externa en diverses rondes i convertir-ne els resultats en coneixement permanent de ia_knowledge. La recerca ha d’identificar buits, contrastar afirmacions i produir fitxes connectades amb fonts verificables.

## Quan s’activa

S’activa quan l’usuari demana investigar, ampliar, contrastar o incorporar coneixement sobre un tema, o quan una fitxa té fonts insuficients.

## Abast i entrades

Abans de començar, llegeix `AGENTS.md`, `index.md`, `hot.md`, `.manifest.json`, les fitxes relacionades de `1. Wiki/` i les skills pertinents.

Defineix:

- tema i pregunta principal;
- 3–5 angles de recerca;
- fitxes que ja existeixen;
- buits que es volen cobrir;
- nivell de profunditat i data de tall.

Les fonts consultades es registren com a **fonts externes** mitjançant URL o referència bibliogràfica. No s’emmagatzemen còpies locals al repositori públic.

## Jerarquia de fonts

Prioritza:

1. paper original o especificació primària;
2. documentació oficial;
3. repositori oficial;
4. curs universitari o tutorial de l’autor;
5. revisió acadèmica o font pedagògica autoritzada;
6. articles divulgatius, només per completar context.

Registra sempre l’URL, el títol, l’autor o organisme, la data de consulta i el paper que ha tingut en la síntesi.

## Ronda 1 — mapa general

Divideix el tema en 3–5 angles i registra afirmacions, conceptes nous, models o autors, aplicacions, limitacions i preguntes obertes.

## Ronda 2 — buits i contrast

Busca contradiccions, limitacions, afirmacions amb una sola font i diferències entre arquitectura, tècnica, model, eina i aplicació.

## Ronda 3 — síntesi i decisió

| Resultat | Acció |
|---|---|
| idea diferenciada | crear o actualitzar fitxa de `conceptes` |
| arquitectura o model | crear o actualitzar fitxa de `models` |
| persona o organisme rellevant | crear o actualitzar fitxa d’`autors` |
| llibre rellevant | crear o actualitzar fitxa de `llibres` |
| font útil però no substantiva | conservar URL o referència al manifest i a `sources` |
| connexió entre fitxes | afegir wikilinks i relacions |
| desacord no resolt | registrar-lo com a qüestió oberta |

## Contracte de sortida

Una recerca completa produeix:

1. una llista de fonts externes verificables;
2. fitxes actualitzades o noves dins de `1. Wiki/`;
3. fonts i relacions al frontmatter;
4. una entrada a `index.md`, `log.md`, `hot.md` i `.manifest.json` quan sigui significativa;
5. una comprovació amb `python scripts/wiki_lint.py`.

La fitxa permanent ha de separar fets documentats, explicació pedagògica, inferències, limitacions i preguntes obertes.

## Criteri de confiança

- **alta**: coincideixen fonts primàries o oficials independents;
- **mitjana**: hi ha una font sòlida, però falta contrast;
- **baixa**: és una inferència, una font secundària o un resultat controvertit.

## Informe de recerca

L’informe final ha d’indicar pregunta i abast, rondes completades, fonts principals, fitxes creades o actualitzades, contradiccions, buits pendents, confiança i resultat del `wiki-lint`.
