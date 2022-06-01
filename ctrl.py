#!/usr/bin/python
# -*- encoding: utf8 -*-
import time
from pynput.keyboard import Key, Controller
import board
import busio
from digitalio import Direction, Pull
from adafruit_extended_bus import ExtendedI2C as I2C
from adafruit_mcp230xx.mcp23017 import MCP23017

keyboard = Controller()

i2c = I2C(11)

mcp = MCP23017(i2c)

pin7 = mcp.get_pin(7)
pin7.direction = Direction.INPUT
pin7.pull = Pull.UP
pin7_status = (
  
while (True):
    if not pin7.value:
        #print ("key 1")
        #time.sleep(1)
        keyboard.press('A')
    

