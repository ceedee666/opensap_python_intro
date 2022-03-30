from sudoku import Sudoku

puzzle = Sudoku(3).difficulty(0.7)
puzzle.show()

solution = puzzle.solve()
solution.show()