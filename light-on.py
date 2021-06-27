from machine import Pin
import time

pin = Pin(25, Pin.OUT)
pin.toggle()