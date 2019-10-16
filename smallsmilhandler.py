#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.tag_list = []
        self.rootlayout = ["width", "height", "background-color"]
        self.region = ["id", "top", "bottom", "left", "right"]
        self.img = ["src", "region", "begin", "dur"]
        self.audio = ["src", "begin", "dur"]
        self.textstream = ["src", "region"]
