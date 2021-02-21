# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 18:18:53 2021

@author: hello
"""

class Variable : 
    
    def __init__(self, value):
        self.value = value
        self.domain = [1,2,3,4,5,6,7,8,9]
        self.assigned = False
        if self.value != 0 :
            self.assigned = True
            
            