"""using binary search using dac"""
import numpy as np

x = 20


def bin (arr, i, j):
    if i == j:
        if arr[i] == x:
            return i
        else:
            return -1

    else:
        mid = int((i + j) / 2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            bin(arr, i, mid)
        elif arr[mid] < x:
            bin(arr, mid + 1, j)


a1 = [10, 20, 30, 40, 50, 60, 70]
val = bin(np.array(a1), 0, 6)
print(val)
