import matplotlib.pyplot as plt
import numpy as np
from math import pi

plt.plot([1,2,3,6],[1,2,3,4])
plt.show()

x=np.linspace(-pi,pi,10)
y=np.sin(x)
plt.plot(x,y)
plt.show()

x=np.arange(10.)
y1=2**x
y2=x**2
plt.plot(x,y1,'r^',x,y2,'g')
plt.show()

x=np.arange(10.)
y=np.sin(x)

plt.plot(x,y,color='coral',linewidth=3.0,linestyle='--')
plt.xlim(-1,11)
plt.ylim(-1,1)
plt.show()

#plt.xticks(()) #show without x-scale
#plt.yticks(()) #show without y-scale

def f(x,y):    # the height function
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X,Y = np.meshgrid(x, y)
plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)
    #block color  (density, transparency, color)
C=plt.contour(X, Y, f(X, Y), 8, colors='black')
    #line color (density, color)

plt.clabel(C, inline=True, fontsize=10) #line color, number cover line?, fontsize
