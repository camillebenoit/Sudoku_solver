import time
import click

from Sudoku import sudoku as sk
from Sudoku import methods as mtd

# python -m Sudoku -dh False -d hard
@click.command()
@click.option("--sudoku_number", "-sn", "sudoku_number", type=int, default=1)
@click.option("--difficulty", "-d", "difficulty", type=str, default="beginners")
@click.option("--use_ac3", "-ac3", "use_ac3", type=bool, default=True)
@click.option("--deg_h", "-dh", "deg_h", type=bool, default=True)
def main(
        sudoku_number: int,
        difficulty: str,
        use_ac3: bool,
        deg_h: bool
) -> None:
    path_to_file = "Sudoku/sudoku_" + difficulty + "/sudoku" + str(sudoku_number) + ".ss"
    sudoku = sk.Sudoku(path_to_file)

    print("Initial sudoku\n")
    print(sudoku)
    start_time = time.time()
    initial_assignment = mtd.init_assigment(sudoku)

    sudoku_final = mtd.backtracking_search(sudoku, initial_assignment, use_ac3, deg_h)
    print(sudoku_final)

    print(f"\nElapsed time : {time.time() - start_time}")


if __name__ == "__main__":
    main()
