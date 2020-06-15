# Ficheros y filesystem

Algo que nos resulta extraño a los que venimos del mundo Arduino o del la programación en C/C++ es el trabajar con un lenguaje interpretado

Hay que recordar que el sistema de archivos es emulado, con lo que no esperemos ver los ficheros al conectar la micro:bit al USB

[Editor v2](https://support.microbit.org/support/solutions/articles/19000102970-python-editor-version-2-update)


Un modulo sustituye a una librería/biblioteca
Unido al uso de REPL facilita mucho el desarrollo (Abrir/cerrar puerto serie)
Micropython además de ser un firmware nos proporciona un entorno de ejecución interactivo,  una shell python que nos permite probar el código antes de ejecutarlo

[](./images/Editorv2Ficheros.jpg)

Podemos subir ficheros de diferentes tipos

Algunos ficheros


[Módulos](https://support.microbit.org/support/solutions/articles/19000098018-beta-testing-python-editor-files-and-modules)

https://support.microbit.org/support/solutions/articles/19000098018-beta-testing-python-editor-files-and-modules

¿Autocompleta?

Editor mu

Ver texto o números por pantalla

Micropython no  incluye los modulos básico de oython, pero si el modulo micropython para controlar el hardware

    Display.show(…)

Se adapta al tipo

O imágenes

```python
from microbit import *

boat = Image("05050:"
             "05050:"
             "05050:"
             "99999:"
             "09990")

display.show(boat)
```

[Code](./codigo/gray_image.py)

Si mostramos varias imágenes a lo largo del tiempo tendremos una animacion

## Animaciones

	from microbit import *
	
	boat1 = Image("05050:"
	              "05050:"
	              "05050:"
	              "99999:"
	              "09990")
	
	boat2 = Image("00000:"
	              "05050:"
	              "05050:"
	              "05050:"
	              "99999")
	
	boat3 = Image("00000:"
	              "00000:"
	              "05050:"
	              "05050:"
	              "05050")
	
	boat4 = Image("00000:"
	              "00000:"
	              "00000:"
	              "05050:"
	              "05050")
	
	boat5 = Image("00000:"
	              "00000:"
	              "00000:"
	              "00000:"
	              "05050")
	
	boat6 = Image("00000:"
	              "00000:"
	              "00000:"
	              "00000:"
	              "00000")
	
	all_boats = [boat1, boat2, boat3, boat4, boat5, boat6]
	display.show(all_boats, delay=200)


[Code](./codigo/image_anim.py)

Con solo ver las posibilidades de mostrar animaciones con niveles de grises ya  se nota la mayor potencia de python frente al editor de bloques 

## botones



¿ Running_time() ?



```python
from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        break
    else:
        display.show(Image.SAD)

display.clear()
```

Más opciones

```python

# returns True or False to indicate if the button is pressed at the time of
# the method call.
button.is_pressed()
# returns True or False to indicate if the button was pressed since the device
# started or the last time this method was called.
button.was_pressed()
# returns the running total of button presses, and resets this counter to zero
button.get_presses()

display.scroll(str(button_a.get_presses())) # número de veces que se ha presionado


```


### Pines


19 pines disponibles: 0-16 y 19-20
 
Los pines 17 y 18 no están disponibles	.

![Pinout](https://microbit-micropython.readthedocs.io/en/latest/_images/pinout.png)


Están definidos los siguientes objetos

pin0
pin1
…
pin15
pin16
Warning: P17-P18 (inclusive) are unavailable.
pin19
pin20


#### Lectura

Ejemplo de lectura de estado del pin

```python

from microbit import *


p16 = Pin(0, Pin.IN)

while True:
    if pin0.read_digital():
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)

```

[Docs](https://microbit-micropython.readthedocs.io/en/latest/pin.html)
[Documentcion](https://microbit-micropython.readthedocs.io/en/v1.0.1/tutorials/io.html)
[More details](https://tech.microbit.org/hardware/edgeconnector/)

### Escritura digital

Como algunos pines (P3, P4, P6, P7, P9, P10) están conectados a los leds frontales, para usarlos debemos desactivar el control de la pantalla con 

```python
display.enable(false)
```

```python
from microbit import *

while True:
    pin0.write_digital(1)
    sleep(1000)
    pin0.write_digital(0)
    sleep(1000)
```


```python

from microbit import *

p16 = Pin(16, Pin.OUT)

while True:
    if button_a.is_pressed():
        pin16.write_digital(True) 
    if button_b.is_pressed():
        pin16.write_digital(False) 

```


### PWM (escritura analógica)

Usa 10 bits para el PWM, estando los valores entre 0 (0%) y 1023(100%). Hay que recordar que la salida es de 3.3V

```python

from microbit import *

p16 = Pin(16, Pin.OUT)
p16.write_analog(511) # 50%
```


# sets the period of the PWM output of the pin in milliseconds
# (see https://en.wikipedia.org/wiki/Pulse-width_modulation)
pin.set_analog_period(int)
# sets the period of the PWM output of the pin in microseconds
# (see https://en.wikipedia.org/wiki/Pulse-width_modulation)
pin.set_analog_period_microseconds(int)


### Touch


```python

rom microbit import *

while True:
    if pin0.is_touched():
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)

```


### Lectura de valor analógico

```python

# returns an integer between 0 and 1023
pin.read_analog()

```

### Interrupciones

	from machine import Pin
	
	def callback(p):
		print('pin change', p)
	
	p0 = Pin(0, Pin.IN)
	p2 = Pin(2, Pin.IN)
	p0.irq(trigger=Pin.IRQ_FALLING, handler=callback)
	p2.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=callback)
	
[Code](./codigo/interrupciones.py)

[Referencia](http://docs.micropython.org/en/v1.9.3/esp8266/esp8266/tutorial/pins.html#external-interrupts)

## Radio

Usando este módulo microbit-radio (https://github.com/rhubarbdog/microbit-radio)  podemos utilizar el protocolo que usa los bloques de MakeCode para compartir pares etiqueta-valor

[Proyecto makecode de ejemplo](https://makecode.microbit.org/_1TAd5D6Vi17C)

![](https://raw.githubusercontent.com/javacasm/microbitLovesPlants/master/images/qr_radio_makecode.gif)


```python
"""
Usando este módulo microbit-radio (https://github.com/rhubarbdog/microbit-radio)  podemos utilizar el protocolo que usa los bloques de MakeCode para compartir pares etiqueta-valor


Proyecto makecode de ejemplo https://makecode.microbit.org/_1TAd5D6Vi17C
# ![](./images/qr_radio_makecode.gif)


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


 



``` 

## Recursos

[Tutorial](https://microbit.org/guide/python/)
[Referencia](https://microbit-micropython.readthedocs.io/en/latest/index.html)
