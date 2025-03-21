
https://hackropole.fr/fr/challenges/forensics/fcsc2024-forensics-soc-simulator-4/

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

On va pas faire compliqué, on reprenant nos évènements, on tri les informations "Workstation2", "4624" et "172.16.20.20", et on essaye de trouver les logs qui pointent.

L'event 4624 c'est les logs réussis, et l'ip "172.16.20.20", c'est grâce à notre découverte exercice 1, on a vu qu'elle faisait des tentatives d'echec.

On retrouve les éléments suivants :
```xml
<?xml version="1.0" encoding="utf-8"?>
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Security-Auditing" Guid="{54849625-5478-4994-a5ba-3e3b0328c30d}">
    </Provider>
    <EventID>4624</EventID>
    <Version>2</Version>
    <Level>0</Level>
    <Task>12544</Task>
    <Opcode>0</Opcode>
    <Keywords>0x8020000000000000</Keywords>
    <TimeCreated SystemTime="2022-07-06T13:26:57.153049100Z">
    </TimeCreated>
    <EventRecordID>112617</EventRecordID>
    <Correlation ActivityID="{52c9385a-8f73-0000-ac38-c952738fd801}">
    </Correlation>
    <Execution ProcessID="592" ThreadID="4616">
    </Execution>
    <Channel>Security</Channel>
    <Computer>Workstation2.tinfa.loc</Computer>
    <Security>
    </Security>
  </System>
  <EventData>
    <Data Name="SubjectUserSid">S-1-0-0</Data>
    <Data Name="SubjectUserName">-</Data>
    <Data Name="SubjectDomainName">-</Data>
    <Data Name="SubjectLogonId">0x0</Data>
    <Data Name="TargetUserSid">S-1-5-21-287873022-4015043350-4189064643-500</Data>
    <Data Name="TargetUserName">Administrator</Data>
    <Data Name="TargetDomainName">WORKSTATION2</Data>
    <Data Name="TargetLogonId">0x5a102a3</Data>
    <Data Name="LogonType">3</Data>
    <Data Name="LogonProcessName">NtLmSsp </Data>
    <Data Name="AuthenticationPackageName">NTLM</Data>
    <Data Name="WorkstationName">-</Data>
    <Data Name="LogonGuid">{00000000-0000-0000-0000-000000000000}</Data>
    <Data Name="TransmittedServices">-</Data>
    <Data Name="LmPackageName">NTLM V2</Data>
    <Data Name="KeyLength">0</Data>
    <Data Name="ProcessId">0x0</Data>
    <Data Name="ProcessName">-</Data>
    <Data Name="IpAddress">172.16.20.20</Data>
    <Data Name="IpPort">63759</Data>
    <Data Name="ImpersonationLevel">%%1833</Data>
    <Data Name="RestrictedAdminMode">-</Data>
    <Data Name="TargetOutboundUserName">-</Data>
    <Data Name="TargetOutboundDomainName">-</Data>
    <Data Name="VirtualAccount">%%1843</Data>
    <Data Name="TargetLinkedLogonId">0x0</Data>
    <Data Name="ElevatedToken">%%1842</Data>
  </EventData>
</Event>
```

J'ai défoncé la plateforme car ça ne voulait pas flag, je mettais bien TINFA\Administrator en user, puis je me suis dit attends c'est un compte local ça, et les comptes locaux c'est le nom de la machine le domaine...

Le flag est donc **FCSC{b99a131f-0d4b-62c3-ce03-00000000db01|C:\windows\system32\inetsrv\attr.exe}**.