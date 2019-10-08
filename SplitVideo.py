import cv2
import numpy as np
import os

cap = cv2.VideoCapture('testVideo.mp4')

try :
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print('Error : creating directory of data')

currentFrame = 0
while(True):
    ret, frame = cap.read()

    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    currentFrame += 1

    cap.release()
    cv2.destroyAllWindows()
    