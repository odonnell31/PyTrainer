# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 11:46:53 2020

@author: ODsLaptop
"""

# import libraries
import numpy as np
import pandas as pd
from collections import Counter

# import helper functions/scripts
import pyTrainer_helper_functions_v1 as hfs

# function to create a dataframe for each endurance workout
def create_endurance_workouts(milage):
    # empty list for press workout dataframes
    endurance_workouts = []
    
    # create the dataframes' default columns
    set_columns = ['workout title', 'set number', 'label', 'length (miles)', 'timed']
    
    # first, create workout 1
    # then, duplicate workout 1 to create the next x number of workouts
    
    # create workout 1 skeleton dataframe
    workout1 = pd.DataFrame(columns = set_columns)
    
    # add workout 1 warm-up sets
    # warm-up sets will be with a few short sprints
    work_sets = pd.Series(['endurance workout 1', 1, 'workout', str(milage)+" miles", 'timed'],
                           index = workout1.columns)
    
    # append warmup_sets to workout 1
    workout1 = workout1.append(work_sets, ignore_index = True)
    
    # add cool down to workout 1
    # the heavy sets will either be a 3x3 or ~3x2
    cool_down_sets = pd.Series(['endurance workout 1', 1, 'walk', str("%.2f" % round(milage/4, 2)) + " miles", 'untimed'],
                                index = workout1.columns)

    # append heavy_sets to workout 1
    workout1 = workout1.append(cool_down_sets, ignore_index = True)
    
    # append workout 1 to press_workouts list
    endurance_workouts.append(workout1)

    # now, add workouts 2 through 10
    # copy workout1
    lastworkout = workout1.copy()
    # set current working milage
    currentMilage = milage
    
    for w in range(2,11):
        # create copy of last weeks workout
        workout = lastworkout.copy()
        
        # create next workout
        # increase by ~2.5 lbs/week
        if (w % 2)  == 0:
            workout['workout title'] = 'endurance workout ' + str(w)
            
        else:
            workout['workout title'] = 'endurance workout ' + str(w)
        
        # reset last workout
        lastworkout = workout.copy()
        
        # append workout to press_workouts list
        endurance_workouts.append(workout)
        
    # add random optional next exercises
        # NOT YET
        
    # create a counter for number of reps at each set
    return endurance_workouts

    
    
# FUNCTIONAL TESTING
"""
endurance_workouts_test = create_endurance_workouts(2)
print(endurance_workouts_test[0])
print("=============")
print(endurance_workouts_test[3])
"""