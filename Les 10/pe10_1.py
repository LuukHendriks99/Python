import xmltodict

with open('pe10_1.xml') as fd:
    doc = xmltodict.parse(fd.read())

    for x in doc['artikelen']['artikel']:
        print(x['naam'])
