
from motor_control import MotorController

"""function to run concurrently in app.py"""
def motor_control_process(motors, pipe_endpoint):

    # initialize keys to empty
    keys = []

    while True:

        # receive key data from pipe
        # NOTE: double-check with someone that this will work
        keys = pipe_endpoint.recv()

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
