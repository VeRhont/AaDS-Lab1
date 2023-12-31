from binary_search import binary_search


def test_binary_search():
    assert binary_search([1, 2, 3, 4], 2) != -1
    assert binary_search([1, 2, 3, 4, 5, 6, 8], 6) != -1
    assert binary_search([1, 2, 3, 4], 5) == -1
    assert binary_search([1, 2, 3, 4], 0) == -1

    print('Binary search: OK')


def test_steps():
    assert binary_search([1, 2, 3, 4, 5], 2) == 2
    assert binary_search([1, 3, 4, 5, 6], 2) == -1
    assert binary_search([1, 1, 1, 1], 1) == 0
    assert binary_search([4, 5, 5, 5, 7, 7, 8], 6) == -1
    assert binary_search([], 1) == -1

    print('Steps: OK')


if __name__ == '__main__':
    test_binary_search()
    test_steps()
