# impl-validator

## Finalitat

Comprovar si una reorganització, skill o fitxa compleix l’objectiu que declara.

## Protocol

1. Defineix l’objectiu i els fitxers que ha d’afectar.
2. Comprova l’estructura i el frontmatter.
3. Revisa contingut, fonts, relacions i consultes.
4. Executa les validacions disponibles.
5. Distingueix errors, advertiments i millores opcionals.

## Informe

~~~markdown
# Informe de validació
## Objectiu
## Comprovacions
| Element | Resultat | Observacions |
## Errors
## Advertiments
## Veredicte: PASS / WARN / FAIL
~~~

No validis només que un fitxer existeix: comprova que la seva informació és coherent amb la carpeta i amb AGENTS.md.