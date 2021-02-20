

#############################################
#   By: Dan Cohen                           #
#   Data: 1/20/2021                         #
#   ASU ID# 1204831845                      #
#   For class: Rapid Prototyping in python  #
#   Prof. Dr. Steve Millman                 #
#   hw2_pi.py                               #
#                                           #
#############################################

# import the necessary packages
import numpy as np
from scipy.integrate import quad


PI = np.pi  # const pi to compare


################################################################################
# Function to be integrated: (1/np.sqrt(z*(1-z)))                              #
# Input:                                                                       #
#    z: The variable used for the value substitution                           #
# Output:  the value of the function at a value called by quad                 #
################################################################################

def intergrand(z):  # function for calling the integrand used during problem
    y = (1/np.sqrt(z*(1-z)))

    return y

 #1/(((1 - z)*(1 - z)) *(1 + (z/(1-z))) * np.sqrt(z/(1-z))) was using this , but simpliftication can bring you closer to
                                                            # a better a anwser


ans, err = quad(intergrand,0, 1) # calculating the solution to the integral and the error




print("PI is ",round(ans,8))

diff = PI-ans  # calculated the difference between PI and what we were able to calculate
print("Difference from numpy.pi is: ",format(diff, '.15f'))  # print the result and show the format in 15 deci and float






