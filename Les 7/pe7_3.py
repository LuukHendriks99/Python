dict = {'Piet': 7, 'Henk': 9.5, 'Klaas': 10, 'Luuk': 8, 'Jan': 3, 'Yvo': 7, 'Guido': 4.7, 'Maurits': 6}
for student in dict:
    if dict[student] >9:
        print('{} heeft cijfer {}'.format(student, dict[student]))