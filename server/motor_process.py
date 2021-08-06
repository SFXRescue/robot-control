
from motor_control import MotorController

# function for app.py to run as a concurrent process for motor control
def motor_control_process(motors, keys):

    while True:

        # for the five keys, if they're in the keys list, move the motors.
        # the keys list should be changed by data being Piped from the rest api
        pass
