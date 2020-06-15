"""
Usando este módulo microbit-radio (https://github.com/rhubarbdog/microbit-radio)  podemos utilizar el protocolo que usa los bloques de MakeCode para compartir pares etiqueta-valor


Proyecto makecode de ejemplo https://makecode.microbit.org/_1TAd5D6Vi17C
![](./images/qr_radio_makecode.gif)

CC by SA by @javacasm
Junio 2020

"""

from microbit import *
import make_radio

radio = make_radio.MakeRadio(group = 7)
radio.off()
radio.on()

def showData(messg):
    uart.write(messg + '\n')
    # display.show(messg)

while True:
    data = radio.receive_packet()
    if data is None:
        display.show('+')
    else:
        if type(data) is int or type(data) is float:
            showData('[' + str(data) + ']')
        elif type(data) is str:
            showData('[' + data + ']')
        else:
            label,value = data
            showData( '[' + label +  '=' + str(value) + ']')
    sleep(100)

