from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

while True:
    orientation = sense.get_gyroscope_raw()
    x = round(orientation['x'])
    y = round(orientation['y'])
    z = round(orientation['z'])
    print(f'x: {x}, y: {y}, z: {z}')


