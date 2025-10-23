import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objects as go

df=pd.read_csv(r"C:\Users\willi\OneDrive\Desktop\Coding Classes HW\p.csv", header=None)
pressure=df.to_numpy()

df=pd.read_csv(r"C:\Users\willi\OneDrive\Desktop\Coding Classes HW\x.csv", header=None)
x_values=df.to_numpy()

df=pd.read_csv(r"C:\Users\willi\OneDrive\Desktop\Coding Classes HW\y.csv", header=None)
y_values=df.to_numpy()


p_gradient_x=np.zeros((pressure.shape[0], pressure.shape[1]))
p_gradient_y=np.zeros((pressure.shape[0], pressure.shape[1]))

f=2*(7.2921e-5)*np.sin(np.radians(41.6))

dx=1000
dy=1000
dz=100
rho=1.2
g=9.8
alpha=3.4e-3

for i in range(pressure.shape[0]):
    for j in range(pressure.shape[1]):
        if i==0:
            p_gradient_x[i][j]=(pressure[i+1][j]-pressure[i][j])/dx
        elif i==pressure.shape[0]-1:
            p_gradient_x[i][j]=(pressure[i][j]-pressure[i-1][j])/dx
        else:
            p_gradient_x[i][j]=(pressure[i+1][j]-pressure[i-1][j])/(2*dx)

        if j==0:
            p_gradient_y[i][j]=(pressure[i][j+1]-pressure[i][j])/dy
        elif j==pressure.shape[1]-1:
            p_gradient_y[i][j]=(pressure[i][j]-pressure[i][j-1])/dy
        else:
            p_gradient_y[i][j]=(pressure[i][j+1]-pressure[i][j-1])/(2*dy)
        
pfx=-p_gradient_y/rho
pfy=-p_gradient_x/rho

u_g=1/f*pfy
v_g=-1/f*pfx

partial_ug=np.zeros((u_g.shape[0], u_g.shape[1]))
partial_vg=np.zeros((v_g.shape[0], v_g.shape[1]))

step=5

# for i in range(u_g.shape[0]):
#     for j in range(u_g.shape[1]):
#         if i==0:
#             partial_ug[i][j]=(u_g[i+1][j]-u_g[i][j])/dx
#         elif i==pressure.shape[0]-1:
#             partial_ug[i][j]=(u_g[i][j]-u_g[i-1][j])/dx
#         else:
#             partial_ug[i][j]=(u_g[i+1][j]-u_g[i-1][j])/(2*dx)

#         if j==0:
#             partial_vg[i][j]=(v_g[i][j+1]-v_g[i][j])/dy
#         elif j==pressure.shape[1]-1:
#             partial_vg[i][j]=(v_g[i][j]-v_g[i][j-1])/dy
#         else:
#             partial_vg[i][j]=(v_g[i][j+1]-v_g[i][j-1])/(2*dy)

# lhs=partial_ug+partial_vg

# plt.figure(figsize=(8, 6))
# plt.contourf(pressure, cmap='coolwarm', levels=20)
# plt.colorbar(label='Pressure (Pa)')
# plt.quiver(
#     x_values[::step, ::step],
#     y_values[::step, ::step],
#     pfx[::step, ::step],
#     pfy[::step, ::step]
# )
# plt.title('Pressure Map with Pressure Gradient Force Arrows')
# plt.xlabel('X (km)')
# plt.ylabel('Y (km)')
# plt.gca().set_aspect('equal')


# plt.figure(figsize=(8, 6))
# plt.contourf(pressure, cmap='coolwarm', levels=20)
# plt.colorbar(label='Pressure (Pa)')
# plt.quiver(
#     x_values[::step, ::step],
#     y_values[::step, ::step],
#     u_g[::step, ::step],
#     v_g[::step, ::step],
# )
# plt.title('Pressure Map with Geostrophic Velocity Arrows')
# plt.xlabel('X (km)')
# plt.ylabel('Y (km)')
# plt.gca().set_aspect('equal')

# plt.figure(figsize=(8, 6))
# plt.contourf(lhs, cmap='coolwarm', levels=20)
# plt.colorbar(label='Left-hand side of mass conservation equation')
# plt.title('Conservation of Mass Equation')
# plt.xlabel('X (km)')
# plt.ylabel('Y (km)')
# plt.gca().set_aspect('equal')


#PROJECT 3

df=pd.read_csv(r"C:\Users\willi\OneDrive\Desktop\Coding Classes HW\T1.csv", header=None)
data1=df.to_numpy()
data1=data1.T
T1=data1.flatten().reshape((101,101,101))
T1=np.transpose(T1, (2,1,0))


