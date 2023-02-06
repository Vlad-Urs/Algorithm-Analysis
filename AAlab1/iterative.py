from timeit import default_timer as timer

def fib_iterativ(n):
    start_time = timer()
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return [a,timer()-start_time]

test_list = [x for x in range(5,500,10)]
fib_it_results = []
fib_sequence = []
aux = []

for n in test_list:
    aux = fib_iterativ(n)
    fib_sequence.append(aux[0])
    fib_it_results.append(aux[1])