nummers = "5-9-7-1-7-8-3-2-4-8-7-9"

list = []
for cijfers in nummers:
    if type(nummers) == int or float:
        list.append(cijfers)
    else:
        cijfers.strip()

print(list)