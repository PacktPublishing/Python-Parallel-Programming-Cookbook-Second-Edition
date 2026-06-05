import numpy
from mpi4py import MPI 
comm = MPI.COMM_WORLD 
size = comm.size 
rank = comm.rank


array_size = 10
recvdata = numpy.zeros(array_size,dtype=numpy.int)
senddata = (rank+1)*numpy.arange(array_size,dtype=numpy.int)

print(" process %s sending %s " %(rank , senddata))


comm.Reduce(senddata,recvdata,root=0,op=MPI.SUM)
print ('on task',rank,'after Reduce:    data = ',recvdata)


