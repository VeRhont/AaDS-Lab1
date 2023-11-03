from random import randint
from colorama import Fore


def generate_random_matrix(n=15):
    matrix = [[1] * n for i in range(n)]

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            matrix[i][j] = randint(0, 1)

    matrix[randint(0, n)][0] = 0
    matrix[randint(0, n)][n - 1] = 0

    return matrix


def draw_path(matrix, visited):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i, j) in visited:
                print(Fore.LIGHTBLUE_EX + '*', end=' ')
            elif matrix[i][j] == 0:
                print(Fore.WHITE + str(matrix[i][j]), end=' ')
            else:
                print(Fore.RED + str(matrix[i][j]), end=' ')
        print()
    print()


def depth_search(matrix, i, j, current_path):
    current_path.add((i, j))

    if j == len(matrix) - 1:
        draw_path(matrix, current_path)
        exit()

    possible = []

    if (matrix[i + 1][j] == 0) and ((i + 1, j) not in current_path):
        possible.append((i + 1, j))
    if (matrix[i][j + 1] == 0) and ((i, j + 1) not in current_path):
        possible.append((i, j + 1))
    if (j > 0) and (matrix[i][j - 1] == 0) and ((i, j - 1) not in current_path):
        possible.append((i, j - 1))
    if (i > 0) and (matrix[i - 1][j] == 0) and ((i - 1, j) not in current_path):
        possible.append((i - 1, j))

    if len(possible) == 0:
        return

    for point in possible:
        depth_search(matrix, point[0], point[1], current_path.copy())

    return "Нет пути"


def depth_search_3d(matrix, i, j, z, current_path):
    current_path.add((i, j, z))

    if (j == len(matrix) - 1) and (z == len(matrix) - 1):
        print(current_path)
        return

    possible = []

    if (matrix[i + 1][j][z] == 0) and ((i + 1, j, z) not in current_path):
        possible.append((i + 1, j, z))
    if (i > 0) and (matrix[i - 1][j][z] == 0) and ((i - 1, j, z) not in current_path):
        possible.append((i - 1, j, z))
    if (matrix[i][j + 1][z] == 0) and ((i, j + 1, z) not in current_path):
        possible.append((i, j + 1, z))
    if (j > 0) and (matrix[i][j - 1][z] == 0) and ((i, j - 1, z) not in current_path):
        possible.append((i, j - 1, z))
    if (matrix[i][j][z + 1] == 0) and ((i, j, z + 1) not in current_path):
        possible.append((i, j, z + 1))
    if (z > 0) and (matrix[i][j][z - 1] == 0) and ((i, j, z - 1) not in current_path):
        possible.append((i, j, z - 1))

    if len(possible) == 0:
        return

    for p in possible:
        depth_search_3d(matrix, p[0], p[1], p[2], current_path.copy())

    return "Нет пути"


if __name__ == '__main__':
    matrix1 = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,1,0,1,0,0,0,0,1,1,1],
        [1,0,1,1,1,1,0,1,0,1,1,0,1,0,1],
        [1,0,1,0,0,0,0,1,0,1,1,0,1,0,1],
        [1,0,1,1,1,1,0,1,0,0,1,0,1,0,1],
        [1,0,0,0,0,1,0,1,0,1,1,0,1,0,1],
        [1,0,1,1,1,1,0,1,0,1,1,0,1,0,1],
        [0,0,1,1,0,1,0,1,0,1,0,0,1,0,0],
        [1,0,1,0,0,0,0,0,0,1,1,0,1,0,1],
        [1,0,1,1,1,0,1,1,0,0,1,0,1,0,1],
        [1,0,0,1,1,0,1,1,1,1,1,0,1,0,1],
        [1,1,0,0,0,0,1,0,0,0,0,0,1,0,1],
        [1,0,0,1,1,1,1,1,1,1,1,0,1,0,1],
        [1,1,1,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ]

    matrix2 = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,1,0,0,0,0,1,1,1],
        [1,0,1,1,1,1,0,1,0,1,1,0,1,0,0],
        [1,0,1,0,0,0,0,1,0,1,1,0,1,0,1],
        [1,0,1,1,1,1,0,1,0,0,1,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,1,1,0,1,0,1],
        [1,0,1,1,1,1,1,1,0,1,1,0,1,0,1],
        [1,0,1,1,0,1,0,1,1,1,0,0,1,0,1],
        [1,0,1,0,0,0,0,0,0,1,1,1,1,0,1],
        [1,0,1,1,1,0,1,1,0,0,0,0,1,0,1],
        [1,0,0,0,0,0,1,1,1,1,1,0,1,0,1],
        [1,1,1,1,1,1,1,0,0,0,0,0,1,0,1],
        [1,0,0,0,0,1,1,0,1,1,1,1,1,0,1],
        [0,0,1,1,0,0,0,0,0,0,0,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ]

    matrix3 = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,1,0,0,0,0,1,1,1],
        [1,0,1,1,1,1,0,1,0,1,1,0,1,0,0],
        [1,0,1,0,0,0,0,1,0,1,1,0,1,0,1],
        [1,0,1,1,1,1,0,1,0,0,1,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,1,1,0,1,0,1],
        [1,1,1,1,1,1,1,1,0,1,1,0,1,0,1],
        [1,0,1,1,0,1,0,1,1,1,0,0,1,0,1],
        [1,0,1,0,0,0,0,0,0,1,1,1,1,0,1],
        [1,0,1,1,1,1,1,1,0,0,0,0,1,0,1],
        [1,0,0,0,0,0,1,1,1,1,1,0,1,0,1],
        [1,1,1,1,1,1,1,0,0,0,0,0,1,0,1],
        [1,0,0,0,0,1,1,0,1,1,1,1,1,0,1],
        [0,0,1,1,0,0,0,0,0,0,0,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ]

    path = set()
    result = depth_search(matrix1, 7, 0, path)
    print(result)

    # path = set()
    # result = depth_search(matrix2, 13, 0, path)
    # print(result)

    # path = set()
    # result = depth_search(matrix3, 13, 0, path)
    # print(result)
