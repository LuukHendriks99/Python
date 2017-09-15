def kwadraten_som(grondgetallen):
    uitkomst = 0
    for lijst in grondgetallen:
        if lijst > 0:
            uitkomst += lijst ** 2
    return uitkomst

grondgetallen = [4, 5, 3, -81]
print(kwadraten_som(grondgetallen))
