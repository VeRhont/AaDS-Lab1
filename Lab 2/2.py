import time
from random import randint


def check_time(func):
    def wrapper(array):
        start = time.time()
        func(array)
        end = time.time()

        print(f'n = {len(array)}: {end - start} seconds')

    return wrapper


@check_time
def bubble_sort(array):
    array_copy = array.copy()

    for i in range(len(array) - 1, -1, -1):
        for j in range(0, i):
            if array_copy[i] < array_copy[j]:
                array_copy[i], array_copy[j] = array_copy[j], array_copy[i]
    return array_copy


@check_time
def quick_sort(array):
    array_copy = array.copy()
    array_copy.sort()
    return array_copy


def generate_random_array(n):
    array = []

    for i in range(n):
        num = randint(0, 1000) * 3 - randint(0, 200)
        array.append(num)

    return array


if __name__ == '__main__':
    n = 30_000
    array = generate_random_array(n)

    print('Bubble Sort:')
    bubble_sort(array)
    print('Quick Sort:')
    quick_sort(array)
