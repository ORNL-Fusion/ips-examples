#import matplotlib.pyplot as plt
#import matplotlib.tri as tri
#from mpl_toolkits.mplot3d import Axes3D
#import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import gitr
if __name__ == "__main__":
    x = [1,2,1,1,2,1.5]
    y = [-1, 0,1,-1,0,-1.5]
    z = [0,0,0,0,0,0]
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)
    plt.show()
