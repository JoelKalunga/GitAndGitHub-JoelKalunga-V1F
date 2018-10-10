import os.path

kluisnummers = list(range(1, 13))


def bagagekluis():
    print("1: Ik wil weten hoeveel kluizen er nog vrij zijn")
    print("2: Ik wil een nieuwe kluis")
    print("3: Ik wil even iets uit mijn kluis halen")
    print("4: Ik geef mijn kluis terug")

    try:
        optie = int(input("Kies een optie:"))

    except ValueError:
        optie = int(input("Kies een optie:"))

    if optie == 1:
        toon_aantal_kluizen_vrij()
    elif optie == 2:
        nieuwe_kluis()
    elif optie == 3:
        kluis_openen()
    else:
        print("Verkeerde optie!")
        print("Kies opnieuw!")

    raise SystemExit(0)


def toon_aantal_kluizen_vrij():
    if os.path.exists("Kluizen.txt"):
        aantal_bezet = 0
        read_file = open("Kluizen.txt", "r+")

        for i in read_file.readlines():
            aantal_bezet += 1

        print("Er zijn", 12 - aantal_bezet, "kluizen beschikbaar.\n")

        read_file.close()


def nieuwe_kluis():
    if os.path.exists("Kluizen.txt"):
        aantal_bezet = 0
        read_file = open("Kluizen.txt", "r+")

    for i in read_file.readlines():
        aantal_bezet += 1
        read_file.close()

    if aantal_bezet < 12:
        read_file = open("Kluizen.txt", "r+")

        for i in read_file:
            kluisnummer = int(i[0])
            if kluisnummer in kluisnummers:
                kluisnummers.remove(kluisnummer)

        read_file.close()

        nieuw_wachtwoord = input("Stel een wachtwoord van minimaal 4 tekens in:")
        if len(nieuw_wachtwoord) < 4:
            nieuw_wachtwoord = input("Uw wachtwoord is te kort!")

        file_append = open("Kluizen.txt", "a")
        file_append.write(str(min(kluisnummers)) + ";" + str(nieuw_wachtwoord) + "\n")
        print("Kluisnummer:", min(kluisnummers))
        print("Code:", nieuw_wachtwoord)

    else:
        print("Er is geen kluis beschikbaar!")
    file_append.close()


def kluis_openen():
    if os.path.exists("Kluizen.txt"):
        read_text = open("kluizen.txt", "r+")
        read_line = read_text.readlines()
        read_text.close()

        kluis_nummers = input("Kluis:")
        kluis_codes = input("Wachtwoord:")

        x = False
        for i in read_line:
            read_split = i.split(";")
            kluisnummer = read_split[0]
            kluis_code = read_split[1].strip()

            if kluis_nummers == kluisnummer and kluis_codes == kluis_code:
                x = True
        if x:
            print("Uw kluis is open!")
        else:
            print("De ingevoerde gegevens kloppen niet!")


bagagekluis()
