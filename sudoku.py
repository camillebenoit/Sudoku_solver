# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import typing as t

import variable as vr

class Sudoku:

    def __init__(self, path_to_file: str):
        # la liste de 81 variables
        self.values = []
        # on va créer la liste des variables déjà assignées via un dictionnaire qui aura comme clé la variable assigné
        # et item sa valeur
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

    def get_neighbours_variable(self, variable: vr) -> t.List:
        neighbours_position = variable.get_neighbours_position()
        neighbours = []
        for position in neighbours_position:
            neighbours.append(self.get_variable(position[0], position[1]))
        return neighbours

    def horizontal_constraint(self, position, value) -> bool:
        # return true si la contrainte est respectée, false sinon
        nb_line = position[0]
        nb_col = position[1]
        for j in range(9):
            if self.values[nb_line][j].value == value and j != nb_col:
                return False
        return True

    def vertical_constraint(self, position, value) -> bool:
        # return true si la contrainte est respectée, false sinon
        nb_line = position[0]
        nb_col = position[1]
        for i in range(9):
            if self.values[i][nb_col].value == value and i != nb_line:
                return False
        return True

    def square_constraint(self, position, value) -> bool:
        # return true si la contrainte est respectée, false sinon
        nb_line = position[0]
        nb_col = position[1]
        # on cherche le carré dans lequel se situe la variable
        v = vr.Variable(0, nb_line, nb_col)
        horizontal_boundaries, vertical_boundaries = v.def_square_boundaries()
        for i in horizontal_boundaries:
            for j in vertical_boundaries:
                if self.values[i][j].value == value and i != nb_line and j != nb_col:
                    return False
        return True

    def all_constraint(self, position, value) -> bool:
        # return true si les trois contraintes sont respectées, false sinon
        if self.horizontal_constraint(position, value) and self.vertical_constraint(position,
                                                                                    value) and self.square_constraint(
                position, value):
            return True
        return False
