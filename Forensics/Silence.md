#android
https://hackropole.fr/fr/challenges/forensics/fcsc2023-forensics-la-gazette-de-windows/

## Description

Vous êtes Bob. Une vieille amie vous avait envoyé un flag pour un FCSC futur, il y a quelques années, avant que vous ne perdiez contact. Elle se rappelle à vous en indiquant qu’elle fait maintenant partie de l’organisation du FCSC. Elle a pu mettre en place ce flag et vous propose de le jouer.

Problème, le flag est resté dans une sauvegarde de SMS de votre application SMS de l’époque, [Silence](https://silence.im/). Vous avez complètement oublié le code que vous utilisiez, vous savez seulement qu’il s’agissait d’un code à 5 chiffres décimaux.

Saurez-vous retrouver ce flag et montrer à Alice que vous ne l’aviez pas oubliée ?

Toute ressemblance avec des faits et des personnages existants ou ayant existé serait purement fortuite et ne pourrait être que le fruit d’une pure coïncidence.

Aucune IA n’a été maltraitée durant la réalisation de ce challenge.

## Write Up

On explore le contenu Zip, on tombe sur des bdds, dont une avec les SMS mais on voit bien que c'est chiffré : 
![[Pasted image 20250213094954.png]]

Et une avec des contacts de téléphone :
![[Pasted image 20250213095056.png]]

Dans le /shared preferences, on tombe sur ceci :
![[Pasted image 20250213095254.png]]
ça a l'air intéressant, puis on a un fichier qui s'appelle "3" dans /files...

On va s'intéresser à comment déchiffrer des SMS avec ces infos. Mais avant tout, on va taper "Silence SMS" sur Google pour voir si ce n'est pas quelque chose de déjà connu :
![[Pasted image 20250213095748.png]]

Ok c'est nickel, si c'est connu, il y a logiquement un github de quelqu'un qui l'a déjà cassé... :
![[Pasted image 20250213095837.png]]
Bingo !!

Après avoir fait l'installation, ça ne marche pas :
![[Pasted image 20250213104803.png]]

Si le code est à 5 chiffres décimaux, ça fait un gros bruteforce ! J'ai essayé "WAP_PUSH_SI!" qui était dans les contacts on sait jamais, mais rien non plus...

On va lancer le bruteforce pendant qu'on essaye de chercher d'autres infos.. Alors j'ai voulu modifié le script bash mais ça marchait pas trop, donc j'ai modifié direct le java pour le repatch derrière mais j'ai eu pas mal d'erreur... Voici la version finale bien patcher :

```java
String userPassphrase = "";
    if (System.console() != null) {

      userPassphrase = new String(System.console().readPassword("Password (leave empty if empty): "));

    } else {

      System.err.println("No console, reading password from stdin.");

      BufferedReader buffer = new BufferedReader(new InputStreamReader(System.in));

      try {

        userPassphrase = buffer.readLine();

      } catch (IOException exc) {

        System.err.println("Can't read stdin");

        exc.printStackTrace(System.err);

        System.exit(74);

        return;

      }

    }

    if (userPassphrase.isEmpty()) {

      userPassphrase = UNENCRYPTED_PASSPHRASE;

    }

  

    InputData silProps = new InputData();

    silProps.passphrase_iterations = Integer.parseInt(props.getProperty("passphrase_iterations"));

    silProps.master_secret = Base64.getDecoder().decode(props.getProperty("master_secret"));

    silProps.mac_salt = Base64.getDecoder().decode(props.getProperty("mac_salt"));

    silProps.encryption_salt = Base64.getDecoder().decode(props.getProperty("encryption_salt"));    

  

    MasterSecret sec = null;

    for (int i = 10000; i <= 99999; i++) {

      try {

        userPassphrase = Integer.toString(i);

        silProps.user_passphrase = userPassphrase;

        sec = getMasterSecret(silProps, silProps.user_passphrase);

        break;

      } catch (InvalidPassphraseException exc) {

        System.err.println("Invalid passphrase!");

        continue;

      } catch (GeneralSecurityException exc) {

        continue;

      } catch (IOException exc) {

        continue;
      }

    }
```

ça ne passe pas les contrôles Qualités, mais ça fonctionne !! Bon pour éviter de se retaper tout le json, p'tite regex :
![[Pasted image 20250213120204.png]]

Le flag est donc **FCSC{98c98d98e5a546dcf6b1ea6e47602972ea1ce9ad7262464604753c4f79b3abd3}**