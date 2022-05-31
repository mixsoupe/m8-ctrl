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

mcp.config(5, mcp.INPUT)
mcp.config(6, mcp.INPUT)
mcp.config(7, mcp.INPUT)
mcp.pullup(3, 1)

while (True):
    print (mcp.input(5))
    #print ("test")
    time.sleep(1)
