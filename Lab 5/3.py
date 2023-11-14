from random import randint


def find_longest_subarray(arr):
    max_length = 1
    current_length = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1

    return max_length


def main():
    array = [randint(-100, 100) for i in range(12)]
    print(array)
    result = find_longest_subarray(array)

    print(f'Длина наибольшей непрерывной возрастающей подпоследовательности: {result}')


if __name__ == '__main__':
    main()