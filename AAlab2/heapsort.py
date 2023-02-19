from timeit import default_timer as timer
import arrays as arr
import matplotlib.pyplot as plt

def heap_sort(arr):
    n = len(arr)
    # Build a max-heap from the input array
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the max-heap in sorted order
    for i in range(n - 1, 0, -1):
        # Swap the largest element to the end of the heap
        arr[0], arr[i] = arr[i], arr[0]
        # Restore the heap property for the remaining elements
        heapify(arr, i, 0)



def heapify(arr, n, i):
    largest = i  # Initialize the largest element as the root
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    # Check if right child is larger than root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest element is not the root, swap them and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


results = []
for array in arr.array_list:
    start_time = timer()
    heap_sort(array)
    results.append(timer()-start_time)

print('Number of elements | Seconds elapsed')
for i in range(0,arr.total_arrays):
    print(arr.array_numbers[i],end=' | ')
    print(results[i])

'''plt.plot(arr.array_numbers[:-2],results[:-2])
plt.xlabel('Number of elements')
plt.ylabel('Seconds elapsed')
plt.title('HeapSort')
plt.show()'''
