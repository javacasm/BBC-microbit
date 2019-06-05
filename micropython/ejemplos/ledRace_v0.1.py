# LedRace usando microbit

from microbit import *
import neopixel

N_pixels = 60


MAX_Color = 50
COLOR_JUGADOR = MAX_Color
Estado_Pulsado = 1
Estado_Libre = 0

np = neopixel.NeoPixel(pin2, N_pixels)

j1 = 0    # Posicion Jugador Azul
j2 = 10   # Posicion Jugado Rojo

LIBRE = 0
PULSADO = 1

button1_state = LIBRE
button2_state = LIBRE

def countDown():
    for i in range(3, -1, -1):
        display.show(i)
        sleep(1000)


def clear():
    for pixel_id in range(0, len(np)):
        np[pixel_id] = (0, 0, 0)

def render():
    (r1, g1, b1) = np[j1]
    (r2, g2, b2) = np[j2]

    clear()

    np[j1] = (r1, g1, COLOR_JUGADOR)
    np[j2] = (COLOR_JUGADOR, g2, b2)

    np.show()

countDown()

while True:
    if button_a.is_pressed() or pin0.is_touched()
        j1 = (j1 + 1) % N_pixels
    # Correcion de ventaja para jugador 1. Gracias @gbarbarov
    if button_b.is_pressed() or pin1.is_touched():
        j2 = (j2 + 1) % N_pixels
    render()