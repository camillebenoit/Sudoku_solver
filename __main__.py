import time
import click

import variable as vr
import sudoku as sk

var1 = vr.Variable(2, 2, 5)


#@clickcommand

def main():
    number_sudoku = "1"
    level = "beginners"
    path_to_file = "sudoku_" + level + "/sudoku" + number_sudoku + ".ss"
    sud = sk.Sudoku(path_to_file)

    print(sud)
    start_time = time.time()
    sud.backtracking_search()
    print(f"\nElapsed time : {time.time() - start_time}")
    print(sud)


if __name__ == "__main__":
    main()
