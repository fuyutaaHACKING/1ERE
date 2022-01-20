from PIL import Image #import l'ensemble des fonctionnalités de manipulation d'image de la bibliothèque PIL (pillow)
import numpy

def draw():
    userInput = int(input("Enter a value betweeen 0-255"))

    width = 365
    height = 141
    gray = None  # Initialise la variable gray a None
    gray = Image.new('L', (width, height))  # Crée une image vide <<<
    pixel_values = list(gray.getdata())

    for x in range(width):  # Itère sur l'image <<<
        for y in range(height):
            pixel_values = numpy.sum(pixel_values).reshape((width, height, 3))

            if (userInput > pixel_values):
                gray.putpixel((x, y), 0)  # affecte la valeur précédente à l'image vide <<<
            else:
                gray.putpixel((x, y), 255)  # affecte la valeur précédente à l'image vide <<<
    gray.show()  # afiche le résultat en niveau de gris <<<

if True:
    draw()