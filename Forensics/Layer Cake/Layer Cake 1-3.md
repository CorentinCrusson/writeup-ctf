
https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-layer-cake-1/

## Description

Un développeur de GoodCorp souhaite publier une nouvelle image Docker. Il utilise une variable d’environnement stockant un flag au moment du build, et vous assure que ce secret n’est pas visible du public. L’image est [`anssi/fcsc2024-forensics-layer-cake-1`](https://hub.docker.com/r/anssi/fcsc2024-forensics-layer-cake-1).

Récupérez ce flag et prouvez-lui le contraire.

Cette épreuve fait partie d’une serie :

- [Layer Cake 1/3](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-layer-cake-1/).
- [Layer Cake 2/3](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-layer-cake-2/).
- [Layer Cake 3/3](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-layer-cake-3/).

## Write Up

On se rend sur l'image docker : https://hub.docker.com/r/anssi/fcsc2024-forensics-layer-cake-1/tags

En naviguant dans les tags, on tombe sur le tag "latest", et on obtient le flag :
![[Pasted image 20250207154829.png]]

Le flag est donc **FCSC{a1240d90ebeed7c6c422969ee529cc3e1046a3cf337efe51432e49b1a27c6ad2}**.