import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #3D plot

x_range = y_range = 100 # km
z_range = 4 # km
f= 10**-4 # s^-1
beta = 10**-11
rho_b = 10**3

z_hat = np.array([0, 0, 1])

def tau_x_function(y_range):
    y_values = np.arange(0, y_range + 1)
    tau_x = 0.1 * np.sin(y_values/33) * np.sin(y_values/18 - 10)
    print(tau_x)
    return tau_x, y_values
windStress, depth = tau_x_function(y_range)


def Mek():
    windStress_vecs = np.column_stack((windStress, np.zeros_like(windStress), np.zeros_like(windStress)))
    mass = np.cross(windStress_vecs, z_hat)/f

    print(mass[:, 1])
    return mass
massTransport = Mek() #[:, 1] means only consider y direction
massTransport_y = massTransport[:, 1]


#Plot Wind Stress
plt.figure()
plt.plot(windStress, depth, marker = 'o', markersize = 4)
plt.gca().invert_yaxis()
plt.xlabel('Wind Stress ($N/m^2$)')
plt.ylabel('Depth ($km$)')
plt.title('Wind Stress over Depth')
plt.show()


#Plot Mass Transport
plt.figure()
plt.plot(massTransport_y, depth, marker = 'o', markersize = 4)
plt.gca().invert_yaxis() #invert y axis (for accurate depth)
plt.xlabel('Mass Transport ($kg/m/s$)')
plt.ylabel('Depth ($km$)')
plt.title('Mass Transport Over Depth')
plt.show()





#3D plot of both Wind Stress & Mass Transport

depth_z = np.linspace(0, z_range, len(depth))

ax = plt.figure().add_subplot(111, projection = '3d')
ax.plot(windStress, np.zeros_like(depth), depth_z, label = 'Wind Stress')
ax.plot(np.zeros_like(depth), massTransport_y, depth_z, label = 'Ekman Transport')
ax.set_xlabel('Wind Stress ($N/m^2$)')
ax.set_ylabel('Ekman Transport ($kg/m/s$)')
ax.set_zlabel('Depth ($km$)')
plt.legend()
plt.show()



