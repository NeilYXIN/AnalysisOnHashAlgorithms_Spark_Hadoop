import random
import sys

str1 = raw_input("Please type in the rows/columns of NxN Matrix:")
path = "/usr/local/hadoop/Recitation2/matmult2/input/part-00000"

fo = open(path, "wb")
rc = int(str1)
for i in range(0, rc):
    for j in range(0, rc):
        stri = str(i)
        strj = str(j)
        strv = str(int(random.uniform(0, 9)))
        if strv != '0':
            strres = 'A' + ' ' + stri + ' ' + strj + ' ' + strv + '\n'

            fo.write(strres)
            print strres

for i in range(0, rc):
    for j in range(0, rc):
        stri = str(i)
        strj = str(j)
        strv = str(int(random.uniform(0, 2)))
        if strv != '0':
            strres = 'B' + ' ' + stri + ' ' + strj + ' ' + strv + '\n'

            fo.write(strres)
            print strres

fo.close()

