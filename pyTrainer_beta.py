# -*- coding: utf-8 -*-
"""
Created on Tue Apr 7 21:17:47 2020

@author: ODsLaptop

@title: PyTrainer
"""

# Purpose/Mission:
"""
    Use python to allow athletes to quickly create custom training plans. 
    
    The first training plan (in beta) will be for athletes with:
        1. Barbell strength goals
        2. Endurance goals
        3. Access to a barbell, plates, jump rope, and a stop watch
        4. Desire for accountability and planned workouts
        5. Realistic expectations to improve strength, endurance, and strenth-to-weight ratio
"""

# Format of scipt:
"""
    This scipt is under construction. But, the final product for the first
    training plan (beta) may look like this:
        
        1. Athlete enters their desired barbell and endruance exercises
        for improvement, their current fitness level for each exercise,
        and a rough estimate of daily caloric intake
        
        2. Athlete then clicks run, and is given a detailed 10-week training plan
        in MS Excel that is acionable, digestable, and specific.
        (Version 2 will make export more flexible, in case a workout is missed)
"""

# Areas for research and improvement:
"""

    1. As of now, this beta script loosely follows Starting Strength methodology
    (by Mark Rippatoe) for strength increase. For example, 5 sets of 5 reps at
    the same wiehgt (5x5) is used very frequently for barbell exercises. 3x3's
    are also used often.
    But, there may be better set and rep counts to increase strength!
    Also, how many seconds between sets is best? Does is vary?
    How much variance is needed among workouts?
    Research needed.
    
    2. If following a plan with 5x5's and 3x3's, how does the script determine
    the starting weight for strength exercises in this plan? For example,
    if the first workout calls for a squat 5x5, how do you determine this weight
    since a substantial part of this plan is based on that starting weight.
    Do you ask for an 8-rep max and that's your starting 5x5 weight?
    Research! Or, functional testing among authors needed.
    
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
    
    5. This idea, and beta workout plan, was designed with myself in mind.
    But, what else do people want in their workout plan?
    
    6. What should next workout plans be?
    For example, a 10-week plan for marathon running from scratch?
    A 10-week plan for an athlete's first spring triathlon? etc.
"""

# Current status
"""
to-do:

    3. create excel write dict to excel tabs
    4. create function to create "top-sheet", a calendar for workouts with links
    5. update formatting of excel writer (a tad)
    6. update workout generators based on cited research!!
        6.1 too many warmup reps..
    7. create function to take inputs from google sheet? or somewhere else
    8. beta complete! test on friends
    9. break into classes? maybe.

helper functions:
    
    1. round_five
    2. insert_row
    3. barbell_calc
    
main functions:
    
    1. create_workout_plan
        - creates a dictionary with a key for each day
        and a value of each workout

"""

# import libraries
import numpy as np
import pandas as pd
from collections import Counter

# import scipts/functions
import pyTrainer_helper_functions_v1 as hfs
import squat_workouts_v1 as squat_workouts
import deadlift_workouts_v1 as deadlift_workouts
import press_workouts_v1 as press_workouts
import bench_press_workouts_v1 as bench_press_workouts
import sprint_workouts_v1 as sprint_workouts
import endurance_workouts_v1 as endurance_workouts

# function to intake an athlete's list of exercises/goals, starting weights,
# and average caloric intake
def athlete_input():
    print("take users inputs with pop-up menu's..")

