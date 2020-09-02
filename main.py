import time

sudoku = [[0, 0, 0, 0, 0, 0, 6, 1, 9],
          [0, 2, 3, 0, 9, 0, 0, 0, 0],
          [0, 0, 0, 1, 4, 0, 0, 2, 0],
          [0, 0, 9, 0, 0, 0, 0, 0, 0],
          [7, 0, 8, 0, 0, 3, 0, 0, 0],
          [0, 0, 0, 0, 0, 5, 3, 4, 0],
          [0, 0, 0, 0, 0, 0, 4, 6, 7],
          [8, 3, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 6, 1, 2, 0, 0, 0]]


# ------------------------------------------------------------ Functionality -----------------------------------------------------------------------------
def find_empty_space(sudoku):
    """return row and colom of next empty Space. Goes from top left to bottom right"""
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                return (i, j)
    # If the Sudoku is filled completly
    return None


def is_valid(sudoku, num, pos):
    """Checks if the number would be valid in the spot"""
    # Check row
    for i in range(len(sudoku[0])):
        # check all spaces in the row, except for the current, for duplicated numbers
        if sudoku[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(sudoku[0])):
        # check all spaces in the column, except for the current, for duplicated numbers
        if sudoku[i][pos[1]] == num and pos[0] != i:
            return False

    # Check in which box the current field is. Devide by 3 to get box 1 to 3. Later multiply box number by 3 to get the first space of box und loop through the next 3 Spaces
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    # Loop through all Spaces of the current box, except the current Space
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if sudoku[i][j] == num and (i, j) != pos:
                return False

    # if it isnt invalid, it is valid
    return True

# ------------------------------------------------------------ Main Functionality -------------------------------------------------------------------------


def solve_sudoku(sudoku):
    """Loops through the Board and fills in all numbers using a validation function and a Backtracking algorithm.
    First the algorithm tries to find a number that would be valid in the current Space. Then it calls itself to check the next empty Space.
    If all Spaces are filled, the algorithm stops. If it cant go  on, it goes back on Step and tries another number on the Space before"""

    empty = find_empty_space(sudoku)
    # Base | if sudoku is solved return True, so that the recursion stops
    if not empty:
        return True
    # Recursion
    else:
        row, col = find_empty_space(sudoku)
    # check for all possible numbers if they are valid, until one is valid
    for i in range(1, 10):
        if is_valid(sudoku, i, (row, col)):
            # add number into board if valid
            sudoku[row][col] = i

            # try to solve the Board from now on
            if solve_sudoku(sudoku):
                return True

            # if it isnt possible with the number triend, empty the Space and try another number
            sudoku[row][col] = 0

    # if no number was valid, the wrong number has to be before this Space, so you get back one Step and try again
    return False

# ------------------------------------------------------------ Interface -------------------------------------------------------------------------


def print_sodoku(sudoku):
    """Prints the Board in an easier to read way"""
    for i in range(len(sudoku)):
        # check wheter or not to print a horiontal line
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        # check wheter or not to print vertikal horiontal line
        for j in range(len(sudoku[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(sudoku[i][j])
            else:
                print(str(sudoku[i][j]) + " ", end="")


def main(sudoku):
    """Only used to pretify the solving, showing the Time and handling  a unsolvable Sudoku. You most likely want to use thin function"""
    print_sodoku(sudoku)
    print("Starting to solve the Sudoku...\n")
    timer_start = time.perf_counter()
    solve_sudoku(sudoku)
    timer_end = time.perf_counter()
    # Check if Sodoku has empty Spaces left and isnt solvable
    if find_empty_space(sudoku) != None:
        print(
            f"Sudoku Solver needed {timer_end - timer_start:0.4f} seconds to find out, that this Sudoku isnt possible to solve!\n")
        print_sodoku(sudoku)
    else:
        print(f"Sudoku Solved in {timer_end - timer_start:0.4f} seconds\n")
        print_sodoku(sudoku)


main(sudoku)
