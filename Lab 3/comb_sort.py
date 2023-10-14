from random import randint
from timeit import timeit


def comb_sort(array):
    h = int(len(array) // 1.247) # текущий шаг
    s = 0 # количество шагов для h
    i = 0

    while (h != 1) or (s != 0):
        if i + h < len(array):
            if array[i] > array[i + h]:
                array[i], array[i + h] = array[i + h], array[i]
                s += 1
            i += 1
        else:
            i, s = 0, 0
            h = int(h // 1.247)


if __name__ == '__main__':
    array = [randint(-100, 100) for _ in range(10)]
    print(f'Исходный массив: {array}')

    print(f'Время: {timeit("lambda: comb_sort(array)")}')

    comb_sort(array)
    print(f'Отсортированный массив: {array}')