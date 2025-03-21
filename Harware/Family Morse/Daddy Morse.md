
https://hackropole.fr/fr/challenges/hardware/fcsc2022-hardware-daddy-morse/

## Description

Les télégraphes Morse permettaient d’échanger des messages de texte à longue distance, en encodant un message sous forme d’impulsions électriques. Le serveur se comporte comme un mini-télégraphe et décode les données que vous lui envoyez.

Vous devez envoyer `CAN I GET THE FLAG`.

Vous avez le code du serveur ainsi qu’un exemple de message à disposition.

Les paramètres de transmission sont les suivants :

- fréquence d’échantillonnage : 24kHz,
- durée d’un `.` : 1 milliseconde,
- durée d’un `-` : 5 millisecondes,
- espacement entre deux lettres : 5 millisecondes,
- espacement entre deux mots : 20 millisecondes.

Cette épreuve a été découpée en trois étapes :

- [Baby Morse](https://hackropole.fr/fr/challenges/hardware/fcsc2022-hardware-baby-morse/).
- [Daddy Morse](https://hackropole.fr/fr/challenges/hardware/fcsc2022-hardware-daddy-morse/).
- [Mommy Morse](https://hackropole.fr/fr/challenges/hardware/fcsc2022-hardware-mommy-morse/).

## Write Up



Le flag est donc **FCSC{de8b4af784cd394ecc305979ffa124a112a18046037b42c94e4e85216180847e}**.