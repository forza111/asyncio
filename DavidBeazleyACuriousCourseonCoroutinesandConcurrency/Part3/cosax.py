# An example showing how to push SAX events into a coroutine target

import xml.sax
from DavidBeazleyACuriousCourseonCoroutinesandConcurrency.Part1.coroutine import coroutine


class EventHandler(xml.sax.ContentHandler):
    def __init__(self,target):
        self.target = target
        # self.sch = 0

    def startElement(self, name, attrs):
        self.target.send(('start', (name, attrs._attrs)))
        # self.sch += 1
        # print('StartELEMENT', self.sch)


    def characters(self, text):
        self.target.send(('text', text))
        # self.sch += 1
        # print('Characters', self.sch)


    def endElement(self, name):
        self.target.send(('end', name))
        # self.sch += 1
        # print('EndELEMENTS', self.sch)



if __name__ == "__main__":
    @coroutine
    def printer():
        while True:
            event = yield
            print(event)

    xml.sax.parse("allroutes.xml", EventHandler(printer()))