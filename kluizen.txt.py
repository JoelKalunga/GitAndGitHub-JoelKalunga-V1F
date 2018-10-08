import os.path

def menu():
    print(50 * "=" + "\
        \n1: Ik wil weten hoeveel kluizen er nog vrij zijn\
        \n2: Ik wil een nieuwe kluis\
        \n3: Ik wil even mijn kluis openen\
        \n4: Ik geef mijn kluis terug\
        \n5: Ik wil stoppen\
        \n" + 50 * "=")

    try:
        keuze = int(input("Welke optie kiest u? \n"))
    except ValueError:
        print("Vul a.u.b. een getal tussen 1 en 5 in.")  # Eigenlijk tussen 1 en 6
        keuze = int(input("Welke optie kiest u? \n"))

    if keuze == 2:
        nieuwe_kluis()


        raise SystemExit(0)


def nieuwe_kluis():
    aantal_bezet = 0
    bestand_read = open("kluizen.txt", "r+")

    for regel in bestand_read.readlines():
        aantal_bezet += 1

    bestand_read.close()

    if aantal_bezet < 12:
        standaard_lijst = list(range(1, 13))
        bestand_read = open("kluizen.txt", "r+")

        for item in bestand_read:
            kluisnummer = int(item[0])
            if kluisnummer in standaard_lijst:
                standaard_lijst.remove(kluisnummer)

        bestand_read.close()

        ww_ingevuld = input("Wat wilt u als wachtwoord instellen? \nHet wachtwoord moet minimaal 4 tekens lang zijn.\n")
        if len(ww_ingevuld) < 4:
            ww_ingevuld = input("Vul a.u.b. een langer wachtwoord in \n")

        bestand_append = open("kluizen.txt", "a")
        bestand_append.write(str(min(standaard_lijst)) + ";" + str(ww_ingevuld) + "\n")
        print("U krijgt kluis", min(standaard_lijst), "met code", ww_ingevuld, "\n")

    else:
        print("Geen vrije kluizen meer.\nOnze excuses.")

    bestand_append.close()

menu()