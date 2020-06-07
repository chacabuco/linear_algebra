import numpy as np
import matplotlib.pyplot as plt

def set_axis():
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))

class Vector:
    def __init__(self,x, y):
        self.x   = x
        self.y   = y

    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)


if __name__ == "__main__":
    set_axis()
    
    v = Vector(-1, 10)
    w = Vector(4, 2)
    s = v + w
    
    x_lim = np.array([v.x, w.x, s.x])
    y_lim = np.array([v.y, w.y, s.y])
    plt.xlim(x_lim.min(), x_lim.max())
    if (y_lim.min() < 0):
        plt.ylim(y_lim.min(), y_lim.max())
    else:
        plt.ylim(0, y_lim.max())
        
    x_pos = [0, 0, 0]
    y_pos = [0, 0, 0]
    x_dir = [v.x, w.x, s.x]
    y_dir = [v.y, w.y, s.y]
    
    plt.quiver(x_pos, y_pos, x_dir, y_dir, angles='xy', scale_units='xy', scale=1, color =['black','black','blue'])

    plt.plot([v.x, s.x], [v.y, s.y],[w.x, s.x],[w.y, s.y], color='black', linewidth=1.0, linestyle="--")

    plt.annotate(r'v = (' + str(v.x) + ',' + str(v.y) + ')',
             xy=(v.x, v.y), xycoords='data',
             xytext=(v.x, v.y + 1), textcoords='data', fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
    plt.annotate(r'w = (' + str(w.x) + ',' + str(w.y) + ')',
             xy=(w.x , w.y), xycoords='data',
             xytext=(w.x, w.y + 1 ), textcoords='data', fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
    plt.annotate(r'v + w',
             xy=(s.x, s.y), xycoords='data',
             xytext=((s.x/2)+1, s.y/2), textcoords='data', fontsize=14, color = "blue")

    plt.show()
