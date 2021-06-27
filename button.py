
from machine import Pin
import utime
# wire up button to pin 14
button =machine.Pin(14,machine.Pin.IN,machine.Pin.PULL_DOWN)

print("listening to buttons")
while True:
    if button.value() == 1:
        print("You pressed the button")
        utime.sleep(2)

