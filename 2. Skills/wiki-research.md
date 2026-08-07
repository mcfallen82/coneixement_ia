# wiki-research

## Finalitat

Activar una recerca externa en diverses rondes i convertir-ne els resultats en coneixement permanent de ia_knowledge. La recerca no és una simple recopilació d’enllaços: ha d’identificar buits, contrastar afirmacions i produir fitxes connectades.

## Quan s’activa

S’activa quan l’usuari demana investigar, ampliar, contrastar o incorporar coneixement sobre un tema. També s’activa quan una fitxa té fonts insuficients, afirmacions no contrastades o preguntes obertes rellevants.

## Abast i entrades

Abans de començar, llegeix:

1. `AGENTS.md`;
2. `index.md`, `hot.md` i `.manifest.json`;
3. les fitxes relacionades de `1. Wiki/`;
4. aquesta skill i `wiki-ingest`, `wiki-update`, `wiki-dedup` i `cross-linker`.

Defineix per escrit:

- tema i pregunta principal;
- 3–5 angles de recerca;
- fitxes que ja existeixen;
- buits que es volen cobrir;
- nivell de profunditat i data de tall.

El material consultat es conserva a `0. Raw/0.2./`. Les fitxes permanents només es creen o actualitzen després de comparar-les amb el contingut existent.

## Jerarquia de fonts

Prioritza, en aquest ordre:

1. paper original o especificació primària;
2. documentació oficial del desenvolupador o organisme;
3. repositori oficial;
4. curs universitari o tutorial de l’autor;
5. revisió acadèmica o font pedagògica autoritzada;
6. articles divulgatius, només per completar context.

No utilitzis fragments de cercadors com a font final. Registra sempre l’URL, el títol, l’autor o organisme, la data de consulta i el paper que ha tingut en la síntesi.

## Ronda 1 — mapa general

Divideix el tema en 3–5 angles. Per a cada angle, consulta fonts amb formulacions diferents i registra:

- afirmacions explícites;
- conceptes nous;
- models o autors;
- aplicacions;
- limitacions;
- preguntes que la font no resol.

Atura la ronda quan cada angle tingui almenys una font primària o oficial i una font pedagògica, si existeix.

## Ronda 2 — buits i contrast

Busca específicament:

- afirmacions importants que només tenen una font;
- contradiccions entre fonts;
- limitacions i casos en què el mètode falla;
- diferències entre arquitectura, tècnica, model, eina i aplicació;
- conseqüències pràctiques per a documents, dades i sistemes de coneixement.

No ampliïs el tema indefinidament. L’objectiu és resoldre els buits que afecten la comprensió de la wiki.

## Ronda 3 — síntesi i decisió

Decideix per a cada resultat:

| Resultat | Acció |
|---|---|
| idea diferenciada | crear o actualitzar fitxa de `conceptes` |
| arquitectura o model | crear o actualitzar fitxa de `models` |
| persona o organisme rellevant | crear o actualitzar fitxa d’`autors` |
| font útil però no substantiva | conservar només a `0. Raw/` i al manifest |
| connexió entre fitxes | afegir wikilinks i relacions |
| desacord no resolt | registrar-lo com a qüestió oberta |

Atura la recerca després de tres rondes o quan cada angle estigui cobert i les preguntes obertes siguin explícites.

## Contracte de sortida

Una recerca completa produeix:

1. un dossier a `0. Raw/0.2./` amb l’abast, les rondes, les fonts i les conclusions;
2. fitxes actualitzades o noves dins de `1. Wiki/`;
3. fonts i relacions bidireccionals al frontmatter;
4. una entrada a `index.md`, `log.md`, `hot.md` i `.manifest.json`;
5. una comprovació amb `python scripts/wiki_lint.py`.

La fitxa permanent ha de separar:

- fets documentats;
- explicació pedagògica;
- inferències;
- limitacions;
- preguntes obertes.

## Criteri de confiança

Assigna una confiança qualitativa a cada conclusió:

- **alta**: coincideixen fonts primàries o oficials independents;
- **mitjana**: hi ha una font sòlida, però falta contrast;
- **baixa**: és una inferència, una font secundària o un resultat controvertit.

No converteixis la confiança en una precisió numèrica falsa.

## Enllaços i no-duplicació

Abans de crear una fitxa:

- comprova títols, sinònims i grafies en català i anglès;
- busca si el contingut ja apareix en una fitxa existent;
- amplia la fitxa existent quan la identitat sigui la mateixa;
- crea una fitxa nova només quan hi hagi una unitat de coneixement clarament diferenciada.

Cada fitxa nova ha d’enllaçar com a mínim amb dues fonts quan sigui possible i amb les fitxes relacionades. Les relacions importants han de funcionar en totes dues direccions.

## Informe de recerca

L’informe final ha d’indicar:

- pregunta i abast;
- rondes completades;
- fonts principals;
- fitxes creades i actualitzades;
- contradiccions;
- buits pendents;
- confiança;
- resultat del `wiki-lint`.