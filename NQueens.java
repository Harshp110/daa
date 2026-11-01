import java.util.Scanner;

class NQueens {
    static int n;
    static int[][] board;

    static boolean isSafe(int row, int col) {
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 1)
                return false;
        }

        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 1)
                return false;
        }

        for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
            if (board[i][j] == 1)
                return false;
        }

        return true;
    }

    static boolean solve(int row) {
        if (row == n)
            return true;

        for (int col = 0; col < n; col++) {
            if (isSafe(row, col)) {
                board[row][col] = 1;

                if (solve(row + 1))
                    return true;

                board[row][col] = 0;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter value of N: ");
        n = sc.nextInt();

        board = new int[n][n];

        System.out.print("Enter first queen's row and column (1 to " + n + "): ");
        int row = sc.nextInt() - 1;
        int col = sc.nextInt() - 1;

        if (row < 0 || row >= n || col < 0 || col >= n) {
            System.out.println("Invalid position!");
        } else {
            board[row][col] = 1;

            boolean safe = true;

            for (int i = 0; i < n; i++) {
                if (i != row && !isSafe(i, col)) {
                    // The first queen must not share a column with another queen.
                    safe = false;
                    break;
                }
            }

            // The first queen must be in row 1 for this simple solver.
            if (row != 0) {
                System.out.println("Place the first queen in row 1.");
            } else if (solve(1)) {
                System.out.println("N-Queens Matrix:");

                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++)
                        System.out.print(board[i][j] + " ");
                    System.out.println();
                }
            } else {
                System.out.println("No solution exists for this position.");
            }
        }

        sc.close();
    }
}
