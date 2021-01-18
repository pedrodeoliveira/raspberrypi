from gpiozero import Button, LED
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

led = LED(25)
led.on()
sleep(3)
led.off()
