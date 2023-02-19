import matplotlib.pyplot as plt
import quicksort as qs
import mergesort as ms
import heapsort as hs
import radixsort as rs
import arrays as arr


plt.plot(arr.array_numbers[:-2],qs.results[:-2])
plt.plot(arr.array_numbers[:-2],ms.results[:-2])
plt.plot(arr.array_numbers[:-2],hs.results[:-2])
plt.plot(arr.array_numbers[:-2],rs.results[:-2])
plt.xlabel('Number of elements')
plt.ylabel('Seconds elapsed')
plt.legend(['QuickSort','Mergesort','HeapSort','RadixSort'])
plt.show()
