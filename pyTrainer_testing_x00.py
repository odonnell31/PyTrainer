# -*- coding: utf-8 -*-
"""
Created on Tue Apr 7 21:17:47 2020

@author: ODsLaptop

@title: PyTrainer
"""

# Purpose/Mission:
"""
    Use python to quickly create a custom training plan for athletes with:
        1. Specific barbell strength goals
        2. Specific endurance goals
        3. Access to a barbell, plates, jump rope, and pull-up bar
        4. Desire for accountability and planned workouts
        5. Expectations to improve strength, endurance, and strenth-to-weight ratio
"""

# Format of scipt:
"""
    This scipt is under construction. But, the final product may look like:
        
        1. Athlete enters their desired exercises/activites for improvement,
        current fitness level, and rough estimate of daily caloric intake
        
        2. Script exports a detailed 90-day training plan in an acionable,
        digestable, specific, and flexible format
"""

# Areas for research and improvement:
"""
    1. As of now, this script loosely follows Starting Strength methodology
    (by Mark Rippatoe) for strength increase. For example, 5 sets of 5 reps (5x5)
    is used very frequently for barbell exercises. 3x3s are also used often.
    But, there may be better set and rep counts to increase strength!
    And, how many seconds between sets is best, etc.
    Research needed.
    
    2. Based on caloric intake, how many lbs/week can an athlete realistically
    expect to gain on press, squat, bench press, deadlift, and other major lifts?
    Research or training plan testers needed.
    
    3. This script will start by creating only the first exercise in the workout.
    For example, if the day's workout is based around the squat then
    the script (as currently constructed) will output all the sets, reps, and weights
    to squat during that workout. But obviously, the athlete
    will want to continue the workout. What exercises are best to do next,
    in what order, super-setted? etc.
    
    4. Best warm-ups and stretches for each workout? Jump rope, run, other?
    
    5. This idea, and subsequent workout plan, was designed with myself in mind.
    But, what else do people want in their workout plan?
"""

# Current status
"""
helper functions:
    
    1. round_five
    2. insert_row
    3. barbell_calc
    
main functions:
    
    1. create_press_workouts
        - returns a list of dataframes. Each dataframe is a workout that can
        then plugged into the final calendar.

"""

# import libraries
import numpy as np
import pandas as pd
from collections import Counter

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

# function to create a dataframe for each press workout
def create_press_workouts(startingWeight: int):
    # empty list for press workout dataframes
    press_workouts = []
    
    # create the dataframes' default columns
    set_columns = ['workout title', 'set number', 'label', 'weight', 'reps']
    
    # first, create workout 1
    # then, duplicate workout 1 to create the next x number of workouts
    
    # create workout 1 skeleton dataframe
    workout1 = pd.DataFrame(columns = set_columns)
    
    # add workout 1 warm-up sets
    # warm-up set 1 will be with an empty bar
    # warm-up set 2 will be halfway between your working weight and an empty bar
    # warm-up set 3 will be 90% of your working weight
    warmup_sets = [pd.Series(['press workout 1', 0, 'warm-up 1', 45, 8],
                             index = workout1.columns),
                   pd.Series(['press workout 1', 0, 'warm-up 2',
                              round_five((startingWeight+45)/2), 6], index = workout1.columns),
                   pd.Series(['press workout 1', 0, 'warm-up 3',
                              round_five(startingWeight*.9), 3], index = workout1.columns)]
    
    # append warmup_sets to workout 1
    workout1 = workout1.append(warmup_sets, ignore_index = True)
    
    # add work sets to workout 1
    # the work sets will be 5 sets of 5 reps (5x5)
    work_sets = [pd.Series(['press workout 1', 1, 'work set 1', startingWeight, 5], index = workout1.columns),
                 pd.Series(['press workout 1', 2, 'work set 2', startingWeight, 5], index = workout1.columns),
                 pd.Series(['press workout 1', 3, 'work set 3', startingWeight, 5], index = workout1.columns),
                 pd.Series(['press workout 1', 4, 'work set 4', startingWeight, 5], index = workout1.columns),
                 pd.Series(['press workout 1', 5, 'work set 5', startingWeight, 5], index = workout1.columns)]

    # append work_sets to workout 1
    workout1 = workout1.append(work_sets, ignore_index = True)
    
    # add heavy sets to workout 1
    # the heavy sets will either be a 3x3 or ~3x2
    heavy_sets = [pd.Series(['press workout 1', 6, 'heavy set 1', startingWeight+5, 3], index = workout1.columns),
                 pd.Series(['press workout 1', 7, 'heavy set 2', startingWeight+5, 3], index = workout1.columns),
                 pd.Series(['press workout 1', 8, 'heavy set 3', startingWeight+5, 3], index = workout1.columns)]

    # append heavy_sets to workout 1
    workout1 = workout1.append(heavy_sets, ignore_index = True)
    
    # append workout 1 to press_workouts list
    press_workouts.append(workout1)

    # now, add workouts 2 through 10
    
    # copy workout1
    lastworkout = workout1.copy()
    # set current working weight
    currentWeight = startingWeight
    # set next working weight
    nextWeight = currentWeight + 5
    
    for w in range(2,11):
        # create copy of last weeks workout
        workout = lastworkout.copy()
        
        # create next workout
        # increase by ~2.5 lbs/week
        if (w % 2)  == 0:
            workout['weight'][1] = round_five(lastworkout['weight'][3] * .7)
            workout['weight'][2] = round_five(lastworkout['weight'][3] * .88)
            workout['weight'][3] = lastworkout['weight'][3]
            workout['weight'][4] = lastworkout['weight'][3]
            workout['weight'][5] = lastworkout['weight'][3] + 5
            workout['weight'][6] = lastworkout['weight'][3] + 5
            workout['weight'][7] = lastworkout['weight'][3] + 5
            workout['weight'][8] = lastworkout['weight'][3] + 10
            workout['weight'][9] = lastworkout['weight'][3] + 10
            workout['weight'][10] = lastworkout['weight'][3] + 10
            workout['reps'][9] = 3
            workout['reps'][10] = 3
            workout['workout title'] = 'press workout ' + str(w)
            
        else:
            workout['weight'][1] = round_five(lastworkout['weight'][3] * .7)
            workout['weight'][2] = round_five(lastworkout['weight'][3] * .88)
            workout['weight'][3] = lastworkout['weight'][3] + 5
            workout['weight'][4] = lastworkout['weight'][3] + 5
            workout['weight'][5] = lastworkout['weight'][3] + 5
            workout['weight'][6] = lastworkout['weight'][3] + 5
            workout['weight'][7] = lastworkout['weight'][3] + 5
            workout['weight'][8] = lastworkout['weight'][3] + 10
            workout['weight'][9] = lastworkout['weight'][3] + 15
            workout['weight'][10] = lastworkout['weight'][3] + 15
            workout['reps'][9] = 2
            workout['reps'][10] = 2
            workout['workout title'] = 'press workout ' + str(w)
        
        # reset last workout
        lastworkout = workout.copy()
        
        # append workout to press_workouts list
        press_workouts.append(workout)
        
    # add random optional next exercises
        # NOT YET
        
    # create a counter for number of reps at each set

    return press_workouts

# fuction to finally build workout plan into calendar
def create_workout_plan(list_of_exercises, list_of_starting_weights, caloric_intake = None):
    print("under construction...")
    

# counter function for number of reps of each workout
def total_progress():
    print("under construction...")
    
### TESTING
    
press = create_press_workouts(100)
print("press workout 4, if starting a a comfortable 100 lbs 5 reps")
print("=======")
print(press[3])
    
