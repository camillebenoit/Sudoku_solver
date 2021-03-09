import time
import click

from Sudoku import sudoku as sk
from Sudoku import methods as mtd


@click.command()
@click.option("--sudoku_number", "-sn", "sudoku_number", type=int, default=1)
@click.option("--difficulty", "-d", "difficulty", type=str, default="beginners")
def main(
        sudoku_number: int,
        difficulty: str
) -> None:
    path_to_file = "Sudoku/sudoku_" + difficulty + "/sudoku" + str(sudoku_number) + ".ss"
    sudoku = sk.Sudoku(path_to_file)

    print("Initial sudoku\n")
    print(sudoku)
    start_time = time.time()
    initial_assignment = mtd.init_assigment(sudoku)

    sudoku_final = mtd.backtracking_search(sudoku, initial_assignment)
    print(sudoku_final)

    print(f"\nElapsed time : {time.time() - start_time}")


if __name__ == "__main__":
    main()
