from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
import time
from threading import *


def sign(num):
    return 1 if num > 0 else -1

def solver(x1, x2, prec=2):
    plot_button['state'] = DISABLED
    i = 1
    y1 = expression(x1)
    y2 = expression(x2)
    xmid = (x1+x2)/2
    ymid = expression(xmid)
    draw_plot(x1, x2, xmid, 0, i)

    while not is_acc(ymid, prec):
        if sign(ymid) == sign(y1):
            x1 = xmid
        else:
            x2 = xmid
        y1 = expression(x1)
        y2 = expression(x2)
        xmid = (x1+x2)/2
        ymid = expression(xmid)
        print(f'{i} {x1} {xmid} {x2} {ymid}')
        draw_plot(x1, x2, xmid, 0, i)
        time.sleep(1)
        i += 1
    # plt.show()
    plot_button['state'] = NORMAL

def is_acc(num, prec=2):
    return (10**(-prec)) > abs(num)

def draw_plot(start, end, xmid, ymid, iteration):
    x = np.linspace(start, end)
    y = expression(x)
    plot1.cla()
    plot1.plot(x,y)
    plot1.text((xmid), ((expression(xmid))/2), f' Difference : {-expression(xmid)}\n Error : {abs(expression(xmid)):%}')
    plot1.plot([xmid,xmid], [0,expression(xmid)])
    plot1.plot(xmid,ymid,'go',label='Mid Point')
    plot1.legend()
    
    plot1.set_title(f'Iteration No : {iteration}')
    canvas.draw()
    canvas.get_tk_widget().pack()

def expression(num):
    return num**3 - 100

def solve(start, end, prec):
    Thread(target = lambda: solver(start, end, prec)).start()
    
    

if __name__ == '__main__':
    window = Tk()
    window.title('Praktikum 1 Bolzano')
    window.geometry("720x720")
    figure = Figure(figsize=(10,10), dpi=100)
    plot1 = figure.add_subplot(111)
    
    start = 3
    end = 5
    prec = 3
    x = np.linspace(start,end)
    y = expression(x)
    plot1.plot(x,y)

    

    plot_button = Button(master=window,
                         command=lambda: solve(start, end, prec),
                         height=2,
                         width=10,
                         text='Plot')
    plot_button.pack()
    canvas = FigureCanvasTkAgg(figure, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    window.mainloop()
    
    
    