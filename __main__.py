import time

import variable as vr
import sudoku as sk
import methods as m

var1 = vr.Variable(2, 2, 5)


#@clickcommand

def main():
   
    level = "beginners"
    number_sudoku = "1"
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
