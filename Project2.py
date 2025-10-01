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
dpdx=np.zeros_like(p)
dpdy=np.zeros_like(p)
u_g = np.zeros_like(p) #geostrophic x velocity
v_g = np.zeros_like(p) #geostrophic y velocity
f = 3 #Coriolis Parameter

for i in range(1,N):
    dpdx, dpdy = np.gradient(p, x[:], y[:])
    u_g = -1/ρ_o/f * dpdx
    v_g = 1/ρ_o/f * dpdy
