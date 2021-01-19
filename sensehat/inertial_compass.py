from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

while True:
    print(sense.get_compass())
