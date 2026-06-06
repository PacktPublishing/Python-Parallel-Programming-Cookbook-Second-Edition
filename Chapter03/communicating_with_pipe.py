# Demonstrates inter-process communication using Pipes

import multiprocessing


# Sends values through first pipe
def create_items(pipe):

    output_pipe, _ = pipe

    for item in range(10):
        output_pipe.send(item)

    output_pipe.close()


# Receives values, squares them,
# and forwards them through second pipe
def multiply_items(pipe_1, pipe_2):

    close, input_pipe = pipe_1
    close.close()

    output_pipe, _ = pipe_2

    try:
        while True:
            item = input_pipe.recv()
            output_pipe.send(item * item)

    except EOFError:
        output_pipe.close()


if __name__ == '__main__':

    # First pipe generates values
    pipe_1 = multiprocessing.Pipe(True)

    process_pipe_1 = multiprocessing.Process(
        target=create_items,
        args=(pipe_1,)
    )

    process_pipe_1.start()

    # Second pipe processes values
    pipe_2 = multiprocessing.Pipe(True)

    process_pipe_2 = multiprocessing.Process(
        target=multiply_items,
        args=(pipe_1, pipe_2)
    )

    process_pipe_2.start()

    pipe_1[0].close()
    pipe_2[0].close()

    # Display processed results
    try:
        while True:
            print(pipe_2[1].recv())

    except EOFError:
        print("End")