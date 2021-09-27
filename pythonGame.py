# Text-based Adventure game in Python
# De game is gebaseerd op het survival spel "The Forest"
# The Forest gaat over een vliegtuig die neerstort op een onbewoond eiland

# Deze versie is aangepast met gebruik van definitions

def game_over(reden):
    print("Game Over! " + reden)

def kelder_level():
    print()
    print("Level 4 - de Kelder")
    print()
    print("Je gaat het luik naar beneden en komt terecht in een ruimte waarin allemaal spullen staan,")
    print("zoals een generator, lampen, een betere bijl en het lijkt erop dat er ook een radio staat. ")
    print("Je zet de generator aan, ga je de radio gebruiken?")
    print("- Ja")
    print("- Nee")
    antwoord = input("> ")
    if antwoord.lower().strip() == "ja":
        print("Goede keuze!")
        print()
        print("Het lijkt erop dat de radio het nog doet en je besluit contact te zoeken met iemand via de radio.")
        print("Je moet een de radio instellen op een frequentie, welke kies je? (hij is al eens eerder voorgekomen) ")
        antwoord = int(input("> "))
        if antwoord == 208:
            print("Goede keuze!")
            print()
            print("Je hoort nu iemand over de radio praten, je vertelt het verhaal en hij vraagt om de coordinaten van het eiland.")
            print("Verzin zelf 2 coordinaten en vul ze in")
            getal1 = input("> ")
            getal2 = input("> ")
            print("Je geeft de coordinaten " + getal1 + ", " + getal2 + " door aan de man over de radio.")
            print()
            print("De man op de radio stelt voor om een boot te varen richting het eiland, neem je dit offer aan? ")
            print("- Ja")
            print("- Nee")
            antwoord = input("> ")
            if antwoord.lower().strip() == "ja":
                print()
                print("De volgende dag hoor je de boot al in de verte aankomen")
                print("Je stapt op de boot zodra die aanmeert en daarmee hebt je get spel gewonnen")
                print("-------------------------------------")
                print("|             You won!              |")
                print("-------------------------------------")
            else:
                game_over("Je hebt het offer niet aangenomen en daarmee hebt je de verkeerde keuze gemaakt. De boot is de enige manier van het eiland af.")
        else:
            game_over("Dit is niet de correcte frequentie en daarmee heb je gefaald om iemand te bereiken aan de andere kant van de radio.")
    else:
        game_over("Je hebt gekozen de radio niet te gebruiken, maar het is de enige manier van het eiland af.")

def huis_level():
    print()
    print("Level 3 - het huis")
    print()
    print("Binnen in het huis ziet het er erg verlaten uit, maar er valt wat op in de grond.")
    print("Het is een luik in de grond van het huis, ga je naar beneden in het luik?")
    print("- Ja")
    print("- Nee")
    antwoord = input("> ")
    if antwoord.lower().strip() == "ja":
        print("Goede keuze!")
        kelder_level()
    else:
        game_over("Het is nog nacht en er komt een monster het huis in die je om het leven brengt.")


def bos_level3():
    print()
    print("Je gaat dieper het bos in en komt een grot tegen.")
    print("Ga je de grot in?")
    print("- Ja")
    print("- Nee")
    antwoord = input("> ")
    if antwoord.lower().strip() == "ja":
        game_over("Je bent de grot van een beer in gegaan en wordt vermoord.")
    else:
        print("Goede keuze!")
        print()
        print("Het wordt nacht.")
        print("Ga je terug naar je slaapplek?")
        print("- Ja")
        print("- Nee")        
        antwoord = input("> ")
        if antwoord.lower().strip() == "ja":
            print()
            game_over("Op de weg terug naar je slaapplek wordt je overvallen door een monster op het eiland.")
        else:
            print("Goede keuze!")
            print()
            print("Je gaat verder het bos in en vindt een verlaten huis.")
            print("Ga je het huis in?")
            print("- Ja")
            print("- Nee")
            antwoord = input("> ")
            if antwoord.lower().strip() == "ja":
                print("Goede keuze!")
                huis_level()
            else:
                game_over("Het is nog nacht en dus komt er een monster uit de bosjes tevoorschijn die jouw vermoord.")


def bos_level2():
    antwoord = input("> ")
    if antwoord.lower().strip() == "bos":
        print("Goede keuze!")
        bos_level3()
    elif antwoord.lower().strip() == "vliegtuig":
        game_over("Je komt aan bij het vliegtuig en er springt ineens een monster op je vanuit de cockpit.")
    else:
        print("Incorrecte keuze, gebruik de woorden 'bos' of 'vliegtuig'.")
        bos_level2()


def bos_level():
    print()
    print("Level 2 - Het Bos")
    print()
    print("Vervolgens ga je vanaf het vliegtuig het bos in.")
    print("Je hebt nog nergens om de nacht door te brengen dus,")
    print("ga je een veilige slaapplek maken voor de nacht?")
    print("- Ja")
    print("- Nee")

    antwoord = input("> ")
    if antwoord.lower().strip() == "ja":
        print("Goede keuze!")
        print()
        print("Je hebt 10 planken nodig voor een slaapplek, 1 boom = 5 planken.")
        print("Hoeveel bomen ga je omhakken voor je slaapplek?")
        
        antwoord = int(input("> "))
        if antwoord >= 2:
            print("Goede keuze!")
            print()
            print("Nadat je de hut af had ben je gaan slapen en is het nu dus de volgende ochtend.")
            print("Je moet een keuze maken, ga je dieper het bos is of ga je naar het vliegtuig om spullen te verzamelen?")
            print("- Bos")
            print("- Vliegtuig")
            bos_level2()
        else:
            game_over("Je faalt om jezelf in de nacht te beschermen tegen de monsters op het eiland.")  
    else:
        game_over("Je faalt om jezelf in de nacht te beschermen tegen de monsters op het eiland.")


def start():
    print("Level 1 - Vliegtuig")
    print("Je hebt net een heftige noodlanding gemaakt omdat een van de motoren van het vliegtuig kapot is gegaan.")
    print("Je wordt wakker zonder enig idee waar je bent in het wrak van het neergestortte vliegtuig")
    print("Je loopt naar de opengebarstte achterkant van het vliegtuig en ziet een bijl op de grond liggen")
    print("(Onthoud de frequentie 208)")
    print()
    print("Neem je de bijl mee?")
    print("- Ja")
    print("- Nee")

    antwoord = input("> ")
    if antwoord.lower().strip() == "ja":
        print("Goede keuze!")
        bos_level()
    elif antwoord.strip().lower() == "nee":
        game_over("Dat was geen goede keuze, je bent in de nacht om het leven gebracht door de monsters op het eiland.")

start()







