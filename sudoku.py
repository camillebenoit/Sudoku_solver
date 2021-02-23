# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import typing as t

from Sudoku import variable as vr
import random as rd


class Sudoku:

    def __init__(self, path_to_file: str):
        #la liste de 81 variables
        self.values = []
        #on va créer la liste des variables déjà assignées via un dictionnaire qui aura comme clé la variable assigné 
        #et item sa valeur
        self.assignement = dict()
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
                    self.assignement[value] = int(element)
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

    def backtracking_search(self):
        return self.recursive_backtracking(self.initial_assignement)

    def recursive_backtracking(self):
        if len(self.assignement) == 81 :
            return self.assignement
        
        #j'imagine que c'est là que doit apparaître MRV et degree heuristic ?
        variable = rd.choice([var for var in self.values if var.assigned == False])
        
        position = variable.position
        domain = variable.domain
        
        #et sur le for least constraining value ?
        for value in domain :
            if self.all_constraint(position, value) :
                #les contraintes sont respectées
                #on met à jour
                self.assignement[variable] = value
                self.value[position[0]][position[1]].assigned = True
                self.value[position[0]][position[1]].value = value
                self.value[position[0]][position[1]].domain = []
                #AC3
                self.AC3()
                #on applique la récursivité
                result = self.recursive_backtracking()
                if result != [] :
                    return result
                #on remet tout comme avant
                del self.assignement[variable]
                self.value[position[0]][position[1]].assigned = False
                self.value[position[0]][position[1]].value = 0
                self.value[position[0]][position[1]].domain = domain
        return []


    def AC3(self):
        queue = []

        for i in range(9):
            for j in range(9):
                var = self.get_variable(i, j)
                neighbours = self.get_neighbours_variable(var)
                for neighbour in neighbours :
                    queue.append([var, neighbour])
        
        #queue = [(self.values[i], neighbours[i]) for i in range(81)]
        #queue = [(xi, xj) for xi in self.values for xj in neighbours]
        while queue:
            [xi, xj] = queue.pop(0)
            if self.remove_inconsistent_values(xi, xj):
                neighbours = self.get_neighbours_variable(xi)
                for xk in neighbours :
                    queue.append([xk, xi])

    def remove_inconsistent_values(self, xi: vr, xj: vr):
        position_xi = xi.position
        i = position_xi[0]
        j = position_xi[1]
        removed = False
        for value in set(xi.domain) :
            if len(set(xj.domain)-set([value]) == 0) :
                self.values[i][j].domain.remove(value)
                removed = True
        return removed


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
        for var in self.unassigned_variables:
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
                if neighbour.assigned == False and value in neighbour.get_domain():
                    count += 1
            if count < min_count:
                min_count = count
                best_value = value
        return best_value


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
        v = Variable(0,nb_line,nb_col)
        horizontal_boundaries, vertical_boundaries = v.def_square_boundaries()
        for i in horizontal_boundaries:
            for j in vertical_boundaries:
                if self.values[i][j].value == value and i != nb_line and j != nb_col:
                    return False
        return True


    def all_constraint(self, position, value) -> bool:
        # return true si les trois contraintes sont respectées, false sinon
        if self.horizontal_constraint(position, value) and self.vertical_constraint(position, value) and self.square_constraint(
                position, value):
            return True
        return False
