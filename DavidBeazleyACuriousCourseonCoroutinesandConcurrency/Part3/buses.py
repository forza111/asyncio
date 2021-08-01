# An example of setting up an event handling pipeline with coroutines
# and XML parsing.

from DavidBeazleyACuriousCourseonCoroutinesandConcurrency.Part1.coroutine import coroutine
import xml.sax
from cosax import EventHandler



@coroutine
def buses_to_dicts(target):
    while True:
        event, value = yield
        # Look for the start of a <bus> element
        if event == 'start' and value[0] == 'bus':
            busdict = {}
            fragments = []
            # Capture text of inner elements in a dict
            while True:
                event, value = yield
                if event == 'start':
                    fragments = []
                elif event == 'text':
                    fragments.append(value)
                elif event == 'end':
                    if value != 'bus':
                        busdict[value] = "".join(fragments)
                    else:
                        target.send(busdict)
                        break


@coroutine
def filter_on_field(fieldname,value,target):
    while True:
        busdict = yield
        if busdict.get(fieldname) == value:
            target.send(busdict)


@coroutine
def bus_locations():
    while True:
        bus = yield
        print ("%(route)s,%(id)s,\"%(direction)s\","\
              "%(latitude)s,%(longitude)s" % bus)



if __name__ == '__main__':
    xml.sax.parse("allroutes.xml",
              EventHandler(
                   buses_to_dicts(filter_on_field("route","22", filter_on_field("direction","North Bound",bus_locations())))
              ))