#!/usr/bin/env python
import sys    


text = sys.stdin.readlines()
size = len(text)

N = int((size/2)**(1.0/3))
A_matrix = [0 for i in range(N)]
B_matrix = [0 for i in range(N)]

time = 0;
for line in text:
    line = line.strip()
    key,value = line.split('\t')  
    element_matrix = value.split(' ',2)[0]
    element_index = value.split(' ',2)[1]
    element_value = value.split(' ',2)[2]
    if(element_matrix == 'A'):
        A_matrix[int(element_index)-1] = int(element_value)
        
    elif(element_matrix == 'B'):
        B_matrix[int(element_index)-1] = int(element_value)
    time=time+1
    if((time % (2*N))==0):
        C_value=0
        for i in range(0,N):
            C_value += A_matrix[i] * B_matrix[i]
        print ('C '+'%s\t%d' % (key,C_value))


