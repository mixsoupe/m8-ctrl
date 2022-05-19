import board
import busio
from digitalio import Direction, Pull
from adafruit_mcp230xx.mcp23017 import MCP23017

# Initialize the I2C bus:
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the MCP23017 chip on the bonnet
mcp = MCP23017(i2c)

# Optionally change the address of the device if you set any of the A0, A1, A2
# pins.  Specify the new address with a keyword parameter:
# mcp = MCP23017(i2c, address=0x21)  # MCP23017 w/ A0 set

# Make a list of all the port B pins (a.k.a 8-15)
port_pins = []
for pin in range(5, 7):
    port_pins.append(mcp.get_pin(pin))


# Set all the port B pins to input, with pullups!
for pin in port_pins:
    pin.direction = Direction.INPUT
    pin.pull = Pull.UP


while True:
    for num, button in enumerate(port_pins):
        if not button.value:
            print("Button #", num, "pressed!")
