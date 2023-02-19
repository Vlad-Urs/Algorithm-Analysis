from timeit import default_timer as timer
import arrays as arr

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            # swap the smallest element found with the bigger one
            (array[i], array[j]) = (array[j], array[i])
    # swap the pivot with greatest identified element pointed by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quick_sort(array, low, high):
    if low < high:
        p = partition(array, low, high)
        quick_sort(array, low, p - 1)
        quick_sort(array, p + 1, high)



results = []
for array in arr.array_list:
    start_time = timer()
    quick_sort(array, 0, len(array) - 1)
    results.append(timer()-start_time)

print('Number of elements | Seconds elapsed')
for i in range(0,arr.total_arrays):
    print(arr.array_numbers[i],end=' | ')
    print(results[i])
