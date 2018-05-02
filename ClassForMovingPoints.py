#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 14:48:48 2018

@author: navneet
"""

#classes and object in object oriented programming in python
#create a class of point, reset the points to origin, move point to another point and calculate the distance
import math

class Point:
    def reset(self):
        self.x = 0
        self.y = 0
    
    def move(self,x,y):
        self.x = x
        self.y = y
    
    def calculate_distance(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
    
p1 = Point()
p2 = Point()

p1.reset()
p2.move(8,6)

print("Distance between point",p2.calculate_distance(p1))

p1.move(1,2)
print("Distance after moving point ",p1.calculate_distance(p2))
    