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
#for pin in range(0, 15):
    #pins.append(mcp.get_pin(pin))

# Set all the port A pins to output
#for pin in pins:
    #pin.direction = Direction.OUTPUT
pin0 = mcp.get_pin(7)
pin0.direction = Direction.OUTPUT

pin7 = mcp.get_pin(3)
pin7.direction = Direction.INPUT
    
while (True):
    print (pin7.value)
    pin0.value = True
    time.sleep(.5)
    pin0.value = False
    
    time.sleep(.5)

