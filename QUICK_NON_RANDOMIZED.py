import random

def partition(arr, low, high):
    pivot = arr[high]  # Last element as pivot
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Move pivot to correct position
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

# Example usage:
arr = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
quicksort(arr, 0, len(arr) - 1)
print("Sorted array (Non-Random Pivot):", arr)
