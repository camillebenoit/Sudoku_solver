from Sudoku import variable as vr
from Sudoku import sudoku as sk

var1 = vr.Variable(2, 2, 5)
# print(var1.get_neighbours_position())


def main():
    number_sudoku = "1"
    level = "beginers"
    path_to_file = "Sudoku/sudoku_" + level + "/sudoku" + number_sudoku + ".ss"
    sud = sk.Sudoku(path_to_file)
    print(sud)
    sud.backtracking_search()
    print(sud)


if __name__ == "__main__":
    main()
