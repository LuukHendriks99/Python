while True:
    woord = input('Geef een string van vier letters: ')
    if len(woord) != 4:
        print( woord, 'heeft', len(woord), 'letters')
    else:
        print('Inlezen van correcte string: {} is geslaag'.format(woord))
        break
