def standaardprijs(afstandKM):
    treinrit = afstandKM * 0.80

    if afstandKM > 50:
        treinrit = 15 + (afstandKM - 50)*0.60
    elif afstandKM < 0:
        treinrit = 0.00

    return treinrit


def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)

    if weekendrit and (leeftijd < 12 or leeftijd >= 65):
        prijs = prijs / 100 * 65
    elif weekendrit:
        prijs = prijs / 100 * 60
    elif leeftijd < 12 or leeftijd >= 65:
        prijs = prijs / 100 * 70
    return prijs


print(ritprijs(11, True, 50))
print(ritprijs(12, True, 50))
