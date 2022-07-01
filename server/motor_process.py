
"""function to run concurrently in app.py"""
def motor_control_process(motor_controller, child):

    # initialize keys to empty
    keys = []

    while True:

        if child.poll():
            keys = child.recv()
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
