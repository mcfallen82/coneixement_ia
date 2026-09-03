# wiki-status

## Finalitat

Mostrar l’estat de la wiki: fonts pendents, fitxes recents, canvis i buits de cobertura.

## Comprovacions

1. Llegeix .manifest.json.
2. Compara les fonts registrades amb 0. Raw/.
3. Identifica fonts noves, modificades, processades o desaparegudes.
4. Revisa fitxes amb status draft, sense sources o sense enllaços.
5. Compara updated de les fitxes amb les darreres entrades de log.md.
6. Resumeix les prioritats següents.

## Informe

~~~markdown
# Estat de la wiki — YYYY-MM-DD

## Resum
## Fonts noves
## Fonts pendents de processar
## Fitxes recents
## Fitxes incompletes
## Relacions febles o fitxes orfes
## Prioritats següents
~~~

No consideris una font processada només perquè existeixi al manifest: ha de tenir status processed i indicar les fitxes creades o actualitzades.
