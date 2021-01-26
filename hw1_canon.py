#   By: Dan Cohen                           #
#   Data: 1/16/2021                         #
#   ASU ID# 1204831845                      #
#   For class: Rapid Prototyping in python  #
#   Prof. Dr. Steve Millman                 #
#   hw1_cannon.py                           #
#                                           #
#############################################

import numpy as np # import numpy

GRAVITY = -9.81 # gravity for earth m/sec^2
PI = np.pi # pi as constant
CANNON_HIGHT=1 # cannon hight is 1 m
THETA_SWEEP = [PI/24,(PI/24)*2,(PI/24)*3,(PI/24)*4,(PI/24)*5,(PI/24)*6,(PI/24)*7,(PI/24)*8,(PI/24)*9,(PI/24)*10,(PI/24)*11]
# THETA_SWEEP is each angle the cannon can be placed as
BAD_INDEX = -1                # if there is a bad index where we should not shoot the person make it -1
posssible_landing_spots = [] # start list for the possible landing spots
posssible_celing_hights = [] # start list for the posible celing hights
time_to_ground = []          # start list for each time to hit the ground
time_to_celing = []          # start list for the time to hit the celing
max_index = 0                # starting the max index at 0
max_celing_index = 0         # starting the max celing index at 0
max_landing = 0.0            # starting the max landing location at 0 meters
max_celing = 0.0             # starting the max celing location at 0 meters
bad_count = 0                # if we count and all of the spots are bad then we should tell the user


celing_height = float(input("enter height: ")) - CANNON_HIGHT# asking the user for the height of the celing
arena_length = float(input("enter length: ")) # asking the user for the length of the arena is
inital_velocity = float(input("enter velocity: ")) # asking the user for the inital velocity


#theta_sweep=np.linspace(PI/24,PI/2,12)
#print(THETA_SWEEP)

# Decompose vel into the x and y dir
sin_sweep =list(map(np.sin, THETA_SWEEP))  # finding the sin of each angle

farthest_spot_less_then_area_length = 0 # assumig the farthest sport is 0

for index in range(len(sin_sweep)): # look at each index at each posible launch angle
    #print("index = ",index)
    time_to_ground.append(-1.0*(2.0*inital_velocity*np.sin(THETA_SWEEP[index]))/GRAVITY) # find the time to hit the ground
    #print(index)
    posssible_landing_spots.append(inital_velocity*time_to_ground[index]*np.cos(THETA_SWEEP[index])) # find posible landing spots
    #print("landing spots before if: " ,posssible_landing_spots)
    time_to_celing.append(-1.0*inital_velocity*np.sin(THETA_SWEEP[index])/GRAVITY) # find the time to hit the celing

    posssible_celing_hights.append(inital_velocity*time_to_celing[index]*np.sin(THETA_SWEEP[index])-((0.5)*-1.0*GRAVITY*time_to_celing[index]*time_to_celing[index]))
    # finding the max hights that each anlge will create when lanched
    #print("posible celing hights ", posssible_celing_hights)
    bad_flag = False
    #print(float(posssible_landing_spots[index]) <= arena_length)
    if float(posssible_landing_spots[index]) <= float(arena_length) and float(posssible_celing_hights[index]) <= celing_height: # if the landing spot is less then the areana length

        if(max_landing <= posssible_landing_spots[index] and max_celing<=posssible_celing_hights[index]): # if the max landing is less the curent reset the value

            max_index = index # setting max index to the curent index
            max_landing = posssible_landing_spots[index] # setting the max landing to the curent one
    else:
        #print("landing spots before if: ", posssible_landing_spots[index], "areana length:  ",float(arena_length))
        bad_flag = True

    #if float(posssible_celing_hights[index]) <= celing_height :
        #print(float(posssible_celing_hights[index]))
        #if (max_celing<=posssible_celing_hights[index]): # if user will not hit the celing

            #max_celing_index = index # setting the max index to curent

           # max_celing = posssible_celing_hights[index] # setting the max celing hight to curent
    #else: # if they would hit the celing

        #print(float(posssible_celing_hights[index]))
        #bad_flag = True

    if(bad_flag == True):
        posssible_landing_spots[index] = BAD_INDEX  # if the cannon will shoot to far to should indicate it is a bad index
        bad_count = bad_count + 1 # add to the count that a bad location occurred

    #print(max_index,max_celing_index)


#time_to_ground = -1.0*(2.0*inital_velocity*list(map(np.sin, THETA_SWEEP)))/GRAVITY

#print(time_to_ground)

#print(max_index)

#print(max_celing)
#print(posssible_celing_hights)

#print(bad_count)
if bad_count >= len(sin_sweep): # If we should not shoot cannon at all

    print("Requirements can't be met. Please reduce initial velocity.")

else: # when we can use the cannon, print the results
    print("optimal settings:")
    print("anlge: ",np.round(THETA_SWEEP[max_index],3)," radians") # show the max anlge in radians
    print("landing: ", np.round(max_landing,1)," m")               # show the landing sport in meters
    print("max height: ",np.round(float(posssible_celing_hights[max_index]),1)) # show the max height
    print("possible landing spots:") # display the landing spots
    print(np.round(posssible_landing_spots,1))