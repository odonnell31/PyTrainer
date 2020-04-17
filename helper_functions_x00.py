# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 23:24:02 2020

@author: ODsLaptop

helper functions for the pyTrainer app
"""

# function to round any number to closest multiple of 5
# (we will assume the athlete has plates necessary for 5lb increments)
def round_five(x, base=5):
    return base * round(x/base)

# function to insert a row into a dataframe at a given row number
def insert_row(row_number, df, row_value):
    start_upper = 0
    end_upper = row_number
    start_lower = row_number
    end_lower = df.shape[0]
    upper_half = [*range(start_upper, end_upper, 1)]
    lower_half = [*range(start_lower, end_lower, 1)]
    lower_half = [x.__add__(1) for x in lower_half]
    index_ = upper_half + lower_half
    df.index = index_
    df.loc[row_number] = row_value
    df = df.sort_index()
    return df

# function to print the plates needed for any weight on a barbell
def barbell_calc(weight):
    print("Required plates for a", weight, "lb lift")
    # Subtract the weight of the bar
    # Divide by 2 for one side of barbell
    if weight >= 45:
        weight = (weight-45)/2.0

        Fourty_Five = int(weight)/45
        weight = weight - (45.0*Fourty_Five)

        Twenty_Five = int(weight)/25
        weight = weight - (25.0*Twenty_Five)

        Ten = int(weight)/10
        weight = weight - (10.0*Ten)
 
        Five = int(weight)/5
        weight = weight - (5.0*Five)

        Two_Point_Five = weight/2.5
        weight = weight - (2.5*Two_Point_Five)

        One_Point_Two_Five = weight/1.25
        weight = weight - (1.25*One_Point_Two_Five)

        print("On each side of barbell (in lb's):")
        print("45's:  ", Fourty_Five)
        print("25's:  ", Twenty_Five)
        print("10's:  ", Ten)
        print("5's:   ", Five)
        print("2.5's: ", int(Two_Point_Five))
        print("1.25's:", int(One_Point_Two_Five))
        
        if weight != 0.0:
            print("-----")
            print("there's some weight left over:", weight)
        
    elif weight > 0:
        print("less than 45 lbs, hit the dumbbells..")
    
    else:
        print("invalid weight..")