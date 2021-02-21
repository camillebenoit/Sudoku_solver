from . import variable as vr
from . import sudoku as sk

number_sudoku = "1"
level = "beginers"
path_to_file = "sudoku_" + level + "\sudoku" + number_sudoku + ".ss"
sud = sk.Sudoku(path_to_file)
print(sud)

var1 = vr.Variable(2, 2, 5)
print(var1.DefSquareBoundaries())


def main():
    pass


if __name__ == "__main__":
    main()
