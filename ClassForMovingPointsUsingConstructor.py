#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 15:03:29 2018

@author: navneet
"""

#program for creating point using constructor, 
#constructor to initialize position of points,
#move function to move points to location
#reset to set it back to origin

import math

class Point:
    def __init__(self,x=0,y=0):
        'constructor is initialized here, constructor is called when object is created'
        self.move(x,y)
        
    def move(self,x,y):
        'move the points to a specific point'
        self.x = x
        self.y = y
    
    def reset(self):
        'reset the point to origin'
        self.move(0,0)
        
    def distance_points(self,other_points):
        'calculate the distance of points'
        return math.sqrt((self.x - other_points.x)**2 + (self.y - other_points.y)**2)
    
p1 = Point()

p2=Point(6,8)

print("Distance between points",p1.distance_points(p2))
    
    

