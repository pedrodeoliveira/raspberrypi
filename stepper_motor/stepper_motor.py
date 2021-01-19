import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

control_pins = [7,11,13,15]


for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
  
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

desired_angle = 90
direction = desired_angle > 0
step_count = int((abs(desired_angle)*512)/360)
print(f'Running {step_count} steps')


for i in range(step_count):
    for halfstep in range(8):
        print(f'halfstep: {halfstep}')
        for pin in range(4):
            GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
        time.sleep(0.001)
  
    
GPIO.cleanup()