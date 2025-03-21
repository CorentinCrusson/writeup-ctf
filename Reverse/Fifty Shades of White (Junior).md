
https://hackropole.fr/fr/challenges/reverse/fcsc2024-reverse-fifty-shades-of-white-1/

## Description

Le grand Walter White a écrit un programme lui permettant de restreindre l’accès à ses données “professionnelles”. Il distribue des licenses au compte-gouttes, mais vous avez néanmoins récupéré une license qu’il a générée pour son fils ! Son système propose deux niveaux de licenses : celle que vous avez récupérée est la moins privilégiée, et vous souhaitez obtenir une license “admin”.

Le programme ci-joint vérifie entre autres le niveau de privilèges de la license, et vous récompense si vous présentez une license “admin”.

![](https://hackropole.fr/challenges/fcsc2024-reverse-fifty-shades-of-white/public/meme-fifty-shades-of-white-junior.jpg)

_[L’abus d’alcool est dangereux pour la santé.](https://www.santepubliquefrance.fr/determinants-de-sante/alcool/articles/quels-sont-les-risques-de-la-consommation-d-alcool-pour-la-sante)_

## Write Up

On nous demande une licence admin valide au nom de Walter White Junior, dès qu'on lance le programme : 
![[Pasted image 20250220152044.png]]

Sauf que sur la capture d'écran, on se rend compte que la licence donné indique que Walter n'est pas admin.  Quand on décode le base64 de la license on tombe là dessus :
	Name: Walter White Junior
	Serial: 1d117c5a-297d-4ce6-9186-d4b84fb7f230
	Type: 1

En effectuant un reverse du binaire donné, on tombe sur le numéro de série à indiquer pour que l'utilisateur soit admin :
![[Pasted image 20250220152731.png]]

On modifie le base64 pour changer le type en 1337 et bingo :
![[Pasted image 20250220152845.png]]

Le flag est donc **FCSC{2053bb69dff8cf975c1a3e3b803b05e5cc68933923aabdd6179eace1ece0c41a}**.