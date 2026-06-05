import concurrent.futures
import time

number_list = list(range(1, 11))


def count(number):
    for i in range(0,10000000):
        i += 1
    return i*number


def evaluate(item):
    result_item = count(item)
    print('Item %s, result %s' % (item, result_item))

if __name__ == '__main__':
    # Sequential Execution
    start_time = time.clock()
    for item in number_list:
        evaluate(item)
    print('Sequential Execution in %s seconds' % (time.clock() - start_time))

   
    # Thread Pool Execution
    start_time = time.clock()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate, item)
    print('Thread Pool Execution in %s seconds' % (time.clock() - start_time))

      
    # Process Pool Execution
    start_time = time.clock()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate, item)
    print('Process Pool Execution in %s seconds' % (time.clock() - start_time))
