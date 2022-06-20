#!/bin/bash

pacmd load-module module-loopback latency_msec=1
python3 /home/pi/code/m8-ctrl/ctrl.py &
/home/pi/code/m8c/m8c


