from gpiozero import Button, LED
from time import sleep

button = Button(2)
led = LED(24)

def turn_led_on():
    led.on()
    sleep(3)
    led.off()

button.when_pressed = turn_led_on

while True:
    pass

