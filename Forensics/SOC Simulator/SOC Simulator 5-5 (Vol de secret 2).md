
https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-soc-simulator-5/

## Description

Durant l’été 2022, un opérateur d’importance vitale (OIV) alerte l’ANSSI car il pense être victime d’une cyberattaque d’ampleur. Le _security operation center_ (SOC) de l’OIV envoie à l’ANSSI un export de sa collecte système des derniers jours. Vous êtes chargé de comprendre les actions réalisées par l’attaquant.

**Note :** Les 5 parties sont numérotées dans l’ordre chronologique de l’attaque mais il n’est pas nécessaire de les résoudre dans l’ordre.

---

Sur une courte période de temps, l’attaquant a essayé de se connecter à de nombreuses machines, comme s’il essayait de réutiliser les secrets volés dans la partie 2. Cela lui a permis de se connecter à la machine `Workstation2`. Retrouver l’IP source, le compte utilisé et l’heure UTC de cette connexion.

**Format du flag (insensible à la casse) :** `FCSC{192.168.42.27|MYCORP\Technician|2021-11-27T17:38:54}`.

Cette épreuve a été découpée en cinq parties :

- [SOC Simulator 1/5 - Vecteur initial](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-soc-simulator-1/).
- [SOC Simulator 2/5 - Vol de secret 1](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-soc-simulator-2/).
- [SOC Simulator 3/5 - Exfiltration](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-soc-simulator-3/).
- [SOC Simulator 4/5 - Latéralisation](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-soc-simulator-4/).
- [SOC Simulator 5/5 - Vol de secret 2](https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-soc-simulator-5/).
## Write Up

En imitant les commandes de l'exercice 2 :
![[Pasted image 20250212164423.png]]

On s'intéresse à la première ligne : 
```
"2022-07-06 18:05:02.006 +02:00","LSASS Memory Dump File Creation","high","Workstation2.tinfa.loc","Sysmon",11,36597,"Path: C:\Users\ADMINI~1\AppData\Local\Temp\3\lsass.DMP ¦ Proc: C:\Windows\system32\taskmgr.exe ¦ PID: 6744 ¦ PGUID: {b7e8a6b7-b273-62c5-bc11-00000000d301}","CreationUtcTime: 2022-07-06 16:05:01.901 ¦ RuleName: - ¦ User: WORKSTATION2\Administrator ¦ UtcTime: 2022-07-06 16:05:01.901"
```

Et on a tout, le GUID du Process, et le dump ! 

Le flag est donc **FCSC{b7e8a6b7-b273-62c5-bc11-00000000d301|C:\Users\ADMINI~1\AppData\Local\Temp\3\lsass.DMP}**.