import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def generate_fractal(x_min, x_max, y_min, y_max):

    width, height = 800, 800  # largeur et hauteur de l'image en px
    max_iterations = 100  # nombre d'itérations par px
    threshold = 10.0  # seuil d'appartenance à la fractale

    # matrice pour stocker les valeurs des couleurs des pixels
    image = np.zeros((height, width, 3), dtype=np.uint8)

    # boucle sur chaque pixel
    for x in range(width):
        for y in range(height):
            # calcule les coordonnées réelles correspondant du pixel
            real = x_min + (x / (width - 1)) * (x_max - x_min)
            imag = y_min + (y / (height - 1)) * (y_max - y_min)

            # initialisation les valeurs
            z = complex(real, imag)
            c = complex(real, imag)

            # itérations pour determner l'appartenance à la fractale
            for i in range(max_iterations):
                if abs(z) > threshold:
                    break
                z = z * z + c

            # applique une couleur en fonction du nombre d'itérations
            color = (i % 4 * 32, i % 16 * 15, i % 32 * 8)

            # Affectation de la couleur au pixel de l'image
            image[y, x] = color

    return image


#def update_zoom(frame, initial_x_min, initial_x_max, initial_y_min, initial_y_max, final_x_min, final_x_max, final_y_min, final_y_max, num_frames):
 #   progress = frame / (num_frames + 1)  # de 0 à 1
  #  new_x_min = initial_x_min + (final_x_min - initial_x_min) * progress
   # new_x_max = initial_x_max + (final_x_max - initial_x_max) * progress
    #new_y_min = initial_y_min + (final_y_min - initial_y_min) * progress
    #new_y_max = initial_y_max + (final_y_max - initial_y_max) * progress

    #return generate_fractal(new_x_min, new_x_max, new_y_min, new_y_max)
def update_zoom(frame, initial_x_min, initial_x_max, initial_y_min, initial_y_max, x_center, y_center, num_frames):
    progress = frame / (num_frames + 1)  # de 0 à 1
    new_x_min = initial_x_min + (x_center - initial_x_min) * progress
    new_x_max = initial_x_max - (initial_x_max - x_center) * progress
    new_y_min = initial_y_min + (y_center - initial_y_min) * progress
    new_y_max = initial_y_max - (initial_y_max - y_center) * progress

    return generate_fractal(new_x_min, new_x_max, new_y_min, new_y_max)
