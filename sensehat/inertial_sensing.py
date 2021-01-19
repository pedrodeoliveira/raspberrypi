from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

orientation = sense.get_orientation()
roll = orientation['roll']
pitch = orientation['pitch']
yaw = orientation['yaw']
print(f'roll: {roll}, pitch: {pitch}, yaw: {yaw}')