
#############################################
#   By: Dan Cohen                           #
#   Data: 1/16/2021                         #
#   ASU ID# 1204831845                      #
#   For class: Rapid Prototyping in python  #
#   Prof. Dr. Steve Millman                 #
#   hw1_13.py                               #
#                                           #
#############################################

import numpy as np


list_of_number=range(3,10001,1,) # list of numbers from 2 to 10,000
prime_number_list = [2] # store the prime numbers

for number_under_evaluation in list_of_number: # looking at each number in the list of number
    has_prime_factor = 0 # start count if it has prime factors
    for potential_factor in prime_number_list: # looking at each potential_factor
        #print('factor being checked',potential_factor)
        #input()
        if (potential_factor or number_under_evaluation) != 0: # do not go on if either number is 0

            top_number_to_check = np.round(np.sqrt(number_under_evaluation))+1 # find the sqrt(n), top number to check

            if(top_number_to_check>potential_factor): # if the top number is bigger then the factor we are checking
                # Do not need to check number after
                #print(top_number_to_check)
                #print("number under eval vs factor")
                #print(number_under_evaluation, potential_factor,)

                if(number_under_evaluation%potential_factor==0): # if there is no remainder then it cant be prime

                    has_prime_factor = has_prime_factor+1 # add to the count if there is no remainder
                    #print("Has factor")
                    #print(has_prime_factor)
            else:
                #print("not looking any futher")
                break # get out of for loop and move on to the next number to check

    if(has_prime_factor==0): # if we could not find a number that goes iot the number in quesiton, the count should be 0
        #print("adding number to list")
        prime_number_list.append(number_under_evaluation) # add to the prime number list

                    # look at factor of the factors



            # do nothing


print(prime_number_list) # print the prime number list