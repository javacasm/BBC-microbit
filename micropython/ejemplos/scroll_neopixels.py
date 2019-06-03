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


def rotateDown():
    # copy in each neopixels the previous colour
    r, g, b = np[0]

    for pixel_id in range(0, len(np)):
        np[i] = np[pixel_id + 1]

    # Get a new colour for the first one
    np[-1] = (r, g, b)

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
    # Iterate over each LED in the strip

    # Intial random state
   # display.show(Image.ARROW_N)
    # randState()
  #  Gradient()

   # sleep(500)
   # display.show(Image.ARROW_NE)
    for i in range(0, N_pixels):
        rotate()
        np.show()
        display.show(Image.ARROW_E)
        sleep(10)