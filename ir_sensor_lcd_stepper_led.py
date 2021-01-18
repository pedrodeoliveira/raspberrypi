import RPi.GPIO as GPIO
from gpiozero import Button, LED
from lirc import RawConnection
import time
import re
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd


# key pattern for digits
KEY_PATTERN = "KEY_[1-9]"

# define GPIO mode and initialize motor driver control pins
GPIO.setmode(GPIO.BCM)
control_pins = [4, 18, 27, 22]

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
red_led = LED(16)


# initialize angle
angle = 0
motor_step = 90

# define global ir_sensor connection
ir_conn = RawConnection()

# Modify this if you have a different sized character LCD
lcd_columns = 16
lcd_rows = 2

# Raspberry Pi Pin Config:
lcd_rs = digitalio.DigitalInOut(board.D26)  # LCD pin 4
lcd_en = digitalio.DigitalInOut(board.D19)  # LCD pin 6
lcd_d7 = digitalio.DigitalInOut(board.D5)   # LCD pin 14
lcd_d6 = digitalio.DigitalInOut(board.D6)   # LCD pin 13
lcd_d5 = digitalio.DigitalInOut(board.D20)  # LCD pin 12
lcd_d4 = digitalio.DigitalInOut(board.D21)  # LCD pin 11

lcd = characterlcd.Character_LCD_Mono(
    lcd_rs, 
    lcd_en, 
    lcd_d4, 
    lcd_d5, 
    lcd_d6, 
    lcd_d7, 
    lcd_columns, 
    lcd_rows
)


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
    if angle >= 180:
        red_led.on()
    else:
        red_led.off()


def rotate_pos():
    global angle
    rotate(motor_step)
    angle += motor_step
    print(f'angle: {angle}, motor_step: {motor_step}')
    check_leds()


def rotate_neg():
    global angle
    rotate(-motor_step)
    angle -= motor_step
    print(f'angle: {angle}, motor_step: {motor_step}')
    check_leds()
    

def process_ir_remote():
       
    # get IR command
    # keypress format = (hexcode, repeat_num, command_key, remote_id)
    try:
        keypress = ir_conn.readline(.0001)
    except:
        keypress=""
              
    if (keypress != "" and keypress != None):
                
        data = keypress.split()
        sequence = data[1]
        command = data[2]
        
        # ignore command repeats
        if (sequence != "00"):
           return
        
        print(command)   
        return command
    return None


def change_step(step):
    global motor_step
    motor_step = step*10


def process_command(command):
    if command == "KEY_CHANNELUP":
        rotate_pos()
    elif command == "KEY_CHANNELDOWN":
        rotate_neg()
    elif re.match(KEY_PATTERN, command) is not None:
        step = int(command[-1])
        change_step(step)
    else:
        print(f'Unknown command {command}')


def update_lcd():
    lcd.clear()
    lcd.message = f"Angle: {angle}\nStep: {motor_step}"


# initialize led and clear lcd
check_leds()
lcd.clear()
update_lcd()


# infinte loop
while True:
    try:
        cmd = process_ir_remote()
        if cmd is not None:
            print(cmd)
            process_command(cmd)
            update_lcd()
    except KeyboardInterrupt:
      GPIO.cleanup()  
      lcd.clear()
