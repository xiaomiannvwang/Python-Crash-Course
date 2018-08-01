#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 16:13:58 2018

@author: sk
"""

import matplotlib.pyplot as plt
from random_walk import RandomWalk

#keep making new walks, as long as the program is active
"""
rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
"""
"""
#script
keep_running = input("make a Walk? (y/n): ")
while keep_running == 'y':
    rw = RandomWalk(50000)
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)
    
    #coloring the points
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, edgecolor='none', s=15)

    #emphasize the first and last points
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolor='none', s=100)
    
    #clear the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    #set the size of the figure
    plt.figure(figsize=(10,6))
    
    plt.show()
    
    keep_running = input("make another Walk? (y/n): ")
    if keep_running == 'n':
        break
"""

#exercise
keep_running = input("make a Walk? (y/n): ")
while keep_running == 'y':
    rw = RandomWalk(5000)
    rw.fill_walk()
    plt.plot(rw.x_values, rw.y_values)
    
    #coloring the points
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, c=(0.4, 0.8, 0.5))

    #emphasize the first and last points
    plt.scatter(0, 0, c='red')
    plt.plot(rw.x_values[-1], rw.y_values[-1], c='blue')
    
    #clear the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    #set the size of the figure
    plt.figure(figsize=(10,6))
    
    plt.show()
    
    keep_running = input("make another Walk? (y/n): ")
    if keep_running == 'n':
        break






