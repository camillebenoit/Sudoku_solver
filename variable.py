# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 18:18:53 2021

@author: hello
"""

class Variable : 
    
    def __init__(self, value, i, j):
        self.value = value
        self.domain = [1,2,3,4,5,6,7,8,9]
        self.assigned = False
        #si ce n'est pas 0 alors ça veut dire que la variable est déjà assignée
        if self.value != 0 :
            self.assigned = True
        self.position = [i,j]
        
        
    def DefSquareBoundaries(self):
        #retourne la liste des lignes et des colonnes dans lesquelles se trouve la variable
        nb_line = self.position[0]
        nb_col = self.position[1]
        i = 0
        j = 0
        while True :
            if nb_line in [i, i+1, i+2] :
                horizontalBoudnaries = [i, i+1, i+2]
                break
            i+=3
        while True :
            if nb_col in [j, j+1, j+2] :
                verticalBoudnaries = [j, j+1, j+2]
                break
            j+=3
        return horizontalBoudnaries, verticalBoudnaries
            
            
