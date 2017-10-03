def namen():
    dict = {}
    while True:
        naam = input('Geef volgende naam: ')
        if not naam == '':
            if naam in dict:
                dict[naam] += 1
            else:
                dict[naam] = 1

        else:
            for key in dict:
                if dict[key] == 1:
                    print('Er is 1 student met de naam {}'.format(key))
                else:
                    print('Er zijn {} studenten met de naam {}'.format(dict[key], key))
            break
namen()