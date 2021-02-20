
#############################################
#   By: Dan Cohen                           #
#   Data: 1/16/2021                         #
#   ASU ID# 1204831845                      #
#   For class: Rapid Prototyping in python  #
#   Prof. Dr. Steve Millman                 #
#   hw1_12.py                               #
#                                           #
#############################################

import numpy as np  # importing numpy


LIST_OF_NUMBERS = range(3, 10000, 1, ) # list of numbers from 2 to 10,000
prime_number_list = [2] # store the prime numbers, starting with 2 per instructions

for number_under_evaluation in LIST_OF_NUMBERS:  # looking at each number in the list of number
    has_prime_factor = 0  # start count if it has prime factors
    for potential_factor in prime_number_list:  # looking at each potential_factor

        if (potential_factor or number_under_evaluation) != 0:  # do not go on if either number is 0

            top_number_to_check = np.round(np.sqrt(number_under_evaluation))+1  # find the sqrt(n), top number to check

            if(top_number_to_check>potential_factor):  # if the top number is bigger then the factor we are checking
                # Do not need to check number after

                if(number_under_evaluation%potential_factor==0):  # if there is no remainder then it cant be prime

                    has_prime_factor = has_prime_factor+1  # add to the count if there is no remainder

            else:

                break # get out of for loop and move on to the next number to check

    if(has_prime_factor==0):  # if we were not able to find a number that goes into the number in question

        prime_number_list.append(number_under_evaluation)  # add to the prime number list





print("")
print("Your prime number list: ")
# print the prime number list
print(prime_number_list)