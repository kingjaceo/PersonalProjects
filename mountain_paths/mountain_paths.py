# mountain_paths.py
# Draws a map using elevation data, then finds and draws greedy shortest paths across the map

from instream import InStream
import stddraw
from color import Color
import random


def map_data(filename, rows, cols):
    # read data from filename into a 2D array
    instream = InStream(filename)
    data = []
    for n in range(rows):
        data.append([])
        for m in range(cols):
            data[n].append(instream.readInt())
    return data


def find_min(a):
    # finds the min elevation over a 2D array, a
    amin = a[0][0]
    for n in range(len(a)):
        for m in range(len(a[n])):
            if a[n][m] < amin:
                amin = a[n][m]
    return amin


def find_max(a):
    # finds the max elevation over a 2D array, a
    amax = a[0][0]
    for n in range(len(a)):
        for m in range(len(a[n])):
            if a[n][m] > amax:
                amax = a[n][m]
    return amax


def draw_map(a):
    # draws and displays a map based on a 2D array, a,
    # using the max and min to set the grayscale
    amin = find_min(a)
    amax = find_max(a)

    stddraw.setXscale(-10, len(a[0]) + 10)
    stddraw.setYscale(-5, len(a) + 5)
    stddraw.setCanvasSize(int(512*1.5), int(512*len(a)/len(a[0])*1.5))

    m = 255 / (amax - amin)
    b = -m*amin

    for i in range(len(a)):
        for j in range(len(a[i])):
            value = int(m*a[i][j] + b)
            # print(a[i][j], value)
            gray = Color(value, value, value)
            stddraw.setPenColor(gray)
            stddraw.filledRectangle(j, len(a) - i, 1, 1)


def draw_lowest_elevation_path(a, row):
    # calculates and draws an optimal greedy path across a 2D
    # array, a, starting at row
    # print(row)
    height = len(a)
    y_pos = row

    stddraw.setPenColor(stddraw.GREEN)
    stddraw.filledRectangle(0, height - y_pos, 1, 1)

    temp = 0
    d_elevation = 0

    for n in range(1, len(a[row])-1):

        forward = abs(a[y_pos][n] - a[y_pos][n-1])
        if y_pos > 0:
            forward_up = abs(a[y_pos-1][n] - a[y_pos][n-1])
        else:
            forward_up = find_max(a)
        if y_pos < len(a)-1:
            forward_down = abs(a[y_pos+1][n] - a[y_pos][n-1])
        else:
            forward_down = find_max(a)

        if forward <= forward_up and forward <= forward_down:
            d_elevation += forward
        elif forward_up < forward_down:
            y_pos -= 1
            d_elevation += forward_up
        elif forward_down < forward_up:
            y_pos += 1
            d_elevation += forward_down
        else:
            choice = random.randint(0,1)
            # print(choice)
            if choice == 0:
                y_pos -= 1
                d_elevation += forward_up
            else:
                y_pos += 1
                d_elevation += forward_down

        stddraw.filledRectangle(n, height - y_pos, 1, 1)
        if d_elevation < temp:
            print('col: ', n, ' y_pos: ', y_pos)
            print("CHANGE IN ELEVATION DECREASED")
        temp = d_elevation
        # stddraw.show(0)

    return d_elevation


def index_of_lowest_elevation_path(a):
    # finds the optimal greedy path across a 2D array, a,
    # considering ALL rows and returns the index of the
    # starting row.
    lowest = draw_lowest_elevation_path(a, 0)
    lowest_i = 0

    for n in range(len(a)):
        d_elevation = draw_lowest_elevation_path(a, n)
        if d_elevation < lowest:
            lowest_i = n
            lowest = d_elevation

    stddraw.show(10)
    return lowest_i, lowest


def main():
    data = map_data('Colorado_844x480.dat', 480, 844)
    draw_map(data)
    change = draw_lowest_elevation_path(data, 11)
    print(change)
    min_i, min_change = index_of_lowest_elevation_path(data)
    print(min_i, min_change)
    stddraw.show()

if __name__ == '__main__':
    main()
