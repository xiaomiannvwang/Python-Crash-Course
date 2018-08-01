#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 17:55:32 2018

@author: sk
"""

from die import Die 
import pygal

#create two D6 die
die_1 = Die()
die_2 = Die()

#make some rolls and store them in a list
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
    #analyze the results
    frequencies = []
    max_result = die_1.num_sides +die_2.num_sides
    for value in range(2, max_result+1):
        frequency = results.count(value)
        frequencies.append(frequency)
        
    #visualize the reults
    hist = pygal.Bar()
    
    hist.title = "Results od rolling two D6 dice 1000 Times"
    hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"
    
    hist.add('D6+D6', frequencies)
    hist.render_to_file('dice_visual.svg')
