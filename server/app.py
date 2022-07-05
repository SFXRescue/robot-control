#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This web application serves a motion JPEG stream
# main.py


# import packages

import argparse
ap = argparse.ArgumentParser()
ap.add_argument('-vs', '--videosource', default='r', help='-vs r for robot, -vs w for webcam.')
ap.add_argument('-em', '--enablemotors', default='e', help='-en e for enable, -en d for disable.')
args = vars(ap.parse_args())

from flask import Flask, render_template, Response, request
from json import loads
import threading
from queue import Queue
from motor_process import motor_control_process
from camera import VideoCamera
from motor_control import MotorController
from motor_process import motor_control_process

pi_camera = VideoCamera(flip=False, videosource=args['videosource'])
motor_controller = MotorController(robot_mode=('e'==args['enablemotors']))
key_presses = Queue()
motors = threading.Thread(target=motor_control_process,
                          args=(motor_controller,key_presses)).start()
print("Motor motion process has started on the server.")
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(pi_camera.gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/motor_control', methods=['POST'])
def motor_control():
    if request.method == 'POST':
        keystrokes = request.json['data']
        key_presses.put(keystrokes) # put the whole list in the queue as one item
    return ""

if __name__ == "__main__":
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)).start()
