import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Circle sizes
statRad = 120               # Stationary Circle size
rotRad = 74                 # moving circle size
drawPointRad = rotRad / 2     # location from center of moving circle to draw

# Drawing parameters
theta = 0.05                    # distance in radians for each step

# how many calculations to do
steps = 2000

axisRange = statRad + 50   # Axis label range

def data_gen(angle=0):
    cnt = 0
    while cnt < 1000:
        cnt += 1
        angle += 0.05
        yield (statRad - rotRad) * np.cos(angle) + drawPointRad * np.cos(((statRad - rotRad) / rotRad) * angle), (statRad - rotRad) * np.sin(angle) - drawPointRad * np.sin(((statRad - rotRad) / rotRad) * angle)
        # (statRad - rotRad) * np.sin(angle) - drawPointRad * np.sin(((statRad - rotRad) / rotRad) * angle)
        #yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)


def init():
    ax.set_ylim(-axisRange, axisRange)
    ax.set_xlim(-axisRange, axisRange)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []


def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()
 
    line.set_data(xdata, ydata)

    return line,

ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=1,
                              repeat=False, init_func=init)
plt.show()