
https://hackropole.fr/fr/challenges/web/fcsc2020-web-enter-the-dungeon/

## Description

On vous demande simplement de trouver le flag.

## Write Up

On arrive sur la page avec la demande d'input d'un secret, mais comme j'avais l'inspecteur d'élément ouvert on tombe sur un truc étrange :

![[Pasted image 20250206151539.png]]

On se rend sur la page "check_secret.txt":
![[Pasted image 20250206151723.png]]

Si on met le secret en md5 bêtement ça ne marche pas, on va plutôt jouer d'une autre façon : /check_secret.php?secret=0e1137126905

![[Pasted image 20250206152851.png]]
Le flag est donc **FCSC{f67aaeb3b15152b216cb1addbf0236c66f9d81c4487c4db813c1de8603bb2b5b}**.