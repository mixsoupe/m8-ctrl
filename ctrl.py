#!/usr/bin/python
# -*- encoding: utf8 -*-
import time

import board
import busio
from digitalio import Direction, Pull

from adafruit_extended_bus import ExtendedI2C as I2C

from adafruit_mcp230xx.mcp23016 import MCP23016

i2c = I2C(11)

mcp = MCP23016(i2c)

pins = []
for pin in range(0, 16):
    pins.append(mcp.get_pin(pin))

# Set all the port A pins to output
for pin in pins:
    pin.direction = Direction.OUTPUT
    pin.pull = digitalio.Pull.UP
    


while (True):
    print ("true")
    pins[0].value = False
    time.sleep(1)
    pins[0].value = True
    time.sleep(1)

