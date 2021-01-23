# Cloud IoT Sensors

This is a first project connecting sensor readings to Google Cloud IoT Core service. 
The setup and part of the code were take from [this blog post](https://medium.com/google-cloud/cloud-iot-step-by-step-connecting-raspberry-pi-python-2f27a2893ab5).


## Requirements

- GCP account
- A registry and device from IoT Core, together with respective pub/sub topic

## How to Run

Before running, you'll need to define the following envirnoment variables:

```bash
export GCP_PROJECT_ID=<PROJECT_ID>
export REGISTRY_ID=<REGISTRY_ID>
export DEVICE_ID=<DEVICE_ID>
```

Then, you can execute:

```bash
python3 projects/03-cloud-iot-sensors.py
```