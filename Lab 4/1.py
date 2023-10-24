def is_correct(sequence):
    stack = []

    for i in range(len(sequence)):
        bracket = sequence[i]

        if bracket in '([{':
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return i

            last_bracket = stack.pop(-1)

            if last_bracket + bracket not in ['()', '[]', '{}']:
                return i

    return True if len(stack) == 0 else len(sequence) - 1



if __name__ == '__main__':
    sequences = ['()', '[]{}()', ')]{}', '(]', '[[[', '(()[]{})', '[])(()', '{[()]}']

    for i in sequences:
        result = is_correct(i)
        if type(result) == bool:
            print(f'{i} - правильно')
        else:
            print(f'{i} - неправильный элемент под номером {result + 1}')

