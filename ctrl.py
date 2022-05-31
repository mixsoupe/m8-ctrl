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
pin0 = mcp.get_pin(0)
pin1 = mcp.get_pin(1)
pin2 = mcp.get_pin(2)
pin3 = mcp.get_pin(3)
pin4 = mcp.get_pin(4)
pin5 = mcp.get_pin(5)
pin6 = mcp.get_pin(6)
pin7 = mcp.get_pin(7)
pin8 = mcp.get_pin(8)
pin9 = mcp.get_pin(9)
pin10 = mcp.get_pin(10)
pin11 = mcp.get_pin(11)
pin12 = mcp.get_pin(12)
pin13 = mcp.get_pin(13)
pin14 = mcp.get_pin(14)
pin15 = mcp.get_pin(15)

pin0.direction = digitalio.Direction.INPUT
pin1.direction = digitalio.Direction.INPUT
pin2.direction = digitalio.Direction.INPUT
pin3.direction = digitalio.Direction.INPUT
pin4.direction = digitalio.Direction.INPUT
pin5.direction = digitalio.Direction.INPUT
pin6.direction = digitalio.Direction.INPUT
pin7.direction = digitalio.Direction.INPUT
pin8.direction = digitalio.Direction.INPUT
pin9.direction = digitalio.Direction.INPUT
pin10.direction = digitalio.Direction.INPUT
pin11.direction = digitalio.Direction.INPUT
pin12.direction = digitalio.Direction.INPUT
pin13.direction = digitalio.Direction.INPUT
pin14.direction = digitalio.Direction.INPUT
pin15.direction = digitalio.Direction.INPUT


while (True):
    #print("Pin 5 is at a high level: {0}".format(pin5.value))
    #print("Pin 6 is at a high level: {0}".format(pin6.value))
    #print("Pin 7 is at a high level: {0}".format(pin7.value))
    print (pin0.value)
    print (pin1.value)
    print (pin2.value)
    print (pin3.value)
    print (pin4.value)
    print (pin5.value)
    print (pin6.value)
    print (pin7.value)
    print (pin8.value)
    print (pin9.value)
    print (pin10.value)
    print (pin11.value)
    print (pin12.value)
    print (pin13.value)
    print (pin14.value)
    print (pin15.value)
    
    time.sleep(1)
