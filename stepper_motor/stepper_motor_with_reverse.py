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

resp = input('What is the desired angle (degrees):')
desired_angle = int(resp)
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
  
    
GPIO.cleanup()