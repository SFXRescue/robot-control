#importing libraries
import RPi.GPIO as GPIO
import keyboard
#The specific elements from the libraries you require
from time import sleep


class MotorController:

    # Initialize everything to do with the motors
    def __init__(self):

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        #Reading the pins where the specific motors are wired up to
        self.Motor1 = {'EN': 25, 'input1': 24, 'input2': 23}
        self.Motor2 = {'EN': 17, 'input1': 27, 'input2': 22}

        for x in self.Motor1:
            GPIO.setup(self.Motor1[x], GPIO.OUT)
            GPIO.setup(self.Motor2[x], GPIO.OUT)

        #Setting the speed in which the motors will spin
        self.EN1 = GPIO.PWM(self.Motor1['EN'], 100)    
        self.EN2 = GPIO.PWM(self.Motor2['EN'], 100)    

        #Start the motors as off
        self.EN1.start(0)            
        self.EN2.start(0)


    def move_forward(self):
        print ("FORWARD MOTION")
        #All motors move forwards
        for x in range(40,100):
            self.EN1.ChangeDutyCycle(x)
            self.EN2.ChangeDutyCycle(x)
            GPIO.output(self.Motor1['input1'], GPIO.HIGH)
            GPIO.output(self.Motor1['input2'], GPIO.LOW)
            GPIO.output(self.Motor2['input1'], GPIO.HIGH)
            GPIO.output(self.Motor2['input2'], GPIO.LOW)


    def move_backward(self):
        print ("BACKWARD MOTION")
        #All motors move backwards
        for x in range(40,100):
            self.EN1.ChangeDutyCycle(x)
            self.EN2.ChangeDutyCycle(x)
            GPIO.output(self.Motor1['input1'], GPIO.LOW)
            GPIO.output(self.Motor1['input2'], GPIO.HIGH)
            GPIO.output(self.Motor2['input1'], GPIO.LOW)
            GPIO.output(self.Motor2['input2'], GPIO.HIGH)


    def turn_left(self):
        print ("LEFT MOTION")
        #One motor moves forward, while the other moves backwards
        for x in range(40,100):
            self.EN1.ChangeDutyCycle(x)
            self.EN2.ChangeDutyCycle(x)
            GPIO.output(self.Motor1['input1'], GPIO.LOW)
            GPIO.output(self.Motor1['input2'], GPIO.HIGH)
            GPIO.output(self.Motor2['input1'], GPIO.HIGH)
            GPIO.output(self.Motor2['input2'], GPIO.LOW)


    def turn_right(self):
        print ("RIGHT MOTION")
        #One motor moves backwards, while the other moves forwards
        for x in range(40,100):
            self.EN1.ChangeDutyCycle(x)
            self.EN2.ChangeDutyCycle(x)
            GPIO.output(self.Motor1['input1'], GPIO.HIGH)
            GPIO.output(self.Motor1['input2'], GPIO.LOW)
            GPIO.output(self.Motor2['input1'], GPIO.LOW)
            GPIO.output(self.Motor2['input2'], GPIO.HIGH)
        

    def stop_moving(self):
        #If no arrow keys are pressed, motors are off
        self.EN1.ChangeDutyCycle(0)                                                 
        self.EN2.ChangeDutyCycle(0)


    def stop_script(self):
        exit()


# run the old functionality if this file is run in the old way
if __name__ == "__main__":
    
    controller = MotorController()
    while True:
        #If up arrow key is pressed
        if keyboard.is_pressed('Up'):
            controller.move_forward()
        
        #If down arrow key is pressed        
        elif keyboard.is_pressed('Down'):
            controller.move_backward()
        
        #If left arrow key is pressed        
        elif keyboard.is_pressed('Left'):
            controller.turn_left()
                
        #If right arrow key is pressed
        elif keyboard.is_pressed('Right'):
            controller.turn_right()
        
        else:
            controller.stop_moving()
            
        if keyboard.is_pressed('Ctrl+c'):
            controller.stop_script()
