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
