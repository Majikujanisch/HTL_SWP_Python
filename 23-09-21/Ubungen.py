import random
#Schmeichelprogramm zum Üben
nomen = ['Mensch', 'Behinderter', 'Katze', 'Thomas']
adjektiv = ['schönste', 'intelligenteste', 'klügste', 'lieblichste']
print('du bist der ' + random.choice(adjektiv) + ' ' + random.choice(nomen))
print()
#Zahlenratespiel zum Üben
number = random.randint(1,100)
durchgange = 0
print('Rate die Zahl:')
while durchgange < 7:
    userinput = input("Zahl: ")
    if int(userinput) > number:
        print("Gesuchte Zahl ist kleiner!")
    if int(userinput) < number:
        print("Gesuchte Zahl ist größer!")
    if int(userinput) == number:
        print("GEWONNEN!")
        durchgange = 8
    durchgange = durchgange + 1
#Chatbot
zufallsantworten = ["AJO", "Wia den des?", "Klingt nice", "BUT WHY????"]

reaktionsantworten = {"hallo": "SERVAAAS",
                      "geht": "Wie solls an bot scho gehn",
                      "essen": "Erdbeerkäääääääse"
                      }

print("Willkommen beim tyrolian Chatbot")
print("Wos geits zu schnacken?")
print("Wenn koan bock mehr hasch: 'bye' eintippen")
print("")

nutzereingabe = ""
while nutzereingabe != "bye":
    nutzereingabe = ""
    while nutzereingabe == "":
        nutzereingabe = input("Ihre Frage/Antwort: ")

    nutzereingabe = nutzereingabe.lower()
    nutzerwoerter = nutzereingabe.split()

    intelligenteAntworten = False
    for einzelwoerter in nutzerwoerter:
        if einzelwoerter in reaktionsantworten:
            print(reaktionsantworten[einzelwoerter])
            intelligenteAntworten = True
    if intelligenteAntworten == False:
        print(random.choice(zufallsantworten))

    print("")

print("Nagstes mol lassesch oba a bissl geld do ge? aloa zahlt sich des da nitta")