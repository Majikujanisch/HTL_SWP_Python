
import random
import Comp
import UserInterface


def inttoSignTranslator (x):
    if x == 0:
        return "Stein"
    if x == 1:
        return "Papier"
    if x == 2:
        return "Schere"
    if x == 3:
        return "Spock"
    if x == 4:
        return "Echse"
def decidelogic (x,y):
    #0=stein, 1=papier, 2=schere, 3=spock, 4=echse
    type(x)
    type(y)
    compare = x - y + 5

    if compare % 5 == 0:
        return "draw"

    elif (compare % 5 + 1) % 2 == 0:
        return "win"

    elif (compare % 5) % 2 == 0:
        return "lose"


def playmulti():
    pass


def game(botlevel):
    gameover = False
    while gameover == False:
        userinput = 7
        user = True
        try:
            while int(userinput) < 0 or int(userinput) > 4:
                userinput = input("Stein(0) Papier(1) Schere(2) Spock(3) echse(4):")
                user = True
        except:
            print("die Eingabe muss als Ganzzahl eingegeben werden")
            user = False
        compinput = 0
        if botlevel == "l":
            pass
        if botlevel == "m":
            compinput = random.randint(0, 4)
        if botlevel == "s":
            pass
        print(type(userinput))
        print(type(compinput))
        if(user == True):
            print("Spieler: " + inttoSignTranslator(int(userinput)))
            print("Computer: " + inttoSignTranslator(compinput))
            print(decidelogic(int(userinput),compinput))
            userinput = input("Weiterspielen[w] oder ins Main-Menu zurück[b]")
            replit.clear()
            if userinput.lower() == "b":
                gameover = True;



    UserInterface.mainmenu()