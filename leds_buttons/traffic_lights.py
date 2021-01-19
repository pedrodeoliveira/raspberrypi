from gpiozero import Button, LED
from time import sleep

button = Button(2)
led_r = LED(25)
led_y = LED(8)
led_g = LED(7)

def turn_led_on():
    led_g.on()
    sleep(3)
    led_g.off()
    led_y.on()
    sleep(1)
    led_y.off()
    led_r.on()
    sleep(3)
    led_r.off()

button.when_pressed = turn_led_on

while True:
    pass