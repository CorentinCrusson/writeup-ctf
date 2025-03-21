
https://hackropole.fr/fr/challenges/reverse/fcsc2024-reverse-fifty-shades-of-white-2/

## Description

Vous incarnez désormais Jesse Pinkman. Vous êtes actuellement en froid avec Walter White et souhaitez lui faire un sale coup.

On vous demande d’écrire un _keygen_ pour le binaire que Walter a conçu pour restreindre l’accès à ses données “professionnelles”. Le flag apparaîtra après 50 validations successives.

![](https://hackropole.fr/challenges/fcsc2024-reverse-fifty-shades-of-white/public/meme-fifty-shades-of-white-pinkman.jpeg)

## Write Up

C'est la suite du challenge FSW (Junior), on a vu qu'après avoir donné la licence Admin de White on tombait sur le prompt pour Pinkman :
![[Pasted image 20250220153239.png]]

Je change donc le contenu de la license pour inclure le nom de Pinkman :
	Name: Jesse Pinkman
	Serial: 1d117c5a-297d-4ce6-9186-d4b84fb7f230
	Type: 1

Et le programme me répond Invalid License, problème au niveau du serial dans la license je pense. Il va falloir retourner sur le reverse du programme. 

Ghidra nous renvoie la fonction "validate" suivante : 

```c
uint validate(char *param_1,char *param_2)
{
  size_t sVar1;
  void *local_38;
  undefined local_2c [4];
  uint local_28;
  uint local_24;
  ulong local_20;
  int local_14;
  int local_10;
  uint local_c;
  
  sVar1 = strlen(param_2);
  sha256(param_2,sVar1,&local_38,local_2c);
  local_c = 1;
  for (local_10 = 0; local_10 < 3; local_10 = local_10 + 1) {
    local_14 = 0;
    local_20 = (ulong)local_10;
    while( true ) {
      sVar1 = strlen(param_1);
      if (sVar1 <= local_20) break;
      local_14 = local_14 + param_1[local_20];
      local_20 = local_20 + 3;
    }
    local_24 = (local_14 * 0x13 + 0x37) % 0x7f;
    local_28 = ((uint)*(byte *)((long)local_10 + (long)local_38) * 0x37 + 0x13) % 0x7f;
    local_c = local_c & local_24 == local_28;
  }
  CRYPTO_free(local_38);
  return local_c;
}
```
Comme on a le code pour vérifier, on peut tenter de bruteforce tout ça, par contre param1 et param2 on ne sait pas à quoi ils correspondent... Après recherche avec ce qu'on avait, param1 = Name et param2 = Serial, ça veut dire qu'ils se basent sur le nom pour générer le numéro de série.

Après modifications ça donne ça :
```python
from Cryptodome.Hash import SHA256

def validate(name,serial):
    hash = SHA256.new()
    hash.update(serial.encode())
    HASH = hash.digest()
    local_c = True

    for local_10 in range(0,3):
        local_14 = 0
        local_20 = local_10
        
        while True:
            sVar1 = len(name)
            if sVar1 <= local_20:
                break

            local_14 = local_14 + ord(name[local_20])
            local_20 = local_20 + 3
        local_24 = (local_14 * 0x13 + 0x37) % 0x7f
        local_28 = (HASH[local_10] * 0x37 + 0x13) % 0x7f
        local_c = local_c and local_24 == local_28
    return local_c
    
if validate("Walter White Junior","1d117c5a-297d-4ce6-9186-d4b84fb7f230"):
    print("Certificat valide")
```

On vérifie avec une licence valide, on a bien un affichage "Certificat valide" et dès qu'on le modifie c'est invalide.

On ajoute une fonction qui génère un numéro de série aléatoire :
```python
def generate_serial(name):
    while True:
        serial = ''.join(random.choices(string.ascii_lowercase + string.digits + '-', k=36))
        if validate(name,serial):
            return serial
            
name = "Walter White Junior"
valid_serial = generate_serial(name)
print("License Valide : {}".format(valid_serial))
```

Et on se rend bien compte que ça marche sur le netcat :
![[Pasted image 20250220162937.png]]

Bon maintenant il reste plus qu'à récupérer la sortie du netcat, et générer le base64 avec ces infos + le type de license si besoin d'un admin ou non.

La suite ça donne ça :
```python
def connection_netcat(host,port):
    # Créer une connexion avec le serveur
    connection = remote(host, port)

    return connection
    
def generate_license(name,serial,type):
    license = "Name: {}\
    Serial: {}\
    Type: {}".format(name,serial,type)
    
    license_b64 = base64.b64encode(license.encode("utf-8"))
    
    return "----BEGIN WHITE LICENSE----\n{}\n-----END WHITE LICENSE-----".format(license_b64)

connection = connection_netcat("127.0.0.1",4000)

# Recevoir la réponse du serveur
response = connection.recvline()

# Envoyer un message au serveur
connection.sendline("Hello, Server!")

for i in range(0,100):

    # Recevoir la réponse du serveur
    response = connection.recvline()

    # Afficher la réponse du serveur
    response_text = response.decode()

    print("Réponse du serveur:", response_text)
    
    if "FCSC" in response_text:
        print(response_text)

    if "username" in response_text:
        name = response_text.split("username: ")[1]
        valid_serial = generate_serial(name)
        text_to_send = generate_license(name,valid_serial,1337 if "admin" in response_text else 1)
        connection.sendline(text_to_send)
```


Le flag est donc **FCSC{9600becd765ca03baa623504244e008e6f3348bce0219fe4027432d790dd074f}**.