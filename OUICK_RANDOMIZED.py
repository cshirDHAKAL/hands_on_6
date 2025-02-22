import random

import time
import numpy as np
import matplotlib.pyplot as plt
def random_partition(arr, low, high):
    rand_pivot = random.randint(low, high)  # Choose a random pivot
    arr[rand_pivot], arr[high] = arr[high], arr[rand_pivot]  # Swap pivot with last element
    from QUICK_NON_RANDOMIZED import partition
    return partition(arr, low, high)  # Use the same partition logic

def quicksort_random(arr, low, high):
    if low < high:
        pi = random_partition(arr, low, high)
        quicksort_random(arr, low, pi - 1)
        quicksort_random(arr, pi + 1, high)

# Example usage:
arr_random = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
quicksort_random(arr_random, 0, len(arr_random) - 1)
print("Sorted array (Random Pivot):", arr_random)
