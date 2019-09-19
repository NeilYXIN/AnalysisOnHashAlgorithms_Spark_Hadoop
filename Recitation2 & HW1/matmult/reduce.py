#!/usr/bin/env python
import sys    

lastkey = None
result = 0
valA = []
valB = []

for i in range(0,100):
    valA.append(0)
    valB.append(0)
  
for line in sys.stdin:    
    line = line.strip()    
   
    key,value = line.split('\t',1)    
    words = value.split();

    if (lastkey != key and lastkey != None):
       for i in range(0,100):
            result+= valA[i] * valB[i]
            valA[i] = 0
            valB[i] = 0
       if result != 0:
           print '%s\t%d' % (lastkey,result)
       lastkey = key
       result = 0

    if(words[0] == 'A'):
        valA[int(words[1])-1] = int(words[2])
    if(words[0] == 'B'):
        valB[int(words[1])-1] = int(words[2])
    lastkey = key

for i in range(0,100):
    result+= valA[i] * valB[i]
    valA[i] = 0
    valB[i] = 0
if result != 0:
   print '%s\t%d' % (lastkey,result)




        
   
