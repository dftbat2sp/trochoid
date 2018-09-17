import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
from math import cos,sin
from time import sleep 


win = pg.GraphicsWindow()           # create graphics window
win.setWindowTitle('Trochoids')     # set title
win.resize(1000,1000)               # set window size

# Circle sizes
statRad = 120               # Stationary Circle size
rotRad = 74                 # moving circle size
circDiff = statRad - rotRad # difference between the two circles, finding the center of rolling circle
drawPointRad = rotRad / 2     # location from center of moving circle to draw

# Drawing paarameters
startAngle = 0                       # starting angle
theta = 0.05                    # distance in radians for each step
oneRotation = int((2 / theta) + ((2 * np.pi) / theta))        # approx number of steps for 1 full rotation
# should only need to do number of rotation less than the ratius of the
                               # stationary circle
steps = int(statRad * oneRotation) 

axisRange = statRad + 50   # Axis label range

# Stationary Circle
statRadX = np.empty(steps) # array for x points
statRadY = np.empty(steps) # corresponding y points

# moving circle point
rollPointRadX = np.empty(steps) # array for x points
rollPointRadY = np.empty(steps) # corresponding y points

# rolling circle outline
rollCircRadX = np.empty(oneRotation)
rollCircRadY = np.empty(oneRotation)

# rolling circle Line
rollLineRadX = np.empty(2)
rollLineRadY = np.empty(2)

# set graph parameters
p1 = win.addPlot(title="testing")           # title
p1.setDownsampling(mode='peak') # reduce drawing load
                                 #p1.setClipToView(True)
p1.showGrid(x=True, y=True)                 # print grid
p1.setRange(xRange=[-axisRange,axisRange],  # set axis range
            yRange=[-axisRange,axisRange])


# reset where drawing starts
angle = startAngle

#print stationary circle
statCirc = pg.PlotCurveItem(pen=(1))
p1.addItem(statCirc)
#statCirc.setPos(0,0)
for t in range(0,oneRotation):
    x = statRad * cos(angle)
    y = statRad * sin(angle)
    
    statRadX[t] = x
    statRadY[t] = y

    angle += theta

# draw stationary circle
statCirc.setData(x=statRadX[:oneRotation], y=statRadY[:oneRotation], connect="finite")

# reset starting angle
angle = startAngle

# object for printing curve
rollPoint = pg.PlotCurveItem(pen=(2))
p1.addItem(rollPoint)

# object for printing rolling circle
rollingCirc = pg.PlotCurveItem(pen=(3))
p1.addItem(rollingCirc)

# object for printing line from center of rolling circle to drawing point
rollingLine = pg.PlotCurveItem(pen=(4))
p1.addItem(rollingLine)

# keeping track of rollPointRad's array index
t = 0

def rollPointDraw():
    global rollPointRadX, rollPointRadY, rollPoint, angle, t
    # hypotrochoid
    # add X and Y values to corresponding arrays
    rollPointRadX[t] = (statRad - rotRad) * cos(angle) + drawPointRad * cos(((statRad - rotRad) / rotRad) * angle)
    rollPointRadY[t] = (statRad - rotRad) * sin(angle) - drawPointRad * sin(((statRad - rotRad) / rotRad) * angle)

    # draw curve
    rollPoint.setData(rollPointRadX[:t],rollPointRadY[:t])

def rollCircDraw():
    global rollCircRadX, rollCircRadY, rollingCirc, circDiff, rotRad, angle, theta, rollingLine, rollLineRadX, rollLineRadY, t, rollPointRadX, rollPointRadY

    #calculate center of rolling circle
    centreX = circDiff * cos(angle)
    centreY = circDiff * sin(angle)

    rollLineRadX[0] = centreX
    rollLineRadY[0] = centreY
    rollLineRadX[1] = rollPointRadX[t]
    rollLineRadY[1] = rollPointRadY[t]

    rollingLine.setData(rollLineRadX[:2], rollLineRadY[:2])

    for rotationStep in range(0,oneRotation):
        # calculate theta (angle) value
        thetaSmall = (rotationStep * theta)

        # calculate point on circle of rollingCircle
        x = centreX + (rotRad * cos(thetaSmall))
        y = centreY + (rotRad * sin(thetaSmall))

        rollCircRadX[rotationStep] = x
        rollCircRadY[rotationStep] = y

    rollingCirc.setData(rollCircRadX[:oneRotation], rollCircRadY[:oneRotation])



def update():
    global angle, theta, t
    rollPointDraw()
    rollCircDraw()

    # move calculation point anti-clockwise theta
    angle+=theta

    #increase step for arrays by one
    t += 1      

timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(10)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()