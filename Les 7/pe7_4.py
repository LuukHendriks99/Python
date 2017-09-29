def ticker(filename):
    dict = {}
    f = open('tickers.txt', 'r')
    regels = f.readlines()
    for line in regels:
        niks = line.strip('\n')
        (key, val) = niks.split(':')
        dict[key] = val
    return dict

invoer = input('Enter Company name: ')
dictionary = ticker('tickers.txt')
print('Ticker symbol:', dictionary[invoer])
invoer2 = input('Enter ticker symbol: ')
for ticker in dictionary:
    if invoer2 == dictionary[ticker]:
        print('Company name: ', ticker)
