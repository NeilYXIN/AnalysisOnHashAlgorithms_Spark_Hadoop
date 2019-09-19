#!/usr/bin/env python
import sys
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

count = 0
currentKey = None

#### Complete the rest of the code

def updateResults(value, count): 
    scount = value      
    newcount = int(scount)
    count += newcount
    return (count)

def printResults(key, count):
    if key:
        print '%s\t%d' % (key, count);


for line in sys.stdin:
    line = line.strip()

    key, value = line.split('\t',1)
    
    if currentKey == key:
        count = updateResults(value, count)
       # count += int(value);
    else:
        printResults(currentKey, count)
        currentKey = key;
       # count = int(value);
        count = updateResults(value, 0)

printResults(currentKey, count)
 

 
