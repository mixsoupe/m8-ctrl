#!/bin/bash

pacmd load-module module-loopback latency_msec=1
~/code/m8c/m8c
python3 ctrl.py
