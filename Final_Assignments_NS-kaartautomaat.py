stations = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal",
            "Amsterdam Amstel", "Utrecht Centraal", "’s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard",
            "Maastricht."]

def inlezen_beginstation(stations):

    beginstation = input("Wat is je beginstation?" + "\n")

    while beginstation not in stations:
         beginstation = input("Deze trein komt niet in " + beginstation + "!\n" + "Wat is je beginstation?" + "\n")
    return beginstation


def inlezen_eindstation(stations, beginstation):

    eindstation = input("Wat is je eindstation?" + "\n")

    while stations.index(eindstation) == stations.index(beginstation):
        eindstation = input(eindstation + " is je beginstation" + "!\n" + "Wat is je eindstation?" + "\n")
    while eindstation not in stations:
        eindstation = input("Deze trein komt niet in " + eindstation + "!\n" + "Wat is je eindstation?" + "\n")
    while stations.index(eindstation) < stations.index(beginstation):
        eindstation = input("Deze trein is al langs " + eindstation + " geweest!\n" + "Wat is je eindstation?" + "\n")
    return eindstation


def omroepen_reis(stations, beginstation, eindstation):

    index_beginstation = stations.index(beginstation) + 1
    index_eindstation = stations.index(eindstation) + 1
    traject = index_eindstation - index_beginstation

    print("\nHet beginstation", beginstation, "is het " + str(stations.index(beginstation) + 1) + "e station in het traject.")
    print("Het eindstation", eindstation, "is het " + str(stations.index(eindstation) + 1) + "e station in het traject.")
    print("De afstand bedraagt", traject, "station(s).")
    print("De prijs van het kaartje is", traject*5, "euro.")
    print("\nJij stapt in de trein in: " + beginstation)

    for station in range(index_beginstation, index_eindstation - 1):
        print("-", (stations[station]))
    print("Jij stapt uit in: " + eindstation)


beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)

omroepen_reis(stations, beginstation, eindstation)
