# wiki-lint

Skill d'auditoria estructural, sintàctica i semàntica de la wiki. És la comprovació final habitual abans de donar una modificació per acabada.

## Quan utilitzar-la

Després d'una ingesta, actualització, reorganització o canvi de metadades.

## Què comprova

- estructura obligatòria del repositori;
- YAML i categories;
- títols duplicats;
- rutes del manifest;
- frontmatter incomplet, fonts absents i wikilinks pendents;
- camps o convencions obsoletes.

## Execució

```bash
python scripts/wiki_lint.py
```

Utilitza `--strict` quan es vulgui convertir el deute de normalització en errors bloquejants.

## Resultat esperat

Una sortida `PASS` o `FAIL`, amb errors bloquejants separats dels advertiments de normalització.

## Procediment complet

Vegeu [wiki-lint.md](wiki-lint.md).
