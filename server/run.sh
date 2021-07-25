#!/bin/sh
argument1=$1
if [ $argument1 = -o ]
then
    echo Running the old sart junior code, from the 2021 competition.
    python3 main.py &
    python3 motor_control.py 
    killall python3
else
    echo Running the robot-control server...
    python3 app.py
    killall python3
fi
