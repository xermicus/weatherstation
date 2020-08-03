#!/usr/bin/python3

import time
import Adafruit_DHT
from prometheus_client import start_http_server, Gauge

SENSOR = Adafruit_DHT.AM2302
PIN = "4"
METRICS_PORT = 8000
INTERVAL = 30

print("Starting probe on port " + str(METRICS_PORT))
start_http_server(METRICS_PORT)
g_temp = Gauge("sensor_temperature_celcius", "Temperature sensor measurements")
g_humid = Gauge("sensor_humidity_percentage", "Humidity sensor measurements")

while True:
    try:
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
        # print('Temp={0:0.1f}C  Humidity={1:0.1f}%'.format(temperature, humidity))

        if temperature is not None:
            g_temp.set(temperature)
        else:
            print("ERROR temperature was None")
        if humidity is not None:
            g_humid.set(humidity)
        else:
            print("ERROR humidity was None")

    except Exception as e:
        print("ERROR Unexpected exception during read_retry: " + str(e))

    time.sleep(INTERVAL)

