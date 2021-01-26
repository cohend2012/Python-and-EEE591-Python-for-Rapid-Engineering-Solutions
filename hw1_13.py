#   By: Dan Cohen                           #
#   Data: 1/16/2021                         #
#   hw1_13.py                               #
#############################################

# start of code

def factorial(n):
    if n==1: # if n is equal to 1
        return 1 # return 1
    else:
        return n*factorial(n-1) # otherwise return n time the factorial n -1

def catalan(n):
    if n==0: # if n is equal to equal to zero
        return 1 # return 1
    if n>0: # if n is greater then 1
        return ((4*n-2)/(n+1))*catalan(n-1)  # calculating the catalan number if n is not 0

def greatest_common_divisor(m,n):
    if n==0: # if n is equal to 0
        return m # return m
    if n>0: # if it greater then 0
        return greatest_common_divisor(n, m % n) # use greatest common divisor function

# gather user input for the factorial functio
factorial_compuation_integer=int(input("Enter an integer for a factorial computation: "))

# gather user input for the the catalin compuation
catalan_compuation_integer=float(input("Enter an integer for a Catalan number computation: "))
# gather input to the first integers for the GCD calculaiton
first_number_for_greatest_common_divisor=int(input("Enter the first of two integers for a GCD calculation: "))
# gather input to the second integers for the GCD calculaiton
second_number_for_greatest_common_divisor=int(input("Enter the second integer for the GCD calculation: "))
# print factorial compuation
print("factorial of ",factorial_compuation_integer," is ",factorial(factorial_compuation_integer))
# print catalan compuation
print("catalan value of ",catalan_compuation_integer," is ",catalan(catalan_compuation_integer))
# print greatest common divisor
print("greatest common divisor of ",first_number_for_greatest_common_divisor," and ", second_number_for_greatest_common_divisor," is ",greatest_common_divisor(first_number_for_greatest_common_divisor,second_number_for_greatest_common_divisor))