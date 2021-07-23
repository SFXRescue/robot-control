#!/bin/sh
python3 main.py &
python3 motor_control.py 
killall python3
