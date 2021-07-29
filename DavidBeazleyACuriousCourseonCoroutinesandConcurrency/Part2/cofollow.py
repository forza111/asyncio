# A simple example showing how to hook up a pipeline with
# coroutines.   To run this, you will need a log file.
# Run the program logsim.py in the background to get a data
# source.

from DavidBeazleyACuriousCourseonCoroutinesandConcurrency.Part1.coroutine import coroutine

# A data source.  This is not a coroutine, but it sends
# data into one (target)

import time
import os

fpath = os.path.join("/asyncio/DavidBeazleyACuriousCourseonCoroutinesandConcurrency/Part1", "access-log")

def follow(thefile, target):
    thefile.seek(0,2)       #Go to the end of the file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)

# A sink.  A coroutine that receives data

@coroutine
def printer():
    while True:
        line = yield
        print(line)


if __name__ == "__main__":
    with open(fpath) as f:
        follow(f, printer())