from Simulator import simulate

from matplotlib import pyplot as plt

v_a = 0.28
v_b = 0.07


Boids = simulate(t=50, n_a=600, n_b=1200, rc = 0.2, re=0.4, r0=0.55, a = 0, b= 0.55 , c= 1 , va=v_a, vb=v_b,NameGif='test media velocidade, 1800 celulas e t 50')
#va=0.028, vb=0.007
data = Boids.boids_t

x1 = []
y1 = []
x2 = []
y2 = []

for boid in data[len(data)-1]:

    if boid.kind == 1:
        x1.append(boid.x)
        y1.append(boid.y)
        v1 = boid.v
    if boid.kind == 2:
        x2.append(boid.x)
        y2.append(boid.y)
        v2 = boid.v

image = plt.plot(x1, y1, 'bo', c='red', label='Velocidade =' + str(v_a))
image2 = plt.plot(x2, y2, 'bo', label='Velocidade =' + str(v_b))
plt.legend()
plt.show()

plt.clf()

x1 = []
y1 = []
x2 = []
y2 = []

for boid in data[0]:

    if boid.kind == 1:
        x1.append(boid.x)
        y1.append(boid.y)
        v1 = boid.v
    if boid.kind == 2:
        x2.append(boid.x)
        y2.append(boid.y)
        v2 = boid.v

image = plt.plot(x1, y1, 'bo', c='red', label='Velocidade =' + str(v_a))
image2 = plt.plot(x2, y2, 'bo', label='Velocidade =' + str(v_b))
plt.legend()
plt.show()
plt.clf()

plt.plot(range(len(Boids.gama)), Boids.gama)
plt.xlabel('t')
plt.ylabel('Gama')
plt.show()