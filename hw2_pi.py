
#   By: Dan Cohen                           #
#   Data: 1/16/2021                         #
#   hw2_pi.py                           #

#############################################



import numpy as np
from scipy.integrate import quad


PI = np.pi # const pi to compare


################################################################################
# Function to be integrated: 1/((1 - z)^2 *(1 + (z/1-z)) * sqrt(z/1-z))                                          #
# input:                                                                       #
#    z: the variable to integrate                                              #                                                  #
#    output:                                                                      #
#    returns the value of the function at                                      #
################################################################################

def intergrand(z):
    y = 1/(((1 - z)*(1 - z)) *(1 + (z/(1-z))) * np.sqrt(z/(1-z)))
    return y




ans, err = quad(intergrand,0, 1)




print("PI is ",round(ans,8))

diff =  PI-ans
print("Difference from numpy.pi is: ",format(diff, '.15f'))






