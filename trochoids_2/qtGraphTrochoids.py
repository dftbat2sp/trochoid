import pyqtgraph as pg
import numpy as np
from math import cos,sin
from time import sleep

win = pg.GraphicsWindow()
win.setWindowTitle('Trochoids')

bigR = 125
smallR = 75
pointR = 125

angle = 0

theta = 0.2
steps = int(6*3.14/theta)

for t in range(0,steps):
    angle+=theta

    x = (bigR - smallR) * cos(angle) + pointR * cos(((bigR-smallR)/smallR)*angle)
    y = (bigR - smallR) * sin(angle) - pointR * sin(((bigR-smallR)/smallR)*angle)

    print("x: ", x)
    print("y: ", y)

    sleep (0.5)
