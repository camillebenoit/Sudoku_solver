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
        #on va créer la liste des variables déjà assignées via un dictionnaire qui aura comme clé la position (tuple) 
        #et item sa valeur
        self.initial_assignement = dict()
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
                    self.initial_assignement[(i,j)] = int(element)
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

    def backtracking(self):
        return self.recursive_backtracking(self.initial_assignement)

    def recursive_backtracking(self, assignement):
        pass

    def AC3(self):
        variables = []
        neighbours = []

        for i in range(9):
            for j in range(9):
                var = self.get_variable(i, j)
                variables.append(var)
                neighbours.append(self.get_neighbours_variable(var))
        #sinon queue = [(variables[i], neighbours[i]) for i in range(len(variables))]
        queue = [(xi, xj) for xi in variables for xj in neighbours]

        while queue:
            (xi, xj) = queue.pop(0)
            if self.remove_inconsistent_values(xi, xj):
                neighbours = self.get_neighbours_variable(xi)
                for xk in neighbours :
                    queue.append((xk, xi))

    def remove_inconsistent_values(self, xi: vr, xj: vr):
        pass

    def MRV(self) -> t.List[int]:
        #choisir la variable avec le plus petit nombre de valeurs légales
        #c'est-à-dire la variable avec le plus petit domaine
        smallest_domain = 9
        variable_position = []
        for i in range(9):
            for j in range(9):
                var = self.get_variable(i, j)
                if var.value == 0:
                    domain_length = len(var.get_domain())
                    if domain_length < smallest_domain:
                        smallest_domain = domain_length
                        variable_position = var.position
        return variable_position

    def degree_heuristic(self):
        #choisir la variable avec le plus grand nombre de contraintes sur les variables restantes
        #c'est à dire la variable qui a le plus grand nombre de voisins non assignés
        max_nb_of_constraints = 0
        variable_position = []
        for i in range(9):
            for j in range(9):
                var = self.get_variable(i, j)
                if var.value == 0:
                    count_constraints = 0
                    neighbours = self.get_neighbours_variable(var)
                    for neighbour in neighbours : 
                        if neighbour.assigned == False :
                            count_constraints += 1
                    if count_constraints > max_nb_of_constraints:
                        max_nb_of_constraints = count_constraints
                        variable_position = var.position
        return variable_position


    def least_constraining_value(self, variable: vr) -> int:
        #pour une variable donnée choisir la valeur la moins contraignante
        #c'est-à-dire la valeur qui est la moins présente dans les domaines de ses voisins
        neighbours = self.get_neighbours_variable(variable)
        variable_domain = variable.get_domain()
        min_count = 9
        best_value = variable_domain[0]
        for value in variable_domain:
            count = 0
            for neighbour in neighbours:
                if value in neighbour.get_domain():
                    count += 1
            if count < min_count:
                min_count = count
                best_value = value
        return best_value

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
