from machine import Pin

def callback(p):
	print('pin change', p)

p0 = Pin(0, Pin.IN)
p2 = Pin(2, Pin.IN)
p0.irq(trigger=Pin.IRQ_FALLING, handler=callback)
p2.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=callback)
