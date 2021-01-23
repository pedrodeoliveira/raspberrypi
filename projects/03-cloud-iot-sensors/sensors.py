#!/usr/bin/python

import datetime
import time
import jwt
import paho.mqtt.client as mqtt
import adafruit_dht
import board


# define some project-based variables to be used below
ssl_private_key_filepath = '/home/pi/demo_private.pem'
ssl_algorithm = 'RS256'
root_cert_filepath = '<root-certificate-filepath>'
project_id = '<GCP project id>'
gcp_location = '<GCP location>'
registry_id = '<IoT Core registry id>'
device_id = '<IoT Core device id>'


cur_time = datetime.datetime.utcnow()

def create_jwt():
  token = {
      'iat': cur_time,
      'exp': cur_time + datetime.timedelta(minutes=60),
      'aud': project_id
  }

  with open(ssl_private_key_filepath, 'r') as f:
    private_key = f.read()

  return jwt.encode(token, private_key, ssl_algorithm)

_CLIENT_ID = 'projects/{}/locations/{}/registries/{}/devices/{}'.format(project_id, gcp_location, registry_id, device_id)
_MQTT_TOPIC = '/devices/{}/events'.format(device_id)

client = mqtt.Client(client_id=_CLIENT_ID)

# authorization is handled purely with JWT
client.username_pw_set(
    username='unused',
    password=create_jwt())

def error_str(rc):
    return '{}: {}'.format(rc, mqtt.error_string(rc))

def on_connect(unusued_client, unused_userdata, unused_flags, rc):
    print('on_connect', error_str(rc))

def on_publish(unused_client, unused_userdata, unused_mid):
    print('on_publish')

client.on_connect = on_connect
client.on_publish = on_publish

# replace this with 3rd party cert if that was used when creating registry
client.tls_set(ca_certs=root_cert_filepath)
client.connect('mqtt.googleapis.com', 8883)
client.loop_start()

# define temperature and humidity sensor
dht = adafruit_dht.DHT11(board.D11, use_pulseio=False)

while True:
    try:
        temperature = dht.temperature
        humidity = dht.humidity        
        print(f"Temp: {temperature:.1f} *C \t Humidity: {humidity}%")

        payload = '{{ "ts": {}, "temperature": {}, "humidity": {} }}'.format(
          int(time.time()), temperature, humidity)

        # Uncomment following line when ready to publish
        #  client.publish(_MQTT_TOPIC, payload, qos=1)
        print("{}\n".format(payload))
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dht.exit()
        client.loop_stop()
        raise error 
 
    time.sleep(30)
