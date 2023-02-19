from timeit import default_timer as timer
import arrays as arr
import matplotlib.pyplot as plt

def merge_sort(arr):
    # Base case: If the array has one or zero elements, it is already sorted.
    if len(arr) <= 1:
        return arr
    # Recursive case: Split the array in half and sort each half recursively.
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    # Merge the sorted halves into a sorted whole.
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Add any remaining elements to the result.
    result += left[i:]
    result += right[j:]

    return result


results = []
for array in arr.array_list:
    start_time = timer()
    merge_sort(array)
    results.append(timer()-start_time)

print('Number of elements | Seconds elapsed')
for i in range(0,arr.total_arrays):
    print(arr.array_numbers[i],end=' | ')
    print(results[i])

'''plt.plot(arr.array_numbers[:-2],results[:-2])
plt.xlabel('Number of elements')
plt.ylabel('Seconds elapsed')
plt.title('MergeSort')
plt.show()'''
