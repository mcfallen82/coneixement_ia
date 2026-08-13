# wiki-rebuild

## Finalitat

Arxivar o reconstruir la wiki sense perdre coneixement.

## Regles de seguretat

- no esborres fitxes sense còpia d’arxiu;
- fes primer una comprovació de l’abast;
- separa archive, rebuild i restore;
- registra cada operació;
- demana confirmació abans d’una eliminació o substitució massiva.

## Modes

- **archive:** copia l’estat actual i no modifica la wiki viva;
- **rebuild:** arxiva, buida només l’abast confirmat i reingesta fonts seleccionades;
- **restore:** arxiva l’estat actual i recupera una versió anterior.

L’arxiu ha d’incloure fitxes, índex, manifest, registre i metadades necessàries. Després de qualsevol reconstrucció executa wiki-lint i comprova el nombre de fitxes i fonts.