# fuction to build workout plan into calendar
def create_workout_plan(list_of_exercises = None, list_of_starting_weights = None, caloric_intake = None):
    
    # first, create a list of all days for the calendar
    from datetime import date, timedelta, datetime
    list_of_dates = []
    
    for i in range(1,72):
        tmrw = datetime.today() + timedelta(days = 1)
        time_delta = timedelta(days = i)
        list_of_dates.append("workout-"+str((tmrw + time_delta).strftime('%Y-%m-%d')))
    
    # next, create a list of all workouts
    list_of_workouts = []
    
    # populate all workouts with default values
    for w in range(1,72):
        rest_df = pd.DataFrame(["rest, recover!"], columns = ['workout title'])
        list_of_workouts.append(rest_df)
        
    # enter exercise 1 into list_of_workouts
    exercise_1_workouts = list_of_exercises[0](list_of_starting_weights[0])
    for x in range(0,10):
       list_of_workouts[(x*7)] = exercise_1_workouts[x]
       
    # enter exercise 2 into list_of_workouts
    exercise_2_workouts = list_of_exercises[1](list_of_starting_weights[1])
    for x in range(0,10):
       list_of_workouts[(x*7+1)] = exercise_2_workouts[x]
       
    # enter exercise 3 into list_of_workouts
    exercise_3_workouts = list_of_exercises[2](list_of_starting_weights[2])
    for x in range(0,10):
       list_of_workouts[(x*7+2)] = exercise_3_workouts[x] 
       
    # enter exercise 4 into list_of_workouts
    exercise_4_workouts = list_of_exercises[3](list_of_starting_weights[3])
    for x in range(0,10):
       list_of_workouts[(x*7+3)] = exercise_4_workouts[x]
       
    # enter exercise 5 into list_of_workouts
    exercise_5_workouts = list_of_exercises[4](list_of_starting_weights[4])
    for x in range(0,10):
       list_of_workouts[(x*7+4)] = exercise_5_workouts[x]
       
    # enter exercise 6 into list_of_workouts
    exercise_6_workouts = list_of_exercises[5](list_of_starting_weights[5])
    for x in range(0,10):
       list_of_workouts[(x*7+5)] = exercise_6_workouts[x]
    
    # create dictionary of all workouts by day!
    # using dictionary comprehension 
    # to convert lists to dictionary 
    workouts_dict = {list_of_dates[i]: list_of_workouts[i] for i in range(len(list_of_dates))} 
    
    # convet dictionary to a dataframe
    workouts_df = pd.DataFrame.from_dict(workouts_dict, orient = 'index')
    
    writer = pd.ExcelWriter('pandas_simple_05.xlsx', engine='xlsxwriter')
    
    for i in list_of_workouts:
        df = i
        tabname = i['workout title'][0]
        df.to_excel(writer, sheet_name=tabname)
    writer.save()
    
    """
    writer = pd.ExcelWriter('pandas_simple_01.xlsx', engine='xlsxwriter')
    
    for i in workouts_df:
        #print(workouts_df[i])
        workouts_df[i].to_excel(writer, sheet_name=str(i))
        writer.save()
        

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

    for i in list_of_dates:
        writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
        tabname = str(i)
        df_name = str(i)
        df = workouts_dict[df_name]
        df.to_excel(writer, sheet_name=tabname)
        writer.save()

    #workouts_dict['2020-04-21'].to_excel(writer, sheet_name='Sheet1')
    #workouts_dict['2020-04-22'].to_excel(writer, sheet_name='Sheet2')
    # Close the Pandas Excel writer and output the Excel file.
    #writer.save()
    """
    return list_of_workouts
    

# function to
# 1. count total number of reps, sets, and weights for each exercise
# 2. visualize your total progress over time
# 3. compare your progress to other pyTrainer athletes
def total_progress():
    print("under construction...")
    
    # Graphs of progress!
    
    # compared to rest of pyTrainer athletes
    
### TESTING
    
#press = press_workouts.create_press_workouts(100)
#print("press workout 4, if starting a a comfortable 100 lbs 5 reps")
#print("=======")
#print(press[3])

# test 3
test_dict = create_workout_plan([press_workouts.create_press_workouts,
                                 squat_workouts.create_squat_workouts,
                                 deadlift_workouts.create_deadlift_workouts,
                                 bench_press_workouts.create_bench_press_workouts,
                                 sprint_workouts.create_sprint_workouts,
                                 endurance_workouts.create_endurance_workouts],
                                [105, 165, 215, 95, 200, 2])

# test 4
#hfs.barbell_calc(220)
