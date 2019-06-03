"""
    neopixel_random.py

    Repeatedly displays random colours onto the LED strip.
    This example requires a strip of 8 Neopixels (WS2812) connected to pin0.

"""
from microbit import *
import neopixel
from random import randint


N_pixels = 60
MAX_Color = 50
# Setup the Neopixel strip on pin0 with a length of 8 pixels
np = neopixel.NeoPixel(pin2, N_pixels)

def rotateUp():
    # copy in each neopixels the previous colour
    r, g, b = np[-1]

    for pixel_id in range(1, len(np)):
        np[N_pixels - pixel_id] = np[N_pixels - pixel_id - 1]

    # Get a new colour for the first one
    np[0] = (r, g, b)
    np.show()


def rotateDown():
    # copy in each neopixels the previous colour
    r, g, b = np[0]

    for pixel_id in range(0, len(np) - 1):
        np[pixel_id] = np[pixel_id + 1]

    # Get a new colour for the first one
    np[-1] = (r, g, b)
    np.show()

def moveUp():
    # copy in each neopixels the previous colour

    for pixel_id in range(1, len(np)):
        np[N_pixels - pixel_id] = np[N_pixels - pixel_id - 1]

    # Get a new colour for the first one
    np[0] = getRandomRGB()


def getRandomRGB():
    red = randint(0, MAX_Color)
    green = randint(0, MAX_Color)
    blue = randint(0, MAX_Color)
    return (red, green, blue)

def Gradient():
    for pixel_id in range(0, len(np)):
        np[pixel_id] = (pixel_id, 0, N_pixels - pixel_id)

def randState():
    for pixel_id in range(0, len(np)):
        np[pixel_id] = getRandomRGB()


Gradient()
while True:
    if button_a.is_pressed() or pin0.is_touched():
        display.show(Image.ARROW_W)
        rotateDown()
    elif button_b.is_pressed() or pin1.is_touched(:
        display.show(Image.ARROW_E)
        rotateUp()
    else:
        display.show(Image.ARROW_N)