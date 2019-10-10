# Tutorial bloques

* Usar  url sencillas y que estén visibles
* CPU https://en.wikipedia.org/wiki/Micro_Bit#Hardware
        Nordic nRF51822 – 16 MHz 32-bit ARM Cortex-M0 microcontroller, 256 KB flash memory, 16 KB static ram
 
Permite usar Batería con voltaje entre  https://support.microbit.org/support/solutions/articles/19000013982-how-do-i-power-my-micro-bit-

* Sensor de temperatura está en la CPU (https://microbit.org/es/guide/temperature/)

No necesitamos instalar nada, funciona via web y en tablet/móviles  

Se puede programar con bloques, javascript, python, C++ de Arduino...

# Programación con bloques https://makecode.microbit.org/

El simulador es interactivo y cambia la imagen del simulador a medida que usamos diferentes bloques

Los programas se guardan por defecto en nuestro navegador

Seleccionamos el idioma

![language](../images/SelecionarIdioma.png)

La pantalla: 
* A la izquierda, Podemos simular nuestro programa
* Centor las paletas de bloques
* Bloques de mi programa

![inicio](../images/Incio_bloques.png)

Añadir nuestros bloques en onStart (para que se ejecute al principio) o forever (para que se ejecute repetitivamente)

EJEMPLO [HOLA MUNDO](https://makecode.microbit.org/_MfyHdrLXVWqL)

![HolaMundo](../images/HolaMundo.png)

Podemos cambiar el nombre
 
Una vez que tenemos un programa vamos a reprogramar la Microbit

1. Conectamos el microbit
1. Aparece una unidad llamada Microbit
1. Descargamos el programa
1. Lo copiamos a la unidad Microbit (veremos como parpadea el led naranja)
(En un tablet o móvil necesitaremos un cable OTG)

Usamos el sensor de temperatura (que está en la CPU con lo que no es muy preciso)


EJEMPLO de temperatura
1. Mostrar temperatura
1. Mostrar la temperatura en forma de barra

[Control de temperatura](https://makecode.microbit.org/_LesCE2h70PAT)

![ControlTemperatura](../images/ControlTemperatura.png)

EJEMPLO: Control de iluminación digital y analógico


[Control de iluminación](https://makecode.microbit.org/_YqD3MePtK6gU)

![Control iluminación](../images/ControlIluminacion.png)



[Control de iluminación II](https://makecode.microbit.org/_7ayKTtKvXFcc)

![ControlIluminacionII](../images/ControlIluminacionII.png)

[ControlIluminacion III](https://makecode.microbit.org/_TVJAFy9mjJ3Y)

![ControlIluminacion2](../images/ControlIluminacionIII.png)

## Eventos

Pulsaciones de botones o cambios de pines, agitado

EJEMPLO: [¿a quién le toca?](https://makecode.microbit.org/_f9EhoRAp1eoR)
* boton A incrementa
* B decrementa 
* agitado pone número aleatorio

![A quien le toca](../images/AquienLeToca.png)

## Juegos

Hay una paleta de juegos que incluyen sprites, puntuaciones, etc

Los leds se direccionan así
(0,0) ..... (4,0)
...          ...
(0,4) ..... (4,4)

EJEMPLO: marcianitos simples

EJEMPLO: [piedra, papel o tijera](https://makecode.microbit.org/_0Xi5xA7gweK5)

![Piedra Papel Tijera](../images/PiedraPapelTijera.png)

EJEMPLO: dado digital

### Extensiones

Permiten usar extensiones que añaden más bloques 


PROYECTO termostato: los botones fijan la temperatura objetivo y la otra barra nos muestra la temperatura actual

PROYECTO maquinilla para dar numeros  en la tienda (innalámbrica)



# TODO

¿Recuperar programas de otro navegador?
Trabajar con la comunicacion serie
    
