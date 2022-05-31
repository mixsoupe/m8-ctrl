#!/usr/bin/python
# -*- encoding: utf8 -*-
import time

import board
import busio
import digitalio

from adafruit_extended_bus import ExtendedI2C as I2C

from adafruit_mcp230xx.mcp23016 import MCP23016

i2c = I2C(11)

mcp = MCP23016(i2c)
#pin7 = mcp.get_pin(7)
pin0 = mcp.get_pin(0)
pin0.switch_to_output(value=True)
#pin7.direction = digitalio.Direction.INPUT

while (True):

    #print (pin4.value)
    pin0.value = False
    
    time.sleep(1)
    pin0.value = True
