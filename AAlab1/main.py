

import matplotlib.pyplot as plt
import iterative
import Dynamic
import Matrix
import Binet
import Eigenvalue

test_list1 = [x for x in range(5,50,2)]
test_list2 = [x for x in range(5,35,2)]

'''
# plotting the graph for the recursive method:
fib_it_results = [9.900000000007125e-06, 1.4199999999991997e-05, 3.3800000000000496e-05, 8.740000000000137e-05, 0.00023420000000000385, 0.0005681000000000019, 0.0014496000000000092, 0.0037634, 0.010521599999999992, 0.028692899999999993, 0.07214020000000002, 0.19336640000000002, 0.5238863, 1.3833416, 3.6297179]
plt.plot(test_list2,fib_it_results)
plt.xlabel('Fibonacci order')
plt.ylabel('Time elapsed (seconds)')
plt.title('Recursive method graph')
plt.legend(['Iterative Complexity','Recursive Complexity'])
plt.show()
'''

# plotting the graph for the iterative method:
plt.plot(iterative.test_list,iterative.fib_it_results)
plt.xlabel('Fibonacci order')
plt.ylabel('Time elapsed (secondsE-6)')
plt.title('Iterative method graph')

# plotting the graph for the dynamic method:
plt.plot(Dynamic.test_list,Dynamic.fib_it_results)
plt.xlabel('Fibonacci order')
plt.ylabel('Time elapsed (seconds)')
plt.title('Dynamic method graph')
plt.legend(['Iterative Complexity','Dynamic Complexity'])


# plotting the graph for the matrix method:
plt.plot(Matrix.test_list,Matrix.fib_it_results)
plt.xlabel('Fibonacci order')
plt.ylabel('Time elapsed (secondsE-6)')
plt.title('Matrix method graph')




# plotting the graph for the Binet method:
plt.plot(Binet.test_list,Binet.fib_it_results)
plt.xlabel('Fibonacci order')
plt.ylabel('Time elapsed (seconds)')
plt.title('All the graphs together')




# plotting the graph for the eigenvalue method:
fib_it_results = [0.011861599999999806, 0.00022220000000006124, 0.0001562999999999981, 0.00014689999999983883, 0.00014309999999984058, 0.0001396000000000175, 0.00013799999999997148, 0.00013540000000000774, 0.00013499999999999623, 0.00013459999999998473, 0.00013430000000003162, 0.00013390000000002011, 0.00013140000000011476, 0.00013260000000014927, 0.00013259999999992722, 0.00013219999999991572, 0.0001335000000000086, 0.0001322999999999741, 0.00013220000000013776, 0.0001335000000000086, 0.0001322999999999741, 0.00013210000000007938, 0.00013250000000009088, 0.00013180000000012626, 0.0001316000000000095, 0.0001310999999999396, 0.00013050000000003337, 0.0001306999999999281, 0.00013039999999997498, 0.00013140000000011476, 0.0001298999999999051, 0.0001310999999999396, 0.00013090000000004487, 0.00013010000000002186, 0.00012940000000005725, 0.000132800000000044, 0.00013180000000012626, 0.0001316000000000095, 0.00013060000000009175, 0.00013079999999998648, 0.0001305999999998697, 0.00013039999999997498, 0.00013010000000002186, 0.00013090000000004487, 0.00013040000000019702]
plt.plot(Eigenvalue.test_list[2:],Eigenvalue.fib_it_results[2:])
plt.xlabel('Fibonacci order')
plt.ylabel('Time elapsed (seconds)')
plt.legend(['Iterative method graph','Dynamic method graph','Matrix Complexity','Binet Complexity','Eigenvalue Complexity'])
plt.show()