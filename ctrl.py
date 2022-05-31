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

port_a_pins = []
for pin in range(0, 16):
    port_a_pins.append(mcp.get_pin(pin))

# Set all the port A pins to output
for pin in port_a_pins:
    pin.direction = Direction.OUTPUT
    


while (True):
    for num, led in enumerate(port_a_pins):
        #print (pin4.value)
        port_a_pins[num].value = False  # turn LED on!

        time.sleep(1)
        port_a_pins[num].value = False  # turn LED off

