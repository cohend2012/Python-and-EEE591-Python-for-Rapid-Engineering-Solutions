#############################################
#   By: Dan Cohen                           #
#   Data: 1/16/2021                         #
#   ASU ID# 1204831845                      #
#   For class: Rapid Prototyping in python  #
#   Prof. Dr. Steve Millman                 #
#   hw1_13.py                               #
#                                           #
#############################################
# start of code


################################################################################
# Function name and how to call: factorial(n)                                  #
# Function Goal: Determine the factorial of a number                           #
# Input:                                                                       #
#        n : An integer number                                                 #
#                                                                              #
# Output:                                                                      #
#          Factorial of the input number also integer                          #
#                                                                              #
#                                                                              #
################################################################################


def factorial(n):
    if n == 1:  # if n is equal to 1
        return 1  # return 1
    else:  # otherwise
        return n * factorial(n - 1)  # otherwise return n time the factorial n -1


################################################################################
# Function name and how to call: catalan(n)                                    #
# Function Goal: Determine the catalan number                                  #
# Input:                                                                       #
#        n : A integer point number                                           #
#                                                                              #
# Output:                                                                      #
#          A floating point catalan number                                     #
#                                                                              #
#                                                                              #
################################################################################

def catalan(n):
    if n == 0:  # if n is equal to equal to zero
        return 1  # return 1
    if n > 0:  # if n is greater then 1
        return ((4 * n - 2) / (n + 1)) * catalan(n - 1)  # calculating the catalan number if n is not 0

################################################################################
# Function name and how to call: greatest_common_divisor(m, n)                 #
# Function Goal: Determine the greatest common divisor                         #
# Inputs:                                                                      #
#        n : An integer number                                                 #
#        m : A second integer number                                           #
#                                                                              #
# Output:                                                                      #
#          An integer which is the greatest common divisor                     #
#                                                                              #
#                                                                              #
################################################################################

def greatest_common_divisor(m, n):
    if n == 0:  # if n is equal to 0
        return m  # return m
    if n > 0:  # if it greater then 0
        return greatest_common_divisor(n, m % n)  # use greatest common divisor function


# gather user input for the factorial function
factorial_compuation_integer = int(input("Enter an integer for a factorial computation: "))

# gather user input for the the catalin computation
catalan_computation_integer = int(input("Enter an integer for a Catalan number computation: "))
# gather input to the first integers for the GCD computation
first_number_for_greatest_common_divisor = int(input("Enter the first of two integers for a GCD calculation: "))
# gather input to the second integers for the GCD computation
second_number_for_greatest_common_divisor = int(input("Enter the second integer for the GCD calculation: "))

print("")
# print factorial computation
print("factorial of ", factorial_compuation_integer, " is ", factorial(factorial_compuation_integer))
# print catalan computation
print("catalan value of ", catalan_computation_integer, " is ", catalan(catalan_computation_integer))
# print greatest common divisor
print("greatest common divisor of ", first_number_for_greatest_common_divisor, " and ",
      second_number_for_greatest_common_divisor, " is ",
      greatest_common_divisor(first_number_for_greatest_common_divisor, second_number_for_greatest_common_divisor))
