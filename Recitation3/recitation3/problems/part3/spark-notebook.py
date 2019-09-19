
# coding: utf-8

# In[62]:


import pyspark
from operator import add
import numpy as np
from pyspark.sql import SparkSession


# Intialize a spark instance-

# In[63]:


try:
    sc.stop()
except:
    pass
sc = pyspark.SparkContext(appName="spark-notebook")
ss = SparkSession(sc)


# In[64]:


myRDD = sc.textFile("file:///usr/local/hadoop/Recitation2/recitation3/problems/part3/numbers.txt", 10)


# Get number of RDD partitions-

# In[65]:


myRDD.getNumPartitions()


# In[66]:


print myRDD.take(20) # get first 20 values


# We will define a square function for our map operation- 

# In[67]:


def square(value):
    return int(value)**2


# In[68]:


newRDD = myRDD.map(square)


# In[69]:


print newRDD.collect() # get map results


# In[70]:


subRDD = newRDD.map(lambda x: (x, 1) if x%2==0 else (x, 0)) # using lamda functions


# The above map function maps generated two types of key value pairs- (even, 1) and (odd, 0)

# In[71]:


print subRDD.collect()


# Now define a lambda function to generate (key, value) pairs where key = even or odd depending upon the input and 
# value = input

# In[72]:


# your code here
testRDD = subRDD.map(lambda x:('even' if x[1]==1 else 'odd',x[0]))


# In[73]:


print testRDD.take(10)


# There are two types of Reduce operations- reduceByKey() and reduce(). Check PySpark documentation for more details

# In[74]:


reduced = testRDD.reduceByKey(add)


# In[75]:


print reduced.collect()


# In[76]:


sc.stop()


# In[77]:


sc = pyspark.SparkContext(appName="spark-notebook")


# In[78]:


mat = np.array([])
with open("/usr/local/hadoop/Recitation2/recitation3/problems/part3/numbers.txt", "r") as file:
    for line in file:
        mat = np.hstack((mat, np.array(int(line))))
        
mymat = mat[:6]


# In[79]:


print mymat


# In MLlib you can use Dense or Sparse matrices for computation.
# Create a Sparse vector for MLlib using mat-

# In[80]:


from pyspark.mllib.linalg import Vectors
sv = Vectors.sparse(6,[0, 1, 3, 4],[1, 2, 4, 5])


# In[81]:


print type(sv)


# ### Labeled point
# 
# A labeled point is a local vector, either dense or sparse, associated with a label/response. In MLlib, labeled points are used in supervised learning algorithms. We use a double to store a label, so we can use labeled points in both regression and classification.

# In[82]:


from pyspark.mllib.regression import LabeledPoint
pos = LabeledPoint(1.0, mat) # label(Y) = 1 and data(X) = mymat
print pos


# ### Local matrix
# 
# A local matrix has integer-typed row and column indices and double-typed values, stored on a single machine. 

# In[83]:


from pyspark.mllib.linalg import Matrix, Matrices
dm = Matrices.dense(2,2,mat[7:11]) # 2x2 dense matrix
print dm 


# ### Distributed matrix
# 
# A distributed matrix has long-typed row and column indices and double-typed values, stored distributively in one or more RDDs. It is very important to choose the right format to store large and distributed matrices. Converting a distributed matrix to a different format may require a global shuffle, which is quite expensive. 

# In[84]:


newmat = np.reshape(mat[:6], (2,3)) # 2x3 matrix
print newmat


# #### Row matrix

# In[85]:


from pyspark.mllib.linalg.distributed import RowMatrix

# Create an RDD of newmat
rows = sc.parallelize(newmat)
rowmat = RowMatrix(rows)
print rowmat.numRows(), rowmat.numCols()


# #### BlockMatrix

# In[88]:


from pyspark.mllib.linalg.distributed import BlockMatrix


# Create an RDD of sub-matrix blocks.
blocks = sc.parallelize([((0, 0), Matrices.dense(2,2,mat[7:11])),
                         ((1, 0), Matrices.dense(2,2,mat[1:5]))])

# Create a BlockMatrix from an RDD of sub-matrix blocks.
mat = BlockMatrix(blocks, 2, 2) # [A | B]
print mat


# In[87]:


sc.stop()

