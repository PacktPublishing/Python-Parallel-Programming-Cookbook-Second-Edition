import numpy 
from numba import cuda 


A = (numpy.arange(10000, dtype=numpy.int64)) + 1 
print("vector to reduce = ", A)

@cuda.reduce 
def sum_reduce(a, b): 
    return a + b 

got = sum_reduce(A)
print("result = " , got)








