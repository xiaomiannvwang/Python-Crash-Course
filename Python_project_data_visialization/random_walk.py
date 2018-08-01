#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 16:02:24 2018

@author: sk
"""

from random import choice

class RandomWalk():
    """ A class to generate ranodm walks"""
    
    def __init__(self, num_points = 5000):
        """initialize attributes of a walk"""
        self.num_points = num_points
        
        #all walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        """calculate all the points in the walk"""
        
        #keep taking steps until rhe walk reachs the designed length.
        while len(self.x_values) < self.num_points:
            """
            #decide which direction to go and how far to go in that direction.
            x_direction = choice([1, -1])
            x_distance = choice (range(0,9))
            x_step = x_direction*x_distance
            
            y_direction = choice([1, -1])
            y_distance = choice ([0, 1, 2, 3, 4])
            y_step = y_direction*y_distance
        
            """
            
            x_step = self.get_step()  #调用class内部函数
            y_step = self.get_step()
        
            #reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue
      
       
       
       
            #calculate the next x and y values.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)
    
    
    def get_step(self):
             #decide which direction to go and how far to go in that direction.
            self.direction = choice([1, -1])
            self.distance = choice (range(0,9))
            self.step = self.direction*self.distance
            
            return self.step
          