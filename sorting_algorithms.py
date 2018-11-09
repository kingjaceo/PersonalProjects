# sorting_algorithms.py
# classic quicksort, mergesort, and selection sort
import random
import numpy as np
import time


###---QUICK SORT---###
def quick_sort(a):
    sort(a, 0, len(a)-1)


def sort(a, first, last):
    if first < last:
        # find a suitable partition index
        split = partition(a, first, last)

        # recursively call sort
        sort(a, first, split-1)
        sort(a, split+1, last)


def partition(a, first, last):
    pivot = a[first]

    # indices for the left and right markers
    left = first + 1
    right = last

    done = False
    while not done:
        # moves the left marker forward as long
        while left <= right and a[left] <= pivot:
            left += 1

        while a[right] >= pivot and right >= left:
            right -= 1

        if right < left:
            done = True
        else:
            temp = a[left]
            a[left] = a[right]
            a[right] = temp

    temp = a[first]
    a[first] = a[right]
    a[right] = temp

    return right
###---END QUICK SORT---###


###---MERGE SORT---###
def merge_sort(a):
    n = len(a)
    if n <= 1:
        return
    mid = n // 2
    left = a[:mid]
    right = a[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, a)


def merge(l, r, a):
    i = 0
    j = 0
    k = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            a[k] = l[i]
            i += 1
        else:
            a[k] = r[j]
            j += 1
        k += 1
    while i < len(l):
        a[k] = l[i]
        i += 1
        k += 1
    while j < len(r):
        a[k] = r[j]
        j += 1
        k += 1
###---END MERGE SORT---###


###---SELECTION SORT---###
def selection(a):
    for i in range(len(a)):
        low = i
        for j in range(i, len(a)):
            if a[j] < a[low]:
                low = j
        temp = a[i]
        a[i] = a[low]
        a[low] = temp
###---END SELECTION SORT---###


def is_sorted(a):
    for n in range(len(a) - 1):
        if a[n] > a[n + 1]:
            return 'not sorted'
    return 'sorted'


def main():
    length = 10000000
    data = np.arange(0, length, 1)
    random.shuffle(data)
    start = time.time()
    quick_sort(data)
    end = time.time() - start
    print(end)

if __name__ == "__main__":
    main()