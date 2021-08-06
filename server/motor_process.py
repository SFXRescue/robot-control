
from motor_control import MotorController

# function for app.py to run as a concurrent process for motor control
def motor_control_process(motors, keys):

    while True:

        # for the five keys, if they're in the keys list, move the motors.
        # the keys list should be changed by data being Piped from the rest api
        if "Up" in keys:
            motors.move_forward()
        elif "Down" in keys:
            motors.move_backward()
        
        if "Left" in keys:
            motors.turn_left()
        elif "Right" in keys:
            motors.turn_right()

        if "Ctrl+c" in keys:
            break
