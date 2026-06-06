# Function executed by child processes

def myFunc(i):
    print('calling myFunc from process n°: %s' % i)

    # Print numbers up to the process index
    for j in range(0, i):
        print('output from myFunc is :%s' % j)

    return