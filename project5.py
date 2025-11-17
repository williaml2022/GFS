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
    #print(tau_x)
    return tau_x, y_values

windStress, width = tau_x_function(y_range)

def Mek():
    #windStress_vecs = np.column_stack((windStress, np.zeros_like(windStress), np.zeros_like(windStress)))
    #mass = np.cross(windStress_vecs, z_hat)/f

    #print(mass[:, 1])
    mass = -1*windStress/f
    return mass
massTransport_y = Mek() #[:, 1] means only consider y direction
#massTransport_y = massTransport[:, 1]

def Psi():
    dTau_dy = -1 * np.gradient(windStress, width) # this is del cross Tau, which is in z direction
    # units of N/m^3
    x_vals = np.arange(0, x_range + 1)
    Psi_vals = np.empty(shape = (len(x_vals), len(width)))
    for i in range(len(x_vals)):
        for j in range(len(width)):
            dT_val = dTau_dy[j] # find the value of dT/dy at the current y value
            # because this dT_val is constant across x, we can take it out of the integral
            Psi_vals[i, j] = 1 / (rho_b * beta) * dT_val * (x_vals[i] - x_vals[0]) # and just multiply by the x distance
    
    return x_vals, Psi_vals

length, Psi_vals = Psi()
Psi_vals = Psi_vals
X, Y = np.meshgrid(length, width, indexing='ij')
V, U = np.gradient(Psi_vals, length, width) # vector components
U = -U

# plot stream function with some [U, V] vectors overlayed
plt.figure()
pcm = plt.pcolormesh(X, Y, Psi_vals, cmap = 'magma')
plt.colorbar(pcm, label = 'Psi(X, Y) (Sverdrups)')
plt.xlabel('X (km)')
plt.ylabel('Y (km)')
plt.title('Stream Function (color) and Depth-Integrated Velocity (arrows)')
# plot V, U too
step = 7
scaling = 0.02
Xp = X[::step, ::step]
Yp = Y[::step, ::step]
Up = U[::step, ::step]
Vp = V[::step, ::step]
plt.quiver(Xp, Yp, scaling*Up, scaling*Vp)

plt.savefig('P5_PsiUV.png')
plt.show()
plt.close()

#Plot Wind Stress
plt.figure()
plt.plot(windStress, width, markersize = 4)
plt.xlabel('Wind Stress ($N/m^2$)')
plt.ylabel('Y ($km$)')
plt.title('Wind Stress over Y')
plt.savefig('P5_stressY.png')
#plt.show()


#Plot Mass Transport
plt.figure()
plt.plot(massTransport_y, width, markersize = 4)
plt.xlabel('Mass Transport ($kg/m/s$)')
plt.ylabel('Y ($km$)')
plt.title('Mass Transport Over Y')
plt.savefig('P5_massY.png')
#plt.show()


#2D plot of both wind stress and mass transport
plt.figure()
plt.plot(windStress, width, label = 'Wind Stress')
plt.plot(massTransport_y / 1000, width, label = 'Ekman Transport (* 10^-3)')
plt.xlabel('Mass Transport and Wind Stress')
plt.ylabel('Y ($km$)')
plt.title('Mass Transport and Wind Stress over Y')
plt.legend()
plt.savefig('P5_massstress2dY.png')
#plt.show()

#3D plot of both Wind Stress & Mass Transport

width_z = np.linspace(0, z_range, len(width))

ax = plt.figure().add_subplot(111, projection = '3d')
ax.plot(windStress, np.zeros_like(width), width_z, label = 'Wind Stress')
ax.plot(np.zeros_like(width), massTransport_y, width_z, label = 'Ekman Transport')
ax.set_xlabel('Wind Stress ($N/m^2$)')
ax.set_ylabel('Ekman Transport ($kg/m/s$)')
ax.set_zlabel('Depth ($km$)')
plt.legend()
plt.savefig('P5_stressmassY.png')
#plt.show()