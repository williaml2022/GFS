ρ_o = 1.2#kg/m^3: reference density for the atmosphere
#41.6 degrees north latittude


import math
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
from scipy.integrate import quad
from pylab import imshow,gray,show
from numpy import empty
import pandas as pd

fig = plt.figure()
#ax = plt.axes(projection ='3d')

N=10000
x = pd.read_csv("x.csv", header = None).values
y = pd.read_csv("y.csv", header = None).values
p = pd.read_csv("p.csv", header = None).values
dpdx=np.zeros(N)
dpdy=np.zeros(N)
f = empty #Coriolis Parameter

for i in range(1,N):
    dpdx[i]=empty
    dpdy[i]=empty
    u_g = -1/ρ_o/f * dpdx #geostophic x velocity
    v_g = 1/ρ_o/f * dpdy #geostrophic y velocity
