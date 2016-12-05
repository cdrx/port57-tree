import opc
import time

STRIPS = 32
LENGTH = 64

LAST = (0, 0, 0)

BLACK = [ (0, 0, 0) ] * LENGTH * STRIPS

tree = opc.Client('10.0.57.25:80')


def colour_tree(r, g, b):
    global LAST
    LAST = (r, g, b)
    strip = [ (r / 3, g / 3, b / 3) ] * LENGTH
    tree.put_pixels(strip * STRIPS)

def wipe(r, g, b):
    global LAST
    for i in range(LENGTH - 1, 0, -1):
        strip = [ (r, g, b) ] * LENGTH

        for x in range(i):
            strip[x] = LAST

        if i < LENGTH:
            strip[i] = (255, 255, 255)

        tree.put_pixels(strip * STRIPS)

        time.sleep(0.025)

    strip = [ (r, g, b) ] * LENGTH
    tree.put_pixels(strip * STRIPS)
    LAST = (r, g, b)

colour_tree(255 / 2, 0, 0)

while True:
    wipe(0, 255 / 2, 0)
    time.sleep(0.5)
    wipe(255 / 2, 0, 0)
    time.sleep(0.5)