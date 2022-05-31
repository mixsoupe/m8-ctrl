#!/usr/bin/python
# -*- encoding: utf8 -*-
from Adafruit_MCP230xx import *

mcp = Adafruit_MCP230XX(address = 0x20, num_gpios = 16) # MCP23017

mcp.config(5, mcp.INPUT)
mcp.config(6, mcp.INPUT)
mcp.config(7, mcp.INPUT)
#mcp.pullup(3, 1)

while (True):
    print (mcp.input(5))
    time.sleep(1)
