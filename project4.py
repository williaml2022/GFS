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

T = ([15.4, 15.52, 15.62]) #Tmin = 15.4C, Tmax = 15.62C
S = ([27.8, 27.9, 27.96]) #Smin = 27.49pss, Smax = 27.9pss
z = ([0, 4, 8]) # depth in meters, zmin = 0m, z avg = 4m, zmax = 8m


def Density(z, S, T):
    rho = np.zeros_like(z)
    beta = 0.808 - 0.0085*z
    c = 999.83 + 5.053*z - 0.048*z**2
    alpha = 0.0708*(1 + 0.351*z + 0.068*(1 - 0.0683*z)*T)
    gamma = 0.003*(1 - 0.059*z - 0.012*(1 - 0.064*z)*T)
    rho = c + beta*S - alpha*T - gamma*(35 - S)*T
    print('Density at ' + str(z) + 'm is ' + str(rho/1000) + ' kg/m^3')
    return rho
rho  = np.array([Density(z[0], S[0], T[0]), Density(z[1], S[1], T[1]), Density(z[2], S[2], T[2])])

#Density Depth Plot
plt.figure()
plt.plot(rho, z, marker = 'o')
plt.gca().invert_yaxis()
plt.xlabel('Density ($kg/m^3$)')
plt.ylabel('Depth ($km$)')
plt.title('Density vs Depth')
plt.show()

#Temperature Depth Plot
plt.figure()
plt.plot(T, z, marker = 'o')
plt.gca().invert_yaxis()
plt.xlabel('Temperature ($^0C$)')
plt.ylabel('Depth ($km$)')
plt.title('Temperature vs Depth')
plt.show()

#Salinity of Vandorn Bottle Depth Plot

S_vandorn = np.array([30, 31, 30.5, 31, 30])  #Salinity readings from Vandorn bottle at depths of 0m, 2m, 4m, 6m, 8m
z_vandorn = np.array([0, 2, 4, 6, 8])  #depths in meters for Vandorn bottle readings

plt.figure()
plt.plot(S_vandorn, z_vandorn, marker = 'o')
plt.gca().invert_yaxis()
plt.xlabel('Salinity ($pss$)')
plt.ylabel('Depth ($km$)')
plt.title('Salinity vs Depth')
plt.show()

#Disolved Oxygen Depth Plot
DO_1 = np.array([9, 8.86, 8.85, 8.85])
DO_2 = np.array([8.84, 8.78, 8.75, 8.75])  #Dissolved Oxygen readings from Vandorn bottle at depths of 0m, 2m, 4m, 6m, 8m
z_DO = np.array([0.5, 1, 1.5, 2])  #depths in meters for Dissolved Oxygen readings

plt.figure()
plt.plot(DO_1, z_DO, marker = 'o')
plt.plot(DO_2, z_DO, marker = 'o')
plt.gca().invert_yaxis()
plt.xlabel('Dissolved Oxygen ($mg/L$)')
plt.ylabel('Depth ($km$)')
plt.title('Dissolved Oxygen vs Depth')
plt.show()

#Stratefication Plot
plt.figure()
plt.plot(S, T, marker = 'o')
plt.xlabel('Salinity ($pss$)')
plt.ylabel('Temperature ($^0C$)')
plt.title('Stratification Plot')
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


#QUESTION 2: For each station, identify the mixed layer, thermocline, halocline, and pycnocline. In a few sentences,
#comment on the differences in the depths of each of these metrics across the stations. What physical
#process(es) may be responsible for such variations?