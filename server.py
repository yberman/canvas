#!/usr/bin/env python3

from math import cos, sin
from random import random, choices
from typing import *
import asyncio
from json import dumps

import PIL.Image
import tornado.ioloop
import tornado.web
from tornado import web
import tornado.websocket


class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def __init__(self, *p, **k):
        super().__init__(*p, **k)
        self.closed = False
        self.img = PIL.Image.open('ml.png')
        self.width, self.height = self.img.size

    async def open(self):
        print("WebSocket opened")
        self.write_message(dumps({'type': 'setup', 'width': self.width, 'height': self.height}))
        i = 0
        for i in range(1000000000):
            msg = ""
            for j in range(100):
                x = 10*random()
                y = 10*random()
#                p1 = cos(x)*cos(x)*cos(y)*cos(y)
#                p2 = cos(x)*cos(x)*sin(y)*sin(y)
#                p3 = sin(x)*sin(x)*cos(y)*cos(y)
#                p4 = sin(x)*sin(x)*sin(y)*sin(y)
                x *= self.width / 10
                y *= self.height / 10
                r,g,b=self.img.getpixel((int(x), int(y)))

#                color = choices(["black", "red", "purple", "green"], weights=[p1, p2, p3, p4], k=1)[0]
                color = f'rgb({r}, {g}, {b})'
                svg_elem = f'<circle cx="{x}" cy="{y}" r="8" stroke="black" stroke-width="0" fill="{color}"  />'
                msg += svg_elem
            self.write_message(dumps({'type': 'circles', 'payload': msg}))
            await asyncio.sleep(0.4) 
 
#        while not self.closed:
#            svg_elem = f'<circ cx="{i*20}" cy="{i*20}" r="10" />'
#            self.write_message(svg_elem)
#            i += 1
#            await asyncio.sleep(0.5)

    def on_message(self, message):
        self.write_message("hello " + message)

    def on_close(self):
        print("WebSocket closed")
        self.closed = True


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('./index.html')

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/index.html", IndexHandler),
        (r"/static/(.*)", web.StaticFileHandler, {"path": "./public/"}),
        (r"/websocket", EchoWebSocket),
    ], debug=True)
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()


