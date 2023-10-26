from collections import deque


metro_map = {
    'Театральная': ['Самарская'],
    'Самарская': ['Театральная', 'Алабинская'],
    'Алабинская': ['Самарская', 'Российская'],
    'Российская': ['Алабинская', 'Московская'],
    'Московская': ['Российская', 'Революционная', "Клиническая", "Гагаринская"],
    'Клиническая': ['Московская', 'Вокзальная'], # по синей от московской вниз
    'Вокзальная': ['Клиническая', 'Молодогвардейская'],
    'Молодогвардейская': ['Вокзальная', 'Стадион'],
    'Стадион': ['Молодогвардейская'],
    'Революционная': ["Московская", 'Орловская'], # по синей от московской вверх
    "Ипподромная": ['Метеоцентр'], # по зелёной вниз
    "Метеоцентр": ["Ипподромная",'Орловская'],
    "Орловская": ['Революционная', "Метеоцентр", "Гагаринская"],
    "Гагаринская": ['Орловская', "Спортивная", "Московская", "Аэродромная"],
    "Аэродромная": ['Гагаринская', "Куйбышевская"],
    "Куйбышевская": ['Аэродромная'],
    "Спортивная": ['Гагаринская', "Советская"], # От гагаринской дальше по красной ветке
    "Советская": ['Спортивная', "Победа"],
    "Победа": ['Советская', "Безымянка"],
    "Безымянка": ['Победа', "Кировская"],
    "Кировская": ['Безымянка', "Юнгородок"],
    "Юнгородок": ['Кировская']
}


def restore_path(target_station, start_station, path_dict):
    path = []
    current = target_station
    while current != start_station:
        path.append(current)
        current = path_dict[current]
    path.append(start_station)

    return ' -> '.join(reversed(path))


def depth_first_search(start_station, target_station):
    stack = [start_station]
    visited = []
    path_dict = {}

    visited.append(start_station)

    while stack:
        current_station = stack.pop()

        if current_station == target_station:
            break

        for next_station in metro_map[current_station]:
            if next_station not in visited:
                stack.append(next_station)
                visited.append(next_station)
                path_dict[next_station] = current_station

    if target_station not in visited:
        return ""

    result = restore_path(target_station, start_station, path_dict)
    return result


def breadth_first_search(start_station, target_station):
    queue = deque([start_station])
    visited = []
    path_dict = {}

    visited.append(start_station)

    while queue:
        current_station = queue.popleft()

        if current_station == target_station:
            break

        for next_station in metro_map[current_station]:
            if next_station not in visited:
                visited.append(next_station)
                queue.append(next_station)
                path_dict[next_station] = current_station

    if target_station not in visited:
        return ""

    result = restore_path(target_station, start_station, path_dict)
    return result


if __name__ == '__main__':
    start = 'Революционная'
    target = 'Спортивная'

    dfs_path = depth_first_search(start, target)
    bfs_path = breadth_first_search(start, target)

    print(f"Кратчайший путь от {start} до {target} (поиск в глубину):")
    print(dfs_path)
    print()
    print(f"Кратчайший путь от {start} до {target} (поиск в ширину):")
    print(bfs_path)