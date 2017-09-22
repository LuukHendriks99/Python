file_in = open('kaartnummer.txt', 'r')

smallestInt = 0

intList = [int(x.split(",")[0]) for x in file_in.readlines()]
regels = len(intList)
number = max(intList)
string_format = 'Deze file telt {0} regels\n' \
                'Het grootste kaartnummer is: {1} en dat staat op regel {2}'
result = string_format.format(regels, number, str(intList.index(max(intList))))
print(result)
