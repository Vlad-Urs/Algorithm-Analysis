from timeit import default_timer as timer

def fib_recursive(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if memo[n] != -1:
        return memo[n]
    memo[n] = fib_recursive(n - 1) + fib_recursive(n - 2)
    return memo[n]

test_list = [x for x in range(5,500,10)]
fib_it_results = []
aux = []
fib_sequence = []

for n in test_list:
    memo = [-1 for x in range(500)]
    start_time = timer()
    fib_sequence.append(fib_recursive(n))
    fib_it_results.append(timer()-start_time)