df=pd.read_csv(r'C:\Users\willi\OneDrive\Desktop\Coding Classes HW\T2.csv', header=None)
data2=df.to_numpy()
data2=data2.T
T2=data2.flatten().reshape((101,101,101))
T2=np.transpose(T2, (2,1,0))


df=pd.read_csv(r"C:\Users\willi\OneDrive\Desktop\Coding Classes HW\z.csv", header=None)
z_values=df.to_numpy()


# question 1
z_levels = [0, 33, 66, 100]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes = axes.flatten()

vmin = T1.min()
vmax = T1.max()

for i, z in enumerate(z_levels):
    temp_slice = T1[:, :, z]
    
    im = axes[i].imshow(
        temp_slice.T,
        origin='lower',
        cmap='coolwarm',
        vmin=vmin,
        vmax=vmax
    )
    
    axes[i].set_title(f'Temperature at z = {z_values[0][z]} km')
    axes[i].set_xlabel('X (km)')
    axes[i].set_ylabel('Y (km)')


fig.subplots_adjust(right=0.85)
cbar_ax = fig.add_axes([0.88, 0.15, 0.02, 0.7])
fig.colorbar(im, cax=cbar_ax, label='Temperature (°C)')

plt.suptitle('Horizontal Temperature Slices at 4 Atmospheric Levels', fontsize=14)

#T2
z_levels = [0, 33, 66, 100]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes = axes.flatten()

vmin = T2.min()
vmax = T2.max()

for i, z in enumerate(z_levels):
    temp_slice = T2[:, :, z]
    
    im = axes[i].imshow(
        temp_slice.T,
        origin='lower',
        cmap='coolwarm',
        vmin=vmin,
        vmax=vmax
    )
    
    axes[i].set_title(f'Temperature at z = {z_values[0][z]} km')
    axes[i].set_xlabel('X (km)')
    axes[i].set_ylabel('Y (km)')


fig.subplots_adjust(right=0.85)
cbar_ax = fig.add_axes([0.88, 0.15, 0.02, 0.7])
fig.colorbar(im, cax=cbar_ax, label='Temperature (°C)')

plt.suptitle('Horizontal Temperature Slices at 4 Atmospheric Levels', fontsize=14)

# #question 3

T1_gradient_x=np.zeros((T1.shape[0], T1.shape[1], T1.shape[2]))
T1_gradient_y=np.zeros((T1.shape[0], T1.shape[1], T1.shape[2]))

for i in range(T1.shape[0]):
    for j in range(T1.shape[1]):
        for k in range(T1.shape[2]):
            if i==0:
                T1_gradient_x[i][j][k]=(T1[i+1][j][k]-T1[i][j][k])/dx
            elif i==T1.shape[0]-1:
                T1_gradient_x[i][j][k]=(T1[i][j][k]-T1[i-1][j][k])/dx
            else:
                T1_gradient_x[i][j][k]=(T1[i+1][j][k]-T1[i-1][j][k])/(2*dx)

            if j==0:
                T1_gradient_y[i][j][k]=(T1[i][j+1][k]-T1[i][j][k])/dy
            elif j==T1.shape[1]-1:
                T1_gradient_y[i][j][k]=(T1[i][j][k]-T1[i][j-1][k])/dy
            else:
                T1_gradient_y[i][j][k]=(T1[i][j+1][k]-T1[i][j-1][k])/(2*dy)

partial_u_g_z=(alpha*g/f)*T1_gradient_y
partial_v_g_z=-(alpha*g/f)*T1_gradient_x

u_g_final=np.zeros((T1.shape[0], T1.shape[1], T1.shape[2]))
v_g_final=np.zeros((T1.shape[0], T1.shape[1], T1.shape[2]))

u_g_final[:, :, 0]= u_g
v_g_final[:, :, 0]= v_g



for i in range(T1.shape[0]):
    for j in range(T1.shape[1]):
        for k in range(1, T1.shape[2]):
            u_g_final[i][j][k]=u_g_final[i][j][k-1]+partial_u_g_z[i][j][k]*dz
            v_g_final[i][j][k]=v_g_final[i][j][k-1]+partial_v_g_z[i][j][k]*dz #is the partial the partial of the lower level of current level being calculated?


u_shear_profile = partial_u_g_z[i, j, :]
v_shear_profile = partial_v_g_z[i, j, :]

step = 15
X, Y, Z = np.meshgrid(
    x_values[0, :],
    y_values[0, :],
    z_values[0, :],
    indexing='ij'
)
X = X[::step, ::step, ::step]
Y = Y[::step, ::step, ::step]
Z = Z[::step, ::step, ::step]
U = u_g_final[::step, ::step, ::step]
V = v_g_final[::step, ::step, ::step]
W = np.zeros_like(U)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.quiver(X, Y, Z, U, V, W, length=0.03, arrow_length_ratio=0.09, color='blue')
ax.set_title('Geostrophic Velocity Vectors for T1')
ax.set_xlabel('X (km)')
ax.set_ylabel('Y (km)')
ax.set_zlabel('Z (km)')
plt.tight_layout()


