from random import randint
from timeit import timeit


def quick_sort(array):
    if len(array) <= 1:
        return array

    random_index = randint(0, len(array) - 1)
    element = array[random_index]

    smaller = [i for i in array if i < element]
    equal = [i for i in array if i == element]
    greater = [i for i in array if i > element]

    return quick_sort(smaller) + equal + quick_sort(greater)


if __name__ == '__main__':
    array = [randint(-100, 100) for _ in range(15)]
    print(f'Исходный массив: {array}')

    print(f'Время: {timeit("lambda: quick_sort(array)")}')

    result = quick_sort(array)
    print(f'Отсортированный массив: {result}')