from __future__ import division

from django.conf import settings
from django.core.management.base import BaseCommand
from request.models import ColourRequest
from draw.models import Drawing
from itertools import cycle, islice
from django.utils import timezone

import opc
import time
import math

STRIPS = 32
LENGTH = 64

HEIGHT = 10

INTENSITY = 100
FUDGE = 1.4

DAMPEN = 0.75

RED = ( INTENSITY, 0, 0 )
GREEN = ( 0, INTENSITY, 0 )
BLUE = ( 0, 0, INTENSITY )
BLACK = ( 0, 0, 0 )
WHITE = ( INTENSITY, INTENSITY, INTENSITY )

YELLOW = ( INTENSITY, INTENSITY, 0 )
LINE = ( INTENSITY, INTENSITY, INTENSITY )


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.tree = opc.Client('%s:%d' % (settings.TREE_HOST, settings.TREE_PORT))

        x = 0
        while True:
            drawings = self.get_drawings()
            if drawings:
                self.draw(drawings)
            else:
                x += 1
                self.update_sequence()
                self.spiral(x, 255, 255, 255)
            time.sleep(0.05)

    def get_drawings(self):
        return Drawing.objects.filter(valid_to__gt=timezone.now())

    def draw(self, drawings):
        pixels = list([ BLACK ] * STRIPS * LENGTH)
        for d in drawings:
            for pos, colour in enumerate(zip(*[iter(d.data.split(","))] * 3)):
                r, g, b = colour
                r, g, b = int(r), int(g), int(b)
                if r or g or b:
                    pixels[pos] = (r, g, b)
        self.tree.put_pixels(pixels)

    def get_colour(self, idx):
        colours = ColourRequest.objects.all().order_by('-requested')[:2]
        return (colours[idx].colour.r * DAMPEN, colours[idx].colour.g * DAMPEN, colours[idx].colour.b * DAMPEN)

    def update_sequence(self):
        A = self.get_colour(0)
        B = self.get_colour(1)
        self.sequence = [A] * HEIGHT + [LINE] + [B] * HEIGHT + [LINE]

    def get_strip(self, start, finish):
        iter = cycle(self.sequence)
        return list(islice(iter, start, finish))

    def spiral(self, offset, r, g, b):
        pixels = []
        for y in range(STRIPS):
            pos = offset + int(math.floor((y * FUDGE)))
            strip = self.get_strip(pos, pos + LENGTH)
            pixels.extend(strip)
        self.tree.put_pixels(pixels)

