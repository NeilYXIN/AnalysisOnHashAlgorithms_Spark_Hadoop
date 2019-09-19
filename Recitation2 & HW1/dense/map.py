#!/usr/bin/env python
import sys

text = sys.stdin.readlines()
size = len(text)
N = int((size/2)**0.5)
for line in text:    
    line = line.strip( )    
    data = line.split( )    
 
    if data[0] == 'A':
        for i in range(0,N):
            key = data[1]+' '+str(i)
            value = data[0]+' '+data[2]+' '+data[3]
            print '%s\t%s' % (key,value)
    elif  data[0] == 'B':
        for i in range(0,N):
            key = str(i)+' '+data[2]
            value = data[0]+' '+data[1]+' '+data[3]
            print '%s\t%s' % (key,value)
         

