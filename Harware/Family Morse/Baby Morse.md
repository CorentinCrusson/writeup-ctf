
https://hackropole.fr/fr/challenges/hardware/fcsc2022-hardware-baby-morse/

## Description

Dites `FLAG` et vous l’aurez.

Cette épreuve a été découpée en trois étapes :

- [Baby Morse](https://hackropole.fr/fr/challenges/hardware/fcsc2022-hardware-baby-morse/).
- [Daddy Morse](https://hackropole.fr/fr/challenges/hardware/fcsc2022-hardware-daddy-morse/).
- [Mommy Morse](https://hackropole.fr/fr/challenges/hardware/fcsc2022-hardware-mommy-morse/).

## Write Up

Quand on arrive sur le netcat, on a un code morse, quand on le décode ça nous donne "QUEVOULEZVOUS" :
![[Pasted image 20250217150126.png]]

On envoie le mot FLAG comme préconisez par l'énoncé, et cela nous ressort "Entrée Invalide", on va tenter en morse :
![[Pasted image 20250217150214.png]]

Le flag est donc **FCSC{de8b4af784cd394ecc305979ffa124a112a18046037b42c94e4e85216180847e}**.