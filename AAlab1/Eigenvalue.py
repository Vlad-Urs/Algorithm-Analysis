from timeit import default_timer as timer
import numpy as np

def eigen_fib(n):
    F1 = np.array([[1, 1], [1, 0]])
    eigenvalues, eigenvectors = np.linalg.eig(F1)
    Fn = eigenvectors @ np.diag(eigenvalues ** n) @ eigenvectors.T
    return int(np.rint(Fn[0, 1]))

test_list = [x for x in range(5,500,10)]
fib_it_results = []
aux = []
fib_sequence = []

for n in test_list:
    start_time = timer()
    fib_sequence.append(eigen_fib(n))
    fib_it_results.append(timer()-start_time)
