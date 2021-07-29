# A simple example showing how to hook up a pipeline with
# coroutines.   To run this, you will need a log file.
# Run the program logsim.py in the background to get a data
# source.

import time
import os
from DavidBeazleyACuriousCourseonCoroutinesandConcurrency.Part1.coroutine import coroutine
# A data source.  This is not a coroutine, but it sends
# data into one (target)



workdir = os.getcwd()
dirname = os.path.dirname(workdir)
access_log = os.path.join(dirname, "Part1", "access-log")


def follow(thefile, target):
    thefile.seek(0,2)      # Go to the end of the file
    while True:
         line = thefile.readline()
         if not line:
             time.sleep(0.1)    # Sleep briefly
             continue
         target.send(line)

# A filter.

@coroutine
def grep(pattern,target):
    while True:
        line = yield          # Receive a line
        if pattern in line:
            target.send(line)    # Send to next stage

# A sink.  A coroutine that receives data

@coroutine
def printer():
    while True:
         line = yield
         print(line)

# Example use
if __name__ == '__main__':
    with open(access_log) as f:
        follow(f, grep('python',printer()))