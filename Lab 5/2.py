from random import randint


def min_matrices_product(matrices):
    n = len(matrices) - 1
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for length in range(2, n + 1):  # для каждой длины подпоследовательности от 2 до n
        for i in range(1, n - length + 2):  # для каждого начального индекса i от 1 до n - l + 1
            j = i + length - 1
            dp[i - 1][j - 1] = float('inf')  # инициализируем минимальное количество операций как бесконечность
            for k in range(i, j):  # перебираем все возможные разбиения подпоследовательности на две части
                q = dp[i - 1][k - 1] + dp[k][j - 1] + matrices[i - 1] * matrices[k] * matrices[j]
                dp[i - 1][j - 1] = min(dp[i - 1][j - 1], q)  # выбираем разбиение с минимальным количеством операций

    return dp[0][n - 1]


def generate_matrices(n):
    matrices = []
    first_matrix = (randint(1, 10), randint(1, 10))
    matrices.append(first_matrix)

    for i in range(1, n):
        matrix = (matrices[i - 1][1], randint(1, 10))
        matrices.append(matrix)

    return matrices


def main():
    matrices = generate_matrices(26)
    matrices_sizes = [i[0] for i in matrices] + [matrices[-1][1]]
    result = min_matrices_product(matrices_sizes)

    print(f'Исходные матрицы: {matrices}')
    print("Минимальное количество произведений:", result)


if __name__ == '__main__':
    main()
