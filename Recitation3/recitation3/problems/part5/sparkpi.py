#!/usr/bin/env python
from pyspark import SparkContext
import random
import sys
import math
from operator import add 
sc = SparkContext(appName="Monte Carlo Pi")
path = "/usr/local/hadoop/Recitation2/recitation3/problems/part5/input/input"

fo = open(path, "wb")
rc = 1000.0
inrc = int(rc)

for i in range(0, inrc):
    key = str(1)
    strres = key + ' '
    fo.write(strres)
fo.close()
lines = sc.textFile(sys.argv[1], 1)
counts = lines.flatMap(lambda x: x.strip().split(' ')) \
              .map(lambda x: (x,0 if (pow(random.uniform(0, 1),2) + pow(random.uniform(0, 1),2))>1 else 1)) \
              .reduceByKey(lambda x,y:x+y)
output = counts.collect()
val = float(output[0][1])
print "By Monte Carlo Sampling, Pi is estimated to be %f"%(4.0*val/rc)

