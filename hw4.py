#############################################
#   By: Dan Cohen                           #
#   Data: 2/7/2021                         #
#   ASU ID# 1204831845                      #
#   For class: Rapid Prototyping in python  #
#   Prof. Dr. Steve Millman                 #
#   hw4.py                                  #
#   Wealth Calculator over 70 years         #
#                                           #
#############################################
# #start of code


import PySimpleGUI as sg  # get the higher-level GUI package
import numpy as np  # get numpy
# import matplotlib                # needed for plotting the results
# matplotlib.use("TkAgg")
import matplotlib.pyplot as plt  # get matplotlib for plotting

# Constants

YEARS = 70  # number of years we want to live to and have money

ANALYSIS = 10  # how many times would we like to run our calcs
PERCENT_CONVERTER = 100  # used during calcs when we divided by 100

# define the field names and their indices
FN_MEAN_RETURN_PERCENT = 'Mean Return (%)'
FN_STD_DEV_RETURN_PERCENT = 'Std Dev Return (%)'
FN_YEARLY_CONTRIBUTION = 'Yearly Contribution ($)'
FN_NO_OF_YEARS_OF_CONTRIBUTION = 'No. of Years of Contribution'
FN_NO_OF_YEARS_TO_RETIREMENT = 'No. of Years to Retirement'
FN_ANNUAL_SPEND_IN_RETIREMENT = 'Annual Spend in Retirement'
FN_RETIREMENT = 'CALCULATING ...'

# placing our names in a list
FIELD_NAMES = [FN_MEAN_RETURN_PERCENT, FN_STD_DEV_RETURN_PERCENT, FN_YEARLY_CONTRIBUTION, \
               FN_NO_OF_YEARS_OF_CONTRIBUTION, FN_NO_OF_YEARS_TO_RETIREMENT, FN_ANNUAL_SPEND_IN_RETIREMENT]

F_MEAN_RETURN_PERCENT = 0  # index for Mean Return (%)
F_STD_DEV_RETURN_PERCENT = 1  # index for Std Dev Return (%)
F_YEARLY_CONTRIBUTION = 2  # index for Yearly Contribution ($)
F_NO_OF_YEARS_OF_CONTRIBUTION = 3  # index for No. of Years of Contribution
F_NO_OF_YEARS_TO_RETIREMENT = 4  # index for No. of Years to Retirement
F_ANNUAL_SPEND_IN_RETIREMENT = 5  # index for Annual Spend in Retirement
F_RETIREMENT = 6  # index for Retirement

NUM_FIELDS = 6  # how many fields there are
# need things in more than one place

B_CALCULATE = 'Calculate'  # the calculate button
B_QUIT = 'Quit'  # the quit button

wealth_store_matrix = np.zeros((YEARS, ANALYSIS), dtype=float)  # create our store matrix


###############################################################################################################
# Function and call wealth_calculation(window, entries)                                                       #
# Inputs:                                                                                                     #
#    window  - the top-level widget                                                                           #
#    entries - the dictionary of entry fields                                                                 #
# Output:                                                                                                     #
#    only output is to screen (for debug) and the GUI and the avg of our analysis at the specified time       #
###############################################################################################################

