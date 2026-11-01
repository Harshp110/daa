def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve(board, row + 1, n):
                return True

            board[row][col] = 0

    return False


n = int(input("Enter value of N: "))
board = [[0 for _ in range(n)] for _ in range(n)]

row, col = map(int, input("Enter first queen's row and column (1 to N): ").split())
row -= 1
col -= 1

if row < 0 or row >= n or col < 0 or col >= n:
    print("Invalid position!")
elif row != 0:
    print("Place the first queen in row 1.")
else:
    board[row][col] = 1

    if solve(board, 1, n):
        print("N-Queens Matrix:")
        for line in board:
            print(*line)
    else:
        print("No solution exists for this position.")
