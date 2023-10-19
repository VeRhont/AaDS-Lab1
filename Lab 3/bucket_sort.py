from random import randint


def bucket_sort(arr):
    bucket_size = 10
    min_val = min(arr)
    max_val = max(arr)

    # Создаем пустые блоки
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]

    # Распределяем значения в блоки
    for num in arr:
        index = (num - min_val) // bucket_size
        buckets[index].append(num)

    # Сортируем значения в каждом блоке
    sorted_arr = []
    for bucket in buckets:
        sorted_arr += insertion_sort(bucket)

    return sorted_arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


if __name__ == '__main__':
    arr = [randint(-100, 100) for _ in range(10)]
    print('Неотсортированный массив: ', arr)
    sorted_arr = bucket_sort(arr)
    print('Неотсортированный массив: ', sorted_arr)