import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageSequence

def create_gif(Boids, FileName):  # CREATE DICOM IMAGE ANIMATION
    # Crie uma lista para armazenar as imagens dos frames
    frames = []

    # Configure os parâmetros de plotagem
    fig, ax = plt.subplots()

    cmap_celula_1 = plt.cm.Blues
    cmap_celula_2 = plt.cm.Reds

    for t in range(len(Boids)):
        x1 = []
        y1 = []
        x2 = []
        y2 = []

        for boid in Boids[t]:
            if boid.kind == 1:
                x1.append(boid.x)
                y1.append(boid.y)
                v1 = boid.v
            if boid.kind == 2:
                x2.append(boid.x)
                y2.append(boid.y)
                v2 = boid.v

        ax.cla()

        # Plote as células usando as informações de posição
        ax.scatter(x1, y1, color=cmap_celula_1(0.7), s=100)
        ax.scatter(x2, y2, color=cmap_celula_2(0.7), s=100)

        # Salve o gráfico como uma imagem em buffer
        fig.canvas.draw()
        image = Image.frombytes('RGB', fig.canvas.get_width_height(), fig.canvas.tostring_rgb())

        frames.append(image)

    frames[0].save("C:/Users/marci/Videos/Captures/"+str(FileName)+".gif", save_all=True, append_images=frames[1:], optimize=False, duration=200,loop=0)

def gama(Boids, rc, t):
    gaman = []
    gaman_t = []
    n1 = 0
    n2 = 0
    for i in range(t):
        for obj in Boids[i]:
            if obj.kind == 1:
                for obj2 in Boids[i]:
                    if abs(np.hypot(obj.x, obj.y) - np.hypot(obj2.x, obj2.y)) >= rc:
                        if obj2.kind == 1:
                            n1 = n1 + 1
                        if obj2.kind == 2:
                            n2 = n2 + 1

                gama = n1 / (n1 + n2)
                gaman.append(gama)

        gaman_t.append(np.mean(gaman))



    return gaman_t