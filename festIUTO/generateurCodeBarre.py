import random
import barcode # pip install python-barcode
from barcode.writer import ImageWriter

def generate_random_barcode():
    # Génération d'une séquence de chiffres aléatoires pour le code-barres
    barcode_data = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    
    # Création d'un objet Code128
    code = barcode.get('code128', barcode_data, writer=ImageWriter())

    # Génération du code-barres en tant qu'image
    code.save('random_barcode')

if __name__ == "__main__":
    generate_random_barcode()
