import variable as vr
import sudoku as sk

var1 = vr.Variable(2, 2, 5)
# print(var1.get_neighbours_position())


def main():
    number_sudoku = "1"
    level = "beginers"
    path_to_file = "sudoku_" + level + "\sudoku" + number_sudoku + ".ss"
    sud = sk.Sudoku(path_to_file)
    sud.backtracking_search()
    print(sud)


if __name__ == "__main__":
    main()
