# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import variable as vr

class Sudoku :
    
    def __init__(self, path_to_file):
        self.values = []
        #extraction des variables depuis le document ss
        sudoku_file = open(path_to_file, "r")
        i = 0
        for line in sudoku_file : 
            the_line = []
            string_line = list(line)
            if string_line[0] == "-" :
                continue
            j = 0
            for element in string_line :
                if element == "." :
                    #on modélise une variable à trouver par un 0
                    value = vr.Variable(0, i,j)
                    the_line.append(value)
                    j+=1
                elif element in ["1","2","3","4","5","6","7","8","9"]:
                    value = vr.Variable(int(element),i,j)
                    the_line.append(value)
                    j += 1
            i += 1
            self.values.append(the_line)
            
    def __str__(self) :
        #il s'agit simplement d'afficher le sudoku de façon propre dans la console
        total_str = ""
        for i in range(9):
            line = ""
            for j in range(9):
                line += str(self.values[i][j].value)
                if j in [2,5] :
                    line += "|"
            total_str += (line + "\n")
            if i in [2,5] :
                total_str += ("-----------" + "\n")    
        return total_str
    
    def GetVariable(self,i,j) :
        return self.values[i][j]
    
    def Backtracking(self): 
        pass
    
    def AC3(self):
        pass
    
    def MRV(self): 
        pass
    
    def DegreeHeuristic(self):
        pass
    
    def LeastConstrainingValue(self):
        pass
    
    def HorizontalConstraint(self, variable):
        #return true si la contrainte est respectée, false sinon
        nb_line = variable.position[0]
        nb_col = variable.position[1]
        for j in range(9):
            if self.values[nb_line][j].value == variable.value and j != nb_col:
                return False
        return True
    
    def VerticalConstraint(self, variable):
        #return true si la contrainte est respectée, false sinon
        nb_line = variable.position[0]
        nb_col = variable.position[1]
        for i in range(9):
            if self.values[i][nb_col].value == variable.value and i != nb_line:
                return False
        return True
        pass
    
    def SquareConstraint(self, variable):
        #return true si la contrainte est respectée, false sinon
        nb_line = variable.position[0]
        nb_col = variable.position[1]
        #on cherche le carré dans lequel se situe la variable
        horitontalBoudnaries, verticalBoundaries = variable.DefSquareBoundaries()
        for i in horitontalBoudnaries :
            for j in verticalBoundaries :
                if self.values[i][j].value == variable.value and i != nb_line and j != nb_col :
                    return False
        return True
    
    def AllConstraint(self, variable):
        #return true si les trois contraintes sont respectées, false sinon
        if self.HorizontalConstraint(variable) and self.VerticalConstraint(variable) and self.SquareConstraint(variable) :
            return True
        return False
    
    
        