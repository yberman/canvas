#!/usr/bin/env python3
"""
svg.py

Help draw an svg.

"""

from collections import namedtuple

Circle = namedtuple("Circle", "cx cy r stroke fill")

class Drawing:
    def __init__(self):
        self.MAX = 10
        self._scale = 1080 / (2 * self.MAX)
        self.color = "black"
        self.dotsize = 0.1

        self.circles = []

        # todo
        # self.rects = []
        # self.lines = []
        # self.polyline = []
        # self.polygons = []
        # self.paths = []
        #
        # def square

    def scale(self, x):
        return self._scale*x

    def fx(self, x):
        return self.scale(x) + 1080/2

    def fy(self, y):
        return 1080 - self.scale(y) - 1080/2

    def circle(self, center, radius):
        self.circles.append(Circle(self.fx(center[0]), self.fy(center[1]), self.scale(radius), self.color, self.color))

    def dot(self, x, y):
        self.circle((x, y), self.dotsize)

    def saveToFile(self, f):
        svg_head = '<?xml version="1.0" standalone="no"?>\n<svg width="1080" height="1080" version="1.1" xmlns="http://www.w3.org/2000/svg">\n'
        f.write(svg_head)
        f.write('<rect x="0" y="0" width="1080" height="1080" stroke="black" fill="transparent" thickness="2"/>\n')
        for circle in self.circles:
            f.write(f'<circle cx="{circle.cx}" cy="{circle.cy}" r="{circle.r}" stroke="{circle.stroke}" fill="{circle.fill}" stroke-width="0"/>\n')
        f.write("</svg>")
        f.close()

    def save(self, filename):
        with open(filename, "w") as svgFile:
            self.saveToFile(svgFile)

    def show(self):
        self.save('canvas.svg')
        import webbrowser
        webbrowser.open('canvas.svg')

