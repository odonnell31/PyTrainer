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
    work_sets = [pd.Series(['endurance workout 1', 1, 'workout', milage, 'timed'])]
    
    # append warmup_sets to workout 1
    workout1 = workout1.append(work_sets, ignore_index = True)
    
    # add cool down to workout 1
    # the heavy sets will either be a 3x3 or ~3x2
    cool_down_sets = [pd.Series(['endurance workout 1', 1, 'walk',
                                 float(milage/3), 'untimed'], index = workout1.columns)]

    # append heavy_sets to workout 1
    workout1 = workout1.append(cool_down_sets, ignore_index = True)
    
    # append workout 1 to press_workouts list
    endurance_workouts.append(workout1)

    # now, add workouts 2 through 10
    
    
    """
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
            workout['workout title'] = 'bench press workout ' + str(w)
            
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
            workout['workout title'] = 'bench press workout ' + str(w)
        
        # reset last workout
        lastworkout = workout.copy()
        
        # append workout to press_workouts list
        bench_press_workouts.append(workout)
        
    # add random optional next exercises
        # NOT YET
        
    # create a counter for number of reps at each set

    return endurance_workouts
    """