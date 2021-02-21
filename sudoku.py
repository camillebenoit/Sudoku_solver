# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import variable as vr

class Sudoku :
    
    def __init__(self, path_to_file):
        self.values = []
        sudoku_file = open(path_to_file, "r")
        for line in sudoku_file : 
            the_line = []
            string_line = list(line)
            if string_line[0] == "-" :
                continue
            for element in string_line :
                if element == "." :
                    value = vr.Variable(0)
                    the_line.append(value)
                if element in ["1","2","3","4","5","6","7","8","9"]:
                    value = vr.Variable(int(element))
                    the_line.append(value)
            self.values.append(the_line)
            
    def __str__(self) :
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
    
        