import numpy as np
import matplotlib.pyplot as plt

y_range = z_range = 100
z_hat = np.array([0, 0, 1])
f= 10**-4
beta = 10**-11
rho_b = 10**3


def tau_x_function(y_range):
    y_values = np.arange(0, y_range + 1)
    tau_x = 0.1 * np.sin(y_values/33) * np.sin(y_values/18 - 10)
    print(tau_x)
    return tau_x, y_values
windStress, depth = tau_x_function(y_range)

def Mek(z_range, windStress):
    windStress_vecs = np.column_stack((windStress, np.zeros_like(windStress), np.zeros_like(windStress)))
    mass = np.cross(windStress_vecs, z_hat)/f
    print(mass)
    return mass
massTransport = Mek(z_range, windStress)

    

# for y in range(y_range + 1):
#     tau_x = tau_x_function(y)
#     print(tau_x)
#     print(y)


plt.figure()
plt.plot(windStress, depth, marker = 'o', markersize = 4)
plt.gca().invert_yaxis()
plt.xlabel('Wind Stress ($N/m^2$)')
plt.ylabel('Depth ($km$)')
plt.title('Wind Stress Over Depth')
plt.show()

plt.figure()
plt.plot(massTransport[:, 1], depth, marker = 'o', markersize = 4)
plt.gca().invert_yaxis()
plt.xlabel('Wind Stress ($N/m^2$)')
plt.ylabel('Depth ($km$)')
plt.title('Mass Transport Over the z-direction')
plt.show()

