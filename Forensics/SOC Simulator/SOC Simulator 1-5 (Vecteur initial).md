
https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-soc-simulator-1/

## Description

Durant l’été 2022, un opérateur d’importance vitale (OIV) alerte l’ANSSI car il pense être victime d’une cyberattaque d’ampleur. Le _security operation center_ (SOC) de l’OIV envoie à l’ANSSI un export de sa collecte système des derniers jours. Vous êtes chargé de comprendre les actions réalisées par l’attaquant.

**Note :** Les 5 parties sont numérotées dans l’ordre chronologique de l’attaque mais il n’est pas nécessaire de les résoudre dans l’ordre.

---

Retrouver le nom de la vulnérabilité et l’heure UTC de la première tentative d’exploitation de cette vulnérabilité.

**Format du flag (insensible à la casse):** `FCSC{EternalBlue|2021-11-27T17:38}`

Cette épreuve a été découpée en cinq parties :

- [SOC Simulator 1/5 - Vecteur initial](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-soc-simulator-1/).
- [SOC Simulator 2/5 - Vol de secret 1](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-soc-simulator-2/).
- [SOC Simulator 3/5 - Exfiltration](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-soc-simulator-3/).
- [SOC Simulator 4/5 - Latéralisation](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-soc-simulator-4/).
- [SOC Simulator 5/5 - Vol de secret 2](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-soc-simulator-5/).

## Write Up

On télécharge le zip donné dans l'exercice, on découvre qu'il y a 450 journaux windows pour une taille totale de 3Go2, cela fait beaucoup de données à analayser.

J'utilise la bibliothèque python py-evtx pour décoder tout ça, une partie de mon code :
```python
import os
from evtx import PyEvtxParser
import xml.etree.cElementTree as et
events_count = {}
ips = {}
   
def main():
    # Définir le répertoire contenant les fichiers .evtx
    event_dir = "./soc_events/soc_events"

    # Définir l'espace de noms XML
    namespaces = {'ns': 'http://schemas.microsoft.com/win/2004/08/events/event'}

    # Lister tous les fichiers dans le répertoire
    for evtx_file in os.listdir(event_dir):
        if evtx_file.endswith(".evtx"):  # Vérifier si le fichier a l'extension .evtx
            evtx_path = os.path.join(event_dir, evtx_file)  # Chemin complet du fichier

            # Parser le fichier .evtx

            parser = PyEvtxParser(evtx_path)

            for record in parser.records():

                sxml = str(record['data'])
                #Parser XML
                try:
                    tree=et.fromstring(sxml)
                    
                    #Allez on balaye le XML
                    for el in tree.iter():
                        if "EventID" in el.tag:
                            event_id = int(el.text)

                    for elem in tree.findall(".//ns:Data[@Name='SourceIp']", namespaces=namespaces):
                        ip = elem.text
                        if "fe80:0:0:0:81f:b104:22cc:90f1" in ip:
                            print(sxml)
                except:
                    print(sxml+"\n ---- a foiré")
main()
```

On commence à voir des choses se dessiner, j'ai check tous les bruteforces (EventID 4625), voici la répartition des IPs :
```json
{'fe80::81f:b104:22cc:90f1': 345, '172.16.20.20': 28, '172.16.10.202': 3}
```

De façon globale, en analysant la 202 ça a l'air légitime. Par contre la .20 un peu moins, et la fe80::81f:b104:22cc:90f1 aussi..

On tombe sur un user TINFA\anssi qui essaye de faire du LDAP sur le domaine DC01.tinfa.loc : je pense que cet IP est celle du domaine ahah

---

On arrête les bêtises, on se focus sur une erreur...

Je regarde une erreur que j'ai en permanence sur le exchange.tinfa.loc : 
```xml
<Data Name="ScriptBlockText">cd Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\autdddddddddddddddd</Data>
    <Data Name="ScriptBlockId">5a830a49-4179-49b9-a45c-a0b23dea2aac</Data>
```

On va s'intéresse de près à ce serveur exchange, c'est peut-être fait exprès qui c'est, je cherche donc dans les xml, les occurences "exchange.tinfa.loc" et "CVE" :
```xml
<Data Name="Threat Name">Exploit:Win32/CVE-2021-31207.B</Data>
```

C'est ce qu'il me ressort et en allant plus loin, on a un chemin d'accès : 
```xml
<Data Name="Path">file:_C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth\2UQkad2dfye5.aspx; file:_C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth\A31NhmZE3.aspx; file:_C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth\JhTUvcYN.aspx; file:_C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth\ZRkXzHVGfJx.aspx</Data>
```
*Et d'après ce blog https://www.trendmicro.com/en_us/research/21/k/analyzing-proxyshell-related-incidents-via-trend-micro-managed-x.html, cette CVE s'apparente à du ProxyShell

Quand on regarde de plus près ce blog, on a un indice sur les IOC à trouver :
![[Pasted image 20250212134128.png]]

On filtre ainsi les logs sur "New-MailboxExportRequest" et "Administrator", puis on fini par chopper le datetime à chaque fois :
```python
system_time = tree.find(".//ns:TimeCreated",namespaces=namespaces).attrib.get("SystemTime")
```

En prenant le premier temps, on tombe sur 2022-07-04T15:36

Le flag est donc **FCSC{ProxyShell|2022-07-04T15:36}**.