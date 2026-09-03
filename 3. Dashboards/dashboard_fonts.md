# Dashboard de fonts

Aquesta pàgina resumeix com es documenten les fonts de la wiki. El repositori públic no conserva còpies locals de les fonts originals: treballa amb **fonts externes verificables** i amb referències bibliogràfiques.

## Entrada ràpida

- [Dashboard de la wiki](dashboard_wiki.md): fitxes permanents navegables.
- [Dashboard d'auditoria](dashboard_auditoria.md): comprovacions de salut i seguiment.
- [Índex](../index.md): accés als blocs principals de coneixement.

## Tipus de fonts prioritàries

| Tipus | Ús principal |
| --- | --- |
| papers originals | fonaments tècnics i resultats acadèmics |
| documentació oficial | especificacions, API i funcionament d'eines |
| repositoris oficials | codi, implementacions i exemples |
| llibres i editorials | context, síntesi i bibliografia |
| cursos o tutorials d'autor | explicació pedagògica |
| articles tècnics | context complementari i interpretació |

## Registre mínim

Cada font hauria de conservar, quan sigui possible:

- títol;
- autor o organisme;
- URL o referència bibliogràfica;
- data de publicació o consulta;
- tipus de font;
- fitxes creades o actualitzades.

## Ruta recomanada

1. Identificar la font externa i comprovar-ne l'origen.
2. Confirmar si ja hi ha fitxes permanents associades a `1. Wiki/`.
3. Crear o ampliar fitxes només quan la font aporti coneixement estable.
4. Afegir la URL o referència bibliogràfica al camp `sources`.
5. Actualitzar `index.md`, `hot.md`, `log.md` i `.manifest.json` quan el canvi sigui significatiu.
6. Executar `python scripts/wiki_lint.py` i `python scripts/graph_scan.py --check`.

## Pendent

- Revisar periòdicament enllaços externs trencats o obsolets.
- Prioritzar fonts primàries i oficials.
- Mantenir la correspondència entre cada afirmació rellevant i la seva font.
