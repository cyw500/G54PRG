size = 8 # size of the board
# creating a list containing the correct amount for each row and column
board = [[0] * size for i in range(size)]
counter = 1 # allow counting the number of solution

def print_board(): # creating a visually symmetric board
    for row in board:
        for unit in row:
            if unit == 0 :
                print(". ", end=" ")
            else:
                print(unit, end=" ")
        print()

def possible(row, col):
    # Check if placing a queen in a given square on the board is a valid move.
    if "Q" in board[row]:
        # If there is already a queen in the row then the move isn't valid.
        return

    # Loop through the rows above the row being checked in order to see if the move is invalid
    # due to another queen being in the same column or along a diagonal from the position being checked.
    for i in range(row+1):
        if board[i][col] == "Q":
            # There is a queen in the same column as the position being checked, so the position is invalid.
            return
        if col + i < size:
            # Check the position diagonally above and to the right of the position being validated only when the
            # position being checked hasn't gone off the right edge of the board.
            if board[row - i][col + i] == "Q":
                # Decrease row by i and increase column by i to check i position in the direction of up right.
                return
        if col - i >= 0:
            # Check the position diagonally above and to the left of the position being validated only when the
            # position being checked hasn't gone off the left edge of the board.
            if board[row - i][col - i] == "Q":
                # Decrease the row by i and the column by i to check i position in the direction of up left.
                return

    return True

def solve(n):
    global counter
    if n == size:
        print ("Solution number",counter)
        print_board()
        input ("Next solution? ")
        counter += 1
        
    else:
        for i in range(size):
            if possible(n, i):
                board[n][i] = "Q"  # Place a "Q" (Queen)
                solve(n + 1)  # solve the next row
                board[n][i] = 0  # backtracking


