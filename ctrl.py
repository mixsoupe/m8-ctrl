#!/usr/bin/python
# -*- encoding: utf8 -*-
import time
from pynput.keyboard import Key, Controller
import board
import busio
from digitalio import Direction, Pull
from adafruit_extended_bus import ExtendedI2C as I2C
from adafruit_mcp230xx.mcp23008 import MCP23008
from gpiozero import Button

import subprocess

#GPIOZERO BUTTONS
button1 = Button(26, bounce_time=0.1)
button2 = Button(19, bounce_time=0.1)

def volup():
    keyboard.press(Key.media_volume_up)
    keyboard.release(Key.media_volume_up)

def voldown():
    keyboard.press(Key.media_volume_down)
    keyboard.release(Key.media_volume_down)

def toggle():
    keyboard.press(Key.alt)
    keyboard.press(Key.enter)
    keyboard.release(Key.alt)
    keyboard.release(Key.enter)
    time.sleep(0.5)
    
button1.when_pressed = volup
button2.when_pressed = voldown
  

#LAUNCH M8C
m8_process = subprocess.Popen(['sh', '/home/pi/code/m8-ctrl/launch-m8.sh'])

#KEYBOARD
keyboard = Controller()

i2c = I2C(11)

mcp = MCP23008(i2c)

pin0 = mcp.get_pin(0)
pin0.direction = Direction.INPUT
pin0.pull = Pull.UP

pin1 = mcp.get_pin(1)
pin1.direction = Direction.INPUT
pin1.pull = Pull.UP

pin2 = mcp.get_pin(2)
pin2.direction = Direction.INPUT
pin2.pull = Pull.UP

pin3 = mcp.get_pin(3)
pin3.direction = Direction.INPUT
pin3.pull = Pull.UP

pin4 = mcp.get_pin(4)
pin4.direction = Direction.INPUT
pin4.pull = Pull.UP

pin5 = mcp.get_pin(5)
pin5.direction = Direction.INPUT
pin5.pull = Pull.UP

pin6 = mcp.get_pin(6)
pin6.direction = Direction.INPUT
pin6.pull = Pull.UP

pin7 = mcp.get_pin(7)
pin7.direction = Direction.INPUT
pin7.pull = Pull.UP

#pin8 = mcp.get_pin(8)
#pin8.direction = Direction.INPUT
#pin8.pull = Pull.UP

#pin9 = mcp.get_pin(9)
#pin9.direction = Direction.INPUT
#pin9.pull = Pull.UP


state0 = False
state1 = False
state2 = False
state3 = False
state4 = False
state5 = False
state6 = False
state7 = False
state8 = False
state9 = False
state89 = False
  
while (True):
    pressed0 = not pin0.value
    pressed1 = not pin1.value
    pressed2 = not pin2.value
    pressed3 = not pin3.value
    pressed4 = not pin4.value
    pressed5 = not pin5.value
    pressed6 = not pin6.value
    pressed7 = not pin7.value
    #pressed8 = not pin8.value
    #pressed9 = not pin9.value
    
    if pressed0 and state0 == False:
        keyboard.press(Key.right)#droite
        state0 = True
    if pressed1 and state1 == False:
        keyboard.press(Key.up)#haut
        state1 = True
    if pressed2 and state2 == False:
        keyboard.press('z')#z option
        state2 = True
    if pressed3 and state3 == False:
        keyboard.press('x')#x edit
        state3 = True
    if pressed4 and state4 == False:
        keyboard.press(Key.down)#bas
        state4 = True
    if pressed5 and state5 == False:
        keyboard.press(Key.left)#gauche
        state5 = True
    if pressed6 and state6 == False:
        keyboard.press('s')#s start
        state6 = True
    if pressed7 and state7 == False:
        keyboard.press('a')#a shift
        state7 = True


        
        
        
        
        
        
    if not pressed0 and state0 == True:
        keyboard.release(Key.right)
        state0 = False
    if not pressed1 and state1 == True:
        keyboard.release(Key.up)
        state1 = False
    if not pressed2 and state2 == True:
        keyboard.release('z')
        state2 = False
    if not pressed3 and state3 == True:
        keyboard.release('x')
        state3 = False
    if not pressed4 and state4 == True:
        keyboard.release(Key.down)
        state4 = False
    if not pressed5 and state5 == True:
        keyboard.release(Key.left)
        state5 = False
    if not pressed6 and state6 == True:
        keyboard.release('s')
        state6 = False
    if not pressed7 and state7 == True:
        keyboard.release('a')
        state7 = False
    #if not pressed8 and state8 == True:
        ##keyboard.release(Key.media_volume_down)
        #state8 = False
    #if not pressed9 and state9 == True:
        #keyboard.release(Key.media_volume_up)
        #state9 = False
    

    
    

