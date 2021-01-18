import RPi.GPIO as GPIO
from gpiozero import Button, LED
import time


# define GPIO mode and initialize motor driver control pins
GPIO.setmode(GPIO.BCM)
control_pins = [4, 17, 27, 22]

for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

# half step specification of stepper motor
halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]

# define push buttons and leds
yellow_button = Button(26)
red_button = Button(19)
red_led = LED(24)
green_led = LED(25)


# initialize angle
angle = 0
push_rotation = 90


def rotate(desired_angle):
    direction = desired_angle > 0
    step_count = int((abs(desired_angle)*512)/360)
    print(f'Running {step_count} steps')

    if direction:
        steps = list(range(8))
    else:
        steps = list(reversed(range(8)))

    for i in range(step_count):
        for halfstep in steps:        
            for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.001)
      
    


def check_leds():
    global angle
    if angle >= 0:
        green_led.on()
        time.sleep(0.001)
        red_led.off()
    else:
        green_led.off()
        time.sleep(0.001)
        red_led.on()


def rotate_pos():
    global angle
    rotate(push_rotation)
    angle += push_rotation
    print(f'angle: {angle}')
    check_leds()


def rotate_neg():
    global angle
    rotate(-push_rotation)
    angle -= push_rotation
    print(f'angle: {angle}')
    check_leds()
    

# define function handlers associated with the push buttons
yellow_button.when_pressed = rotate_pos
red_button.when_pressed = rotate_neg


check_leds()

# infinte loop
while True:
    try:
        pass
    except KeyboardInterrupt:
      GPIO.cleanup()  

