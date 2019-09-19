#!/usr/bin/env python
import sys    

for line in sys.stdin:    
    line = line.strip( )    
    data = line.split( )    
 
    if data[0] == 'A':
        for i in range(0,100):
            key = data[1]+' '+str(i)
            value = data[0]+' '+data[2]+' '+data[3]
            print '%s\t%s' % (key,value);
    elif  data[0] == 'B':
        for i in range(0,100):
            key = str(i)+' '+data[2]
            value = data[0]+' '+data[1]+' '+data[3]
            print '%s\t%s' % (key,value);
   
