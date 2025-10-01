ρ_o = 1.2#kg/m^3: reference density for the atmosphere
#41.6 degrees north latittude


import math
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
from scipy.integrate import quad
from pylab import imshow,gray,show
from numpy import empty

fig = plt.figure()
#ax = plt.axes(projection ='3d')

N=10000
x = np.loadtxt("x.csv", delimiter = ",") #x.csv
y = np.loadtxt("y.csv", delimiter = ",") #y.csv
p = np.loadtxt("p.csv", delimiter = ",") #p.csv
print(p[0][1])
# dpdx=np.zeros(N)
# dpdy=np.zeros(N)
# f = empty #Coriolis Parameter

# for i in range(1,N):
#     dpdx[i]=empty
#     dpdy[i]=empty
#     u_g = -1/ρ_o/f * dpdx #geostrophic x velocity
#     v_g = 1/ρ_o/f * dpdy #geostrophic y velocity
