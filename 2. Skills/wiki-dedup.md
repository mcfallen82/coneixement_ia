# wiki-dedup

## Finalitat

Detectar fitxes que descriuen el mateix concepte, model o autor amb noms diferents.

## Detecció

Compara:

- títols i grafies alternatives;
- noms en català i anglès;
- tags i camps de categoria;
- fonts compartides;
- definicions i objectius;
- wikilinks entrants i sortints.

Classifica els candidats com a alta confiança, confiança mitjana o revisió humana.

## Fusió segura

1. Escull la fitxa canònica amb millor contingut i procedència.
2. Combina-hi la informació única de l’altra fitxa.
3. Conserva totes les fonts vàlides.
4. Reescriu els enllaços cap a la fitxa canònica.
5. Converteix la fitxa secundària en una nota de redirecció només si l’usuari ho aprova.
6. Actualitza index.md, log.md, hot.md i .manifest.json.

No eliminis fitxes ni fusiones conceptes simplement perquè siguin semblants. La diferència entre un concepte, un model i una aplicació pot ser significativa.