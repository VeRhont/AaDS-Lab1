from random import randint
from colorama import Fore


def generate_random_matrix(n=15):
    matrix = [[randint(0, 1) for j in range(n)] for i in range(n)]
    return matrix


def draw_path(matrix, visited):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i, j) in visited:
                print(Fore.LIGHTBLUE_EX + '*', end=' ')
            else:
                print(Fore.WHITE + str(matrix[i][j]), end=' ')
        print()
    print()


def depth_search(matrix, i, j, current_path):
    current_path.add((i, j))

    if j == len(matrix) - 1:
        draw_path(matrix, current_path)
        return current_path


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

    return current_path



def depth_search1(matrix, i, j, path, visited):
    path.add((i, j))

    draw_path(matrix, path)

    if j == len(matrix) - 1:
        return path

    possible = []

    if (matrix[i + 1][j] == 0) and ((i + 1, j) not in path) and ((i + 1, j) not in visited):
        possible.append((i + 1, j))
    if (matrix[i][j + 1] == 0) and ((i, j + 1) not in path) and ((i, j + 1) not in visited):
        possible.append((i, j + 1))
    if (j > 0) and (matrix[i][j - 1] == 0) and ((i, j - 1) not in path) and ((i, j - 1) not in visited):
        possible.append((i, j - 1))
    if (i > 0) and (matrix[i - 1][j] == 0) and ((i - 1, j) not in path) and ((i - 1, j) not in visited):
        possible.append((i - 1, j))

    if len(possible) == 0:
        visited |= path
        path = set()

    for point in possible:
        depth_search(matrix, point[0], point[1], path, visited)

    return path


if __name__ == '__main__':
    matrix = [
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

    # matrix = [
    #     [1, 1, 1, 1, 1],
    #     [1, 0, 0, 0, 1],
    #     [0, 0, 1, 0, 1],
    #     [1, 0, 1, 0, 0],
    #     [1, 1, 1, 1, 1],
    # ]

    path = set()

    depth_search(matrix, 7, 0, path)
