import board
from digitalio import DigitalInOut, Direction, Pull
from adafruit_mcp230xx.mcp23017 import MCP23017

MCP23017_I2C_ADDRESS = 0x20

leds = []
switches = []

mcp23017 = MCP23017(board.I2C(), address=MCP23017_I2C_ADDRESS)

def configure_pins():
    for pin in range(5, 7):
        switches.append(mcp23017.get_pin(pin))
    for switch in switches:
        switch.direction = Direction.INPUT
        switch.pull = Pull.UP
        switch.invert_polarity = True

def read_and_write_pin():
    for pin, switch in enumerate(switches):
        if switch.value:
            print ("Button " + pin)

# Main
configure_pins()

while True:
    read_and_write_pin()
