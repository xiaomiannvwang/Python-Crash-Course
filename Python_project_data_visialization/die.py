#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 17:19:53 2018

@author: sk
"""

from random import randint

class Die():
    """a class represents a single die"""
    
    def __init__(self, num_sides=6):
        """assume a six-sided die"""
        self.num_sides = 6
        
    def roll(self):
        """return a random value between 1 ans numbers of sides"""
        return randint(1, self.num_sides)
    
    