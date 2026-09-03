# wiki-update

## Finalitat

Sincronitzar informació nova amb les fitxes permanents de la wiki, tant si prové d’una font com d’un projecte.

## Protocol

1. Llegeix AGENTS.md, la fitxa objectiu, les fitxes relacionades i log.md.
2. Compara el contingut nou amb el contingut existent.
3. Separa dades noves, precisions, correccions, exemples, relacions causals, contradiccions i informació obsoleta.
4. Conserva el text vàlid, les fonts i la data created.
5. Incorpora la informació nova en la secció adequada i actualitza updated.
6. Afegeix la font al frontmatter i a la secció Fonts.
7. Revisa els enllaços cap a autors, conceptes i models.

## Criteri de decisió

~~~text
mateix concepte → actualitzar
sinònim o grafia alternativa → enllaçar o redirigir
subconcepte autònom → crear fitxa
font contradictòria → conservar les dues evidències i explicar la diferència
exemple nou → afegir-lo a la fitxa existent
informació irrellevant → no incorporar-la
~~~

## Actualització d’un projecte

Quan el contingut prové d’un repositori:

- revisa README, estructura, dependències, decisions i historial de canvis;
- extreu patrons, alternatives, errors i solucions;
- evita copiar llistats de codi o detalls efímers;
- desa el resultat enllaçat amb el projecte o la font corresponent;
- registra l’últim commit sincronitzat al manifest quan sigui possible.

## Relacions bidireccionals

Si una fitxa de model cita un concepte, el model ha d’enllaçar-lo i el concepte ha d’incloure el model a related_models. Aplica el mateix criteri a autors i obres.

## Validació final

Executa wiki-lint, comprova que la fitxa apareix a les consultes de index.md i actualitza log.md, hot.md i .manifest.json.
