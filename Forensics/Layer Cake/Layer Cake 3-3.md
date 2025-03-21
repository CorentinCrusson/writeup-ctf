
https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-layer-cake-3/

## Description

Un développeur de GoodCorp souhaite publier une nouvelle image Docker. Suite à ses mésaventures avec les Dockerfile, il décide d’utiliser [Nix](https://nixos.org/) pour construire son image. En utilisant Nix, il donne un flag en argument à un service. Il vous assure que ce secret n’est pas visible du public. L’image est [`anssi/fcsc2024-forensics-layer-cake-3`](https://hub.docker.com/r/anssi/fcsc2024-forensics-layer-cake-3).

Récupérez ce flag et prouvez-lui le contraire.

Cette épreuve fait partie d’une serie :

- [Layer Cake 1/3](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-layer-cake-1/).
- [Layer Cake 2/3](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-layer-cake-2/).
- [Layer Cake 3/3](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-layer-cake-3/).

## Write Up

On se rend sur l'image docker : https://hub.docker.com/r/anssi/fcsc2024-forensics-layer-cake-3

En naviguant dans les tags, on tombe sur le tag "latest", on obtient RIEN :
![[Pasted image 20250207160836.png]]

On télécharge l'image :
![[Pasted image 20250207161204.png]]

On sauvegarde l'image en archive, puis on recherche dans celle ci s'il n'y a pas un flag qui traine :
![[Pasted image 20250207161328.png]]

Et on retrouve bien le flag, avec la commande "nix" comme stipulé dans la description

Le flag est donc **FCSC{c12d9a48f1635354fe9c32b216f144ac66f7b8466a5ac82a35aa385964ccbb61}**.