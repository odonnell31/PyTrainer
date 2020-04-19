# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 11:46:26 2020

@author: ODsLaptop
"""

# import libraries
import numpy as np
import pandas as pd
from collections import Counter

# import helper functions/scripts
import pyTrainer_helper_functions_v1 as hfs

# function to create a dataframe for each press workout
def create_press_workouts(startingWeight: int, calories = 2500):
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
                              hfs.round_five((startingWeight+45)/2), 6], index = workout1.columns),
                   pd.Series(['press workout 1', 0, 'warm-up 3',
                              hfs.round_five(startingWeight*.9), 3], index = workout1.columns)]
    
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
            workout['weight'][1] = hfs.round_five(lastworkout['weight'][3] * .7)
            workout['weight'][2] = hfs.round_five(lastworkout['weight'][3] * .88)
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
            workout['weight'][1] = hfs.round_five(lastworkout['weight'][3] * .7)
            workout['weight'][2] = hfs.round_five(lastworkout['weight'][3] * .88)
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