#!/usr/bin/env python
import sys    

for line in sys.stdin:    
 
    line = line.strip( )    
    
    words = line.split( )    

    matrix = words[0]
    rowindex = words[1]
    colindex = words[2]
    value = words[3]
    if matrix == 'A':
        for i in range(0,10):
            mkey = str(rowindex)+' '+str(i) 
            mvalue = matrix+' '+str(colindex)+' '+str(value)
            print '%s\t%s' % (mkey,mvalue);
    elif matrix == 'B':
        for i in range(0,10):
            mkey = str(i)+' '+str(colindex) 
            mvalue = matrix+' '+str(rowindex)+' '+str(value)
            print '%s\t%s' % (mkey,mvalue);
   
