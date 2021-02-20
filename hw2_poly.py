
#############################################
#   By: Dan Cohen                           #
#   Data: 1/20/2021                         #
#   ASU ID# 1204831845                      #
#   For class: Rapid Prototyping in python  #
#   Prof. Dr. Steve Millman                 #
#   hw2_poly.py                             #
#                                           #
#############################################
# start of code


import numpy as np                     # get array functions
from scipy.integrate import quad       # get the integration function
import matplotlib.pyplot as plt        # get plotting functions

R = 5                                  # max range you would like to integrate to
STEP = 0.01                            # step size to use
START = 0                              # starting value of x and start of of integration range
END = R + STEP  # calculating the end value by adding the end range value R and the STEP size


A_1 = 2  # The Constant Value A_1 being used for the polynomial integrand function
B_1 = 3  # The Constant Value B_1 being used for the polynomial integrand function
C_1 = 4  # The Constant Value C_1 being used for the polynomial integrand function

A_2 = 2  # The Constant Value A_2 being used for the polynomial integrand function
B_2 = 1  # The Constant Value B_2 being used for the polynomial integrand function
C_2 = 1  # The Constant Value C_2 being used for the polynomial integrand function

RANGE_OF_INTEGRAL = np.arange(START, END, STEP)  # the discrete points to sample over the range for the integration
num_zs = len(RANGE_OF_INTEGRAL)  # how many values are their for us to integrate over at assist the for loop


################################################################################
# Function to be integrated: ax^2 + bx + c                                     #
# input:                                                                       #
#    x: the variable to integrate                                              #
#    a: a constant to be used                                                  #
#    b: b constant to be used                                                  #
#    c: c constant to be used                                                  #
# output:                                                                      #
#    returns the value of the function at                                      #
################################################################################

def intergrand(x, a, b, c):  # take in x, a , b, c
    y = a * (x * x) + b * x + c  # calculate the value in terms of a , b, c
    return y



vals_1 = np.zeros(num_zs, float)  # pre-allocating the array we will use to store the solution

for index in range(num_zs):  # for loop to calculated the integral from 0 to the range

    current_range_of_integral = RANGE_OF_INTEGRAL[index] + STEP  # create the top number we would like to integrate to

    ans, err = quad(intergrand, 0, current_range_of_integral, args=(A_1, B_1, C_1))  # calculate the integral and the error
    # using the quad too to integrate with input arguments, ie the const. A , B and C

    vals_1[index] = ans  # store the solution



# how many there are
vals_2 = np.zeros(num_zs, float) # pre-allocating the array we will use to store the solution

for index in range(num_zs):  # for loop to calculated the integral from 0 to the range
    current_range_of_integral = RANGE_OF_INTEGRAL[index] + STEP # create the top number we would like to integrate to

    ans, err = quad(intergrand, 0, current_range_of_integral, args=(A_2, B_2, C_2)) # calculate the integral and the error
    # using the quad too to integrate with input arguments, ie the const. A , B and C

    vals_2[index] = ans # store the solution
# print(vals_2)

# plot the curve of the fist integral
plt.plot(RANGE_OF_INTEGRAL, vals_1, label='ax^2 + bx + c, a=2,b=3,c=4', linestyle=':')
# plot the curve of the second integral
plt.plot(RANGE_OF_INTEGRAL, vals_2, label='ax^2 + bx + c, a=2,b=1,c=1', linestyle='-.')

plt.xlabel('Steps')  # add labels, title, grid and show it
plt.ylabel('Y-axis output value from the integrand')
plt.title('hw2_pi, integral curves from ax^2 + bx + c,')
plt.legend()
plt.grid()
plt.show()
