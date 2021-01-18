from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        