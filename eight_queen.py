N = [[0]*4 for i in range(4)]


def is_place(row: int, col: int):
    for i in range(col):
        if N[row][i] == 1:
            return False

    # ???
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if N[i][j] == 1:
            return False

    # ???
    for i, j in zip(range(row, 4, 1), range(col, -1, -1)):
        if N[i][j] == 1:
            return False
    return True

def print_solution(N):
    for i in range(len(N)):
        for j in range(len(N)):
            print(N[i][j], end=" ")
        print()
    print()


def eight_queen(col):
    if col >= 4:
        print_solution(N)
    else:
        for i in range(4):
            if is_place(i, col):
                N[i][col] = 1
                print(i, '--->', col)
                print('----------------------------------------------')
                eight_queen(col + 1)
                print(i, '***>', col)
                N[i][col] = 0
    return False



if __name__ == '__main__':
    eight_queen(0)