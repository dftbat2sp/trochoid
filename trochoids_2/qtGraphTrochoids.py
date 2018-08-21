import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
from math import cos,sin
from time import sleep 


win = pg.GraphicsWindow()           # create graphics window
win.setWindowTitle('Trochoids')     # set title
win.resize(1000,1000)               # set window size

# Circle sizes
statRad = 144               # Stationary Circle size
rotRad = 72                 # moving circle size
drawPointRad = rotRad/2     # location from center of moving circle to draw

# Drawing paarameters
startAngle = 0                       # starting angle
theta = 0.05                    # distance in radians for each step
oneRotation = int(3.14/theta)        # number of steps for 1 full rotation
# should only need to do number of rotation less than the ratius of the stationary circle
steps = int(statRad * oneRotation) 

axisRange = statRad + 50   # Axis label range

# Stationary Circle
statRadX = np.empty(steps) # array for x points
statRadY = np.empty(steps) # corresponding y points

# moving circle
rotRadX = np.empty(steps) # array for x points
rotRadY = np.empty(steps) # corresponding y points

# set graph parameters
p1 = win.addPlot(title="testing")           # title
#p1.setDownsampling(mode='peak')             # reduce drawing load
#p1.setClipToView(True)
p1.showGrid(x=True, y=True)                 # print grid
p1.setRange(xRange=[-axisRange,axisRange],  # set axis range
            yRange=[-axisRange,axisRange])

#don't know what this does yet, used for "live" drawing
#curve = p1.plot()

angle = startAngle
# print stationary circle
for t in range(0,oneRotation * 10):
    x = statRad * cos(angle)
    y = statRad * sin(angle)

    statRadX[t] = x
    statRadY[t] = y

    print("x: ",x,", y: ",y)

    angle += theta

# draw stationary circle
p1.plot(statRadX, statRadY)

angle = startAngle
#for t in range(0,steps):

#    # hypotrochoid
#    # add X and Y values to corresponding arrays
#    rotRadX[t] = (statRad - rotRad) * cos(angle) + drawPointRad * cos(((statRad - rotRad) / rotRad) * angle)
#    rotRadY[t] = (statRad - rotRad) * sin(angle) - drawPointRad * sin(((statRad - rotRad) / rotRad) * angle)

#    # draw curve
#    curve.setData(rotRadX[:t], rotRadY[:t])

#    # move calculation point clockwise theta
#    angle+=theta    

#    sleep(0.05) # TEST

# print plot after calculating all the points
# p1.plot(rotRadX, rotRadY)


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()