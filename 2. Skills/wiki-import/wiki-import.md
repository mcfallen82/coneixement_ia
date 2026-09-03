# wiki-import

## Finalitat

Reconstruir o incorporar fitxes a partir d'un export de graf o d'un paquet compatible.

## Procés

1. Identifica el format d'entrada. Conserva l'original fora del repositori públic o en una ubicació local ignorada per Git si només és material temporal de treball.
2. Comprova categories, títols, identificadors i conflictes.
3. Tria mode `merge`, `overwrite` o `dry-run`.
4. Mapifica els nodes a autors, conceptes, models i altres categories admeses.
5. Reescriu les relacions com a wikilinks cap a rutes reals.
6. No sobreescriguis fitxes existents sense una comparació prèvia.
7. Actualitza `index.md`, `log.md`, `hot.md` i `.manifest.json` quan correspongui.
8. Executa `wiki-lint`.

En mode `merge`, conserva la informació existent i afegeix només dades noves amb la seva procedència. Els nodes desconeguts s'han de revisar abans de crear-los.
