from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math
import gitr
if __name__ == "__main__":
    x1,x2,x3,y1,y2,y3,z1,z2,z3,area,Z,surfIndArray,surf=gitr.read3dGeom(filename='/Users/tyounkin/Code/gitr2/iter/iter_milestone/3d/input/iterRefinedTest.cfg')
    rBound = 5.554-0.018
    r1 = np.sqrt(np.multiply(x1,x1) + np.multiply(y1,y1)) 
    r2 = np.sqrt(np.multiply(x2,x2) + np.multiply(y2,y2)) 
    r3 = np.sqrt(np.multiply(x3,x3) + np.multiply(y3,y3)) 
    Surf = np.where((surf>0) & (r1>=rBound) & (r2>=rBound) & (r3>=rBound) )
    xc = (x1[Surf[0]]+x2[Surf[0]]+x3[Surf[0]])/3.0
    yc = (y1[Surf[0]]+y2[Surf[0]]+y3[Surf[0]])/3.0
    zc = (z1[Surf[0]]+z2[Surf[0]]+z3[Surf[0]])/3.0

    print "number of w surfaces",len(Surf[0])
    x = []
    y = []
    z = []
    for j in range(len(Surf[0])):
        i = Surf[0][j]
        x.append(x1[i])
        x.append(x2[i])
        x.append(x3[i])
        y.append(y1[i])
        y.append(y2[i])
        y.append(y3[i])
        z.append(z1[i])
        z.append(z2[i])
        z.append(z3[i])
    x=np.array(x)
    y=np.array(y)
    z=np.array(z)
    print 'mininum z',z.min()
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.scatter(xc, yc, zc, c='r', marker='o')
    #ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)
    plt.show()
    #plt.savefig('surfaces.png')
    #plt.close()
