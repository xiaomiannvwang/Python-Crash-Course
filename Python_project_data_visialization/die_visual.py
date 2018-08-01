#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 17:24:10 2018

@author: sk
"""
from die import Die 
import pygal
#create a D6 die

die = Die()

#make some rolls and store them in a list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
    
    #analyze the results
    frequencies = []
    for value in range(1, die.num_sides+1):
        frequency = results.count(value)
        frequencies.append(frequency)
        
    #visualize the reults
    hist = pygal.Bar()
    
    hist.title = "Results od rolling D6 1000 Times"
    hist.x_labels = ['1', '2', '3', '4', '5', '6']
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"
    
    hist.add('D6', frequencies)
    hist.render_to_file('die_visual.svg')

