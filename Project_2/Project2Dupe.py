import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pressure_data = pd.read_csv("/Users/nolanstratton/Desktop/p.csv", header=None).values
ny, nx = pressure_data.shape
x = np.linspace(0, 100, nx)
y = np.linspace(0, 100, ny)
X, Y = np.meshgrid(x,y)
rho0 = 1.2
f = 1e-4
dpdx, dpdy = np.gradient(pressure_data, x, y, edge_order=2)
fu = -(1/rho0)*dpdx
fv = -(1/rho0)*dpdy
ug = -(1/(f*rho0))*dpdy
vg = (1/(f*rho0))*dpdx
dug_dy, dug_dx = np.gradient(ug, y, x, edge_order=2)
dvg_dy, dvg_dx = np.gradient(vg, y, x, edge_order=2)
div = dug_dx + dvg_dy

plt.figure(figsize=(8,6))
cont = plt.contourf(X, Y, pressure_data, cmap="coolwarm", levels=20)
cbar = plt.colorbar(cont)
cbar.set_label('Pressure (hPa)')
skip = (slice(None, None, 5), slice(None, None, 5))
plt.quiver(X[skip], Y[skip], fu[skip], fv[skip], color='black')
plt.title('Pressure Field with Pressure Gradient Force Vectors')
plt.xlabel("x (0-100)")
plt.ylabel("y (0-100)")
plt.show()

plt.figure(figsize=(8,6))
cont1 = plt.contourf(X, Y, pressure_data, cmap="coolwarm", levels=20)
cbar1 = plt.colorbar(cont1)
cbar1.set_label('Pressure (hPa)')
skip1 = (slice(None, None, 5), slice(None, None, 5))
plt.quiver(X[skip1], Y[skip1], ug[skip1], vg[skip1], color='black')
plt.title('Pressure Field with Geostrophic Velocity Vectors')
plt.xlabel("x (0-100)")
plt.ylabel("y (0-100)")
plt.show()

print(div)
plt.figure(figsize=(8,6))
im = plt.imshow(div, origin='lower', extent=(x.min(), x.max(), y.min(), y.max()), aspect='equal')
cbar = plt.colorbar(im)
plt.title('Divergence of Geostrophic Flow')
plt.xlabel("x (0-100)")
plt.ylabel("y (0-100)")
skip2 = (slice(None, None, max(1, nx//15)), slice(None, None, max(1, ny//15)))
plt.quiver(X[skip2], Y[skip2], ug[skip2], vg[skip2], scale=None, width = 0.002, alpha = 0.7)
plt.tight_layout()
plt.show()
