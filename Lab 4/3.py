from random import randint


def generate_random_matrix(n=15):
    matrix = [[randint(0, 1) for j in range(n)] for i in range(n)]
    return matrix


def draw_path(matrix, visited):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i, j) in visited:
                print('*', end=' ')
            else:
                print(matrix[i][j], end=' ')
        print()


def depth_search(matrix, i, j, visited):
    visited.add((i, j))

    if j == 14:
        return visited

    if (i + 1 >= 15) or (i - 1 < 0) or (j - 1 < 0) or (j + 1 >= 15):
        return


    possible = []

    if (matrix[i + 1][j] == 0) and ((i + 1, j) not in visited):
        possible.append((i + 1, j))
    if (matrix[i][j + 1] == 0) and ((i, j + 1) not in visited):
        possible.append((i, j + 1))
    if (matrix[i][j - 1] == 0) and ((i, j - 1) not in visited):
        possible.append((i, j - 1))
    if (matrix[i - 1][j] == 0) and ((i - 1, j) not in visited):
        possible.append((i - 1, j))


    if len(possible) == 0:
        return

    for point in possible:
        depth_search(matrix, point[0], point[1], visited)


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

    visited = set()
    visited.add((7, 0))

    result = depth_search(matrix, 7, 1, visited)
    draw_path(matrix, visited)
