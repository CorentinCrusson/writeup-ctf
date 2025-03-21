
https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-layer-cake-2/

## Description

Un développeur de GoodCorp souhaite publier une nouvelle image Docker. Il copie au moment du build un fichier contenant un flag, puis le supprime. Il vous assure que ce secret n’est pas visible du public. L’image est [`anssi/fcsc2024-forensics-layer-cake-2`](https://hub.docker.com/r/anssi/fcsc2024-forensics-layer-cake-2).

Récupérez ce flag et prouvez-lui le contraire.

Cette épreuve fait partie d’une serie :

- [Layer Cake 1/3](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-layer-cake-1/).
- [Layer Cake 2/3](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-layer-cake-2/).
- [Layer Cake 3/3](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-layer-cake-3/).
## Write Up

On se rend sur l'image docker : https://hub.docker.com/r/anssi/fcsc2024-forensics-layer-cake-2

En naviguant dans les tags, et puis en tombant sur le tag latest on se rend compte qu'il y a une variable "secret" qui a l'air de contenir une information précieuse :
![[Pasted image 20250207155107.png]]

On a rien, on va analyser l'image docker, on la download :
![[Pasted image 20250207155737.png]]

On transforme l'image dans une archive, ici du .tar : 
![[Pasted image 20250207160438.png]]

Et on se prend pas la tête, on cherche le flag : 
![[Pasted image 20250207160624.png]]

Le flag est donc **FCSC{b38095916b2b578109cbf35b8be713b04a64b2b2df6d7325934be63b7566be3b}**.