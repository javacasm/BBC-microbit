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

from microbit import *

boat = Image("05050:"
             "05050:"
             "05050:"
             "99999:"
             "09990")

display.show(boat)

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


display.scroll(str(button_a.get_presses())) # número de veces quexse ha presionado

button_a.is_pressed()

Running_time()




from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        break
    else:
        display.show(Image.SAD)

display.clear()


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

## Recursos

[Tutorial](https://microbit.org/guide/python/)
[Referencia](https://microbit-micropython.readthedocs.io/en/latest/index.html)
