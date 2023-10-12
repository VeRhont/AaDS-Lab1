students = {
    'Иванов Иван': "01",
    'Петров Петр': "11",
    'Длдывоады': '00',
    'фыафывафыва': '10'
}

questions = {
    'Студент курит? ',
    'Студент блондин? ',
}

current_answer = ''

for question in questions:
    print(question)
    answer = input()

    if answer.strip().lower() == 'да':
        current_answer += '1'
    else:
        current_answer += '0'

for student, value in students.items():
    if value == current_answer:
        print(student)
