# pip install opencv-python
# pip install pywin32
# pip install numpy
# pip install PyAutoGUI

import cv2
import pyautogui       # used for take screenshot
from win32api import GetSystemMetrics
import numpy as np
import time

width = GetSystemMetrics(0)      # will start the width from 0
height = GetSystemMetrics(1)     # will capture the complete height
dimention = (width,height)
f=cv2.videoWriter_fourcc(*"XVID")  # type of video like-mp3,mp.......
# f=cv2.cv.CV_FOURCC(*'XVID')
output=cv2.VideoWriter("test1.mp4",f,30.0,dimention)
now_start_time = time.time()
duration = 10
end_time=now_start_time+duration
while True:
    image = pyautogui.screenshot()
    frame_1=np.array(image)
    frame =cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB)
    output.write(frame)
    c_time=time.time()
    if c_time>end_time:
        break
output.release()
print("screen recorded succesfully")
