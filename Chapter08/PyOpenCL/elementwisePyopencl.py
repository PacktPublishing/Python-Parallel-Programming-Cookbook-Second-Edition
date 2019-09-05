import pyopencl as cl
import pyopencl.array as cl_array
import numpy as np  

context = cl.create_some_context()  # Initialize the Context
queue = cl.CommandQueue(context)  # Instantiate a Queue

vector_dimension = 100
vector_a = cl_array.to_device(queue,  np.random.randint(vector_dimension, size=vector_dimension))
vector_b = cl_array.to_device(queue,  np.random.randint(vector_dimension, size=vector_dimension))  
result_vector = cl_array.empty_like(vector_a)  

elementwiseSum = cl.elementwise.ElementwiseKernel(context, "int *a, int *b, int *c", "c[i] = a[i] + b[i]", "sum")
elementwiseSum(vector_a, vector_b, result_vector)  

print ("PyOpenCL ELEMENTWISE SUM OF TWO VECTORS")
print ("VECTOR LENGTH = %s" %vector_dimension)
print ("INPUT VECTOR A")
print (vector_a)
print ("INPUT VECTOR B")
print (vector_b)
print ("OUTPUT VECTOR RESULT A + B ")
print (result_vector)
