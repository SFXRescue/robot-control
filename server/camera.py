#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This scrtipt script..

import cv2
import imutils
import time
import numpy as np

class VideoCamera(object):
    def __init__(self, flip=False, videosource='w'):
        if videosource == 'r':
            self.vs = imutils.video.pivideostream.PiVideoStream().start()
        elif videosource == 'w':
            self.vs = imutils.video.VideoStream(src=0).start()
        self.flip = flip
        time.sleep(2.0)

    def __del__(self):
        self.vs.stop()

    def flip_if_needed(self, frame):
        if self.flip:
            return np.flip(frame, 0)
        return frame

    def get_frame(self):
        frame = self.flip_if_needed(self.vs.read())
        _, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

    def gen(self):
        while True:
            frame = self.get_frame()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
