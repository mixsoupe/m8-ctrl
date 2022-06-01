#!/bin/bash

pacmd load-module module-loopback latency_msec=1
python3 ctrl.py &
~/code/m8c/m8c

