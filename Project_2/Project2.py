import math
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
from scipy.integrate import quad
from pylab import imshow,gray,show
from numpy import empty

ρ_o = 1.2#kg/m^3: reference density for the atmosphere
#41.6 degrees north latittude

x = np.loadtxt("x.csv", delimiter = ",") #x.csv
y = np.loadtxt("y.csv", delimiter = ",") #y.csv
p = np.loadtxt("p.csv", delimiter = ",") #p.csv
dpdx = np.zeros_like(p)
dpdy = np.zeros_like(p)
u_g = np.zeros_like(p) #geostrophic x velocity
v_g = np.zeros_like(p) #geostrophic y velocity
f = 1E-4 #Coriolis Parameter


dpdx, dpdy = np.gradient(p, x[:], y[:])
u_g = -1/ρ_o/f * dpdx
v_g = 1/ρ_o/f * dpdy

#Part 1
cp = plt.contourf(x, y, p, cmap='coolwarm') 
plt.colorbar(cp, label = 'Pressure (Pa)')
plt.title('Pressure Field colorized')
plt.xlabel='X'
plt.ylabel='Y'
plt.show()


#Part 5

_, du_gdx = np.gradient(v_g, x[:], y[:])
dv_gdy, _ = np.gradient(u_g, x[:], y[:])
mass_conservation = du_gdx + dv_gdy

cp = plt.contourf(x, y, mass_conservation, cmap='coolwarm') 
plt.colorbar(cp, label = 'Pressure (Pa)')
plt.title('Is Mass Conserved?')
plt.xlabel='X'
plt.ylabel='Y'
plt.show()
