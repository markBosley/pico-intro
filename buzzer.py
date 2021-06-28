from machine import Pin
import utime

pin = Pin(28, Pin.OUT)

while True:
    pin.toggle()
    utime.sleep_ms(1000)
    