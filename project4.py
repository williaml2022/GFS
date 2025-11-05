import math
import numpy as np
import matplotlib.pyplot as plt

#QUESTION 1: Create a plot of temperature, salinity, dissolved oxygen, density, and stratification as a function of
#depth at each of the stations that we occupied during the cruise. In the titles, indicate the station
#number (i.e. Station One is the first station at which we collected data, etc.).

#z in km
#S in pss (practical salinity scale)
#T in celsius

#rho = density
#c = reference density
#beta = haline contraction coefficient
#alpha = thermal expansion coefficient
#gamma = cabbeling coefficient
#Tmin = 15.4C, Tmax = 15.62C

S_near = np.array([25.5, 25.51, 25.53, 25.54, 25.56, 25.57, 25.59, 25.6, 25.61, 25.62,
    25.63, 25.64, 25.65, 25.66, 25.67, 25.68, 25.69, 25.69, 25.7, 25.71, 25.72, 25.73,
    25.73, 25.74, 25.76, 25.78, 25.79, 25.81, 25.82, 25.84, 25.86, 25.87, 25.89])

T_near = np.array([15, 15.01, 15.02, 15.02, 15.03, 15.04, 15.05, 15.06, 15.06, 15.07,
    15.07, 15.07, 15.08, 15.08, 15.09, 15.09, 15.09, 15.1, 15.1, 15.1, 15.11, 15.11,
    15.12, 15.12, 15.13, 15.14, 15.15, 15.17, 15.18, 15.19, 15.20, 15.21, 15.22])

z_near = np.array([0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8,
                   3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4, 5.6, 5.8, 
                   6, 6.2, 6.4]) # depth in meters



S_far = np.array([29.5, 29.52, 29.54, 29.56, 29.58, 29.6, 29.62, 29.64, 29.66, 29.69, 
                  29.72, 29.74, 29.77, 29.8, 29.83, 29.85, 29.87, 29.89, 29.91, 29.93,
                  29.95, 29.97, 29.99, 30.01, 30.04, 30.07, 30.1, 30.13, 30.16, 30.19,
                  30.21, 30.24, 30.26, 30.28, 30.3, 30.32, 30.34, 30.36, 30.38, 30.4, 
                  30.42, 30.44])

T_far = np.array([14.5, 14.52, 14.53, 14.55, 14.57, 14.59, 14.6, 14.62, 14.64, 14.65, 
                  14.67, 14.69, 14.7, 14.72, 14.74, 14.76, 14.77, 14.79, 14.81, 14.83,
                  14.85, 14.87, 14.89, 14.91, 14.95, 14.98, 15.01, 15.05, 15.08, 15.11,
                  15.14, 15.17, 15.19, 15.2, 15.21, 15.22, 15.23, 15.24, 15.25, 15.26,
                  15.27, 15.28])

z_far = np.array([0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3,
              3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4, 5.6, 5.8, 6, 
              6.2, 6.4, 6.6, 6.8, 7, 7.2, 7.4, 7.6, 7.8, 8, 8.2])


#constants:
rho_ref = 1000 #kg/m^3
g = -9.8 #m/s^2
drho = 0


def Density(z, S, T):
    rho = np.zeros_like(z)
    z /= 1000 #Change m to km

    for i in range(len(z)):
        beta = 0.808 - 0.0085*z[i]
        c = 999.83 + 5.053*z[i] - 0.048*z[i]**2
        alpha = 0.0708*(1 + 0.351*z[i] + 0.068*(1 - 0.0683*z[i])*T[i])
        gamma = 0.003*(1 - 0.059*z[i] - 0.012*(1 - 0.064*z[i])*T[i])
        rho[i] = c + beta*S[i] - alpha*T[i] - gamma*(35 - S[i])*T[i]
        print('Density at ' + str(z[i]) + 'm is ' + str(rho[i]) + ' kg/m^3')
    return rho
rho_near = Density(z_near, S_near, T_near)
rho_far = Density(z_far, S_far, T_far)

def Stratification(z, S, T):
    strat = np.zeros_like(z)
    rho = np.zeros_like(z)
    z /= 1000 #Change m to km
    for i in range(len(z)):
        beta = 0.808 - 0.0085*z[i]
        c = 999.83 + 5.053*z[i] - 0.048*z[i]**2
        alpha = 0.0708*(1 + 0.351*z[i] + 0.068*(1 - 0.0683*z[i])*T[i])
        gamma = 0.003*(1 - 0.059*z[i] - 0.012*(1 - 0.064*z[i])*T[i])
        rho[i] = c + beta*S[i] - alpha*T[i] - gamma*(35 - S[i])*T[i]
    drho = np.gradient(rho, z)
    strat = -g/rho_ref * drho
    print('Stratification per depth point is' + str(strat) + ' kg/m^3')
    return strat

strat_near = Stratification(z_near, S_near, T_near)
strat_far = Stratification(z_far, S_far, T_far)





# def Density(z, S, T):
#     for i in range(len(z)):
#         beta = 0.808 - 0.0085*z[i]
#         c = 999.83 + 5.053*z[i] - 0.048*z[i]**2
#         for T in range(len(T)):
#             alpha = 0.0708*(1 + 0.351*z[i] + 0.068*(1 - 0.0683*z[i])*T)
#             gamma = 0.003*(1 - 0.059*z[i] - 0.012*(1 - 0.064*z[i])*T)
#             for S in range(len(S)):
#                 rho[i] = c + beta*S - alpha*T - gamma*(35 - S)*T
#                 print('Density at ' + str(z[i]) + 'm is ' + str(rho[i]/1000) + ' kg/m^3')

