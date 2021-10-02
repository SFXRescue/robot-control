#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This web application serves a motion JPEG stream
# main.py


# import packages
from flask import Flask, render_template, Response, request
from json import loads
from multiprocessing import Process, Pipe
from motor_process import motor_control_process
from camera import VideoCamera
from motor_control import MotorController
from motor_process import motor_control_process


# camera object
pi_camera = VideoCamera(flip=True)


# motor controller object
motor_controller = MotorController()


# pipe communication endpoints
parent, child = Pipe()


# process for controlling motors on separate thread
# give it one end of pipe communication (child)
motors = Process(target=motor_control_process, args=(motor_controller,child))
motors.start()
print("Motor motion process has started on the server.")


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
        keystrokes = request.json['data']
        parent.send(keystrokes) # send keystrokes to pipe endpoint in motor process
        print(keystrokes) # debug text
    return ""


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
    motors.join()
