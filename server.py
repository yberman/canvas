#!/usr/bin/env python3
from math import cos, sin
import tornado.ioloop
from random import random, choices
import tornado.websocket
import tornado.web
from tornado import web
import asyncio
from typing import *

class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def __init__(self, *p, **k):
        super().__init__(*p, **k)
        self.closed = False

    async def open(self):
        print("WebSocket opened")
        i = 0
        for i in range(1000000000):
            msg = ""
            for j in range(50):
                x = 10*random()
                y = 10*random()
                p1 = cos(x)*cos(x)*cos(y)*cos(y)
                p2 = cos(x)*cos(x)*sin(y)*sin(y)
                p3 = sin(x)*sin(x)*cos(y)*cos(y)
                p4 = sin(x)*sin(x)*sin(y)*sin(y)
                x *= 80
                y *= 40
                color = choices(["black", "red", "purple", "green"], weights=[p1, p2, p3, p4], k=1)[0]
                svg_elem = f'<circle cx="{x}" cy="{y}" r="8" stroke="black" stroke-width="0" fill="{color}"  />'
                msg += svg_elem
            self.write_message(msg)
            await asyncio.sleep(0.1) 
 
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

