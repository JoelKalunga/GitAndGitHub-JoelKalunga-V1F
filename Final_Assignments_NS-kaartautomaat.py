stations = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal",
            "Amsterdam Amstel", "Utrecht Centraal", "’s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard",
            "Maastricht"]


def inlezen_beginstation(stations):

    while True:
        eindbestemming = "Maastricht is je eindbestemming!"
        beginstation = input("Wat is je beginstation? " + "\n")

        if beginstation == "Maastricht":
            print(eindbestemming)
            continue
        if beginstation in stations:
            return beginstation
        else:
            print("Deze trein komt niet in " + beginstation + "!")


def inlezen_eindstation(stations, beginstation):

    while True:
        eindstation = input("Wat is je eindstation?" + "\n")

        if eindstation in stations:
            if stations.index(beginstation) < stations.index(eindstation):
                return eindstation
            else:
                print("Dat klopt niet!")
        else:
            print("Deze trein komt niet in " + eindstation + "!")


def omroepen_reis(stations, beginstation, eindstation):
    index_beginstation = stations.index(beginstation) + 1
    index_eindstation = stations.index(eindstation) + 1
    traject = index_eindstation - index_beginstation 

    print("\nHet beginstation" + beginstation + "is het " + str(
        stations.index(beginstation) + 1) + "e station in het traject.")
    print("Het eindstation" + eindstation + "is het " + str(
        stations.index(eindstation) + 1) + "e station in het traject.")
    print("De afstand bedraagt", traject, "station(s).")
    print("De prijs van het kaartje is", traject * 5, "euro.")
    print("\nJij stapt in de trein in: " + beginstation)

    for station in range(index_beginstation, index_eindstation):
        print("-", (stations[station]))
    print("Jij stapt uit in: " + eindstation)


beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
