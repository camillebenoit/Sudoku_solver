# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 17:51:20 2021

@author: hello
"""

import typing as t
from Sudoku import sudoku as sk
from Sudoku import variable as vr


def init_assigment(sudoku: sk) -> t.Dict:
    assignment = {}

    for i in range(9):
        for j in range(9):
            if sudoku.values[i][j].value != 0:
                assignment[(i, j)] = sudoku.values[i][j].value

    return assignment


def backtracking_search(sudoku: sk, initial_assignment: t.Dict, use_ac3: bool, deg_h: bool) -> sk:
    assignment_final = recursive_backtracking(sudoku, initial_assignment, use_ac3, deg_h)

    for pos in assignment_final.keys():
        i = pos[0]
        j = pos[1]
        sudoku.values[i][j].value = assignment_final.get(pos)

    return sudoku


def recursive_backtracking(sudoku: sk, assignment: t.Dict, use_ac3: bool, deg_h: bool) -> t.Dict:
    if len(assignment) == 81:
        print("Sudoku solved !\n")
        return assignment

    positions = MRV(sudoku)

    if deg_h:
        if len(positions) > 1:
            # si plusieurs variables sont choisies via le MRV on les départage avec degree heuristic
            position = degree_heuristic(sudoku, positions)
        else:
            position = positions[0]
    else:
        position = positions[0]

    variable = sudoku.get_variable(position[0], position[1])

    domain = least_constraining_value(sudoku, variable)

    for value in domain:
        if sudoku.all_constraint(position, value):
            # les contraintes sont respectées
            # on met à jour assignement
            assignment[(position[0], position[1])] = value
            assign(sudoku, position, value)

            # AC3
            if use_ac3:
                AC3(sudoku)

            # on applique la récursivité
            result = recursive_backtracking(sudoku, assignment, use_ac3, deg_h)
            if result != {}:
                return result

            # on remet tout comme avant
            del assignment[(position[0], position[1])]
            unassign(sudoku, position, domain)

    return {}


def assign(sudoku: sk, position: t.List, value: int) -> None:
    sudoku.values[position[0]][position[1]].assigned = True
    sudoku.values[position[0]][position[1]].value = value
    sudoku.values[position[0]][position[1]].domain = []


def unassign(sudoku: sk, position: t.List, domain: t.List) -> None:
    sudoku.values[position[0]][position[1]].assigned = False
    sudoku.values[position[0]][position[1]].value = 0
    sudoku.values[position[0]][position[1]].domain = domain


def AC3(sudoku: sk) -> None:
    queue = []

    # on remplit queue
    for i in range(9):
        for j in range(9):
            var = sudoku.get_variable(i, j)
            if var.value == 0:
                neighbours = sudoku.get_neighbours(var)
                for neighbour in neighbours:
                    # if [var, neighbour] not in queue or [neighbour, var] not in queue:
                    queue.append([var, neighbour])

    while len(queue):
        [xi, xj] = queue.pop()
        if remove_inconsistent_values(sudoku, xi, xj):
            neighbours = sudoku.get_neighbours(xi)
            for xk in neighbours:
                # if [xk, xi] not in queue or [xi, xk] not in queue:
                queue.append([xk, xi])


def remove_inconsistent_values(sudoku, xi, xj) -> bool:
    position_xi = xi.position

    xi_domain = xi.domain
    xj_domain = xj.domain

    i = position_xi[0]
    j = position_xi[1]

    remove = False
    for value in xi_domain:
        if len(xj_domain) > 0:
            if not any([is_different(value, poss) for poss in xj_domain]):
                sudoku.values[i][j].domain.remove(value)
                remove = True

    return remove


def is_different(var1: int, var2: int) -> bool:
    return var1 != var2


def MRV(sudoku: sk):
    # choisir la variable avec le plus petit nombre de valeurs légales
    # c'est-à-dire la variable avec le plus petit domaine
    smallest_domain = 10
    variable_position = []

    for i in range(9):
        for j in range(9):
            var = sudoku.get_variable(i, j)
            if var.value == 0:
                domain_length = len(var.get_domain())
                if domain_length <= smallest_domain:
                    if domain_length == smallest_domain:
                        variable_position.append(var.position)
                    else:
                        smallest_domain = domain_length
                        variable_position = [var.position]

    return variable_position


def degree_heuristic(sudoku: sk, positions: t.List) -> t.List:
    # choisir la variable avec le plus grand nombre de contraintes sur les variables restantes
    # c'est à dire la variable qui a le plus grand nombre de voisins non assignés
    max_nb_of_constraints = -1
    variable_position = []

    for position in positions:
        i = position[0]
        j = position[1]
        var = sudoku.get_variable(i, j)
        neighbours = sudoku.get_neighbours(var)

        count_constraints = len(neighbours)

        if count_constraints > max_nb_of_constraints:
            max_nb_of_constraints = count_constraints
            variable_position = [i, j]

    return variable_position


def least_constraining_value(sudoku: sk, variable: vr) -> t.List:
    # pour une variable donnée choisir la valeur la moins contraignante
    # c'est-à-dire la valeur qui est la moins présente dans les domaines de ses voisins
    # on va retourner une liste ordonnée des valeurs à tester
    neighbours = sudoku.get_neighbours(variable)
    variable_domain = variable.get_domain()
    ordered_values = []
    constraints_count = {}

    # on associe à chaque valeur possible le nombre de voisins qu'elle constraint
    for value in variable_domain:
        count = 0
        for neighbour in neighbours:
            neighbour_domain = neighbour.get_domain()
            if value in neighbour_domain:
                count += 1
        constraints_count[value] = count

    # on trie le dictionnaire et le transforme en liste de tuple
    sorted_dict = sorted(constraints_count.items(), key=lambda x: x[1])

    # on crée la liste finale des valeurs à tester
    for i in range(len(sorted_dict)):
        ordered_values.append(sorted_dict[i][0])

    return ordered_values
