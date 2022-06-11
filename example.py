#!/usr/bin/env python3
from svg import Drawing

from random import random, choices
from math import sin, cos

c = Drawing()
for i in range(100000):
    x = -10 + 20*random()
    y = -10 + 20*random()

    p1 = cos(x)*cos(x)*cos(y)*cos(y)
    p2 = cos(x)*cos(x)*sin(y)*sin(y)
    p3 = sin(x)*sin(x)*cos(y)*cos(y)
    p4 = sin(x)*sin(x)*sin(y)*sin(y)

    c.color = choices(["black", "red", "blue", "green"], weights=[p1, p2, p3, p4], k=1)[0]
    c.dot(x, y)

c.show()
