import time
import click

import variable as vr
import sudoku as sk
import methods as m


#@clickcommand

def main():

    number_sudoku = "1"
    level = "beginners"
    path_to_file = "sudoku_" + level + "/sudoku" + number_sudoku + ".ss"
    sudoku = sk.Sudoku(path_to_file)
    print("Sudoku initial\n")
    print(sudoku)
    start_time = time.time()
    initial_assignment =  m.init_assigment(sudoku)
    sudoku_final = m.backtracking_search(sudoku, initial_assignment)
    print(f"\nElapsed time : {time.time() - start_time}")
    print(sudoku_final)



if __name__ == "__main__":
    main()
