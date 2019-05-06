from machine import Pin
from time import sleep
import dht

sensor = dht.DHT11(Pin(14))

while True:
    t = sensor.temperature()
    h = sensor.humidity()
    sensor.measure()
    print('Temperature = {} celcius, Humidity = {} % '.format(t,h))
    sleep(1)