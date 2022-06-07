def fib(input):
    if input == 0:
        return 1
    elif input == 1:
        return 1
    else:
        # When input == 3 (see below)
        #                                fib(0) = 1    fib(1) = 1
        #      output: 1       fib(2) => fib(2-2) + fib(2-1)
        return fib(input-2) + fib(input-1)

print(fib(4))

def fib_runner(input):
    for i in range(0, input+1):
        print(f'Iteration {i}: {fib(i)}')

fib_runner(8)