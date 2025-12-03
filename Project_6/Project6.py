from random import uniform
import numpy as np
import matplotlib.pyplot as plt

λ1 = 15 #W/m^2/K
λ2 = 50 #W/m^2/K
rho = 1000 # Ocean density in kg/m^3
c_p = 3850 # Specific heat of ocean inJ/kg/K
h = 100 # Mixed layer depth, assume 100m for project


n = 3652 # days = 10 years
dt = 24*3600 #24 hour = 24*3600 seconds (Time step is per day)
t = np.arange(n) #Time scale over 10 years
all_T = []



#Q = randrange(-300000, 300000)/100000

all_Qnet = []

#LOOP OF 4 SIMULATIONS
for run in range(4):
    T = np.zeros(n)
    T[0] = 0 #Initial condition

    Qnet = np.random.uniform(-3, 3, n) # Reset Qnet for each simulation
    
    all_Qnet.append(Qnet) # Save Q data cause why not

    for i in range(1, n):
        dT_dt = (Qnet[i] - λ1 * T[i - 1]) / (rho * c_p * h)
        T[i] = T[i - 1] + dt * dT_dt
    all_T.append(T)

plt.figure(figsize = (15, 6))
for i in range(4):
     plt.plot(t, all_T[i], label = 'Simulation' + str(i + 1))
plt.xlabel('Day')
plt.ylabel('Temperature Anomoly (°C)')
plt.legend()
plt.grid(True)
plt.title('Temperature evolution over 10 years\n(4 random Qnet values)')
plt.show()










# Qnet_1 = Qnet[0]
# Qnet_2 = Qnet[1]
# Qnet_3 = Qnet[2]
# Qnet_4 = Qnet[3]

# print('Qnet_1 = ' + str(Qnet_1))
# print('Qnet_2 = ' + str(Qnet_2))
# print('Qnet_3 = ' + str(Qnet_3))
# print('Qnet_4 = ' + str(Qnet_4))



