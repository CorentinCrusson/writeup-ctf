
https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-1/

## Description

Vous venez d’être embauché en tant que Responsable de la Sécurité des Systèmes d’Information (RSSI) d’une entreprise stratégique.

En arrivant à votre bureau le premier jour, vous vous rendez compte que votre prédécesseur vous a laissé une clé USB avec une note dessus : `VPN compromis (intégrité). Version 22.3R1 b1647`.

---

Sur la clé USB, vous trouvez deux fichiers : une archive chiffrée et les journaux de l’équipement. Vous commencez par lister le contenu de l’archive, dont vous ne connaissez pas le mot de passe. Vous gardez en tête un article que vous avez lu : il paraît que les paquets installés sur l’équipement ne sont pas à jour…

Le flag est le mot de passe de l’archive.

**Remarque :** Le mot de passe est long et aléatoire, inutile de chercher à le _bruteforcer_.

Cette épreuve a été découpée en cinq parties :

- [Horreur, malheur 1/5 - Archive chiffrée](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-1/).
- [Horreur, malheur 2/5 - Accès initial](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-2/).
- [Horreur, malheur 3/5 - Simple persistance](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-3/).
- [Horreur, malheur 4/5 - Pas si simple persistance](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-4/).
- [Horreur, malheur 5/5 - Un peu de CTI](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-5/).

## Write Up

On tombe sur une archive "archive.encrypted", on effectue une tâche banale, en le transformant en .zip/.7z pour l'ouvrir et on tombe sur ceci : 
![[Pasted image 20250211160117.png]]

- Dans le /data, on tombe sur le "flag.txt" 
- Dans le /home, on tombe sur un fichier "VERSION"
- Dans le /tmp, on tombe sur une archive "temp-scanner-archive-20240315-065846.tgz"

Sauf que pour y accéder, il nous faut un mot de passe.

On se rapatrie sur l'énoncé et on reprend l'indication `VPN compromis (intégrité). Version 22.3R1 b1647` , on tombe sur plein de vulnérabilités sur Ivanti Connect, pas oublier de patcher (:

En lisant les différents blogs (https://www.assetnote.io/resources/research/high-signal-detection-and-exploitation-of-ivantis-pulse-connect-secure-auth-bypass-rce) sur la vulnérabilité, on tombe sur le contenu du /home/VERSION !!! : 
![[Pasted image 20250211160710.png]]
Bon on stock tout ça dans un fichier : ![[Pasted image 20250211161708.png]]

En tapant quelques mots clés du type "zip break encryption", on tombe sur cette article : https://www.acceis.fr/cracking-encrypted-archives-pkzip-zip-zipcrypto-winzip-zip-aes-7-zip-rar/

Donc on s'intéresse à bkcrack, on omet toute l'installation et on s'attaque direct au vif du sujet.

D'abord on s'amuse avec cette commande : 
![[Pasted image 20250211162838.png]]
On voit que la méthode de chiffrement est ZipCrypto donc c'est bien vulnérable à notre attaque avec bkcrack !

On tente des trucs : 
![[Pasted image 20250211163420.png]]
Au lieu de faire les dégénérés, on met tout dans un versionning.txt, on lit la doc et on réessaye : 
![[Pasted image 20250211164745.png]]
Ici, le "versionning.zip" n'est qu'un zip content mon versionning.txt

On recommence car le R1 n'est pas entre guillemets : 
![[Pasted image 20250211165438.png]]

Eh bah dis donc ça fonctionne mieux maintenant :
![[Pasted image 20250211165713.png]]

Et on suit le beau tuto d'acceis, pour finir sur ce screen :
![[Pasted image 20250211165846.png]]

J'omets l'étape, ou on fait le cat data/flag.txt ;)

Le flag est donc **FCSC{50c53be3eece1dd551bebffe0dd5535c}**.