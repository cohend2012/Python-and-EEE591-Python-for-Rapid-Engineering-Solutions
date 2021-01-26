
#   By: Dan Cohen                           #
#   Data: 1/16/2021                         #
#   hw2_poly.py                           #

#############################################

import numpy as np                     # get array functions
from scipy.integrate import quad       # get the integration function
import matplotlib.pyplot as plt        # get plotting functions

R = 5
STEP = 0.01                                   # step size to use
START = 0                                  # starting value of x
END = 5+STEP
################################################################################
# Function to be integrated: ax^2 + bx + c                                            #
# input:                                                                       #
#    x: the variable to integrate                                              #
#    a: a constant to be used
#    b: b constant to be used
#    c: c constant to be used
# output:                                                                      #
#    returns the value of the function at                                      #
################################################################################

def intergrand(x,a,b,c):
    y = a*(x*x)+b*x+c
    return y


a = 2
b = 3
c = 4
range_of_intergral = np.arange(START,END,STEP)         # the discrete points to sample
num_zs = len(range_of_intergral)                       # how many there are
vals_1 = np.zeros(num_zs,float)

for index in range(num_zs):


    ans, err = quad(intergrand,0, range_of_intergral[index]+STEP, args=(a,b,c))

    vals_1[index] = ans
print(vals_1)

a = 2
b = 1
c = 1
range_of_intergral = np.arange(START,END,STEP)         # the discrete points to sample
num_zs = len(range_of_intergral)                       # how many there are
vals_2 = np.zeros(num_zs,float)

for index in range(num_zs):


    ans, err = quad(intergrand,0 , range_of_intergral[index]+STEP, args=(a,b,c))

    vals_2[index] = ans
print(vals_2)




plt.plot(vals_1, label='ax^2 + bx + c, a=2,b=3,c=4', linestyle=':')
plt.plot(vals_2, label='ax^2 + bx + c, a=2,b=1,c=1', linestyle='-.')

plt.xlabel('Steps')          # add labels, title, grid and show it
plt.ylabel('Y-axis output value from the intergrand')
plt.title('hw2_pi, intergral curves from ax^2 + bx + c,')
plt.legend()
plt.grid()
plt.show()