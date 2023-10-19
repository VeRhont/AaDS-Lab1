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

    return len(stack) == 0



if __name__ == '__main__':
    sequences = ['()', '[]{}()', ')]{}', '(]', '[[[', '(()[]{})', '[])(()', '{[()]}']

    for i in sequences:
        print(i, is_correct(i))