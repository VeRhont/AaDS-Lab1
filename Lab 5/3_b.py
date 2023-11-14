from random import randint


def max_increasing_sequence(array):
    n = len(array)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if array[i] > array[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def main():
    array = [randint(-100, 100) for i in range(6)]
    print(array)

    result = max_increasing_sequence(array)
    print(f'Длина наибольшей возрастающей подпоследовательности: {result}')


if __name__ == '__main__':
    main()