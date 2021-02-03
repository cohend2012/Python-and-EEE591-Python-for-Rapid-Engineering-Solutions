#############################################
#   By: Dan Cohen                           #
#   Date: 1/30/2021                         #
#   ASU ID# 1204831845                      #
#   For class: Rapid Prototyping in python  #
#   Prof. Dr. Steve Millman                 #
#   netlist_stub                            #
# solve resister network with voltage and/or current sources #
#############################################




################################################################################
# Created on Fri Aug 24 13:36:53 2018                                          #
#                                                                              #
# @author: olhartin@asu.edu; updates by sdm                                    #
#                                                                              #
# Outline solve resister network with voltage and/or current sources           #
################################################################################

import numpy as np                     # needed for arrays
from numpy.linalg import solve         # needed for matrices
from read_netlist import read_netlist  # supplied function to read the netlist
import comp_constants as COMP          # needed for the common constants

# this is the list structure that we'll use to hold components:
# [ Type, Name, i, j, Value ]

################################################################################
# How large a matrix is needed for netlist? This could have been calculated    #
# at the same time as the netlist was read in but we'll do it here             #
# Input:                                                                       #
#   netlist: list of component lists                                           #
# Outputs:                                                                     #
#   node_cnt: number of nodes in the netlist                                   #
#   volt_cnt: number of voltage sources in the netlist                         #
################################################################################

def get_dimensions(netlist):           # pass in the netlist

    ### EXTRA STUFF HERE!
    max_node_number = 0   # finding max node number start with 0
    max_voltage_count = 0  # finding the max voltage, starting with 0
    for index in range(len(netlist)):  # run over the index of length of the netlist input
        # print(netlist[index][0])

        if ((netlist[index][2] or netlist[index][3]) > max_node_number):
            # if it grader then the max node number we want to reset it

            if netlist[index][3] > netlist[index][2]:  # if the Res value is grader of 3 then 2 then use 3

                max_node_number = netlist[index][3]

            elif netlist[index][3] < netlist[index][2]: # if the Res value is grader of 2 then 3 then use 2

                max_node_number = netlist[index][2]

            elif netlist[index][2] == netlist[index][3]: # if they enter in a weird net lis that should not happen
                print("weird both are the same, what should we do now")

        if netlist[index][0] == 1:  # counting how many times we see a voltage
            max_voltage_count = max_voltage_count + 1

    #print(type(max_node_number),type(max_voltage_count))
    node_cnt = int(max_node_number)  # make sure node count is an int
    volt_cnt = int(max_voltage_count)  # make sure the voltage count is an int



    #print(' Nodes ', node_cnt, ' Voltage sources ', volt_cnt)  # printing the counts
    # return the node count and voltage count
    return node_cnt,volt_cnt

################################################################################
# Function to stamp the components into the netlist                            #
# Input:                                                                       #
#   y_add:    the admittance matrix                                            #
#   netlist:  list of component lists                                          #
#   currents: the matrix of currents                                           #
#   node_cnt: the number of nodes in the netlist                               #
# Outputs:                                                                     #
#   node_cnt: the number of rows in the admittance matrix                      #
################################################################################

def stamper(y_add,netlist,currents,num_nodes):
    # return the total number of rows in the matrix for
    # error checking purposes
    # add 1 for each voltage source...

    for comp in netlist:                  # for each component...
        #print(' comp ', comp)            # which one are we handling...

        # extract the i,j and fill in the matrix...
        # subtract 1 since node 0 is GND and it isn't included in the matrix

        #print("i: ",i,"j: ",j)

        if ( comp[COMP.TYPE] == COMP.R ):
            i = comp[COMP.I] - 1
            j = comp[COMP.J] - 1
            # a resistor
            if (i >= 0):                            #  dont if it less then 0 if not on the diagonal
                y_add[i,i] += 1.0/comp[COMP.VAL]    # take the value of the comp and place on diga
            if(j >= 0):
                y_add[j,j] += 1.0 / comp[COMP.VAL]  # if j is bigger then 0 then place 1/comp value in j,j
            if(i>=0 and j>=0):
                y_add[i,j] += -1.0 / comp[COMP.VAL]  # i an j are bigger then 0 load -1/comp value in i,j
                y_add[j,i] += -1.0 / comp[COMP.VAL]  # i an j are bigger then 0 load -1/comp value in j,i
                #print("y_add",y_add)
            #EXTRA STUFF HERE!
        elif (comp[COMP.TYPE] == COMP.VS):  # a voltage source?
            i = comp[COMP.I] - 1
            j = comp[COMP.J] - 1
            #if (i > num_nodes and j > num_nodes):
            num_nodes = num_nodes + 1  # we found a voltage source and thus we should add it to the tot count
            M = num_nodes
            #print("num_nodes",num_nodes)
            #print("i",i,"j",j)
            #y_add[M-1,:] = 0.0
            #y_add[:, M-1] = 0.0

            if(i>=0): # if i is bigger then 0 then proceed

                y_add[M-1, i] = 1.0  # placing a 1 in the the bottom left row
                y_add[i, M-1] = 1.0  # placing a 1 in the the far right col

            #:

            if(j>=0):

                y_add[M-1, j] = -1.0  # placing a -1 in the bottom left row
                y_add[j, M-1] = -1.0  # placing a -1 in the the far right col


            currents[M-1] = comp[COMP.VAL] # loading in the comp values

            voltage[M-1] = 0  # set location to 0 for voltage
           # print("y_add", y_add)
            #print("currents", currents)
            #print("voltage",voltage)

        elif (comp[COMP.TYPE] == COMP.IS):  # a current source?
            i = comp[COMP.I] - 1
            j = comp[COMP.J] - 1


            #print("Is C S: ",comp[COMP.TYPE] == COMP.IS)
            if (i>=0): # if i is bigger then 0
                if comp[COMP.VAL] >= 0:  # if the value of the current is bigger the 0

                    currents[i] -= 1.0*comp[COMP.VAL]  # load the neg comp value

                    #print("currents",currents)
                else:
                    currents[i] += 1.0 * comp[COMP.VAL]  # otherwise load the pos one in

            if(j>=0): # if j is bigger then 0

                if comp[COMP.VAL] >=0:
                    currents[j] += 1.0 * comp[COMP.VAL]  # if the comp value is bigger then 0  then load into current
                else:

                    currents[j] -= 1.0 * comp[COMP.VAL]  # if the comp value is less then 0  then load into current
                    #print("currents", currents)



    #print(y_add)
    #currents[3]=abs(currents[3])
    node_cnt = num_nodes
    return node_cnt  # should be same as number of rows!

################################################################################
# Start the main program now...                                                #
################################################################################

# Read the netlist!
netlist = read_netlist()


# Print the netlist so we can verify we've read it correctly





#print("we found the max node number to be",max_node_number)
#print("\n")

#EXTRA STUFF HERE!
node_cnt,volt_cnt = get_dimensions(netlist) # get dims

print("adding the count",node_cnt+volt_cnt)

total_count = node_cnt+volt_cnt

y_add = np.zeros((total_count ,total_count),dtype=float)

currents = np.zeros(total_count,dtype=float)

voltage = np.zeros(total_count,dtype=float)
# create matrix of right size
node_cnt = stamper(y_add,netlist,currents,node_cnt)


# use linalg to solve system, need to find
# find the left hand side and right hand side

voltage = np.linalg.solve(y_add, currents)

print(voltage)