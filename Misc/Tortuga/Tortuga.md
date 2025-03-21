https://hackropole.fr/fr/challenges/misc/fcsc2024-misc-tortuga/

## Description

On vous propose une séance de dessin !

Le fichier `tortuga-flag.txt` contient le flag dessiné uniquement à l’aide de segments.

La méthode pour encoder ces segments est simpliste. On fixe un point de départ `P(x, y)` initialisé à un point quelconque dans le plan, par exemple `(0, 0)`. Puis, chaque élément `(dx, dy)` dans la liste `L` fournie dans le fichier `tortuga.txt` permet d’atteindre un nouveau point `Q(x + dx, y + dy)` et le segment `PQ` est tracé entre ces deux points. Une fois ce segment tracé, le point courant `P` est remplacé par le point `Q`, et ce procédé est itéré sur tous les éléments de la liste.

Afin d’autoriser plusieurs symboles, la valeur spéciale `(0, 0)` pour `(dx, dy)` est utilisée pour déplacer le point `P` comme décrit ci-dessus avec l’élément suivant de la liste, mais aucun segment n’est tracé.

On donne l’exemple suivant (`tortuga-example.txt`) où le point initial `P` est choisi tout en haut à gauche.

```py
[
  # Draw triangle pointing down (drawn clockwise)
  (2, 0), (-1, 2), (-1, -2),
  # Skip
  (0, 0), (3, 0),
  # Draw triangle pointing up (drawn counterclockwise)
  (-1, 2), (2, 0), (-1, -2),
  # Skip
  (0, 0), (1, 0),
] * 6
```

Et l’image associée :

![](https://hackropole.fr/challenges/fcsc2024-misc-tortuga/public/tortuga-example.png)

**Note :** le flag est de la forme `FCSC{[0-9]+}`.

![](https://hackropole.fr/challenges/fcsc2024-misc-tortuga/public/tortuga-meme.jpeg)

## Write Up

On cherche un module python qui pourrait nous faire le taff :
![[Pasted image 20250214085718.png]]
On tombe sur le Module "Turtle".

Deux fonctions à retenir "pen" (penup pour lever le crayon et pendown pour baisser le crayon) et "goto" pour se tp.

On va pas expliquer toute la suite du code, mais aucune IA n'a été maltraitée :
```python
from turtle import *
from time import sleep
import pyautogui
from PIL import Image

# Tableau de tuples représentant les déplacements
tab = [(0,2),(0,-2),(1,0),(-1,0),(0,1),(1,0),(0,0),(1,1),(0,-2),(1,0),(-1,0),(0,2),(1,0),(0,0),(2,-2),(-1,0),(0,1),(1,0),(0,1),(-1,0),(0,0),(2,0),(0,-2),(1,0),(-1,0),(0,2),(1,0),(0,0),(3,-2),(-1,0),(0,1),(-1,0),(1,0),(0,1),(1,0),(0,0),(4,-2),(-2,0),(0,0),(0,2),(2,0),(0,-2),(0,1),(-2,0),(0,0),(3,-1),(0,2),(0,0),(3,-2),(-1,0),(-1,1),(0,1),(2,0),(0,-1),(-2,0),(0,0),(3,0),(1,0),(0,-1),(-1,0),(0,2),(1,0),(0,-1),(0,0),(1,1),(1,0),(0,-2),(-1,0),(0,0),(0,1),(1,0),(0,0),(2,1),(0,-2),(-1,1),(2,0),(0,0),(1,-1),(1,0),(-1,2),(0,0),(0,-1),(1,0),(0,0),(1,-1),(1,0),(0,1),(-1,0),(0,1),(1,0),(0,0),(1,0),(1,0),(0,-1),(-1,0),(0,-1),(1,0),(0,0),(1,2),(0,-2),(1,0),(-1,0),(0,2),(1,0),(0,-1),(-1,0),(0,0),(2,1),(1,0),(-1,0),(0,-2),(1,0),(-1,2),(1,0),(0,-2),(0,0),(1,0),(0,1),(1,0),(0,-1),(0,2),(0,0),(2,-2),(1,0),(0,1),(1,0),(-1,0),(0,1),(-1,0)]

# Position initiale de la tortue
x = 0
y = 0
SPEED = 50  # Réduire la vitesse pour mieux voir le tracé

# Fonction pour déplacer la tortue
def move_turtle(dx, dy):
    global x, y
    x += dx
    y += dy
    goto(x * SPEED, y * SPEED)

# Configuration initiale de la tortue
speed(5)  # Vitesse de la tortue (1 = lent, 10 = rapide)
penup()   # Lever le crayon pour ne pas dessiner pendant le déplacement initial
goto(0, 0)  # Position initiale de la tortue
pendown()  # Baisser le crayon pour commencer à dessiner

# Agrandir la fenêtre de la tortue
screensize(50000, 50000)

# Parcourir le tableau de tuples et déplacer la tortue
i = 0
while i < len(tab):
    dx, dy = tab[i]
    if dx == 0 and dy == 0:
        penup()  # Lever le crayon pour les déplacements "Skip"
        i += 1
        
        if i < len(tab):
            dx, dy = tab[i]
            move_turtle(dx, dy)
            
        pendown()  # Baisser le crayon pour continuer à dessiner
    else:
        move_turtle(dx, dy)
    i += 1

# Attendre 5 secondes avant de fermer la fenêtre
sleep(5)

# Capturer l'écran et sauvegarder en PNG
screenshot = pyautogui.screenshot()
screenshot.save("turtle_drawing.png")

done()  # Terminer le dessin et fermer la fenêtre
```

Après automatisation ça nous donne tout ça :
![[Pasted image 20250214094005.png]]
À l'endroit (à savoir que la fin est coupé, car j'ai pas pu tout screen) => à la fin on aperçoit un 4 :
![[Pasted image 20250214100722.png]]

Le flag est donc **FCSC{316834725604}**.