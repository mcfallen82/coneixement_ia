# daily-update

## Finalitat

Executar una revisió periòdica de la wiki i mantenir sincronitzats fonts, fitxes i fitxers de control.

## Cicle

1. Revisa fonts noves o modificades a 0. Raw/.
2. Consulta el manifest i identifica pendents.
3. Executa wiki-ingest o wiki-update quan correspongui.
4. Actualitza index.md, log.md i hot.md.
5. Executa wiki-lint.
6. Resumeix errors, fitxes incompletes i prioritats següents.

## Informe

~~~markdown
# Actualització de la wiki — YYYY-MM-DD
## Fonts processades
## Fitxes creades o actualitzades
## Problemes detectats
## Prioritats següents
~~~

No modifiquis contingut només per fer activitat: si no hi ha canvis, registra que la revisió ha estat sense novetats.