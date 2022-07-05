
from queue import Queue
from motor_control import MotorController

"""function to run concurrently in app.py"""
def motor_control_process(motor_controller : MotorController, key_presses : Queue):

    # initialize keys to empty
    keys = []

    while True:

        if not key_presses.empty():
            keys = key_presses.get()
        print(keys)

        if "Up" in keys:
            motor_controller.move_forward()

        elif "Down" in keys:
            motor_controller.move_backward()
        
        if "Left" in keys:
            motor_controller.turn_left()
            
        elif "Right" in keys:
            motor_controller.turn_right()

        if "Ctrl+c" in keys:
            break
