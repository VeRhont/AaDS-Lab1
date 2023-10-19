# Процедура для преобразования в двоичную кучу поддерева с корневым узлом i, что является индексом в arr[].
# Функция просеивания
from random import randint


def swap(array, sizek, root_node):
    biggest = root_node # Большое - корень
    left_el = 2 * root_node + 1
    right_el = 2 * root_node + 2   # right = 2*i + 2
  # Проверяем существует ли левый дочерний элемент больший, чем корневой
    if left_el < sizek and array[root_node] < array[left_el]:
        biggest = left_el
    # Проверяем существует ли правый дочерний элемент больший, чем корневой
    if right_el < sizek and array[biggest] < array[right_el]:
        biggest = right_el
    # Заменяем корень, если нужно
    if biggest != root_node:
        array[root_node],array[biggest] = array[biggest],array[root_node] # свапаем
        # Применяем heapify к корню.
        swap(array, sizek, biggest)


# Основная функция для сортировки массива заданного размера
def heap_sort(array):
    sizek = len(array)
    # Построение max-heap.
    for i in range(sizek, -1, -1):
        swap(array, sizek, i)
    # Один за другим извлекаем элементы
    for i in range(sizek - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        swap(array, i, 0)


if __name__ == '__main__':
    array = [randint(-100, 100) for _ in range(10)]
    print ("Неотсортированный массив: ", array)
    heap_sort(array)
    print("Сортированный массив: ", array)