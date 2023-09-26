from random import randint


def check_time(name):
    def decorator(func):
        def wrapper(n):

            print(name)
            for i in range(n):
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


@check_time('O(nlogn)')
def f2(n):
    pass


@check_time('O(n!)')
def f3(n):
    steps = 0
    return steps


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

    # for i in range(3):
    m = n
    while m > 0:
        steps += 1

        if m % 2 == 0:
            break
        else:
            m //= 2


    return steps


if __name__ == '__main__':
    n = 10

    # f1(n)
    # f2(n)
    # f3(n)
    # f4(n)
    f5(n)

