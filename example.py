#!/usr/bin/env python3
from svg import Drawing

from math import sin, cos, pi

c = Drawing()

c.color = "black"
for i in range(-9, 10):
    c.dot(i, i*abs(i)/10)

c.color = "red"
for i in range(10000):
    j = -10 + (20 * i / 10000)
    c.dot(j, 3*sin(j))

c.color = "green"
for i in range(10000):
    j = -10 + (20 * i / 10000)
    c.dot(j, 3*cos(j))


R = 7
N = 400
c.color = "blue"
for i in range(N):
    theta = 2*pi*i / N
    if c.color == "blue":
        c.color = "yellow"
    else:
        c.color = "blue"
    c.dot(R*cos(theta), R*sin(theta))

c.show()
