from random import randint


def merge(a, b):
    c = []
    i, j = 0, 0
    while (i < len(a)) and (j < len(b)):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i == len(a):
        for k in range(j, len(b)):
            c.append(b[k])
    else:
        for k in range(i, len(a)):
            c.append(a[k])
    return c


def merge_sort(a):
    if len(a) <= 1: return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)


if __name__ == '__main__':
    array = [randint(-100, 100) for _ in range(10)]
    print("Неотсортированный массив: ", array)
    array = merge_sort(array)
    print("Сортированный массив: ", array)
