import time
 
import adafruit_dht
import board
 
dht = adafruit_dht.DHT11(board.D22, use_pulseio=False)

 
while True:
    try:
        temperature = dht.temperature
        humidity = dht.humidity
        # Print what we got to the REPL
        print("Temp: {:.1f} *C \t Humidity: {}%".format(temperature, humidity))
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dht.exit()
        raise error        
 
    time.sleep(3)