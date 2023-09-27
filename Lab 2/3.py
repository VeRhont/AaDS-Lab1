from random import randint


def check_time(name):
    def decorator(func):
        def wrapper(n):

            print(name)
            for i in range(1, n + 1):
                result = func(i)
                print(f'{i}: {result} steps')
            print()

        return wrapper
    return decorator


@check_time('O(3n)')
def f1(n):
    matrix = [[0] * n for _ in range(3)]
    steps = 0

    for i in range(3):
        for j in range(n):
            matrix[i][j] = i + j
            steps += 1

    return steps


steps = 0
# @check_time('O(nlogn)')
def f2(n):
    def merge_sort(array):
        global steps
        if len(array) < 2: return array[:]
        steps += 1
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)

    def merge(array1, array2):
        result = []
        i, j = 0, 0
        while (i < len(array1)) and (j < len(array2)):
            if array1[i] < array2[j]: result.append(array1[i]); i += 1
            else: result.append(array2[j]); j += 1

        while i < len(array1): result.append(array1[i]); i += 1
        while j < len(array2): result.append(array2[j]); j += 1
        return result

    array = [randint(-100, 100) for _ in range(n)]
    result = merge_sort(array)

    return steps


@check_time('O(n!)')
def f3(n):
    def f3_1(n):
        if n == 1: return 1
        steps = 0

        for i in range(0, n):
            steps += f3_1(n - 1)

        return steps

    return f3_1(n)


@check_time('O(n^3)')
def f4(n):
    steps = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                steps += 1

    return steps


@check_time('O(3logn)')
def f5(n):
    steps = 0

    for i in range(3):
        m = n + (n % 2 != 0)
        while m > 1:
            steps += 1
            m /= 2

    return steps


if __name__ == '__main__':
    n = 10

    # f1(n)
    # f2(n)
    # f3(n)
    # f4(n)
    # f5(n)

    print(f2(10))