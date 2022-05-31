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

pin5 = mcp.get_pin(5)
pin6 = mcp.get_pin(6)
pin7 = mcp.get_pin(28)

pin5.direction = digitalio.Direction.INPUT
#pin5.pull = digitalio.Pull.UP

pin6.direction = digitalio.Direction.INPUT
#pin6.pull = digitalio.Pull.UP

pin7.direction = digitalio.Direction.INPUT
#pin7.pull = digitalio.Pull.UP

while (True):
    #print("Pin 5 is at a high level: {0}".format(pin5.value))
    #print("Pin 6 is at a high level: {0}".format(pin6.value))
    #print("Pin 7 is at a high level: {0}".format(pin7.value))
    print (pin7.value)
    
    time.sleep(1)
