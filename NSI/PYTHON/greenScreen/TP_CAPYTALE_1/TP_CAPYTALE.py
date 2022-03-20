## Cas du fond vert
'''
Etudions un cas d'école : remplacer un fond vert par un fond de paysage. Pour cela nous allons utiliser trois images : 
- *bonhomme_fond_vert.png*, l'image de référence, un bonhomme sur un fond vert,
- *fond_montagne.png*, une image de fond,
- *fond_plage.png*, une autre image de fond, pour varier les plaisirs.
'''

#Commençons par charger la bibliothèque PIL, pour la manipulation d'image.

from PIL import Image #charge la librairie PIL

#Ensuite, ouvrons l'image de référence

bfv = Image.open('bonhomme_fond_vert.png') #Ouvre l'image source

width, height = bfv.size                   #stock la taille de l'image pour une utilisation ultérieur <<<
mode = bfv.mode                            #stock le lode de l'image pour une utilisation ultérieur :
                                           # - 'L'    : image en niveaux de gris
                                           # - 'RGB'  : image en couleur
                                           # - 'RGBA' : image en couleur + transparence
                                           # - Il existe d'autre mode, voir documentation

#Créons une nouvelle image

nouvelle_image = Image.new(mode, (width, height))   #Crée une image vide <<<

'''
Nous pouvons commencer. Le code suivant permet de parcourir une image, de récupérer les valeurs d'un pixel et d'affecter une valeur à un pixel.

Modifier ce code pour modifier le fond vert par la couleur de votre choix.
'''

for x in range(width):                                    # Parcours l'image en largeur
    for y in range(height):                               # Parcours l'image en hauteur
        r,g,b,a = bfv.getpixel((x, y))                    # recupere les donnees du pixel (x,y), ici en couleur + transparence
        if r == 0 and g == 255 and b == 0:                # regarde la couleur du pixel
            value = (31, 30, 51, a)                        # cree un pixel de couleur + transparence -> tuple de 4 valeurs (r, g, b, a)
            nouvelle_image.putpixel((x, y), value)        # affecte la valeur précédente à la nouvelle image
        else :
            nouvelle_image.putpixel((x, y), (r, g, b, a)) # si la couleur du pixel (x, y) n'est pas celle a changer, reutilise les valeurs de l'image de reference


#Affichons le résultat

bfv.show()            # affiche l'image de base
nouvelle_image.show() # affiche la nouvelle image

#Ouvrez l'image de fond de votre choix

fond_plage = Image.open('fond_plage.png') #Ouvre l'image source

''''
En vous inspirant du code précédent, changez le fond vert par le fond de votre choix.

Il vous faudra :
- créer une image vide
- parcourir l'image avec le fond vert
- détecter les pixels vert, copier les pixel du fond choisi dans l'image vide
- copier les pixels non vert dans l'image vide

Vous devriez avoir un bonhomme sur un fond non vert (à moins de choisir une forêt)
'''

plage = Image.new(mode, (width, height))   #Crée une image vide <<<
for x in range(width):                                    # Parcours l'image en largeur
    for y in range(height):                               # Parcours l'image en hauteur
        r,g,b,a = bfv.getpixel((x, y))                    # recupere les donnees du pixel (x,y), ici en couleur + transparence
        if r == 0 and g == 255 and b == 0:                # regarde la couleur du pixel
            r,g,b,a = fond_plage.getpixel((x,y))
            value = (r, g, b, a)                        # cree un pixel de couleur + transparence -> tuple de 4 valeurs (r, g, b, a)
            plage.putpixel((x, y), value)        # affecte la valeur précédente à la nouvelle image
        else :
            plage.putpixel((x, y), (r, g, b, a)) # si la couleur du pixel (x, y) n'est pas celle a changer, reutilise les valeurs de l'image de reference

plage.show()

'''
Dans la vrai vie, pas en laboratoire, le fond n'est pas uni.

Pour s'approcher du réel, vous utiliserez l'image *bonhomme_fond_vert_degrade.png*. Adaptez votre code, la partie de test, pour que le fond s'applique sur cette "nouvelle" image.

*TIPS* : vous pouvez vous aider des selecteurs de couleurs sur le Web pour voir a quelles valeurs de pixel correspondent les nuances de vert.
'''

bonhomme_fond_vert_degrade = Image.open('bonhomme_fond_vert_degrade.png') #Ouvre l'image source
fond_montagne = Image.open('fond_montagne.png') #Ouvre l'image source

montagneImageFinale = Image.new(mode, (width, height))   #Crée une image vide <<<

for x in range(width):                                    # Parcours l'image en largeur
    for y in range(height):                               # Parcours l'image en hauteur
        r,g,b,a = bonhomme_fond_vert_degrade.getpixel((x, y))                    # recupere les donnees du pixel (x,y), ici en couleur + transparence
        for greenValue in range(0,255):
            if r == 0 and g == greenValue and b == 0:                # regarde la couleur du pixel
                r,g,b,a = fond_montagne.getpixel((x,y))
                value = (r, g, b, a)                        # cree un pixel de couleur + transparence -> tuple de 4 valeurs (r, g, b, a)
                montagneImageFinale.putpixel((x, y), value)        # affecte la valeur précédente à la nouvelle image
            else :
                montagneImageFinale.putpixel((x, y), (r, g, b, a)) # si la couleur du pixel (x, y) n'est pas celle a changer, reutilise les valeurs de l'image de reference

montagneImageFinale.show()

# nos greenValues
for i in range(0,255):
    print(i)

