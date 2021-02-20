#   By: Dan Cohen                           #
#   Data: 1/16/2021                         #
#   ASU ID# 1204831845                      #
#   For class: Rapid Prototyping in python  #
#   Prof. Dr. Steve Millman                 #
#   hw1_canon.py                            #
#                                           #
#############################################

import numpy as np  # import numpy

GRAVITY = -9.81  # gravity for earth m/sec^2
PI = np.pi  # pi as constant
CANON_HEIGHT=1 # canon height is 1 m
THETA_SWEEP = [PI/24,(PI/24)*2,(PI/24)*3,(PI/24)*4,(PI/24)*5,(PI/24)*6,(PI/24)*7,(PI/24)*8,(PI/24)*9,(PI/24)*10,(PI/24)*11]
# THETA_SWEEP is each angle the cannon can be placed as
SIN_SWEEP = list(map(np.sin, THETA_SWEEP))  # finding the sin of each angle
BAD_INDEX = -1                # if there is a bad index where we should not shoot the person make it -1
possible_landing_spots = [] # start list for the possible landing spots
possible_ceiling_heights = [] # start list for the possible ceiling heights
time_to_ground = []          # start list for each time to hit the ground
time_to_ceiling = []          # start list for the time to hit the ceiling
max_index = 0                # starting the max index at 0
max_ceiling_index = 0         # starting the max ceiling index at 0
max_landing = 0.0            # starting the max landing location at 0 meters
max_ceiling = 0.0             # starting the max ceiling location at 0 meters
bad_count = 0                # if we count and all of the spots are bad then we should tell the user


ceiling_height = float(input("enter height: ")) - CANON_HEIGHT  # asking the user for the height of the ceiling in meters
arena_length = float(input("enter length: ")) # asking the user for the length of the arena in meters
initial_velocity = float(input("enter velocity: ")) # asking the user for the initial velocity in meters per sec



# Decompose vel into the x and y dir


farthest_spot_less_then_area_length = 0 # assuming the farthest sport is 0

for index in range(len(SIN_SWEEP)): # look at each index at each possible  launch angle

    time_to_ground.append(-1.0 * (2.0 * initial_velocity * np.sin(THETA_SWEEP[index])) / GRAVITY) # find the time to hit the ground

    possible_landing_spots.append(initial_velocity * time_to_ground[index] * np.cos(THETA_SWEEP[index])) # find posible landing spots

    time_to_ceiling.append(-1.0 * initial_velocity * np.sin(THETA_SWEEP[index]) / GRAVITY) # find the time to hit the celing

    possible_ceiling_heights.append(initial_velocity * time_to_ceiling[index] * np.sin(THETA_SWEEP[index]) - ((0.5) * -1.0 * GRAVITY * time_to_ceiling[index] * time_to_ceiling[index]))
    # finding the max height that each angle will create when launched

    bad_flag = False # initialize flag to determine if a bad landing spot was found or if the user was going to get the celing

    if float(possible_landing_spots[index]) <= float(arena_length) and float(possible_ceiling_heights[index]) <= ceiling_height: # if the landing spot is less then the arena length

        if(max_landing <= possible_landing_spots[index] and max_ceiling<=possible_ceiling_heights[index]): # if the max landing is less the curent reset the value

            max_index = index # setting max index to the current index
            max_landing = possible_landing_spots[index]  # setting the max landing to the current one
    else:

        bad_flag = True



    if(bad_flag == True):
        possible_landing_spots[index] = BAD_INDEX  # if the cannon will shoot to far to should indicate it is a bad index
        bad_count = bad_count + 1 # add to the count that a bad location occurred


if bad_count >= len(SIN_SWEEP): # If we should not shoot cannon at all
    print("")
    print("Requirements can't be met. Please reduce initial velocity.")

else: # when we can use the cannon, print the results
    print("")
    print("optimal settings:")
    print("anlge: ",np.round(THETA_SWEEP[max_index],3)," radians") # show the max angle in radians
    print("landing: ", np.round(max_landing,1)," m")               # show the landing sport in meters
    print("max height: ", np.round(float(possible_ceiling_heights[max_index]), 1), " m") # show the max height in meters
    print("")
    print("possible landing spots:") # display the landing spots
    print(np.round(possible_landing_spots, 1))