from timeit import default_timer as timer

def fib_recursive(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)

test_list = [x for x in range(5,35,2)]
fib_it_results = []
fib_sequence = []
aux = []

for n in test_list:
    start_time = timer()
    fib_sequence.append(fib_recursive(n))
    fib_it_results.append(timer()-start_time)


