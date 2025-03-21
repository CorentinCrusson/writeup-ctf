
https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-2/

## Description

Vous venez d’être embauché en tant que Responsable de la Sécurité des Systèmes d’Information (RSSI) d’une entreprise stratégique.

En arrivant à votre bureau le premier jour, vous vous rendez compte que votre prédécesseur vous a laissé une clé USB avec une note dessus : `VPN compromis (intégrité). Version 22.3R1 b1647`.

---

Sur la clé USB, vous trouvez deux fichiers : une archive chiffrée et les journaux de l’équipement. Vous focalisez maintenant votre attention sur les journaux. L’équipement étant compromis, vous devez retrouver la vulnérabilité utilisée par l’attaquant ainsi que l’adresse IP de ce dernier.

Le flag est au format : `FCSC{CVE-XXXX-XXXXX:<adresse_IP>}`

Cette épreuve a été découpée en cinq parties :

- [Horreur, malheur 1/5 - Archive chiffrée](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-1/).
- [Horreur, malheur 2/5 - Accès initial](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-2/).
- [Horreur, malheur 3/5 - Simple persistance](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-3/).
- [Horreur, malheur 4/5 - Pas si simple persistance](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-4/).
- [Horreur, malheur 5/5 - Un peu de CTI](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-5/).
## Write Up

On télécharge l'archive horreur-malheur.tar.xz, une fois extraite (tar -xf), on tombe sur l'arborescence /data/var/dlogs, où on trouve à l'intérieur tout un tas de fichiers de log :
![[Pasted image 20250212084645.png]]

Avant d'attaquer l'analyse, on s'intéresse à notre page https://www.assetnote.io/resources/research/high-signal-detection-and-exploitation-of-ivantis-pulse-connect-secure-auth-bypass-rce précédemment vu.

On va prendre la CVE en question et vérifier si des traces d'exploit sont dans les logs ! Focus sur la CVE-2023-46805 qui a l'air intéressante :
![[Pasted image 20250212085005.png]]

Rien avec cet CVE, on attaque sur celle-ci, la CVE-2024-21887 :
![[Pasted image 20250212085440.png]]

Et paf, on retrouve bien une trace, cela confirme notre suspicion sur la  CVE-2024-21887 :
![[Pasted image 20250212085647.png]]

Bon par contre l'IP 172.18.0.4 ne fonctionne pas :), on cherche dans le fichier nodemonlog car on voit qu'on a des logs réseaux :
![[Pasted image 20250212090103.png]]
On voit qu'une IP revient, la 20.13.3.0 et c'est flag !

Le flag est donc **FCSC{CVE-2024-21887:FCSC{CVE-2023-46805:20.13.3.0}**.