from time import time  # Import time tools

import pyopencl as cl  
import numpy as np   
import deviceInfoPyopencl as device_info
import numpy.linalg as la

#input vectors 
a = np.random.rand(10000).astype(np.float32)  
b = np.random.rand(10000).astype(np.float32)   

def test_cpu_vector_sum(a, b):  
    c_cpu = np.empty_like(a)   
    cpu_start_time = time()  
    for i in range(10000):
            for j in range(10000):  
                    c_cpu[i] = a[i] + b[i]  
    cpu_end_time = time()   
    print("CPU Time: {0} s".format(cpu_end_time - cpu_start_time))   
    return c_cpu   

def test_gpu_vector_sum(a, b):
    #define the PyOpenCL Context
    platform = cl.get_platforms()[0]
    device = platform.get_devices()[0]
    context = cl.Context([device])
    queue = cl.CommandQueue(context, \
                            properties=cl.command_queue_properties.PROFILING_ENABLE)   
    #prepare the data structure
    a_buffer = cl.Buffer\
               (context, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=a)
    b_buffer = cl.Buffer\
               (context, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=b)
    c_buffer = cl.Buffer\
               (context, cl.mem_flags.WRITE_ONLY, b.nbytes)   
    program = cl.Program(context, """
    __kernel void sum(__global const float *a, __global const float *b, __global float *c)
    {
        int i = get_global_id(0);
        int j;
        for(j = 0; j < 10000; j++)
        {
            c[i] = a[i] + b[i];
        }
    }""").build()
    #start the gpu test
    gpu_start_time = time()   
    event = program.sum(queue, a.shape, None, a_buffer, b_buffer, c_buffer)   
    event.wait()   
    elapsed = 1e-9*(event.profile.end - event.profile.start)   
    print("GPU Kernel evaluation Time: {0} s".format(elapsed))   
    c_gpu = np.empty_like(a)  
    cl._enqueue_read_buffer(queue, c_buffer, c_gpu).wait()  
    gpu_end_time = time()  
    print("GPU Time: {0} s".format(gpu_end_time - gpu_start_time))   
    return c_gpu   

#start the test
if __name__ == "__main__":
    #print the device info
    device_info.print_device_info()
    #call the test on the cpu
    cpu_result = test_cpu_vector_sum(a, b)
    #call the test on the gpu
    gpu_result = test_gpu_vector_sum(a, b)
    assert (la.norm(cpu_result - gpu_result)) < 1e-5
        
