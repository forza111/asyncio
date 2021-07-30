# An example of broadcasting a data stream onto multiple coroutine targets.
# This example shows "fan-in"---a situation where multiple coroutines
# send to the same target.


import time
from copipe import access_log  #file
from DavidBeazleyACuriousCourseonCoroutinesandConcurrency.Part1.coroutine import coroutine
# A data source.  This is not a coroutine, but it sends
# data into one (target)


def follow(thefile, target):
    thefile.seek(0,2)       #Go to end of the file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)


#A filter
@coroutine
def grep(pattern, target):
    while True:
        line = yield
        if pattern in line:
            target.send(line)


#A sink. A coroutine that receives data
@coroutine
def printer():
    while True:
        line = yield
        print(line)


#Broadcast a stream ontp multiple targerts
@coroutine
def broadcast(targets):
    while True:
        item = yield
        for target in targets:
            target.send(item)


if __name__ == "__main__":
    with open(access_log) as f:
        p = printer()
        follow(f, broadcast([grep("python", p),
                             grep("ply",p),
                             grep("swig",p)])
               )