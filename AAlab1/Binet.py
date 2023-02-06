from timeit import default_timer as timer
import math


def fib_recursive(n):
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return round((phi**n - psi**n) / math.sqrt(5))

test_list = [x for x in range(5,500,10)]
fib_it_results = []
aux = []
fib_sequence = []

for n in test_list:
    start_time = timer()
    fib_sequence.append(fib_recursive(n))
    fib_it_results.append(timer()-start_time)

