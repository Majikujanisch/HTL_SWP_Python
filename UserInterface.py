import game
import files
def playAlonemenu():
    print("Welche Schwierigkeit möchtest du?")
    print("l...leicht[ab flask server]")
    print("m...mittel")
    print("s...Schwer[ab flask server]")
    print("b...Zurück zum Menü")
    uinput = input("Wähle eine Möglichkeit")
    uinput = uinput.lower()
    if(uinput == "l"):
        game.game("l")
    elif(uinput == "m"):
        game.game("m")
    elif(uinput == "s"):
        game.game("s")
    elif(uinput == "b"):
        mainmenu()
    else:
        print("FALSCHE EINGABE!")
        playAlonemenu()
def playmenu():
    print("Wie möchtest du spielen?")
    print("a...Alleine")
    print("m...lokaler Multiplayer")
    print("b...Zurück zum Menü")
    uinput = input("Wähle eine Möglichkeit: ")
    uinput = uinput.lower()
    if(uinput == "a"):
        playAlonemenu()
    elif(uinput == "m"):
        game.playmulti()
    elif(uinput == "b"):
        mainmenu()
    else:
        print("FALSCHE EINGABE!")
        playmenu()
def optionmenu():
    print("w...Ausgabe der gesammelten Daten")
    print("e...mainmenu")
    uinput = input("Wähle eine Möglichkeit")
    uinput = uinput.lower()
    if uinput == "e":
        mainmenu()
    elif uinput == "w":
        files.dataAuswertung()
        optionmenu()
    else:
        print("FALSCHE EINGABE!")
        optionmenu()
def mainmenu():
    print("Willkommen bei Schere-Stein-Papier-Echse-Spock")
    print("p...play")
    print("o...options")
    print("e...exit")
    uinput = input("Wähle eine Möglichkeit: ")
    uinput = uinput.lower()
    if uinput == "e":
        print("Aufwiedersehen")
    elif uinput == "p":
        playmenu()
    elif uinput == "o":
        optionmenu()
    else:
        print("FALSCHE EINGABE!")
        mainmenu()