#Density Depth Plot
plt.figure()
plt.plot(rho_near, z_near, marker = 'o', markersize = 4)
plt.gca().invert_yaxis()
plt.xlabel('Density ($kg/m^3$)')
plt.ylabel('Depth ($m$)')
plt.title('Density vs Depth @ Near Coast')
plt.show()

plt.figure()
plt.plot(rho_far, z_far, marker = 'o', markersize = 4)
plt.gca().invert_yaxis()
plt.xlabel('Density ($kg/m^3$)')
plt.ylabel('Depth ($m$)')
plt.title('Density vs Depth @ Far Coast')
plt.show()


#Temperature Depth Plot
plt.figure()
plt.plot(T_near, z_near, marker = 'o', markersize = 4, label = 'Near Coast')
plt.plot(T_far, z_far, marker = 'o', markersize = 4, label = 'Far Coast')
plt.gca().invert_yaxis()
plt.xlabel('Temperature ($^0C$)')
plt.ylabel('Depth ($m$)')
plt.title('Temperature vs Depth')
plt.legend()
plt.show()

#Salinity of Vandorn Bottle Depth Plot

S_vandorn_near = np.array([31, 32, 32])
z_vandorn_near = np.array([0, 2, 4])

S_vandorn_far = np.array([30, 31, 30.5, 31, 30])  #Salinity readings from Vandorn bottle at depths of 0m, 2m, 4m, 6m, 8m
z_vandorn_far = np.array([0, 2, 4, 6, 8])  #depths in meters for Vandorn bottle readings

plt.figure()
plt.plot(S_vandorn_near, z_vandorn_near, marker = 'o', markersize = 4, label = 'Near Coast')
plt.plot(S_vandorn_far, z_vandorn_far, marker = 'o', markersize = 4, label = 'Far Coast')
plt.gca().invert_yaxis()
plt.xlabel('Salinity ($psu$)')
plt.ylabel('Depth ($m$)')
plt.title('Salinity vs Depth')
plt.legend()
plt.show()

#Disolved Oxygen Depth Plot
DO_1 = np.array([9, 8.86, 8.85, 8.85])
DO_2 = np.array([8.84, 8.78, 8.75, 8.75])  #Dissolved Oxygen readings from Vandorn bottle at depths of 0m, 2m, 4m, 6m, 8m
z_DO = np.array([0.5, 1, 1.5, 2])  #depths in meters for Dissolved Oxygen readings

plt.figure()
plt.plot(DO_1, z_DO, marker = 'o', markersize = 4, label = 'One')
plt.plot(DO_2, z_DO, marker = 'o', markersize = 4, label = 'Two')
plt.gca().invert_yaxis()
plt.xlabel('Dissolved Oxygen ($mg/L$)')
plt.ylabel('Depth ($m$)')
plt.title('Dissolved Oxygen vs Depth')
plt.legend()
plt.show()

#Stratefication Plot
plt.figure()
plt.plot(strat_near*10**-4, z_near, marker = 'o', markersize = 3, label = 'Near Coast')
plt.plot(strat_far*10**-4, z_far, marker = 'o', markersize = 3, label = 'Far Coast')
plt.xlabel('Salinity ($psu$)')
plt.ylabel('Depth ($m$)')
plt.gca().invert_yaxis()
plt.title('Stratification Plot')
plt.legend()
plt.show()





# Tmin = np.array([15.4])  #Tmin = 15.4C, Tmax = 15.62C
# Tmax = np.array([15.62])
# Smin = np.array([27.8])
# Smax = np.array([27.96]) #Smin = 27.49pss, Smax = 27.9pss
# z = np.array([8])  #depth in meters

# def Density(z, S, T):
#     for i in range(len(z)):
#         beta = 0.808 - 0.0085*z[i]
#         c = 999.83 + 5.053*z[i] - 0.048*z[i]**2
#         for T in range(len(T)):
#             alpha = 0.0708*(1 + 0.351*z[i] + 0.068*(1 - 0.0683*z[i])*T)
#             gamma = 0.003*(1 - 0.059*z[i] - 0.012*(1 - 0.064*z[i])*T)
#             for S in range(len(S)):
#                 rho[i] = c + beta*S - alpha*T - gamma*(35 - S)*T
#                 print('Density at ' + str(z[i]) + 'm is ' + str(rho[i]/1000))


# T = ([15.4, 15.52, 15.62]) #Tmin = 15.4C, Tmax = 15.62C
# S = ([27.8, 27.9, 27.96]) #Smin = 27.49pss, Smax = 27.9pss
# z = ([0, 4, 8]) # depth in meters, zmin = 0m, z avg = 4m, zmax = 8m


# def Density(z, S, T):
#     rho = np.zeros_like(z)
#     beta = 0.808 - 0.0085*z
#     c = 999.83 + 5.053*z - 0.048*z**2
#     alpha = 0.0708*(1 + 0.351*z + 0.068*(1 - 0.0683*z)*T)
#     gamma = 0.003*(1 - 0.059*z - 0.012*(1 - 0.064*z)*T)
#     rho = c + beta*S - alpha*T - gamma*(35 - S)*T
#     print('Density at ' + str(z) + 'm is ' + str(rho/1000) + ' kg/m^3')
#     return rho
# rho  = np.array([Density(z[0], S[0], T[0]), Density(z[1], S[1], T[1]), Density(z[2], S[2], T[2])])
