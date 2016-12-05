from TwitterAPI import TwitterAPI
import opc
import time

from colours import COLOURS as COLOURS
from colours import FLAT_COLOURS as COLOURS2

CONSUMER_KEY = 'xx'
CONSUMER_SECRET = 'xx'
ACCESS_TOKEN_KEY = 'xx'
ACCESS_TOKEN_SECRET = 'xx'

TERMS = [x[0] for x in COLOURS]

STRIPS = 32
LENGTH = 64
LAST = (0, 0, 0)
BLACK = [ (0, 0, 0) ] * LENGTH * STRIPS

tree = opc.Client('10.0.57.25:8080')
twitter = TwitterAPI(CONSUMER_KEY,
                     CONSUMER_SECRET,
                     ACCESS_TOKEN_KEY,
                     ACCESS_TOKEN_SECRET)

def colour_tree(r, g, b):
    global LAST
    LAST = (r, g, b)
    strip = [ (r , g, b) ] * LENGTH
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

colour_tree(255, 0, 0)

r = twitter.request('statuses/filter', {'track': "port57tree"})
for tweet in r:
    if 'text' in tweet:
        changed = False
        print tweet['text']
        for r, g, b, colour in COLOURS:
            if "%s" % colour.lower() in tweet['text'].lower():
                wipe(r, g, b)
                print colour
                changed = True
                break

        if not changed:
            for colour, r, g, b in COLOURS2:
                if "%s" % colour.lower() in tweet['text'].lower():
                    wipe(r, g, b)
                    print colour
                    break
