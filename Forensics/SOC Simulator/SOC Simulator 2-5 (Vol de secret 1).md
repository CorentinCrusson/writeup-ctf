
https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-soc-simulator-2/

## Description

Durant l’été 2022, un opérateur d’importance vitale (OIV) alerte l’ANSSI car il pense être victime d’une cyberattaque d’ampleur. Le _security operation center_ (SOC) de l’OIV envoie à l’ANSSI un export de sa collecte système des derniers jours. Vous êtes chargé de comprendre les actions réalisées par l’attaquant.

**Note :** Les 5 parties sont numérotées dans l’ordre chronologique de l’attaque mais il n’est pas nécessaire de les résoudre dans l’ordre.

---

Après l’action vue dans la partie 1, l’attaquant vole les identifiants système en mémoire. Retrouver le GUID du processus effectuant ce vol et le nom du fichier où il écrit les secrets volés.

**Format du flag (insensible à la casse) :** `FCSC{6ccf8905-a033-4edc-8ed7-0a4b0a411e15|C:\Windows\Users\toto\Desktop\fichier.pdf}`

Cette épreuve a été découpée en cinq parties :

- [SOC Simulator 1/5 - Vecteur initial](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-soc-simulator-1/).
- [SOC Simulator 2/5 - Vol de secret 1](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-soc-simulator-2/).
- [SOC Simulator 3/5 - Exfiltration](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-soc-simulator-3/).
- [SOC Simulator 4/5 - Latéralisation](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-soc-simulator-4/).
- [SOC Simulator 5/5 - Vol de secret 2](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-soc-simulator-5/).

## Write Up

Bon ici, on a l'indice de vol d'identifiants systèmes en mémoire, on s'interroge donc à des accès à "LSASS.exe".

Pour la suite, je vais m'intéresse à hayabusa : https://github.com/Yamato-Security/hayabusa, de ce que j'ai vu sur le discord de hackropole ça a l'air pas mal, et j'avoue que mon pauvre python est un peu lent à chaque requête. Puis ça permet de tester différentes possibilités ;)

Une fois hayabusa installé, on le lance, et on demande juste le "Core" soit les high / critical, on verra si ça nous bloque dans le futur :
```sh
.\hayabusa-3.0.1-win-x64\hayabusa-3.0.1-win-x64.exe csv-timeline  --directory .\soc_events\soc_events\ -o timeline.csv
```

On a des p'tites stats : 
![[Pasted image 20250212150428.png]]

En lançant un grep dans notre CSV avec "LSASS", on tombe sur ceci :
![[Pasted image 20250212150711.png]]

On recherche ensuite, les commandes faites avec rundll32 :
![[Pasted image 20250212151700.png]]
```c
"C:\Windows\system32\rundll32.exe" C:\Windows\System32\comsvcs.dll MiniDump 652 attr.exe full 
```
En regardant le fonctionnement de plus près de comsvcs.dll , sur Lolbas https://lolbas-project.github.io/lolbas/Libraries/comsvcs/ , on voit que le dump est **attr.exe**

On regarde où il a été créé (le crea c'est car j'étais désespéré):
![[Pasted image 20250212152352.png]]
On trouve le répertoire "C:\windows\system32\inetsrv\"

Le flag est donc **FCSC{b99a131f-0d4b-62c3-ce03-00000000db01|C:\windows\system32\inetsrv\attr.exe}**.