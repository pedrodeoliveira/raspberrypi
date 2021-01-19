from gpiozero import Button, LED
from time import sleep
from random import uniform
from os import _exit

led = LED(4)
right_button = Button(14)
left_button = Button(15)

left_name = input('Left player name is: ')
right_name = input('Right player name is: ')

led.on()
sleep(uniform(5, 10))
led.off()

def pressed(button):
    if button.pin.number == 14:
        print('here')
        print(f'{right_name} won the game!')
    else:
        print(f'{left_name} won the game!')
    _exit(0)
 

right_button.when_pressed = pressed
left_button.when_pressed = pressed

