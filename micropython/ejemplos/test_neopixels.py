"""
    neopixel_random.py

    Repeatedly displays random colours onto the LED strip.
    This example requires a strip of 8 Neopixels (WS2812) connected to pin0.

"""
from microbit import *
import neopixel
from random import randint


N_pixels = 60
# Setup the Neopixel strip on pin0 with a length of 8 pixels
np = neopixel.NeoPixel(pin8, N_pixels)

while True:
    #Iterate over each LED in the strip

    for pixel_id in range(0, len(np)):
        red = randint(0, N_pixels)
        green = randint(0, N_pixels)
        blue = randint(0, N_pixels)

        # Assign the current LED a random red, green and blue value between 0 and N_pixels
        np[pixel_id] = (red, green, blue)

        # Display the current pixel data on the Neopixel strip

    np.show()
    sleep(10)