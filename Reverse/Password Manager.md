
https://hackropole.fr/fr/challenges/reverse/fcsc2022-reverse-password-manager/

# Description

J’ai développé un gestionnaire de mots de passe super sécurisé, seulement il est complètement bogué et je n’ai plus accès ni au code ni au binaire :((( En effet, il ouvre bien mon fichier de mots de passe, mais ensuite il refuse de m’afficher son contenu !!! Heureusement, avant de me faire déconnecter du serveur j’ai réussi à lancer GDB, peut-être que vous pourrez m’aider ?

# Write Up

On a bien un gdb de lancer :
![[Pasted image 20250217154320.png]]

On cherche une cheatsheet :
https://github.com/reveng007/GDB-Cheat-Sheet

Quand je fais un run je tombe là dessus :
![[Pasted image 20250217154956.png]]

Je suis un peu perdu, je me base sur un article : https://secgroup.dais.unive.it/teaching/security-course/gdb/



### On attaque le désassemblage !

On lance cette commande :
![[Pasted image 20250217154854.png]]

ça fait un peu mal à la tête, je m'interroge sur les @plt, je trouve ça étrange, le pputs on dirait un appel de fonction, cf chat GPT :
![[Pasted image 20250217155241.png]]



### Mais lisons ce fichier bordel..

On relit la description et on voit ce texte "En effet, il ouvre bien mon fichier de mots de passe, mais ensuite il refuse de m’afficher son contenu !!! ". 

Bon puts c'est pour écrire une chaine de caractère, peut-être du fopen ou du open ? Bingo ! :
![[Pasted image 20250217155514.png]]

Il y a également read qui peut-être un bon concurrent :
![[Pasted image 20250217155636.png]]

Bon du coup, on va mettre un breakpoint après le read, comme ça on vérifie bien que tout marche, la ligne juste après est :
0x00000000000012fe <+409>:   mov    %eax,-0xc(%rbp)

Donc il faut ajouter à notre breakpoint un décalage de 409 : 
![[Pasted image 20250217160502.png]]



### Lire le contenu d'une fonction ?

ChatGPT, aide moi non :
![[Pasted image 20250217161006.png]]

Mais il a raison la brute :
![[Pasted image 20250217161238.png]]

Sauf que ces fonctions ne marchent pas, il faut chercher son $rsi à la main... 

On remonte et on voit que rsi a pris la valeur de rcx :
0x00000000000012f4 <+399>:   mov    %rcx,%rsi

Pour la suite, je m'aide de cette cheatsheet https://cs.brown.edu/courses/cs033/docs/guides/x64_cheatsheet.pdf 

Elle me permet donc de comprendre l'instruction suivante :
0x00000000000012e5 <+384>:   lea    -0x410(%rbp),%rcx

Et on remontant le programme entre open et read, on voit que rbp n'a pas l'air d'être modifié, pour reprendre la commande de chat gépéto : ça ne marche pas





Le flag est donc **FCSC{f9a38adace9dda3a9ae53e7aec180c5a73dbb7c364fe137fc6721d7997c54e8d}**.