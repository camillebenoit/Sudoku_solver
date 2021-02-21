# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import typing as t

from Sudoku import variable as vr


class Sudoku:

    def __init__(self, path_to_file: str):
        self.values = []
        # extraction des variables depuis le document ss
        sudoku_file = open(path_to_file, "r")
        i = 0
        for line in sudoku_file:
            the_line = []
            string_line = list(line)
            if string_line[0] == "-":
                continue
            j = 0
            for element in string_line:
                if element == ".":
                    # on modélise une variable à trouver par un 0
                    value = vr.Variable(0, i, j)
                    the_line.append(value)
                    j += 1
                elif element in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    value = vr.Variable(int(element), i, j)
                    the_line.append(value)
                    j += 1
            i += 1
            self.values.append(the_line)

    def __str__(self):
        # il s'agit simplement d'afficher le sudoku de façon propre dans la console
        total_str = ""
        for i in range(9):
            line = ""
            for j in range(9):
                line += str(self.values[i][j].value)
                if j in [2, 5]:
                    line += "|"
            total_str += (line + "\n")
            if i in [2, 5]:
                total_str += ("-----------" + "\n")
        return total_str

    def get_variable(self, i, j):
        return self.values[i][j]

    def backtracking(self):
        pass

    def AC3(self):
        pass

    def MRV(self) -> t.List[int]:
        smallest_domain = 9
        variable_position = []

        for i in range(9):
            for j in range(9):
                if self.values[i][j].value == 0:
                    domain_length = len(self.values[i][j].get_domain())
                    if domain_length < smallest_domain:
                        smallest_domain = domain_length
                        variable_position = self.values[i][j].position
        return variable_position

    def degree_heuristic(self):
        pass

    def least_constraining_value(self):
        pass

    def horizontal_constraint(self, variable: vr) -> bool:
        # return true si la contrainte est respectée, false sinon
        nb_line = variable.position[0]
        nb_col = variable.position[1]
        for j in range(9):
            if self.values[nb_line][j].value == variable.value and j != nb_col:
                return False
        return True

    def vertical_constraint(self, variable: vr) -> bool:
        # return true si la contrainte est respectée, false sinon
        nb_line = variable.position[0]
        nb_col = variable.position[1]
        for i in range(9):
            if self.values[i][nb_col].value == variable.value and i != nb_line:
                return False
        return True
        pass

    def square_constraint(self, variable: vr) -> bool:
        # return true si la contrainte est respectée, false sinon
        nb_line = variable.position[0]
        nb_col = variable.position[1]
        # on cherche le carré dans lequel se situe la variable
        horizontal_boundaries, vertical_boundaries = variable.def_square_boundaries()
        for i in horizontal_boundaries:
            for j in vertical_boundaries:
                if self.values[i][j].value == variable.value and i != nb_line and j != nb_col:
                    return False
        return True

    def all_constraint(self, variable: vr) -> bool:
        # return true si les trois contraintes sont respectées, false sinon
        if self.horizontal_constraint(variable) and self.vertical_constraint(variable) and self.square_constraint(
                variable):
            return True
        return False

    def get_neighbours_variable(self, variable):
        neighbours_position = variable.get_neighbours_variable()
        neighbours = []
        for position in neighbours_position:
            neighbours.append(self.get_variable(position[0], position[1]))
        return neighbours
