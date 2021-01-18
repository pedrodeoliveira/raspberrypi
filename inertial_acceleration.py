from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

while True:
    acceleration = sense.get_accelerometer_raw()
    x = round(acceleration['x'])
    y = round(acceleration['y'])
    z = round(acceleration['z'])
    print(f'x: {x}, y: {y}, z: {z}')
