
https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-soc-simulator-3/

## Description

Durant l’été 2022, un opérateur d’importance vitale (OIV) alerte l’ANSSI car il pense être victime d’une cyberattaque d’ampleur. Le _security operation center_ (SOC) de l’OIV envoie à l’ANSSI un export de sa collecte système des derniers jours. Vous êtes chargé de comprendre les actions réalisées par l’attaquant.

**Note :** Les 5 parties sont numérotées dans l’ordre chronologique de l’attaque mais il n’est pas nécessaire de les résoudre dans l’ordre.

---

Dans la continuité de ce qui été vu précédemment, l’attaquant a collecté une quantité importante de données métier. Retrouver la commande qui a permis collecter de tous ces éléments.

**Format du flag :** `FCSC{sha256(<commande en UTF8 sans saut de ligne>)}`

Par exemple si la commande malveillante était `7z a "Fichiers volés.zip" C:\Windows\System32`, le flag serait `FCSC{bc5640e69c335a8dbe369db382666070e05198a6c18ce88498563d2c4ac187b1}`

Cette épreuve a été découpée en cinq parties :

- [SOC Simulator 1/5 - Vecteur initial](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-soc-simulator-1/).
- [SOC Simulator 2/5 - Vol de secret 1](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-soc-simulator-2/).
- [SOC Simulator 3/5 - Exfiltration](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-soc-simulator-3/).
- [SOC Simulator 4/5 - Latéralisation](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-soc-simulator-4/).
- [SOC Simulator 5/5 - Vol de secret 2](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-soc-simulator-5/).
## Write Up

Vu la consigne, dans le doute on teste de trouver des cmdline d'archive :
-> Nada

Je décide, de refaire un tour au niveau de Hayabusa.

Comme on est sur du microsoft exchange, on va se focus sur de l'export de mails, p'tit recherche google :
![[Pasted image 20250212162931.png]]

On voit que cette commande permettre d'exporter une boite mail vers un .pst file qui est une archive, ce qui fait écho à notre énoncé...

On fait donc un p'tit grep :
![[Pasted image 20250212162840.png]]

On observe deux lignes parlant de .pst :
```c
"2022-07-05 15:41:11.371 +02:00","PwSh Scriptblock","info","exchange.tinfa.loc","PwSh",4104,231722,"ScriptBlock: foreach ($Mailbox in (Get-Mailbox -ResultSize Unlimited)) {New-MailboxExportRequest -Mailbox $Mailbox.DisplayName -FilePath ""C:\windows\system32\xwin\($Mailbox.Alias).pst""}","MessageNumber: 1 ¦ MessageTotal: 1 ¦ ScriptBlockId: fc59836f-c8b0-4a99-bffb-d524852150b0"
```

Le flag est donc **FCSC{bd4d7ea91a29c48cdf5b6b4813600dd202ea034e6aa59c1268f8210f2991955c}**.