def nummers():
    bestand = open('kaartnummers.txt', 'r')
    aantal = sum(1 for line in bestand)
    print("Deze file telt " + str(aantal) + " regels.")


def maximale():
    getallen = list()
    bestand = open('kaartnummers.txt', 'r')
    lijst = list(bestand)

    for x in lijst:
        lijn = x.split()
        getallen.append(lijn[0])

    z = "Het grootste kaartnummer is " + max(getallen)
    print(z.replace(',', ''))
    print("Dit staat op regel " + str(getallen.index(max(getallen)) + 1))


nummers()
maximale()