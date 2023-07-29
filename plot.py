import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

style.use('fivethirtyeight')

fig = plt.figure(figsize=(14.5,8.36))
ax1 = fig.add_subplot(1,1,1)
global_time=0

def animate(i):
    global global_time
    graph_data1 = open('data/N-TCP','r').read()
    graph_data2 = open('data/G-TCP','r').read()
    graph_data3 = open('data/B-UDP','r').read()

    lines1 = graph_data1.split('\n')
    lines2 = graph_data2.split('\n')
    lines3 = graph_data3.split('\n')

    xs1 = []
    ys1 = []
    xs2 = []
    ys2 = []
    xs3 = []
    ys3 = []

    times = 0
    for line in lines1:
        if len(line) > 1:
            xs1.append(float(times))
            ys1.append(float(line)/1000)
        times = times + 1

    times = 0
    for line in lines2:
        if len(line) > 1:
            xs2.append(float(times))
            ys2.append(float(line)/1000)
        times = times + 1
    times = 0
    for line in lines3:
        if len(line) > 1:
            xs3.append(float(times))
            ys3.append(float(line)/1000)
        times = times + 1

    xs1 = xs1[0:global_time+1]
    ys1 = ys1[0:global_time+1]
    xs2 = xs2[0:global_time+1]
    ys2 = ys2[0:global_time+1]
    xs3 = xs3[0:global_time+1]
    ys3 = ys3[0:global_time+1]
    global_time+=1
    
    ax1.clear()
    #plt.yscale("log", basey=2)
    ax1.set_ylim([0,14])
    ax1.plot(xs1, ys1,color='red',label='Non Guaranteed TCP')
    ax1.plot(xs2, ys2,color='blue',label='Guaranteed TCP')
    ax1.plot(xs3, ys3,color='green',label='Background UDP')
    plt.xticks(size=22)
    plt.yticks(size=22)
    ax1.legend(loc='upper left', shadow=True, prop={'size':22}) 
    ax1.set_xlabel('Time (s)',size=22)
    ax1.set_ylabel('Bandwidth (Gbit/s)',size=22)
    ax1.xaxis.set_label_coords(0.5, -0.05)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
