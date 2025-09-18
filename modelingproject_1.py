import math
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
from scipy.integrate import quad
from pylab import imshow,gray,show
from numpy import empty

fig = plt.figure()
ax = plt.axes(projection ='3d')

N=10000
r=float(input("Enter a value r:"))
# The less the value of r is, the more thinner and flatter the Lorenz Attractor will be.
time=180
deltaT=time/N
x=np.zeros(N)
y=np.zeros(N)
z=np.zeros(N)
t=np.linspace(0,time,N)

dxdt=np.zeros(N)
dydt=np.zeros(N)
dzdt=np.zeros(N)

# initial conditions:
x[0]=2
y[0]=2
z[0]=2
# Doesn't work if all initial conditions are set to zero.

for i in range(1,N):
    dxdt[i]=-3*(x[i-1]-y[i-1])
    dydt[i]=(-x[i-1]*z[i-1])+(r*x[i-1])-y[i-1]
    dzdt[i]=(x[i-1]*y[i-1])-z[i-1]

    x[i]=x[i-1]+dxdt[i]*deltaT
    y[i]=y[i-1]+dydt[i]*deltaT
    z[i]=z[i-1]+dzdt[i]*deltaT


# Individual plots per each value against time:
# plt.plot(x,t)
# plt.title("X-Value VS. Time")
# plt.show()

# plt.plot(y,t)
# plt.title("Y-Value VS. Time")
# plt.show()

# plt.plot(z,t)
# plt.title("Z-Value VS. Time")
# plt.show()

# ----

# plt.plot(x,y)
# plt.title("x vs. y")

# plt.plot(x,z)
# plt.title("x vs. z")


#2D plot of x vs y and x vs z on the same graph:
plt.figure()
plt.plot(x, y, label = "x vs y")
plt.title('Lorenz Attractor, Initial Conditions (2,2,2)')
plt.xlabel='X'
plt.ylabel='Y or Z'
plt.legend()

plt.figure()
plt.plot(x, z, label = "x vs z")
plt.title('Lorenz Attractor, Initial Conditions (2,2,2)')
plt.xlabel='X'
plt.ylabel='Y or Z'
plt.legend()


#3D plot of x vs y vs z:
ax.plot3D(x, y, z,'.', markersize=0.2,color='red', label = '3D trajectory')
ax.set_title('Lorenz Attractor, Initial Conditions (2,2,2)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()