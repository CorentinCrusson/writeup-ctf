## Description

La startup _TypeWriters & Co._ a une idée géniale : elle souhaite proposer en ligne un service de traitement de texte qui va révolutionner le monde de l’édition !

Mais la veille de l’inauguration, le chef de projet se souvient d’une vague mention concernant des exigences de sécurité…

Comme vous êtes la personne chargée de la sécurité, il a besoin de votre validation. Selon lui, cela n’est qu’une simple formalité car le code a été relu par leurs meilleurs développeurs et le binaire s’exécute avec toutes les protections classiques (canaris, W^X, ASLR, etc.).

Vérifiez s’il est possible de lire le fichier `flag.txt` qui se trouve sur le serveur distant.

Une variante plus difficile de cette épreuve est disponible ici : [`Book Writer`](https://hackropole.fr/fr/challenges/pwn/fcsc2024-pwn-book-writer/).

## Write-Up

On s'intéresse d'abord au code donné "book-writer-easy.c", on aperçoit rapidement la fonction win():
```c
void win()
{
    system("cat flag.txt");
    exit(EXIT_SUCCESS);
}
```

Sauf que dans le code, on ne voit pas d'appel à la fonction win().

Il y a du bufferoverflow à faire, c'est plus du reverse que du pwn à mon avis..