import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from fractale_func import generate_fractal, update_zoom
import imageio

# paramètres de zoom
initial_x_min, initial_x_max, initial_y_min, initial_y_max = -2.0, 2.0, -2.0, 2.0
final_x_min, final_x_max, final_y_min, final_y_max = -5.0, 5.0, -5.0, 5.0
num_frames = 50  # nombre d'images pour le zoom

fig, ax = plt.subplots()  # figure et un axe
ax.axis('on')  # axes affichés ou non

anim = FuncAnimation(fig, update_zoom, frames=range(num_frames), repeat=False,
                     fargs=(initial_x_min, initial_x_max, initial_y_min, initial_y_max,
                            final_x_min, final_x_max, final_y_min, final_y_max))


# liste pour stocker les images de l'animation
images = []

for i in range(num_frames):
    progress = i / (num_frames - 1)  # de 0 à 1
    new_x_min = initial_x_min + (final_x_min - initial_x_min) * progress
    new_x_max = initial_x_max + (final_x_max - initial_x_max) * progress
    new_y_min = initial_y_min + (final_y_min - initial_y_min) * progress
    new_y_max = initial_y_max + (final_y_max - initial_y_max) * progress

    frame = generate_fractal(new_x_min, new_x_max, new_y_min, new_y_max)
    images.append(frame)

# Enregistre les images dans un fichier .GIF
imageio.mimsave('zoom_fractal.gif', images,
                duration=0.1)  # durée entre les images

# Affichez le GIF généré
plt.imshow(images[-1])  # affiche la dernière image générée
plt.show()
