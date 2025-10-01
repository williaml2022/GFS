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
x=np.zeros(N)
y=np.zeros(N)
z=np.zeros(N)

dpdx=np.zeros(N)
dpdy=np.zeros(N)
f = #

for i in range(1,N):
    dpdx[i]=empty
    dpdy[i]=empty
    f*u_g == -1/ρ_o * dpdx
    f*v_g == 1/ρ_o * dpdy
