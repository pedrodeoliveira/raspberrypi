from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180

camera.start_recording('/home/pi/Videos/test.h264')
sleep(10)
camera.stop_recording() 
