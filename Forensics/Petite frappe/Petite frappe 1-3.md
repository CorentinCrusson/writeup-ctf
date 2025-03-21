
https://hackropole.fr/fr/challenges/forensics/fcsc2020-forensics-petite-frappe-1/

## Description

Lors de l’investigation d’un poste GNU/Linux, vous analysez un fichier qui semble être généré par un programme d’enregistrement de frappes de clavier (enregistrement de l’activité de chaque touche utilisée). Retrouvez ce qui a bien pu être écrit par l’utilisateur de ce poste à l’aide de ce fichier !

**Note :** Insérer le contenu tapé au clavier de ce poste entre `FCSC{...}` pour obtenir le flag.

Cette épreuve est découpée en trois parties :

- [Petite frappe 1/3](https://hackropole.fr/fr/challenges/forensics/fcsc2020-forensics-petite-frappe-1/)
- [Petite frappe 2/3](https://hackropole.fr/fr/challenges/forensics/fcsc2020-forensics-petite-frappe-2/)
- [Petite frappe 3/3](https://hackropole.fr/fr/challenges/forensics/fcsc2020-forensics-petite-frappe-3/)

## Write Up

Quand on va sur le fichier, on se rend compte que c'est des inputs clavier, en toute logique, ce ne sont que les inputs où la valeur = 1

On tente une regex :
$ grep -Po "KEY_\S+(?=.*value 1)" a.txt 
KEY_U),
KEY_N),
KEY_E),
KEY_G),
KEY_E),
KEY_N),
KEY_T),
KEY_I),
KEY_L),
KEY_L),
KEY_E),
KEY_I),
KEY_N),
KEY_T),
KEY_R),
KEY_O),
KEY_D),
KEY_U),
KEY_C),
KEY_T),
KEY_I),
KEY_O),
KEY_N),

Le flag est donc **FCSC{UNEGENTILLEINTRODUCTION}**.