import sudoku as sk
import variable as vr

number_sudoku = "1"
level = "beginers"
path_to_file = "sudoku_" + level + "\sudoku" + number_sudoku +".ss"
sud = sk.Sudoku(path_to_file)
print(sud)

var1 = vr.Variable(2,2,5)
print(var1.DefSquareBoundaries())