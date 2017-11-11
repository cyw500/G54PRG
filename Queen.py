size = 8 # what size board
board = []

for c in range(size):
    board += [[]]
    for r in range(size):
        board[c] += [0]


def print_board():
    for row in board:
        for unit in row:
            if unit == 0 :
                print(". ", end=" ")
            else:
                print(unit, end=" ")
        print()


def possible(r, c):
    for i in range(size):
        if board[i][c] == "Q" or "Q" in board[r]:
            return False
    for i in range(min(c + 1, r + 1)):
        if board[r - i][c - i] == "Q":
            return False
    for i in range(1, min(r + 1, size - c)):
        if board[r - i][c + i] == "Q":
            return False
    else:
        return True

counter = 1

def solve(n):
    global counter
    if n == size:
        counter += 1
        print_board()
        input ("Next solution? ")
        print ("Solution number ",counter)
    else:
        for i in range(size):
            if possible(n, i):
                board[n][i] = "Q"  # place the "Q"
                solve(n + 1)
                board[n][i] = 0  # backtracking




