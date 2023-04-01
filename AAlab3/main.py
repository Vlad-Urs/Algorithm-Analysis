from timeit import default_timer as timer
import algo1 as a1
import algo2 as a2
import algo3 as a3
import algo4 as a4
import algo5 as a5
import matplotlib.pyplot as plt

n = [i*100 for i in range(1,300)]


algo1_times = []
for number in n:
    start_time = timer()
    a1.algorithm1(number)
    algo1_times.append(timer()-start_time)

plt.plot(n,algo1_times)


algo2_times = []
for number in n:
    start_time = timer()
    a2.algorithm2(number)
    algo2_times.append(timer()-start_time)

plt.plot(n,algo2_times)


algo3_times = []
for number in n[:100]:
    start_time = timer()
    a3.algorithm3(number)
    algo3_times.append(timer()-start_time)

plt.plot(n[:100],algo3_times)


algo4_times = []
for number in n[:50]:
    start_time = timer()
    a4.algorithm4(number)
    algo4_times.append(timer()-start_time)

plt.plot(n[:50],algo4_times)


algo5_times = []
for number in n[:200]:
    start_time = timer()
    a5.algorithm5(number)
    algo5_times.append(timer()-start_time)

plt.plot(n[:200],algo5_times)
plt.xlabel('sieve limit')
plt.ylabel('seconds')
plt.legend(['Algorithm1','Algorithm2','Algorithm3','Algorithm4','Algorithm5'])
plt.show()