def wealth_calculation(window, entries):
    # period (monthly) rate:

    y_in = float(entries[FN_YEARLY_CONTRIBUTION])  # get the user yearly contribution

    y_out = float(entries[FN_ANNUAL_SPEND_IN_RETIREMENT])  # get the user spending after retirment

    r = float(entries[FN_MEAN_RETURN_PERCENT])  # get the users percent you get over the years

    total_contribution_years = float(entries[FN_NO_OF_YEARS_OF_CONTRIBUTION])  # how many years did they want contribute

    total_years_to_retirement = float(entries[FN_NO_OF_YEARS_TO_RETIREMENT])  # how many years untill you retirment
    sigma = float(entries[FN_STD_DEV_RETURN_PERCENT])  # what is the standard devation of the mean return percent

    plt.figure()  # create our single fiugre we want to use
    for index_analysis in range(ANALYSIS):
        current_val = 0  # start with a value of $0 for our calculations
        last_index = 0  # assume the last index is 0, when it is not
        noise = (sigma / PERCENT_CONVERTER) * np.random.randn(YEARS)  # calculate the noise array
        for year in range(YEARS):  # for reach year from 0-70 run the calcs and store it

            if (total_contribution_years - 1 > year):  # phase 1
                current_val = current_val * (
                            1 + (r / PERCENT_CONVERTER) + noise[year]) + y_in  # adding money and investing
            # print("adding money with stocks and income", "The year is ",year)

            elif (total_years_to_retirement - 1 > year):  # phase 2
                current_val = current_val * (
                            1 + (r / PERCENT_CONVERTER) + noise[year])  # not adding money but still investing
            # print("adding money via just stocks","The year is ",year)

            else:  # phase 3

                current_val = current_val * (
                            1 + (r / PERCENT_CONVERTER) + noise[year]) - y_out  # not working need to take money out
                # print("need to take money out but stocks are still active","The year is ",year)

            # finding out if this is the last year we should record
            if (current_val >= 0):  # as long as our investments are in the green
                wealth_store_matrix[year, index_analysis] = current_val
                last_index = year
            else:
                # cant invest any money if we lose it all
                break  # end this analysis
                # when it is below 0

        plt.plot(range(last_index + 1), wealth_store_matrix[0:last_index + 1, index_analysis], '-x')  # plot
        plt.title('Wealth Over 70 Year $ ')  # add lable
        plt.ylabel('$ Wealth')  # y-axis how much $ we have made
        plt.xlabel('Years')  # how many years
        plt.grid(True)  # help with grids
    plt.show()  # show after for loop to plot all curves on the same graph

    # total_sum = np.sum(np.sum(wealth_store_matrix[0:41], axis=0))  # calc total sum

    # print("total matrix",wealth_store_matrix[(total_years_to_retirement+1),:])
    # print("sum of each run",np.sum(wealth_store_matrix[(total_years_to_retirement+1),:], axis=0))

    # print("tot years",total_years_to_retirement,total_years_to_retirement.type)

    total_sum = np.sum(wealth_store_matrix[(int(total_years_to_retirement) + 1), :],
                       axis=0)  # find the sum at the ret year
    # print("avg",total_sum/ANALYSIS)

    # plt.plot(range(YEARS), recording_wealth)
    # plt.ylabel('$')
    # plt.xlabel('Years')
    # plt.show()

    # monthly = ("%8.2f" % monthly).strip()

    # put the values into the GUI and print to the screen

    # print("Money: %f" % float(total_sum/ANALYSIS))
    return (total_sum / ANALYSIS)  # return the avg of our invests at that year


################################################################################
# Function and call update_layout(NUM_FIELDS2,FIELD_NAMES2,money)              #
# Input:                                                                       #
#    NUM_FIELDS  - The number of fields on the gui                             #
#    FIELD_NAMES - The field names                                             #
# Output:                                                                      #
#    window - gui output window                                                #
################################################################################

def update_layout(NUM_FIELDS, FIELD_NAMES, money):
    # period (monthly) rate:
    # print("in the update function")
    sg.set_options(font=('Helvetica', 20))  # set up the font and size
    if (money == 0):
        calc_tot = 'Enter info then double click Calculate...'  # start up
    else:
        calc_tot = str(money)  # otherwise print how much money when you retire
        # print('calc total',calc_tot)

    # The layout is a list of lists
    # Each each entry in the top-level list is a row in the GUI
    # Each entry in the next-level lists is a widget in that row
    # Order is top to bottom, then left to right

    # need a fresh layout
    layout = []  # start with the empty list
    for index2 in range(NUM_FIELDS):  # for each of the fields to create
        layout.append([sg.Text(FIELD_NAMES[index2] + ': ', size=(30, 1)), \
                       sg.InputText(key=FIELD_NAMES[index2], size=(30, 1))])

        # print(FIELD_NAMES2[index2])
    layout.append([sg.Text(calc_tot, key='-OUTPUT-', size=(30, 1))])  # add on the output text box
    layout.append([sg.Button(B_CALCULATE), sg.Button(B_QUIT)])  # add on the buttons clac and quit
    # print(layout)
    # start the window manager
    window = sg.Window('70 Year Wealth Calculator', layout)
    event, values = window.read()
    # print("final Bal")
    return window


# first call for the update layer
window = update_layout(NUM_FIELDS, FIELD_NAMES, 0)

window.Refresh()  # refresh based
# Run the event loop
while True:

    event, values = window.read()
    # print("event",event,"values",values)
    if event == sg.WIN_CLOSED or event == B_QUIT:  # does the use want to quit ths program
        break
    if event == B_CALCULATE:  # does the user want to calculate the wealth
        # print("event", event, "values", values)
        money_avg = (wealth_calculation(window, values))  # calc wealth
        money_avg_with_format = 'Wealth at retirement: ${:,}'.format(int(money_avg))  # save string we want to display
        # print(money_avg_with_format)

        window['-OUTPUT-'].update(str(money_avg_with_format))  # update the list of lists

        window.Refresh()  # refresh
    else:
        print("Not Good")  # if something really unexpected happens

window.close()  # close gui
