
https://hackropole.fr/fr/challenges/forensics/fcsc2020-forensics-petite-frappe-3/

## Description

Lors de l’investigation d’un serveur GNU/Linux en France, plusieurs fichiers inconnus de l’administrateur ont été retrouvés dont le fichier

```
-rw-r--r-- 1 root root 55K Mar 21 02:45 /tmp/input
```

Ce fichier est soupçonné d’être lié à une activité d’un enregistreur de frappe clavier mais aucun programme ne semble avoir été installé sur ce serveur à cette fin. Identifiez le format de ce fichier puis essayez de le décoder afin de trouver le mot de passe de `flag.gpg`.

Cette épreuve est découpée en trois parties :

- [Petite frappe 1/3](https://hackropole.fr/fr/challenges/forensics/fcsc2020-forensics-petite-frappe-1/)
- [Petite frappe 2/3](https://hackropole.fr/fr/challenges/forensics/fcsc2020-forensics-petite-frappe-2/)
- [Petite frappe 3/3](https://hackropole.fr/fr/challenges/forensics/fcsc2020-forensics-petite-frappe-3/)
## Write Up

On retrouve un peu la même chose, je sens la couille, car il y a du press / release, donc il faut attendre le release pour taper le mot mais on va tenter sur le press :
![[Pasted image 20250214134747.png]]

En décodant tout ça, on tombe sur le flag.

Le flag est donc **FCSC{un_clavier_azerty_en_vaut_deux}**.