#windows
https://hackropole.fr/fr/challenges/forensics/fcsc2023-forensics-la-gazette-de-windows/

## Description

Il semblerait qu’un utilisateur exécute des scripts Powershell suspects sur sa machine. Heureusement cette machine est journalisée et nous avons pu récupérer le journal d’évènements Powershell. Retrouvez ce qui a été envoyé à l’attaquant.

## Write Up

On télécharge le fichier d'évènements windows, et on l'explore.

On tombe sur une log intéressante avec un script powershell :
![[Pasted image 20250210090712.png]]

On recopie la partie du code suivante :
```powershell
$l = 0x46, 0x42, 0x51, 0x40, 0x7F, 0x3C, 0x3E, 0x64, 0x31, 0x31, 0x6E, 0x32, 0x34, 0x68, 0x3B, 0x6E, 0x25, 0x25, 0x24, 0x77, 0x77, 0x73, 0x20, 0x75, 0x29, 0x7C, 0x7B, 0x2D, 0x79, 0x29, 0x29, 0x29, 0x10, 0x13, 0x1B, 0x14, 0x16, 0x40, 0x47, 0x16, 0x4B, 0x4C, 0x13, 0x4A, 0x48, 0x1A, 0x1C, 0x19, 0x2, 0x5, 0x4, 0x7, 0x2, 0x5, 0x2, 0x0, 0xD, 0xA, 0x59, 0xF, 0x5A, 0xA, 0x7, 0x5D, 0x73, 0x20, 0x20, 0x27, 0x77, 0x38, 0x4B, 0x4D
$s = ""
for ($i = 0; $i -lt 72; $i++) {
    $s += [char]([int]$l[$i] -bxor $i)
}
$s
```

Et hop, on choppe le flag : 
![[Pasted image 20250210091425.png]]

Le flag est donc **FCSC{98c98d98e5a546dcf6b1ea6e47602972ea1ce9ad7262464604753c4f79b3abd3}**