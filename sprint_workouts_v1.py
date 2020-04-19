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

# function to create a dataframe for each sprint workout
def create_sprint_workouts(distance):
    # empty list for press workout dataframes
    sprint_workouts = []
    
    # create the dataframes' default columns
    set_columns = ['workout title', 'set number', 'label', 'length (meters)', 'timed']
    
    # first, create workout 1
    # then, duplicate workout 1 to create the next x number of workouts
    
    # create workout 1 skeleton dataframe
    workout1 = pd.DataFrame(columns = set_columns)
    
    # add workout 1 warm-up sets
    # warm-up sets will be with a few short sprints
    warmup_sets = [pd.Series(['sprint workout 1', 0, 'warm-up 1', 50, 'untimed'],
                             index = workout1.columns),
                   pd.Series(['sprint workout 1', 0, 'warm-up 2', 100, 'untimed'],
                             index = workout1.columns),
                   pd.Series(['sprint workout 1', 0, 'warm-up 3', 200, 'untimed'],
                             index = workout1.columns)]
    
    # append warmup_sets to workout 1
    workout1 = workout1.append(warmup_sets, ignore_index = True)
    
    # add work sets to workout 1
    work_sets = [pd.Series(['sprint workout 1', 1, 'work set 1', distance, 'timed'], index = workout1.columns),
                 pd.Series(['sprint workout 1', 1, 'rest', '120 seconds', 'rest'], index = workout1.columns),
                 pd.Series(['sprint workout 1', 2, 'work set 2', distance, 'timed'], index = workout1.columns),
                 pd.Series(['sprint workout 1', 2, 'rest', '120 seconds', 'rest'], index = workout1.columns),
                 pd.Series(['sprint workout 1', 3, 'work set 3', distance, 'timed'], index = workout1.columns),
                 pd.Series(['sprint workout 1', 3, 'rest', '120 seconds', 'rest'], index = workout1.columns),
                 pd.Series(['sprint workout 1', 4, 'work set 4', distance, 'timed'], index = workout1.columns),
                 pd.Series(['sprint workout 1', 4, 'rest', '120 seconds', 'rest'], index = workout1.columns),
                 pd.Series(['sprint workout 1', 5, 'work set 5', distance, 'timed'], index = workout1.columns)]

    # append work_sets to workout 1
    workout1 = workout1.append(work_sets, ignore_index = True)
    
    # add heavy sets to workout 1
    # the heavy sets will either be a 3x3 or ~3x2
    final_sets = [pd.Series(['sprint workout 1', 6, 'final set 1', distance/2, 'untimed'], index = workout1.columns),
                  pd.Series(['sprint workout 1', 6, 'rest', '45 seconds', 'rest'], index = workout1.columns),
                  pd.Series(['sprint workout 1', 7, 'final set 2', distance/2, 'untimed'], index = workout1.columns),
                  pd.Series(['sprint workout 1', 7, 'rest', '45 seconds', 'rest'], index = workout1.columns),
                  pd.Series(['sprint workout 1', 8, 'final set 3', distance/2, 'untimed'], index = workout1.columns)]

    # append heavy_sets to workout 1
    workout1 = workout1.append(final_sets, ignore_index = True)
    
    # append workout 1 to press_workouts list
    sprint_workouts.append(workout1)

    # now, add workouts 2 through 10
    # copy workout1
    lastworkout = workout1.copy()
    # set current working weight
    currentDistance = distance
    
    for w in range(2,11):
        # create copy of last weeks workout
        workout = lastworkout.copy()
        
        # create next workout
        # increase by ~2.5 lbs/week
        if (w % 2)  == 0:
            workout['workout title'] = 'sprint workout ' + str(w)
            
        else:
            workout['workout title'] = 'sprint workout ' + str(w)
        
        # reset last workout
        lastworkout = workout.copy()
        
        # append workout to press_workouts list
        sprint_workouts.append(workout)
        
    # add random optional next exercises
        # NOT YET
        
    # create a counter for number of reps at each set

    return sprint_workouts

    
# FUNCTIONAL TESTING
"""
sprint_workouts_test = create_sprint_workouts(200)
print(sprint_workouts_test[0])
print("=============")
print(sprint_workouts_test[3])
"""