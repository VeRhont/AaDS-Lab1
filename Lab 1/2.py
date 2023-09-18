def read_data():
    with open('questions.txt', 'r', encoding='utf-8') as file:
        questions = [s.strip() for s in file.readlines()]

    with open('students_data.txt', 'r', encoding='utf-8') as file:
        students = [tuple(s.split()) for s in file.readlines()]
        students.sort()

    return questions, students


def upper_bound(array, key):
    left = -1
    right = len(array)

    while right > left + 1:
        middle = (left + right) // 2
        if int(array[middle]) > key:
            right = middle
        else:
            left = middle

    return right


def lower_bound(array, key):
    left = -1
    right = len(array)

    while right > left + 1:
        middle = (left + right) // 2
        if int(array[middle]) >= key:
            right = middle
        else:
            left = middle

    return right


def main():
    questions, students = read_data()

    for index, question in enumerate(questions):
        user_input = input(f'{question}\n-> ').strip().lower()
        answer = 1 if user_input == 'да' else 0

        temp = [student[index] for student in students]

        if answer:
            left_bound = lower_bound(temp, answer)
            students = students[left_bound:]
        else:
            right_bound = upper_bound(temp, answer)
            students = students[:right_bound]


    if students:
        result = f'{students[0][-2]} {students[0][-1]}'
        print(f'Вы загадали студента: {result}')
    else:
        print('Студент не найден')


if __name__ == '__main__':
    main()
