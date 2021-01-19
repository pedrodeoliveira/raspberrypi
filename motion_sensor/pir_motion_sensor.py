import RPi.GPIO as GPIO
from gpiozero import MotionSensor, LED
from time import sleep


# set BCM board mode 
GPIO.setmode(GPIO.BCM)


red_led = LED(16)
red_led.off()
pir_sensor = MotionSensor(27)

while True:
    pir_sensor.wait_for_motion()
    print('motion detected!')
    red_led.on()
    pir_sensor.wait_for_inactive()
    print('motion stopped!')
    red_led.off()
