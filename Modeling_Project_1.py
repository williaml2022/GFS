import math
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
from scipy.integrate import quad
from pylab import imshow, gray, show
from numpy import empty

x = np.zeros
y = np.zeros
z = np.zeros
r = np.zeros
# r is a constant, make it a range or give it a value


Dx_t = -3(x - y)

Dy_t = -x*z + r*x - y

Dz_t = x*y - z