#question 4

T2_gradient_x=np.zeros((T2.shape[0], T2.shape[1], T2.shape[2]))
T2_gradient_y=np.zeros((T2.shape[0], T2.shape[1], T2.shape[2]))

for i in range(T2.shape[0]):
    for j in range(T2.shape[1]):
        for k in range(T2.shape[2]):
            if i==0:
                T2_gradient_x[i][j][k]=(T2[i+1][j][k]-T2[i][j][k])/dx
            elif i==T2.shape[0]-1:
                T2_gradient_x[i][j][k]=(T2[i][j][k]-T2[i-1][j][k])/dx
            else:
                T2_gradient_x[i][j][k]=(T2[i+1][j][k]-T2[i-1][j][k])/(2*dx)

            if j==0:
                T2_gradient_y[i][j][k]=(T2[i][j+1][k]-T2[i][j][k])/dy
            elif j==T2.shape[1]-1:
                T2_gradient_y[i][j][k]=(T2[i][j][k]-T2[i][j-1][k])/dy
            else:
                T2_gradient_y[i][j][k]=(T2[i][j+1][k]-T2[i][j-1][k])/(2*dy)

partial_u_g_z=alpha*g/f*T2_gradient_y
partial_v_g_z=-alpha*g/f*T2_gradient_x

dz=100

u_g_final=np.zeros((T2.shape[0], T2.shape[1], T2.shape[2]))
v_g_final=np.zeros((T2.shape[0], T2.shape[1], T2.shape[2]))

u_g_final[:, :, 0]= u_g
v_g_final[:, :, 0]= v_g


for i in range(T2.shape[0]):
    for j in range(T2.shape[1]):
        for k in range(1, T2.shape[2]):
            u_g_final[i][j][k]=u_g_final[i][j][k-1]+partial_u_g_z[i][j][k]*dz
            v_g_final[i][j][k]=v_g_final[i][j][k-1]+partial_v_g_z[i][j][k]*dz #is the partial the partial of the lower level of current level being calculated?

step = 15
X, Y, Z = np.meshgrid(
    x_values[0, :],
    y_values[0, :],
    z_values[0, :],
    indexing='ij'
)
X = X[::step, ::step, ::step]
Y = Y[::step, ::step, ::step]
Z = Z[::step, ::step, ::step]
U = u_g_final[::step, ::step, ::step]
V = v_g_final[::step, ::step, ::step]
W = np.zeros_like(U)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.quiver(X, Y, Z, U, V, W, length=0.005, arrow_length_ratio=0.09, color='blue')
ax.set_title('Geostrophic Velocity Vectors for T2')
ax.set_xlabel('X (km)')
ax.set_ylabel('Y (km)')
ax.set_zlabel('Z (km)')
plt.tight_layout()




#THE FOLLOWING ILLUSTRATES THERES A PROBLEM with the 3d graphing
# X, Y = np.meshgrid(
#     np.arange(0, T1.shape[0], step),
#     np.arange(0, T1.shape[1], step),
#     indexing='ij'
# )

# # Extract the gradient values at z=0
# U = u_g_final[::step, ::step, 0]
# V = v_g_final[::step, ::step, 0]

# # Plot 2D quiver
# plt.figure(figsize=(10, 8))
# # plt.quiver(
# #     x_values[::step, ::step],
# #     y_values[::step, ::step],
# #     u_g_final[::step, ::step, 0],
# #     v_g_final[::step, ::step, 0], # THIS IS GOOD
# # )
# plt.quiver(Y, X, U, V, color='black', scale=50)  # Adjust scale for visibility
# plt.title('2D Gradient Vectors of Temperature at Z = 0')
# plt.xlabel('X (km)')
# plt.ylabel('Y (km)')
# plt.axis('equal')
# plt.tight_layout()
# plt.show()


#the following code is an interaction-based graph that shows isotherms designated by isomin and isomax

# fig = go.Figure(data=go.Isosurface(
#     x=np.arange(101).repeat(101*101),
#     y=np.tile(np.arange(101).repeat(101), 101),
#     z=np.tile(np.arange(101), 101*101),
#     value=T1.flatten(),
#     isomin=33,
#     isomax=46,
#     surface_count=3,
#     colorscale='blues',
#     caps=dict(x_show=False, y_show=False, z_show=False)
# ))

# fig.update_layout(
#     title='3D Temperature Isosurface',
#     scene=dict(
#         xaxis_title='X (km)',
#         yaxis_title='Y (km)',
#         zaxis_title='Z (km)'
#     )
# )

plt.show()