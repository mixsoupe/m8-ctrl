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

state = False
  
while (True):
    pressed = not pin7.value
    if pressed and pressed != state:
        keyboard.press('A')
        state = pressed
    if not pressed and pressed == state:
        state = pressed
    

    
    

