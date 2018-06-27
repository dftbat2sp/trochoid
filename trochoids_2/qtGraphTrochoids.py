import pyqtgraph as pg
import numpy as np
from math import cos,sin
from time import sleep

#win = pg.GraphicsWindow()
#win.setWindowTitle('Trochoids')

bigR = 125
smallR = 75
pointR = 125

angle = 0

theta = 0.2
steps = int(6*3.14/theta)

dataX = np.empty(steps)
dataY = np.empty(steps)
dataArray = np.array([dataX, dataY], np.float)

for t in range(0,steps):
    angle+=theta

    x = (bigR - smallR) * cos(angle) + pointR * cos(((bigR-smallR)/smallR)*angle)
    y = (bigR - smallR) * sin(angle) - pointR * sin(((bigR-smallR)/smallR)*angle)

    dataX[t] = x
    dataY[t] = y

    print("x: ", x)
    print("y: ", y)

#p1 = win.addPlot()
pg.show(dataArray)
#