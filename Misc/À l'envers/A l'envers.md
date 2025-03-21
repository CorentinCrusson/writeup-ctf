
https://hackropole.fr/fr/challenges/misc/fcsc2022-misc-a-l-envers/

## Description

Connectez vous au service distant et pour chaque chaîne de caractères reçue, vous devez renvoyer la chaîne de caractères contenant les caractères dans l’ordre inverse.

**Exemple :** pour la chaîne `ANSSI`, vous devez renvoyer `ISSNA` (note : le respect de la casse est important).


## Write Up

On laisse le script python (il faut juste reverse la chaine [::-1])
```bash
[*] C'est pas moi ! j'ai vu, je sais qui c'est, mais je ne dirais rien !
[+] Opening connection to localhost on port 4000: Done
b'>>> ANSSI\n'
b'Well done, continue!\n'
b'>>> Agence\n'
b'Well done, continue!\n'
b'>>> nationale\n'
b'Well done, continue!\n'
b'>>> Oui\n'
b'Well done, continue!\n'
b'>>> Bonjour\n'
b'Well done, continue!\n'
b'>>> France\n'
b'Well done, continue!\n'
b'>>> baguette\n'
b'Well done, continue!\n'
b'>>> cassoulet\n'
b'Well done, continue!\n'
b'>>> CmqqnvrD\n'
b'Well done, continue!\n'
b'>>> Dz3WRc0h\n'
b'Well done, continue!\n'
b'>>> n8sLScWB\n'
b'Well done, continue!\n'
b'>>> 9pXicFm4\n'
b'Well done, continue!\n'
b'>>> qYNTRryX\n'
b'Well done, continue!\n'
b'>>> wV8hDDmz\n'
b'Well done, continue!\n'
b'>>> AIiELi1H\n'
b'Well done, continue!\n'
b'>>> 97LopDdt\n'
b'Well done, continue!\n'
b'>>> LN3CmOLEaDQQVO8e5WE9MCN5nkG93A67\n'
b'Well done, continue!\n'
b'>>> S94FAf6rY65LBUazLZXNpb5n5PJf86Ak\n'
b'Well done, continue!\n'
b'>>> HpJAY4GASMkh66fuWgP1BVWHWBrCZ3G6\n'
b'Well done, continue!\n'
b'>>> n0E4gazxXEsadX8PMKtVHY7soItPNi5c\n'
b'Well done, continue!\n'
b'>>> eDDm6smY9JYTqMZgu2QlPbw2d8NDViuN\n'
b'Well done, continue!\n'
b'>>> pV0eIYYiosimuRY4pJvmRCfOjisF0q6c\n'
b'Well done, continue!\n'
b'>>> nVhS6kg45VTLoaLdpUskEg846H1ApDmH\n'
b'Well done, continue!\n'
b'>>> q8VwXrqOuhn96c7nZ99SXU7HnqVYUjY9\n'
b'Well done, continue!\n'
b'Congratulations!! Here is your flag:\n'
b'FCSC{7b20416c4f019ea4486e1e5c13d2d1667eebac732268b46268a9b64035ab294d}\n'
[*] FLAG FOUND
[*] b'FCSC{7b20416c4f019ea4486e1e5c13d2d1667eebac732268b46268a9b64035ab294d}\n'
[*] Ah ! C'était donc ça tout ce tintouin.
[*] Closed connection to localhost port 4000
```

Le flag est donc **FCSC{7b20416c4f019ea4486e1e5c13d2d1667eebac732268b46268a9b64035ab294d}**.