# wiki-status

## Finalitat

Mostrar l'estat de la wiki: fonts externes pendents, fitxes recents, canvis i buits de cobertura.

## Comprovacions

1. Llegeix `.manifest.json`.
2. Revisa l'estat de les fonts externes registrades (`pending`, `processed` o equivalent) i comprova que conserven una URL o referència verificable.
3. Identifica fonts pendents de processar o entrades del manifest que ja no tenen una referència vàlida.
4. Revisa fitxes amb `status: draft`, sense `sources` o sense enllaços.
5. Compara `updated` de les fitxes amb les darreres entrades de `log.md`.
6. Resumeix les prioritats següents.

## Informe

~~~markdown
# Estat de la wiki — YYYY-MM-DD

## Resum
## Fonts pendents de processar
## Fitxes recents
## Fitxes incompletes
## Relacions febles o fitxes orfes
## Prioritats següents
~~~

No consideris una font processada només perquè existeixi al manifest: ha de tenir un estat coherent i indicar les fitxes creades o actualitzades quan correspongui.
