#!/usr/bin/env python
import sys    

A_matrix = [0 for i in range(100)]
B_matrix = [0 for i in range(100)]
    
oldkey = 'first'
C_value = 0

for line in sys.stdin:    
    line = line.strip()  
    key = line.split('\t')[0]
    value= line.split('\t')[1]   
    element_matrix = value.split(' ',2)[0]
    element_index = value.split(' ',2)[1]
    element_value = value.split(' ',2)[2]
    
    if (oldkey != key and oldkey != 'first'):
       for i in range(0,100):
            C_value += A_matrix[i] * B_matrix[i]
            A_matrix[i] = 0
            B_matrix[i] = 0
       print ('C '+'%s\t%d' % (oldkey,C_value))
       oldkey = key
       C_value = 0
       
    if(element_matrix == 'A'):
        A_matrix[int(element_index)-1] = int(element_value)
        
    if(element_matrix == 'B'):
        B_matrix[int(element_index)-1] = int(element_value)

    oldkey = key
        
   
