from random import randint


def occupy(field, i, j):
    diagonal_1 = i - j
    diagonal_2 = i + j

    for row in range(n):
        field[row][j] = 1

        if 0 <= row - diagonal_1 < n:
            field[row][row - diagonal_1] = 1

    for column in range(n):
        field[i][column] = 1

        if 0 <= diagonal_2 - column < n:
            field[diagonal_2 - column][column] = 1

    field[i][j] = '*'


def is_correct(n, field):
    if sum([1 for i in range(n) for j in range(n) if field[i][j] == '*']) != n: return False

    for i in range(n):
        for j in range(n):
            if field[i][j] == '*':
                diagonal_1 = i - j
                diagonal_2 = i + j

                for row in range(n):
                    if (field[row][j] == '*') and (row != i): return False

                    if 0 <= row - diagonal_1 < n:
                        if (row != i) and (field[row][row - diagonal_1] == '*'): return False

                for column in range(n):
                    if (field[i][column] == '*') and (column != j): return False

                    if 0 <= diagonal_2 - column < n:
                        if (column != j) and (field[diagonal_2 - column][column] == '*'): return False

    return True


def generate(n, visited):
    field = [[0] * n for i in range(n)]

    vis = ()
    for _ in range(n):
        point = (randint(0, n - 1), randint(0, n - 1))
        vis += (point)

    if vis not in visited:
        for i in range(0, n * 2, 2):
            occupy(field, vis[i], vis[i + 1])

    visited.add(vis)
    return field


if __name__ == '__main__':
    # print(is_correct(4, [[1, '*', 1, 1], [1, 1, 1, '*'], ['*', 1, 1, 1], [1, 1, 1, '*']]))

    n = int(input())

    visited = set()

    while True:
        field = generate(n, visited)

        if is_correct(n, field):
            for row in field:
                print(*row)
            print()

            break
