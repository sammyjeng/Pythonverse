#!/usr/bin/python3

import sys

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = list(map(int,(sys.argv[1:])))
print("Input array: ", arr, "\n")
bubbleSort(arr)
print ("Sorted array: ", arr)
