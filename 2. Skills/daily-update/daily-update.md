# daily-update

## Finalitat

Executar una revisió periòdica de la wiki i mantenir sincronitzats fonts externes registrades, fitxes i fitxers de control.

## Cicle

1. Revisa `.manifest.json` i identifica fonts externes noves, modificades o pendents de processar.
2. Comprova si hi ha fitxes en `draft`, sense `sources` o amb actualitzacions pendents.
3. Executa `wiki-ingest` o `wiki-update` quan correspongui.
4. Actualitza `index.md`, `log.md` i `hot.md` quan hi hagi canvis significatius.
5. Executa `wiki-lint`.
6. Resumeix errors, fitxes incompletes i prioritats següents.

## Informe

~~~markdown
# Actualització de la wiki — YYYY-MM-DD
## Fonts revisades o processades
## Fitxes creades o actualitzades
## Problemes detectats
## Prioritats següents
~~~

No modifiquis contingut només per generar activitat: si no hi ha canvis, registra que la revisió ha estat sense novetats quan sigui útil.
