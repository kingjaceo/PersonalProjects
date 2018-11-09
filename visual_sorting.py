# visual_sorting.py
# draws a visualization of three sorting algorithms, where comparisons appear in red
import stddraw
import numpy as np
import random


def less(a, b):
    return a < b


def exch(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
    stddraw.clear()
    for n in range(length):
        if n == j or n == i:
            stddraw.setPenColor(stddraw.RED)
        else:
            stddraw.setPenColor(stddraw.BLUE)
        stddraw.filledRectangle(n, 0, 0.5, a[n])
    stddraw.show(300)


def selection(a):
    for i in range(len(a)):
        low = n
        for j in range(i, len(a)):
            if less(a[j], a[low]):
                low = j
        exch(a, i, low)


def insertion(a):
    # Define the length of the list
    n = len(a)
    # Loop through elements of the list
    for i in range(n):
        # Set a new index starting at the current index
        j = i
        # Continue swapping the new index with previous elements,
        # as long as the current element is less than the previous.
        while j > 0 and less(a[j], a[j-1]):
            exch(a, j, j-1)
            j -= 1


def shell(a):
    # Define the length of the list
    n = len(a)
    # Define the starting interval size, h, as 1
    h = 1
    # Determine the max for h, by using the formula
    # 3x + 1, as long as h is less than 1/3 of n
    while h < int(n / 3):
        h = 3 * h + 1
    # While h > 0, move through each element of the
    # list starting at the hth element.
    while h > 0:
        for i in range(h, n):
            # Use insertion sort on each subset of the
            # the list with distance of h between each
            # element.
            j = i
            while j >= h and less(a[j], a[j - h]):
                exch(a, j, j - h)
                j -= h
                # Reduce h to one third of itself.
        h = h // 3


# generate random list or perhaps a list of evenly spaced integers (see numpy's arrange function)
length = 20
indices = np.arange(0, length, 1)
data = np.arange(0, length/2, 0.5)
random.shuffle(data)

# draw the data on the canvas
sf = 10
stddraw.setPenRadius(0)
stddraw.setPenColor(stddraw.BLUE)
stddraw.setXscale(-5, 25)
stddraw.setYscale(-5, 15)
for n in range(length):
    stddraw.filledRectangle(n, 0, 0.5, data[n])

stddraw.show(1000)

# choose from insertion, selection, or shell sort
selection(data)
stddraw.show()