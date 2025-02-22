import time
import numpy as np
import matplotlib.pyplot as plt


# Non-random pivot QuickSort (choosing the last element as pivot) with an optimized partitioning scheme
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choose middle element as pivot to improve performance
    left = []
    right = []
    equal = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            equal.append(x)  # Handle duplicate elements efficiently

    if len(left) == len(arr) or len(right) == len(arr):  # Prevent infinite recursion
        return arr

    return quicksort(left) + equal + quicksort(right)


# Benchmarking function
def benchmark_quicksort(input_generator, sizes):
    times = []
    for n in sizes:
        arr = input_generator(n)
        start_time = time.time()
        quicksort(arr)
        end_time = time.time()
        times.append(end_time - start_time)
    return times


# Input generators
def best_case(n):
    return list(range(n))  # Already sorted list


def worst_case(n):
    return list(range(n, 0, -1))  # Reverse sorted list


def average_case(n):
    return np.random.randint(0, 100000, n).tolist()  # Random numbers


# Define input sizes
sizes = [100, 500, 1000, 5000, 10000, 20000]

# Run benchmarks
best_case_times = benchmark_quicksort(best_case, sizes)
worst_case_times = benchmark_quicksort(worst_case, sizes)
average_case_times = benchmark_quicksort(average_case, sizes)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(sizes, best_case_times, label='Best Case (O(n log n))', marker='o', linestyle='--')
plt.plot(sizes, worst_case_times, label='Worst Case (O(n^2))', marker='s', linestyle='--')
plt.plot(sizes, average_case_times, label='Average Case (O(n log n))', marker='^', linestyle='--')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Quicksort Performance for Different Cases')
plt.legend()
plt.grid()
plt.show()
