# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 18:18:53 2021

@author: hello
"""

import typing as t


class Variable:

    def __init__(self, value: int, i: int, j: int):
        self.value = value
        self.domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assigned = False
        # si ce n'est pas 0 alors ça veut dire que la variable est déjà assignée
        if self.value != 0:
            self.domain = []
            self.assigned = True
        self.position = [i, j]

    def def_square_boundaries(self) -> t.Tuple[t.List, t.List]:
        # retourne la liste des lignes et des colonnes dans lesquelles se trouve la variable
        nb_line = self.position[0]
        nb_col = self.position[1]
        i = 0
        j = 0
        while True:
            if nb_line in [i, i + 1, i + 2]:
                horizontal_boundaries = [i, i + 1, i + 2]
                break
            i += 3
        while True:
            if nb_col in [j, j + 1, j + 2]:
                vertical_boundaries = [j, j + 1, j + 2]
                break
            j += 3
        return horizontal_boundaries, vertical_boundaries

    def get_neighbours_position(self) -> t.List:
        nb_line = self.position[0]
        nb_col = self.position[1]
        neighbours_position_list = []

        for k in range(9):
            if k != nb_line:
                neighbours_position_list.append([k, nb_col])
            if k != nb_col:
                neighbours_position_list.append([nb_line, k])

        horizontal_boundaries, vertical_boundaries = self.def_square_boundaries()

        for i in horizontal_boundaries:
            for j in vertical_boundaries:
                if [i, j] not in neighbours_position_list:
                    neighbours_position_list.append([i, j])
        neighbours_position_list.remove([nb_line, nb_col])

        return neighbours_position_list

    def __eq__(self, other):
        # on compare les positions des variables
        return self.position == other.position

    def get_domain(self):
        return self.domain
