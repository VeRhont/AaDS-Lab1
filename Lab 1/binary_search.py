from random import choice


def search(array, target):
    steps = 0
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = left + (right - left) // 2

        if array[middle] == target:
            return steps
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

        steps += 1

    return -1


def main():
    test_data = [
        [1, 4, 5, 7, 8, 10, 17, 23, 25, 97, 100, 232],
        [1, 2, 3, 6, 7, 8, 10, 13, 25, 42, 71, 100, 453, 1204],
        [1, 4, 5, 7, 8, 10, 17, 23, 24, 97, 100, 232],
    ]

    for i in range(len(test_data)):
        target = choice(test_data[i])
        result = search(test_data[i], target)

        if result != -1:
            print(f'Потребуется {result} шагов, чтобы найти {target}')
        else:
            print('Элемент не присутствует в массиве')



if __name__ == '__main__':
    main()
