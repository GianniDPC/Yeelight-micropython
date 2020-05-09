from uyeelight import *

# see yeelight app for IP
bulb = Bulb("192.168.0.180")

try:
    if not bulb.is_on:
        bulb.turn_on()
except YeeLightException as e:
    print(e)
