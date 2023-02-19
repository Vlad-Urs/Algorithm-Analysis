from timeit import default_timer as timer
import arrays as arr
import matplotlib.pyplot as plt

def radix_sort(lst):
    # Find the maximum value to know the number of digits
    max_value = max(lst)
    # Get the number of digits of the maximum value
    num_digits = len(str(max_value))

    # Iterate through each digit, starting from the least significant
    for digit in range(num_digits):
        # Create 10 buckets for each digit value (0-9)
        buckets = [[] for _ in range(10)]

        # Place each element in the appropriate bucket based on its digit value
        for num in lst:
            # Get the digit value of the current digit
            digit_value = (num // 10 ** digit) % 10
            buckets[digit_value].append(num)

        # Flatten the buckets back into the original list in order
        lst = [num for bucket in buckets for num in bucket]

    return lst


results = []
for array in arr.array_list:
    start_time = timer()
    radix_sort(array)
    results.append(timer()-start_time)

print('Number of elements | Seconds elapsed')
for i in range(0,arr.total_arrays):
    print(arr.array_numbers[i],end=' | ')
    print(results[i])

'''plt.plot(arr.array_numbers[:-2],results[:-2])
plt.xlabel('Number of elements')
plt.ylabel('Seconds elapsed')
plt.title('RadixSort')
plt.show()'''