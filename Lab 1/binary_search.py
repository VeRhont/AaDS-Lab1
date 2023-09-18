def binary_search(array, target):
    steps = 0
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2

        if array[middle] == target:
            return steps
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

        steps += 1

    return -1


def main():
    test_data = {
        4: [1, 4, 5, 7, 8, 10, 17, 23, 25, 97, 100, 232],
        25: [2, 3, 6, 7, 8, 10, 13, 25, 42, 71, 100, 453, 1204],
        9: [7, 8, 10, 17, 23, 24, 97, 100, 232],
    }

    for target, array in test_data.items():
        result = binary_search(array, target)

        print(f'Список: {array}\nЦель: {target}')
        if result != -1:
            print(f'Потребуется {result} шага, чтобы найти элемент {target}')
        else:
            print('Элемент не присутствует в массиве')

        print()


if __name__ == '__main__':
    main()
