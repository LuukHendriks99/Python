def standaardprijs(afstandKM):
    if afstandKM >= 50:
        prijs = 15 + 0.60*afstandKM
    elif afstandKM <=0:
        prijs = 0
    else:
        prijs = afstandKM * 0.80
    return prijs

def ritprijs(leeftijd, weekendrit, afstandKM):
    standaard = standaardprijs(afstandKM)
    if leeftijd < 12 or leeftijd >=65:
        if weekendrit:
           return standaard * 0.65
        return standaard * 0.70
    else:
        if weekendrit:
            return standaard *0.60
        return standaard



weekend = ("zaterdag", "zondag")
leeftijd = eval(input("Vul hier je leeftijd in:"))
dag = input("Vul hier de dag in:")
afstandKM = eval(input("Voer de afstand in die je moet reizen:"))


dag = dag.lower()
if dag in weekend:
    weekendrit = True
else:
    weekendrit = False
print( "€", ritprijs(leeftijd, weekendrit, afstandKM))