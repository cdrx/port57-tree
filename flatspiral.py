from __future__ import division

from collections import defaultdict
from itertools import cycle, islice
import opc
import time
import math
import random

STRIPS = 32
LENGTH = 64

HEIGHT = 10

INTENSITY = 150
FUDGE = 1.0

RED = ( INTENSITY, 0, 0 )
GREEN = ( 0, INTENSITY, 0 )
BLUE = ( 0, 0, INTENSITY )
YELLOW = ( INTENSITY, INTENSITY, 0 )
LINE = ( INTENSITY, INTENSITY, INTENSITY )

tree = opc.Client('10.0.57.25:8080')

sequence = [RED] * HEIGHT + [LINE] + \
           [YELLOW] * HEIGHT + [LINE] + \
           [GREEN] * HEIGHT + [LINE]

def get_strip(start, finish):
    iter = cycle(sequence)
    return list(islice(iter, start, finish))

def spiral(offset, r, g, b):
    pixels = []
    for y in range(STRIPS):
        pos = offset
        strip = get_strip(pos, pos + LENGTH)
        pixels.extend(strip)
    tree.put_pixels(pixels)

x = 0
while True:
    x += 1
    spiral(x, 255, 255, 255)
    time.sleep(0.04)