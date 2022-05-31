#!/usr/bin/python
# -*- encoding: utf8 -*-
import time
#import adafruit_mcp230xx
from adafruit_mcp230xx.mcp23016 import MCP23016


mcp = MCP23016(address = 0x20, num_gpios = 16) # MCP23017

mcp.config(5, mcp.INPUT)
mcp.config(6, mcp.INPUT)
mcp.config(7, mcp.INPUT)
mcp.pullup(3, 1)

while (True):
    print (mcp.input(5))
    #print ("test")
    time.sleep(1)
