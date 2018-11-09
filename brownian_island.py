# brownian_island.py
# Generates an island using Brownian motion
import math
import stdrandom
import stddraw

def curve(x0, y0, x1, y1, variance, scale_factor, n):
    if n == 0:
        stddraw.line(x0, y0, x1, y1)
        stddraw.show(0)
        return
    xmid = (x0 + x1) / 2
    ymid = (y0 + y1) / 2
    deltax = stdrandom.gaussian(0, math.sqrt(variance))
    deltay = stdrandom.gaussian(0, math.sqrt(variance))
    variance = variance / scale_factor
    curve(x0, y0, xmid + deltax, ymid + deltay, variance, scale_factor, n - 1)
    curve(xmid + deltax, ymid + deltay, x1, y1, variance, scale_factor, n - 1)

def main():
    stddraw.setPenRadius(0)
    stddraw.setXscale(-3, +3)
    stddraw.setYscale(-3, +3)
    variance = 3
    hurst_exponent = 0.76
    scale_factor = 2 ** (2.0 * hurst_exponent)
    n = 13
    curve(0, 0, 0, 0, variance, scale_factor, n)
    stddraw.show()

if __name__ == '__main__':
    main()