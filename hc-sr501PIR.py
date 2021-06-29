from machine import Pin
import utime

sensor_pir = machine.Pin(27,machine.Pin.IN,machine.Pin.PULL_DOWN)

def pir_handler(pin):
    utime.sleep_ms(100)
    if pin.value():
        print("Alarm! Motion Detected. Release the hounds")

sensor_pir.irq(trigger=machine.Pin.IRQ_RISING,handler=pir_handler)