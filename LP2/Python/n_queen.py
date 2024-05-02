def print_solution(board):
    queen_positions = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                queen_positions.append(j)
    print("Solution:", " ".join(map(str, queen_positions)))

    for i in range(N):
        for j in range(N):
            print(" Q " if board[i][j] == 1 else " . ", end="")
        print()

def solve_nq_util(board, col):
    if col >= N:
        return True

    for i in range(N):
        if (ld[i - col + N - 1] != 1 and rd[i + col] != 1) and cl[i] != 1:
            board[i][col] = 1
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 1

            if solve_nq_util(board, col + 1):
                return True

            board[i][col] = 0
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 0

    return False

def solve_nq():
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solve_nq_util(board, 0):
        print("Solution does not exist")
        return False

    print_solution(board)
    return True

if __name__ == "__main__":
    N = int(input("Enter the size of the N-Queens problem: "))
    ld = [0] * (2 * N - 1)
    rd = [0] * (2 * N - 1)
    cl = [0] * N
    solve_nq()
