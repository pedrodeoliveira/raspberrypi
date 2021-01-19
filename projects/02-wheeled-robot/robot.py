from lirc import RawConnection
from gpiozero import CamJamKitRobot, DistanceSensor
import time

# Define GPIO pins to use for the distance sensor
pintrigger = 27
pinecho = 18


robot = CamJamKitRobot()
sensor = DistanceSensor(echo=pinecho, trigger=pintrigger)

# Set the relative speeds of the two motors, between 0.0 and 1.0
leftmotorspeed = 0.58
rightmotorspeed = 0.52

motorforward = (leftmotorspeed, rightmotorspeed)
motorbackward = (-leftmotorspeed, -rightmotorspeed)
motorleft = (0.4, 0)
motorright = (0, 0.4) 

# Distance Variables
hownear = 50.0
reversetime = 2
turntime = 1.5

#robot.value = motorforward
#time.sleep(6)

# Return True if the ultrasonic sensor sees an obstacle
def isnearobstacle(localhownear):
    distance = sensor.distance * 100

    print("IsNearObstacle: " + str(distance))
    if distance < localhownear:
        return True
    else:
        return False


# Move back a little, then turn right
def avoidobstacle():
    # Back off a little
    print("Backwards")
    robot.value = motorbackward
    time.sleep(reversetime)
    robot.stop()

    # Turn right
    #print("Right")
    #robot.value = motorright
    #time.sleep(turntime)
    #robot.stop()

def ProcessIRRemote():
       
    #get IR command
    #keypress format = (hexcode, repeat_num, command_key, remote_id)
    try:
        keypress = conn.readline(.0001)
    except:
        keypress=""
              
    if (keypress != "" and keypress != None):
                
        data = keypress.split()
        sequence = data[1]
        command = data[2]
        
        #ignore command repeats
        if (sequence != "00"):
           return
        
        print(command)        
        return command
            

def process_command(command):
        if command == "KEY_UP":
                robot.value = motorforward
        elif command == "KEY_DOWN":
                robot.value = motorbackward
        elif command == "KEY_LEFT":
                robot.value = motorright
        elif command == "KEY_RIGHT":
                robot.value = motorleft
        elif command == "KEY_OK":
                robot.stop()
        else:
                print(f'Unknown command {command}')

#define Global
conn = RawConnection()

print("Starting Up...")


while True:         

    cmd = ProcessIRRemote()
    if cmd is not None:
        print(f'Received command: {cmd}')
        process_command(cmd)
    time.sleep(0.2)
    if isnearobstacle(hownear):
        robot.stop()
        avoidobstacle()
