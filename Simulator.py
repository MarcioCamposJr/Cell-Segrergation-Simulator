import random
import numpy as np
from copy import copy
import math

from Analyzes import create_gif,gama


class Boid:

    def __init__(self, x, y, v_x, v_y, kind):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.v = np.hypot(self.v_x, self.v_y)
        self.kind = kind

    def update(self, boids, a, b, c, r0, rc, re):

        f_x = []
        f_y = []
        v_x = []
        v_y = []

        self.x = self.v_x + self.x
        self.y = self.v_y + self.y
        for boid in boids:
            if boid != self:

                dx = boid.x - self.x
                dy = boid.y - self.y
                dist = np.hypot(dx, dy)

                v = np.hypot(self.v_x, self.v_y)
                v_rel_x = boid.v_x / v
                v_rel_y = boid.v_y / v

                if dist >= r0:
                    f_ = 0
                elif dist <= rc:
                    f_ = 1000000
                elif rc < dist < r0:
                    f_ = 1 - (dist / re)

                e_x = dx / dist
                e_y = dy / dist

                f_e_x = e_x * f_
                f_e_y = e_y * f_

                f_x.append(f_e_x)
                f_y.append(f_e_y)

                v_x.append(v_rel_x)
                v_y.append(v_rel_y)

        u_x = np.random.uniform(-0.1, 0.1)
        u_y = np.random.uniform(-0.1, 0.1)

        f_x_sum = sum(f_x)
        f_y_sum = sum(f_y)

        v_x_sum = sum(v_x)
        v_y_sum = sum(v_y)

        theta_x = a * v_x_sum + b * f_x_sum + c * u_x
        theta_y = a * v_y_sum + b * f_y_sum + c * u_y

        theta = np.arccos(theta_x / np.hypot(theta_x, theta_y))

        self.v_x = np.cos(theta) * self.v
        self.v_y = np.sin(theta) * self.v

        return self


class simulate:

    def __init__(self, va_x=None, va_y=None, vb_x=None, vb_y=None, va=0.03, vb=0.007, n_a=500, n_b=500,
                 t=1000, a=1, b=0.1, c=0.1, rc=0.2, r0=0.55, re=0.4, fp=5, NameGif='gif'):

        boids = []
        self.boids_t = []
        self.gama = None
        radius0 = ((n_a + n_b) ** (1 / 2)) * re

        for _ in range(n_a):
            if va_x is None and va_y is None:
                va_x = random.uniform(-va, va)

                va_y = np.square(va ** 2 - va_x ** 2) * random.choice([-1, 1])

            theta = random.uniform(0, 2 * math.pi)  # Ângulo aleatório em radianos
            r = random.uniform(0, radius0)  # Distância aleatória até o raio máximo
            xa = r * math.cos(theta)
            ya = r * math.sin(theta)

            boid = Boid(xa, ya, va_x, va_y, kind=1)
            boids.append(boid)

        for _ in range(n_b):
            if vb_x is None and vb_y is None:
                vb_x = random.uniform(-vb, vb)

                vb_y = np.square(vb ** 2 - vb_x ** 2) * random.choice([-1, 1])

            theta = random.uniform(0, 2 * math.pi)  # Ângulo aleatório em radianos
            r = random.uniform(0, radius0)  # Distância aleatória até o raio máximo
            xb = r * math.cos(theta)
            yb = r * math.sin(theta)

            boid = Boid(xb, yb, vb_x, vb_y, kind=2)
            boids.append(boid)

        self.boids_t.append(boids)

        perc = 100 / t

        for i in range(t - 1):
            interBoids = []
            for obj in self.boids_t[i]:
                var = copy(self.boids_t[i])
                var2 = copy(obj)
                interBoids.append(var2.update(var, a, b, c, r0, rc, re))
            self.boids_t.append(interBoids)
            perc = perc + 100 / t
            print(str(perc) + '%')

        self.SimulationResult(t, NameGif, rc)

    def SimulationResult(self, t, FileName, rc):

        self.gama = gama(self.boids_t, rc, t)

        create_gif(self.boids_t, FileName)





