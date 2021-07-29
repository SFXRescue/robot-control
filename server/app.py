#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This web application serves a motion JPEG stream
# main.py
# import the necessary packages
from flask import Flask, render_template, Response, request
from camera import VideoCamera
from motor_control import MotorController
from json import loads

# camera object
pi_camera = VideoCamera(flip=True)

# motor controller object
motors = MotorController()

# web app object
app = Flask(__name__)

# home route
@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/motor_control', methods=['POST'])
def motor_control():
    if request.method == 'POST':
        print(request.json)
        keystrokes = request.json['data']
        while keystrokes != []:
            if keystrokes[0] == 'Up':
                motors.move_forward()
            if keystrokes[0] == 'Down':
                motors.move_backward()
            if keystrokes[0] == 'Left':
                motors.turn_left()
            if keystrokes[0] == 'Right':
                motors.turn_right()
            if keystrokes[0] == 'Ctrl+c':
                exit()
            keystrokes = keystrokes[1:]
        motors.stop_moving()
    return ""


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
