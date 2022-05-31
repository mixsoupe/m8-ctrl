#!/usr/bin/python
# -*- encoding: utf8 -*-
from Adafruit_MCP230xx import *

mcp = Adafruit_MCP230XX(address = 0x20, num_gpios = 16) # MCP23017

mcp.config(5, mcp.INPUT)
mcp.config(6, mcp.INPUT)
mcp.config(7, mcp.INPUT)
#mcp.pullup(3, 1)

while (True):
    print "Pin 5 = %d" % (mcp.input(5) >> 5)
    print "Pin 6 = %d" % (mcp.input(6) >> 6)
    print "Pin 7 = %d" % (mcp.input(7) >> 7)
    time.sleep(1)
