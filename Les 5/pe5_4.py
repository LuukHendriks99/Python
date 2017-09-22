import time
file = open('hardlopers.txt', 'a')
timestr = time.strftime(" %a %d %b %Y, %H:%M:%S, ")
file.write(timestr)
file.write(input('Vul hier de hardlopernaam in: \n '))
file.close()
