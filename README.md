# pico-intro
Introduction to Rapberry Pi Pico

pwm.freq(50)
pwm.duty_ns(MID)

while True:
    pwm.duty_ns(MIN)
    utime.sleep(1)
    pwm.duty_ns(MID)
    utime.sleep(1)
    pwm.duty_ns(MAX)
    utime.sleep(1)
