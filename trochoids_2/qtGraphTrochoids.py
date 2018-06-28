import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
from math import cos,sin
from time import sleep 

win = pg.GraphicsWindow()
win.setWindowTitle('Trochoids')
win.resize(1000,1000)

bigR = 125
smallR = 100
pointR = 100

angle = 0

theta = 0.01
steps = int(1000 * 3.14 / theta)

dataX = np.empty(steps)
dataY = np.empty(steps)

circleX = np.empty(steps)
circleY = np.empty(steps)

for t in range(0,steps):
    angle+=theta

    x = (bigR - smallR) * cos(angle) + pointR * cos(((bigR - smallR) / smallR) * angle)
    y = (bigR - smallR) * sin(angle) - pointR * sin(((bigR - smallR) / smallR) * angle)

    dataX[t] = x
    dataY[t] = y

    x = bigR * cos(angle)
    y = bigR * sin(angle)

    circleX[t] = x
    circleY[t] = y
    #print("x: ", x)
    #print("y: ", y)

#p1 = win.addPlot(title="Basic array plotting", y=np.random.normal(size=100))
p1 = win.addPlot(title="testing")
#p1.setDownsampling(mode='peak')
#p1.setClipToView(True)
p1.showGrid(x=True, y=True)
p1.setRange(xRange=[-150,150], yRange=[-150,150])
p1.plot(dataX, dataY)
p1.plot(circleX, circleY)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()