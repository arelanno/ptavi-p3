#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.tags_list = []

        self.rootlayout = ["width", "height", "background-color"]
        self.region = ["id", "top", "bottom", "left", "right"]
        self.img = ["src", "region", "begin", "dur"]
        self.audio = ["src", "begin", "dur"]
        self.textstream = ["src", "region"]

        self.tags = {'root-layout': self.rootlayout,
                     'region': self.region,
                     'img': self.img,
                     'audio': self.audio,
                     'textstream': self.textstream}

    def startElement(self, name, attrs):

        dicctag = {}

        if name in self.tags:
            dicctag = {'Tag': name}
            for atribute in self.tags[name]:
                dicctag[atribute] = attrs.get(atribute, "")
            self.tags_list.append(dicctag)
            
    def get_tags(self):

        return self.tags_list


if __name__ == "__main__":
    parser = make_parser()
    Handler = SmallSMILHandler()
    parser.setContentHandler(Handler)
    parser.parse(open('karaoke.smil'))
    print(Handler.get_tags())
